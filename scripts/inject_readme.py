#!/usr/bin/env python3
"""
Surgical README injection — inject showcase galleries without destroying manual docs.

Usage:
    python3 scripts/inject_readme.py [--readme README.md] [--gallery "..."] [--check]
"""

import re
import argparse
import sys
import shutil
from datetime import datetime


SHOWCASE_MARKER = "## 🎬 Showcase Gallery"
BADGE_MARKER = "[![Live App]"


def read_readme(path):
    """Read README content, return empty string if missing."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""


def has_section(content, heading):
    """Check if a section with the given heading exists."""
    pattern = rf"^##?\s+{re.escape(heading)}"
    return bool(re.search(pattern, content, re.MULTILINE))


def find_section_pos(content, heading):
    """Find the start position of a section."""
    match = re.search(rf"^##?\s+{re.escape(heading)}", content, re.MULTILINE)
    if match:
        return match.start()
    return -1


def inject_showcase_gallery(content, gallery_block):
    """
    Inject the showcase gallery into the README.
    Strategy:
      1. If a Showcase Gallery section exists, replace it.
      2. Otherwise, insert after the first paragraph/badges, before the next ## section.
      3. Never duplicate — checks for the marker first.
    """
    normalized_gallery = gallery_block.strip()

    # Check for existing showcase
    if SHOWCASE_MARKER in content:
        # Replace everything from the marker to the next ## section or end
        pattern = rf"{re.escape(SHOWCASE_MARKER)}.*?(?=\n## |\Z)"
        replaced = re.sub(pattern, normalized_gallery + "\n", content, flags=re.DOTALL)
        return replaced, "replaced"

    # Find insertion point: after the first meaningful content block
    # Look for the first ## heading that's not the title
    sections = [(m.start(), m.group()) for m in re.finditer(r"\n## ", content)]

    if sections:
        # Insert before the first ## section (usually Installation or Features)
        insert_pos = sections[0][0]
        result = content[:insert_pos] + "\n" + normalized_gallery + "\n" + content[insert_pos:]
    else:
        # No sections — append to end
        result = content.rstrip() + "\n\n" + normalized_gallery + "\n"

    return result, "injected"


def inject_badges(content, badges_block):
    """
    Inject badges at the very top of the README (after the # title line).
    Won't duplicate badges that already exist.
    """
    lines = content.splitlines()
    if not lines:
        return badges_block + "\n"

    result_lines = []
    badge_injected = False
    title_found = False

    for line in lines:
        if not title_found and line.startswith("# "):
            result_lines.append(line)
            title_found = True
            # Inject badges right after title
            if badges_block:
                result_lines.append("")
                for badge_line in badges_block.strip().splitlines():
                    if badge_line.strip() and badge_line.strip() not in content:
                        result_lines.append(badge_line.strip())
                badge_injected = True
            continue

        # Skip existing badge lines (shields.io images on consecutive lines)
        if not badge_injected and BADGE_MARKER in line and title_found:
            continue

        result_lines.append(line)

    return "\n".join(result_lines)


def ensure_no_duplicate_sections(content):
    """
    Check for duplicate section headings and warn.
    Returns (content, warnings).
    """
    warnings = []
    headings = re.findall(r"^##?\s+(.+)$", content, re.MULTILINE)
    seen = {}
    for h in headings:
        normalized = h.strip().lower()
        # Strip emoji for comparison
        clean = re.sub(r"[^\w\s]", "", normalized).strip()
        if clean in seen:
            warnings.append(f"Duplicate section detected: '{h}' (also at position {seen[clean]})")
        seen[clean] = h

    return content, warnings


def deduplicate_sections(content):
    """
    Remove duplicate section headings, keeping the first occurrence.
    """
    lines = content.splitlines()
    result = []
    seen_headings = set()
    skip_until_next = False

    for line in lines:
        match = re.match(r"^(#+)\s+(.+)$", line)
        if match:
            level = match.group(1)
            heading = match.group(2).strip().lower()
            clean = re.sub(r"[^\w\s]", "", heading).strip()

            if clean in seen_headings:
                skip_until_next = True
                continue
            else:
                seen_headings.add(clean)
                skip_until_next = False

        if skip_until_next:
            # Check if this is a content line (not a heading)
            if line.startswith("#"):
                skip_until_next = False
            else:
                continue

        result.append(line)

    return "\n".join(result)


def run_injection(readme_path, gallery_block, badges_block=None, dry_run=False, backup=True):
    """Main injection pipeline."""
    content = read_readme(readme_path)
    if not content:
        print(f"❌ README not found at {readme_path}", file=sys.stderr)
        sys.exit(1)

    original = content

    # Step 1: Inject badges (if provided)
    if badges_block:
        content = inject_badges(content, badges_block)

    # Step 2: Inject showcase gallery
    content, action = inject_showcase_gallery(content, gallery_block)

    # Step 3: Check for duplicates
    content, warnings = ensure_no_duplicate_sections(content)
    if warnings:
        print("⚠️ Section warnings:")
        for w in warnings:
            print(f"   - {w}")

    # Step 4: Auto-deduplicate if requested
    if warnings:
        content = deduplicate_sections(content)

    if dry_run:
        if content != original:
            print(f"✅ Would {action} showcase gallery ({len(content) - len(original)} chars diff)")
        else:
            print("ℹ️ No changes needed")
        return

    # Write
    if backup:
        backup_path = readme_path + f".bak.{datetime.now().strftime('%Y%m%d%H%M%S')}"
        shutil.copy2(readme_path, backup_path)
        print(f"💾 Backup: {backup_path}")

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Gallery {action} in {readme_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Surgical README injection")
    parser.add_argument("--readme", default="README.md", help="README path")
    parser.add_argument("--gallery", help="Gallery block to inject")
    parser.add_argument("--badges", help="Badge block to inject")
    parser.add_argument("--check", action="store_true", help="Check for issues only")
    parser.add_argument("--dry-run", action="store_true", help="Show what would change")
    parser.add_argument("--no-backup", action="store_true", help="Skip backup")
    args = parser.parse_args()

    if args.check:
        content = read_readme(args.readme)
        content, warnings = ensure_no_duplicate_sections(content)
        if warnings:
            print("⚠️ Issues found:")
            for w in warnings:
                print(f"   - {w}")
        else:
            print("✅ No duplicate sections found")
        sys.exit(0 if not warnings else 1)

    if not args.gallery and not args.badges:
        print("❌ Provide --gallery and/or --badges", file=sys.stderr)
        sys.exit(1)

    run_injection(
        args.readme,
        args.gallery or "",
        args.badges,
        dry_run=args.dry_run,
        backup=not args.no_backup,
    )
