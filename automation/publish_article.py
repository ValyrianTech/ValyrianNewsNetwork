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
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

import requests
import yaml
from dotenv import load_dotenv

# Load .env file from automation directory or repo root
load_dotenv(Path(__file__).parent / '.env')
load_dotenv(Path(__file__).parent.parent / '.env')


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


class DuplicateSlugError(ValueError):
    """Raised when an article with the same slug already exists."""

    def __init__(self, slug: str, existing_path: Path):
        super().__init__(f"Article with slug '{slug}' already exists")
        self.slug = slug
        self.existing_path = existing_path


class FrontMatterValidationError(ValueError):
    """Raised when front matter validation fails."""

    def __init__(self, errors: list[str]):
        super().__init__("Article validation failed: " + "; ".join(errors))
        self.errors = errors


def publish_article_content(
    markdown: str,
    dest_dir: Path,
    commit: bool = False,
    repo_root: Path | None = None,
    dry_run: bool = False,
) -> tuple[Path, dict, str]:
    """
    Publish an article (given its full markdown content) to the content directory.

    Args:
        markdown: Full article markdown including YAML front matter.
        dest_dir: Destination directory (src/content/posts/).
        commit: Whether to git commit the change (ignored if dry_run).
        repo_root: Root of the git repository (for commit).
        dry_run: If True, validate and compute the destination path but
            do not write to disk or touch git.

    Returns:
        Tuple of (destination path, parsed front matter, body).
    """
    front_matter, body = parse_front_matter(markdown)

    print(f"📝 Title: {front_matter.get('title', 'Unknown')}")
    print(f"📅 Date: {front_matter.get('date', 'Unknown')}")

    errors = validate_front_matter(front_matter)
    if errors:
        print("❌ Validation errors:")
        for error in errors:
            print(f"   - {error}")
        raise FrontMatterValidationError(errors)

    print("✅ Front matter validated")

    existing = find_existing_slug(dest_dir, front_matter['slug'])
    if existing:
        print(f"❌ Duplicate slug detected!")
        print(f"   Slug '{front_matter['slug']}' already exists at: {existing}")
        raise DuplicateSlugError(front_matter['slug'], existing)

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

    if dry_run:
        print(f"🧪 Dry run — would publish to: {dest_path}")
        return dest_path, front_matter, body

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

    return dest_path, front_matter, body


def publish_article(
    source_path: Path,
    dest_dir: Path,
    commit: bool = False,
    repo_root: Path | None = None
) -> Path:
    """Read an article from disk and publish it. Thin wrapper around
    ``publish_article_content`` for the CLI."""
    print(f"📄 Reading article from: {source_path}")
    content = source_path.read_text(encoding='utf-8')
    dest_path, _, _ = publish_article_content(
        markdown=content,
        dest_dir=dest_dir,
        commit=commit,
        repo_root=repo_root,
    )
    return dest_path


def extract_countries(tags: list[str]) -> list[str]:
    """Extract canonical country labels from tags.

    IMPORTANT: This map MUST stay in sync with `src/utils/countries.ts` on the
    site, because subscribers register using the canonical labels produced
    there (e.g. "US", "UK", "UAE"). If publisher and site diverge, push
    notifications target a country string with zero matching subscribers.
    """
    COUNTRY_TAGS = {
        # A
        'afghanistan': 'Afghanistan', 'albania': 'Albania', 'algeria': 'Algeria',
        'andorra': 'Andorra', 'angola': 'Angola',
        'antigua and barbuda': 'Antigua and Barbuda',
        'argentina': 'Argentina', 'armenia': 'Armenia', 'australia': 'Australia',
        'austria': 'Austria', 'azerbaijan': 'Azerbaijan',
        # B
        'bahamas': 'Bahamas', 'bahrain': 'Bahrain', 'bangladesh': 'Bangladesh',
        'barbados': 'Barbados', 'belarus': 'Belarus', 'belgium': 'Belgium',
        'belize': 'Belize', 'benin': 'Benin', 'bhutan': 'Bhutan',
        'bolivia': 'Bolivia',
        'bosnia and herzegovina': 'Bosnia and Herzegovina',
        'bosnia': 'Bosnia and Herzegovina',
        'botswana': 'Botswana', 'brazil': 'Brazil', 'brunei': 'Brunei',
        'bulgaria': 'Bulgaria', 'burkina faso': 'Burkina Faso',
        'burundi': 'Burundi',
        # C
        'cabo verde': 'Cabo Verde', 'cape verde': 'Cabo Verde',
        'cambodia': 'Cambodia', 'cameroon': 'Cameroon', 'canada': 'Canada',
        'central african republic': 'Central African Republic',
        'chad': 'Chad', 'chile': 'Chile', 'china': 'China',
        'colombia': 'Colombia', 'comoros': 'Comoros', 'congo': 'Congo',
        'democratic republic of the congo': 'DR Congo',
        'dr congo': 'DR Congo',
        'costa rica': 'Costa Rica', 'croatia': 'Croatia', 'cuba': 'Cuba',
        'cyprus': 'Cyprus', 'czech republic': 'Czech Republic',
        'czechia': 'Czech Republic',
        # D
        'denmark': 'Denmark', 'djibouti': 'Djibouti', 'dominica': 'Dominica',
        'dominican republic': 'Dominican Republic',
        # E
        'east timor': 'East Timor', 'timor-leste': 'East Timor',
        'ecuador': 'Ecuador', 'egypt': 'Egypt', 'el salvador': 'El Salvador',
        'equatorial guinea': 'Equatorial Guinea', 'eritrea': 'Eritrea',
        'estonia': 'Estonia', 'eswatini': 'Eswatini',
        'swaziland': 'Eswatini', 'ethiopia': 'Ethiopia',
        # F
        'fiji': 'Fiji', 'finland': 'Finland', 'france': 'France',
        # G
        'gabon': 'Gabon', 'gambia': 'Gambia', 'georgia': 'Georgia',
        'germany': 'Germany', 'ghana': 'Ghana', 'greece': 'Greece',
        'grenada': 'Grenada', 'guatemala': 'Guatemala', 'guinea': 'Guinea',
        'guinea-bissau': 'Guinea-Bissau', 'guyana': 'Guyana',
        # H
        'haiti': 'Haiti', 'honduras': 'Honduras', 'hungary': 'Hungary',
        # I
        'iceland': 'Iceland', 'india': 'India', 'indonesia': 'Indonesia',
        'iran': 'Iran', 'iraq': 'Iraq', 'ireland': 'Ireland',
        'israel': 'Israel', 'italy': 'Italy', 'ivory coast': 'Ivory Coast',
        "cote d'ivoire": 'Ivory Coast',
        # J
        'jamaica': 'Jamaica', 'japan': 'Japan', 'jordan': 'Jordan',
        # K
        'kazakhstan': 'Kazakhstan', 'kenya': 'Kenya', 'kiribati': 'Kiribati',
        'kosovo': 'Kosovo', 'kuwait': 'Kuwait', 'kyrgyzstan': 'Kyrgyzstan',
        # L
        'laos': 'Laos', 'latvia': 'Latvia', 'lebanon': 'Lebanon',
        'lesotho': 'Lesotho', 'liberia': 'Liberia', 'libya': 'Libya',
        'liechtenstein': 'Liechtenstein', 'lithuania': 'Lithuania',
        'luxembourg': 'Luxembourg',
        # M
        'madagascar': 'Madagascar', 'malawi': 'Malawi', 'malaysia': 'Malaysia',
        'maldives': 'Maldives', 'mali': 'Mali', 'malta': 'Malta',
        'marshall islands': 'Marshall Islands', 'mauritania': 'Mauritania',
        'mauritius': 'Mauritius', 'mexico': 'Mexico',
        'micronesia': 'Micronesia', 'moldova': 'Moldova', 'monaco': 'Monaco',
        'mongolia': 'Mongolia', 'montenegro': 'Montenegro',
        'morocco': 'Morocco', 'mozambique': 'Mozambique',
        'myanmar': 'Myanmar', 'burma': 'Myanmar',
        # N
        'namibia': 'Namibia', 'nauru': 'Nauru', 'nepal': 'Nepal',
        'netherlands': 'Netherlands', 'new zealand': 'New Zealand',
        'nicaragua': 'Nicaragua', 'niger': 'Niger', 'nigeria': 'Nigeria',
        'north korea': 'North Korea',
        'north macedonia': 'North Macedonia', 'norway': 'Norway',
        # O
        'oman': 'Oman',
        # P
        'pakistan': 'Pakistan', 'palau': 'Palau', 'palestine': 'Palestine',
        'panama': 'Panama', 'papua new guinea': 'Papua New Guinea',
        'paraguay': 'Paraguay', 'peru': 'Peru',
        'philippines': 'Philippines', 'poland': 'Poland',
        'portugal': 'Portugal',
        # Q
        'qatar': 'Qatar',
        # R
        'romania': 'Romania', 'russia': 'Russia', 'rwanda': 'Rwanda',
        # S
        'saint kitts and nevis': 'Saint Kitts and Nevis',
        'saint lucia': 'Saint Lucia',
        'saint vincent and the grenadines': 'Saint Vincent and the Grenadines',
        'samoa': 'Samoa', 'san marino': 'San Marino',
        'sao tome and principe': 'São Tomé and Príncipe',
        'saudi arabia': 'Saudi Arabia', 'senegal': 'Senegal',
        'serbia': 'Serbia', 'seychelles': 'Seychelles',
        'sierra leone': 'Sierra Leone', 'singapore': 'Singapore',
        'slovakia': 'Slovakia', 'slovenia': 'Slovenia',
        'solomon islands': 'Solomon Islands', 'somalia': 'Somalia',
        'south africa': 'South Africa', 'south korea': 'South Korea',
        'korea': 'South Korea',
        'south sudan': 'South Sudan', 'spain': 'Spain',
        'sri lanka': 'Sri Lanka', 'sudan': 'Sudan',
        'suriname': 'Suriname', 'sweden': 'Sweden',
        'switzerland': 'Switzerland', 'syria': 'Syria',
        # T
        'taiwan': 'Taiwan', 'tajikistan': 'Tajikistan',
        'tanzania': 'Tanzania', 'thailand': 'Thailand', 'togo': 'Togo',
        'tonga': 'Tonga', 'trinidad and tobago': 'Trinidad and Tobago',
        'tunisia': 'Tunisia', 'turkey': 'Turkey',
        'turkmenistan': 'Turkmenistan', 'tuvalu': 'Tuvalu',
        # U
        'uganda': 'Uganda', 'ukraine': 'Ukraine',
        'united arab emirates': 'UAE', 'uae': 'UAE',
        'united kingdom': 'UK', 'uk': 'UK',
        'uk news': 'UK', 'uk politics': 'UK', 'britain': 'UK',
        'united states': 'US', 'united_states': 'US',
        'us': 'US', 'usa': 'US', 'america': 'US',
        'uruguay': 'Uruguay', 'uzbekistan': 'Uzbekistan',
        # V
        'vanuatu': 'Vanuatu', 'vatican': 'Vatican City',
        'vatican city': 'Vatican City', 'venezuela': 'Venezuela',
        'vietnam': 'Vietnam',
        # Y
        'yemen': 'Yemen',
        # Z
        'zambia': 'Zambia', 'zimbabwe': 'Zimbabwe',
    }
    countries = set()
    for tag in tags:
        match = COUNTRY_TAGS.get(tag.lower())
        if match:
            countries.add(match)
    return list(countries)


def send_push_notifications(front_matter: dict) -> None:
    """Send push notifications to subscribers."""
    print("🔔 send_push_notifications: starting")
    api_key = os.environ.get('VNN_PUSH_API_KEY')
    if not api_key:
        print("⚠️  VNN_PUSH_API_KEY not set, skipping push notifications")
        return
    print(f"🔔 VNN_PUSH_API_KEY present (len={len(api_key)})")

    worker_url = os.environ.get('VNN_PUSH_WORKER_URL', 'https://vnn-push.valyriannewsnetwork.workers.dev')
    print(f"🔔 Worker URL: {worker_url}")

    tags = front_matter.get('tags', [])
    countries = extract_countries(tags)
    print(f"🔔 Tags={tags} → countries={countries}")
    if not countries:
        print("ℹ️  No country tags found, skipping push notifications")
        return

    date_path = get_date_path(front_matter)
    payload = {
        'title': front_matter['title'],
        'description': front_matter['meta_description'],
        'url': f"https://valyriantech.github.io/ValyrianNewsNetwork/posts/{date_path}/{front_matter['slug']}",
        'countries': countries,
    }
    print(f"🔔 POST {worker_url}/send payload={payload}")

    try:
        response = requests.post(
            f"{worker_url}/send",
            json=payload,
            headers={'Authorization': f'Bearer {api_key}'},
            timeout=30,
        )
        print(f"🔔 Response status: {response.status_code}")
        response.raise_for_status()
        result = response.json()
        print(f"🔔 Push notifications: {result.get('message', 'sent')} (full response: {result})")
    except requests.RequestException as e:
        print(f"⚠️  Failed to send push notifications: {e}")
        if getattr(e, 'response', None) is not None:
            print(f"⚠️  Response body: {e.response.text}")


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
        '--no-commit',
        action='store_true',
        help='Skip committing the published article to git'
    )
    parser.add_argument(
        '--dest',
        type=Path,
        default=None,
        help='Destination directory (default: auto-detect from script location)'
    )
    parser.add_argument(
        '--no-notify',
        action='store_true',
        help='Skip sending push notifications'
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
            commit=not args.no_commit,
            repo_root=repo_root
        )
        print(f"\n🎉 Successfully published article!")
        print(f"   Location: {published_path}")
        
        # Send push notifications
        if not args.no_notify:
            content = args.article_path.read_text(encoding='utf-8')
            front_matter, _ = parse_front_matter(content)
            send_push_notifications(front_matter)
    except Exception as e:
        print(f"\n❌ Failed to publish article: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
