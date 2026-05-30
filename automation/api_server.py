#!/usr/bin/env python3
"""
VNN Publish API Server

A small FastAPI service that accepts article markdown over HTTP and runs
the same publish flow as ``publish_article.py``: validate front matter,
write to ``src/content/posts/YYYY/MM/DD/``, and (optionally) ``git add`` +
``git commit``.

The service intentionally does NOT push to the remote — pushing is still
a manual step until the workflow is finalized.

Run locally:

    uvicorn automation.api_server:app --host 0.0.0.0 --port 8787

Environment variables (loaded from ``automation/.env`` or repo-root ``.env``):

    VNN_PUBLISH_API_KEY   Required. Bearer token clients must present.
    VNN_PUSH_API_KEY      Optional. Enables push notifications when notify=true.
    VNN_PUSH_WORKER_URL   Optional. Override push worker URL.
"""

from __future__ import annotations

import asyncio
import hmac
import logging
import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, Header, HTTPException, Request, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

from publish_article import (
    DuplicateSlugError,
    FrontMatterValidationError,
    GitPublishError,
    parse_front_matter,
    publish_article_content,
    send_push_notifications,
)

# --- Configuration ----------------------------------------------------------

SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
DEST_DIR = REPO_ROOT / "src" / "content" / "posts"

load_dotenv(SCRIPT_DIR / ".env")
load_dotenv(REPO_ROOT / ".env")

MAX_BODY_BYTES = 1 * 1024 * 1024  # 1 MiB
NOTIFICATION_DELAY_SECONDS = 60

logger = logging.getLogger("vnn.api")
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")

_API_KEY = os.environ.get("VNN_PUBLISH_API_KEY", "").strip()
if not _API_KEY:
    raise RuntimeError(
        "VNN_PUBLISH_API_KEY is not set. Refusing to start an unauthenticated publish API."
    )

# Serialize all publish operations so concurrent requests don't race on git.
_publish_lock = asyncio.Lock()


# --- Auth -------------------------------------------------------------------


def require_bearer(authorization: str | None = Header(default=None)) -> None:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing bearer token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    presented = authorization.removeprefix("Bearer ").strip()
    if not hmac.compare_digest(presented, _API_KEY):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid bearer token",
            headers={"WWW-Authenticate": "Bearer"},
        )


# --- Schemas ----------------------------------------------------------------


class PublishRequest(BaseModel):
    markdown: str = Field(..., description="Full article markdown including YAML front matter.")
    commit: bool = Field(default=True, description="git add + git commit the new file.")
    notify: bool = Field(default=True, description="Send push notifications after publishing.")
    dry_run: bool = Field(default=False, description="Validate only; do not write or commit.")


class PublishResponse(BaseModel):
    path: str
    relative_path: str
    slug: str
    title: str
    committed: bool
    pushed: bool
    notified: bool
    dry_run: bool


# --- App --------------------------------------------------------------------

app = FastAPI(
    title="VNN Publish API",
    version="1.0.0",
    description="Publish SERENDIPITY pipeline articles to the VNN site from a remote machine.",
)


@app.middleware("http")
async def limit_body_size(request: Request, call_next):
    """Reject oversized request bodies before they hit handlers."""
    cl = request.headers.get("content-length")
    if cl is not None:
        try:
            if int(cl) > MAX_BODY_BYTES:
                return JSONResponse(
                    status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
                    content={"detail": f"Request body exceeds {MAX_BODY_BYTES} bytes"},
                )
        except ValueError:
            pass
    return await call_next(request)


@app.get("/healthz")
async def healthz() -> dict:
    return {"status": "ok"}


@app.post(
    "/articles",
    response_model=PublishResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_bearer)],
)
async def publish(req: PublishRequest) -> PublishResponse:
    if len(req.markdown.encode("utf-8")) > MAX_BODY_BYTES:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail=f"markdown exceeds {MAX_BODY_BYTES} bytes",
        )

    async with _publish_lock:
        try:
            # Run the (synchronous, disk + git touching) publish in a thread
            # so the event loop stays responsive.
            dest_path, front_matter, _body, committed, pushed = await asyncio.to_thread(
                publish_article_content,
                req.markdown,
                DEST_DIR,
                req.commit and not req.dry_run,
                REPO_ROOT,
                req.dry_run,
            )
        except FrontMatterValidationError as e:
            logger.warning("Validation failed: %s", e.errors)
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={"errors": e.errors},
            )
        except DuplicateSlugError as e:
            logger.warning("Duplicate slug: %s", e.slug)
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail={
                    "error": str(e),
                    "slug": e.slug,
                    "existing_path": str(e.existing_path),
                },
            )
        except ValueError as e:
            logger.warning("Bad request: %s", e)
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except GitPublishError as e:
            logger.error("Git publish failed during %s: %s", e.step, e.detail)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail={
                    "error": str(e),
                    "step": e.step,
                },
            )

        notified = False
        logger.info(
            "Notify branch: notify=%s dry_run=%s pushed=%s tags=%s",
            req.notify, req.dry_run, pushed, front_matter.get('tags'),
        )
        if req.notify and not req.dry_run and pushed:
            logger.info("Waiting %s seconds before sending push notifications", NOTIFICATION_DELAY_SECONDS)
            await asyncio.sleep(NOTIFICATION_DELAY_SECONDS)
            logger.info("Calling send_push_notifications for slug=%s", front_matter.get('slug'))
            try:
                await asyncio.to_thread(send_push_notifications, front_matter)
                notified = True
                logger.info("send_push_notifications returned")
            except Exception as e:  # noqa: BLE001 - notifications are best-effort
                logger.warning("Push notifications failed: %s", e)
        else:
            logger.info(
                "Skipping push notifications (notify=%s, dry_run=%s, pushed=%s)",
                req.notify, req.dry_run, pushed,
            )

    try:
        relative_path = str(dest_path.relative_to(REPO_ROOT))
    except ValueError:
        relative_path = str(dest_path)

    return PublishResponse(
        path=str(dest_path),
        relative_path=relative_path,
        slug=front_matter["slug"],
        title=front_matter["title"],
        committed=committed,
        pushed=pushed,
        notified=notified,
        dry_run=req.dry_run,
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "api_server:app",
        host=os.environ.get("VNN_API_HOST", "0.0.0.0"),
        port=int(os.environ.get("VNN_API_PORT", "8787")),
        reload=False,
    )
