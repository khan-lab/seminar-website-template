#!/usr/bin/env python3
"""
Generate events/*.md pages from _data/speakers.yml

- Ensures each entry has a unique `id` (slug of title if missing).
- Writes one Markdown file per event using the `event` layout.
- Optionally writes back added IDs to _data/speakers.yml (with a .bak backup).
"""

import argparse
import os
import re
import sys
import unicodedata
import yaml
from pathlib import Path
from typing import List, Dict, Any

def slugify(text: str) -> str:
    # Normalize, strip accents, keep alnum/dash, collapse dashes
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-{2,}", "-", text).strip("-")
    return text or "event"

def unique_id(desired: str, taken: set) -> str:
    if desired not in taken:
        return desired
    i = 2
    while f"{desired}-{i}" in taken:
        i += 1
    return f"{desired}-{i}"

def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)

def save_yaml(path: Path, data: Any) -> None:
    with path.open("w", encoding="utf-8") as fh:
        yaml.safe_dump(data, fh, allow_unicode=True, sort_keys=False)

def main():
    ap = argparse.ArgumentParser(description="Generate event pages from speakers.yml")
    ap.add_argument("--data", default="_data/speakers.yml", help="Path to speakers.yml")
    ap.add_argument("--out", default="events", help="Output directory for event pages")
    ap.add_argument("--base-permalink", default="/events/", help="Base permalink path")
    ap.add_argument("--force", action="store_true", help="Overwrite existing .md files")
    ap.add_argument("--no-write-back", action="store_true", help="Do not write back missing IDs to speakers.yml")
    ap.add_argument("--quiet", action="store_true", help="Suppress info logs")
    args = ap.parse_args()

    data_path = Path(args.data)
    out_dir = Path(args.out)
    base_permalink = args.base_permalink.rstrip("/") + "/"

    if not data_path.exists():
        print(f"ERROR: {data_path} not found", file=sys.stderr)
        sys.exit(1)

    speakers = load_yaml(data_path)
    if not isinstance(speakers, list):
        print(f"ERROR: Expected a list in {data_path}", file=sys.stderr)
        sys.exit(1)

    out_dir.mkdir(parents=True, exist_ok=True)

    # Collect existing IDs to enforce uniqueness
    existing_ids = set()
    for ev in speakers:
        ev_id = ev.get("id")
        if ev_id:
            existing_ids.add(ev_id)

    created = 0
    skipped = 0
    assigned_any = False

    for ev in speakers:
        title = ev.get("title") or ""
        ev_id = ev.get("id")

        if not ev_id:
            if not title:
                if not args.quiet:
                    print("! Skipping entry without title and id")
                continue
            ev_id = unique_id(slugify(title), existing_ids)
            ev["id"] = ev_id
            existing_ids.add(ev_id)
            assigned_any = True
            if not args.quiet:
                print(f"• Assigned id: {ev_id}  ({title})")

        page_path = out_dir / f"{ev_id}.md"
        if page_path.exists() and not args.force:
            skipped += 1
            if not args.quiet:
                print(f"– Skipping existing {page_path}")
            continue

        front_matter = {
            "layout": "event",
            "title": title or ev_id.replace("-", " ").title(),
            "event_id": ev_id,
            "permalink": f"{base_permalink}{ev_id}/",
        }

        # Write YAML front matter only; event layout pulls details from _data/speakers.yml
        content = "---\n" + yaml.safe_dump(front_matter, allow_unicode=True, sort_keys=False) + "---\n"
        page_path.write_text(content, encoding="utf-8")
        created += 1
        if not args.quiet:
            print(f"✓ Wrote {page_path}")

    # Optionally write back IDs we assigned
    if assigned_any and not args.no_write_back:
        backup = data_path.with_suffix(".yml.bak")
        backup.write_text(data_path.read_text(encoding="utf-8"), encoding="utf-8")
        save_yaml(data_path, speakers)
        if not args.quiet:
            print(f"🔧 Updated {data_path} (backup: {backup.name})")

    if not args.quiet:
        print(f"Done. Created: {created}, Skipped: {skipped}")

if __name__ == "__main__":
    main()
