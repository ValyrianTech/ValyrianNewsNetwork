#!/usr/bin/env python3
"""
VNN Article Publisher

This script takes an article from the SERENDIPITY pipeline output and
publishes it to the VNN website by:
1. Validating the article front matter
2. Copying it to src/content/posts/YYYY/MM/DD/ (date-based folder structure)
3. Optionally committing the change to git

Usage:
    python publish_article.py <path_to_article.md> [--commit]
    
Example:
    python publish_article.py /path/to/stories/2026-03-27-china-reforms/article.md --commit
"""

import argparse
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

import yaml


def parse_front_matter(content: str) -> tuple[dict, str]:
    """Extract YAML front matter and body from markdown content."""
    pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
    match = re.match(pattern, content, re.DOTALL)
    
    if not match:
        raise ValueError("No valid front matter found in article")
    
    front_matter = yaml.safe_load(match.group(1))
    body = match.group(2)
    
    return front_matter, body


def validate_front_matter(front_matter: dict) -> list[str]:
    """Validate required fields in front matter. Returns list of errors."""
    required_fields = [
        'title',
        'date',
        'meta_description',
        'slug',
        'read_time_minutes',
        'word_count',
    ]
    
    errors = []
    
    for field in required_fields:
        if field not in front_matter:
            errors.append(f"Missing required field: {field}")
    
    if 'slug' in front_matter:
        slug = front_matter['slug']
        if not re.match(r'^[a-z0-9]+(?:-[a-z0-9]+)*$', slug):
            errors.append(f"Invalid slug format: {slug} (use lowercase letters, numbers, and hyphens)")
    
    if 'read_time_minutes' in front_matter:
        if not isinstance(front_matter['read_time_minutes'], int) or front_matter['read_time_minutes'] < 1:
            errors.append("read_time_minutes must be a positive integer")
    
    if 'word_count' in front_matter:
        if not isinstance(front_matter['word_count'], int) or front_matter['word_count'] < 1:
            errors.append("word_count must be a positive integer")
    
    return errors


def get_date_path(front_matter: dict) -> Path:
    """Generate date-based path (YYYY/MM/DD) from article date."""
    date_val = front_matter['date']
    
    if isinstance(date_val, datetime):
        dt = date_val
    elif isinstance(date_val, str):
        dt = datetime.fromisoformat(date_val.replace('Z', '+00:00'))
    else:
        dt = datetime.now()
    
    return Path(str(dt.year)) / f"{dt.month:02d}" / f"{dt.day:02d}"


def generate_filename(front_matter: dict) -> str:
    """Generate filename from slug."""
    return f"{front_matter['slug']}.md"


def find_existing_slug(posts_dir: Path, slug: str) -> Path | None:
    """Search for an existing article with the same slug across all date folders."""
    if not posts_dir.exists():
        return None
    
    for md_file in posts_dir.rglob('*.md'):
        try:
            content = md_file.read_text(encoding='utf-8')
            match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
            if match:
                fm = yaml.safe_load(match.group(1))
                if fm and fm.get('slug') == slug:
                    return md_file
        except Exception:
            continue
    
    return None


def publish_article(
    source_path: Path,
    dest_dir: Path,
    commit: bool = False,
    repo_root: Path | None = None
) -> Path:
    """
    Publish an article to the content directory.
    
    Args:
        source_path: Path to the source article markdown file
        dest_dir: Destination directory (src/content/posts/)
        commit: Whether to git commit the change
        repo_root: Root of the git repository (for commit)
    
    Returns:
        Path to the published article
    """
    print(f"📄 Reading article from: {source_path}")
    
    content = source_path.read_text(encoding='utf-8')
    front_matter, body = parse_front_matter(content)
    
    print(f"📝 Title: {front_matter.get('title', 'Unknown')}")
    print(f"📅 Date: {front_matter.get('date', 'Unknown')}")
    
    errors = validate_front_matter(front_matter)
    if errors:
        print("❌ Validation errors:")
        for error in errors:
            print(f"   - {error}")
        raise ValueError("Article validation failed")
    
    print("✅ Front matter validated")
    
    existing = find_existing_slug(dest_dir, front_matter['slug'])
    if existing:
        print(f"❌ Duplicate slug detected!")
        print(f"   Slug '{front_matter['slug']}' already exists at: {existing}")
        raise ValueError(f"Article with slug '{front_matter['slug']}' already exists")
    
    print("✅ No duplicate slug found")
    
    if 'draft' not in front_matter:
        front_matter['draft'] = False
    if 'categories' not in front_matter:
        front_matter['categories'] = []
    if 'tags' not in front_matter:
        front_matter['tags'] = []
    if 'style' not in front_matter:
        front_matter['style'] = 'formal_news'
    
    date_path = get_date_path(front_matter)
    filename = generate_filename(front_matter)
    full_dest_dir = dest_dir / date_path
    dest_path = full_dest_dir / filename
    
    full_dest_dir.mkdir(parents=True, exist_ok=True)
    
    new_content = "---\n"
    new_content += yaml.dump(front_matter, default_flow_style=False, allow_unicode=True, sort_keys=False)
    new_content += "---\n"
    new_content += body
    
    dest_path.write_text(new_content, encoding='utf-8')
    print(f"✅ Article published to: {dest_path}")
    
    if commit and repo_root:
        print("📦 Committing to git...")
        try:
            subprocess.run(
                ['git', 'add', str(dest_path)],
                cwd=repo_root,
                check=True,
                capture_output=True
            )
            
            commit_msg = f"Publish: {front_matter['title']}"
            subprocess.run(
                ['git', 'commit', '-m', commit_msg],
                cwd=repo_root,
                check=True,
                capture_output=True
            )
            print(f"✅ Committed: {commit_msg}")
        except subprocess.CalledProcessError as e:
            print(f"⚠️  Git commit failed: {e.stderr.decode() if e.stderr else str(e)}")
    
    return dest_path


def main():
    parser = argparse.ArgumentParser(
        description='Publish an article to the VNN website',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument(
        'article_path',
        type=Path,
        help='Path to the article markdown file'
    )
    parser.add_argument(
        '--commit',
        action='store_true',
        help='Commit the published article to git'
    )
    parser.add_argument(
        '--dest',
        type=Path,
        default=None,
        help='Destination directory (default: auto-detect from script location)'
    )
    
    args = parser.parse_args()
    
    if not args.article_path.exists():
        print(f"❌ Article not found: {args.article_path}")
        sys.exit(1)
    
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    
    if args.dest:
        dest_dir = args.dest
    else:
        dest_dir = repo_root / 'src' / 'content' / 'posts'
    
    try:
        published_path = publish_article(
            source_path=args.article_path,
            dest_dir=dest_dir,
            commit=args.commit,
            repo_root=repo_root
        )
        print(f"\n🎉 Successfully published article!")
        print(f"   Location: {published_path}")
    except Exception as e:
        print(f"\n❌ Failed to publish article: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
