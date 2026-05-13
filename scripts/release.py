#!/usr/bin/env python3
"""
GitHub Release automation — create releases with auto-generated changelogs.

Usage:
    python3 scripts/release.py [--version v1.0.0] [--title "..."] [--notes "..."] [--dry-run]
"""

import subprocess
import argparse
import sys
import os
import json
from datetime import datetime


def run(cmd, check=True, capture=True):
    """Run a shell command."""
    result = subprocess.run(
        cmd, shell=True, capture_output=capture, text=True
    )
    if check and result.returncode != 0:
        print(f"❌ Command failed: {cmd}", file=sys.stderr)
        if result.stderr:
            print(f"   {result.stderr.strip()}", file=sys.stderr)
        sys.exit(1)
    return result


def check_prerequisites():
    """Verify gh CLI is available and authenticated."""
    try:
        result = run("gh auth status", check=False)
        if result.returncode != 0:
            print("❌ gh CLI not authenticated. Run: gh auth login", file=sys.stderr)
            return False
    except FileNotFoundError:
        print("❌ gh CLI not found. Install: https://cli.github.com/", file=sys.stderr)
        return False

    # Check we're in a git repo
    result = run("git rev-parse --git-dir", check=False)
    if result.returncode != 0:
        print("❌ Not a git repository", file=sys.stderr)
        return False

    return True


def get_latest_tag():
    """Get the latest git tag."""
    result = run("git describe --tags --abbrev=0 2>/dev/null || echo ''", check=False)
    return result.stdout.strip()


def get_commits_since(tag):
    """Get commits since a tag (or all commits if no tag)."""
    if tag:
        range_spec = f"{tag}..HEAD"
    else:
        range_spec = "HEAD"

    result = run(
        f'git log {range_spec} --pretty=format:"%h|%s|%b" --reverse',
        check=False
    )
    commits = []
    for line in result.stdout.strip().splitlines():
        if "|" in line:
            parts = line.split("|", 2)
            commits.append({
                "hash": parts[0],
                "subject": parts[1],
                "body": parts[2] if len(parts) > 2 else "",
            })
    return commits


def generate_changelog(commits, version):
    """Generate a changelog from commits."""
    categories = {
        "feat": "✨ Features",
        "fix": "🐛 Bug Fixes",
        "docs": "📝 Documentation",
        "style": "💄 Styling",
        "refactor": "♻️ Refactoring",
        "perf": "⚡ Performance",
        "test": "✅ Tests",
        "chore": "🔧 Chores",
        "security": "🛡️ Security",
    }

    grouped = {v: [] for v in categories.values()}
    uncategorized = []

    for commit in commits:
        subject = commit["subject"]
        matched = False
        for prefix, label in categories.items():
            if subject.lower().startswith(f"{prefix}:") or subject.lower().startswith(f"{prefix}("):
                grouped[label].append(subject)
                matched = True
                break
        if not matched:
            uncategorized.append(subject)

    lines = [f"## What's New in {version}\n"]
    has_content = False

    for label, items in grouped.items():
        if items:
            has_content = True
            lines.append(f"### {label}")
            for item in items:
                lines.append(f"- {item}")
            lines.append("")

    if uncategorized:
        has_content = True
        lines.append("### Other Changes")
        for item in uncategorized:
            lines.append(f"- {item}")
        lines.append("")

    if not has_content:
        lines.append("See commit history for details.\n")

    return "\n".join(lines)


def suggest_version(latest_tag):
    """Suggest next version based on commits."""
    if not latest_tag:
        return "v0.1.0"

    # Parse semver
    tag = latest_tag.lstrip("v")
    parts = tag.split(".")
    if len(parts) >= 3:
        major, minor, patch = int(parts[0]), int(parts[1]), int(parts[2].split("-")[0])
        # Check for breaking changes
        commits = get_commits_since(latest_tag)
        for c in commits:
            if "BREAKING" in c["subject"] or "BREAKING" in c["body"]:
                return f"{major + 1}.0.0"
        # Check for features
        has_features = any(c["subject"].startswith("feat") for c in commits)
        if has_features:
            return f"{major}.{minor + 1}.0"
        return f"{major}.{minor}.{patch + 1}"

    return "v0.1.0"


def create_release(version, title=None, notes=None, dry_run=False, prerelease=False):
    """Create a GitHub release."""
    if not check_prerequisites():
        sys.exit(1)

    latest_tag = get_latest_tag()
    commits = get_commits_since(latest_tag)

    if not commits:
        print("ℹ️ No new commits since last tag. Nothing to release.")
        return

    # Auto-generate notes if not provided
    if not notes:
        notes = generate_changelog(commits, version)

    release_title = title or version

    print(f"📦 Creating release: {release_title}")
    print(f"   Version: {version}")
    print(f"   Commits since {latest_tag or 'beginning'}: {len(commits)}")
    print(f"   Pre-release: {prerelease}")
    print()

    if dry_run:
        print("🔍 DRY RUN — would execute:")
        print(f"   gh release create {version} --title '{release_title}' --notes '...'")
        print(f"\n   Notes preview:\n{notes[:500]}...")
        return

    # Create the release
    cmd = f'gh release create {version} --title "{release_title}"'
    if prerelease:
        cmd += " --prerelease"
    if notes:
        # Write notes to temp file to avoid shell escaping issues
        notes_file = "/tmp/release_notes.md"
        with open(notes_file, "w") as f:
            f.write(notes)
        cmd += f' --notes-file {notes_file}'

    result = run(cmd, check=False)
    if result.returncode == 0:
        print(f"✅ Release {version} created successfully!")
        print(f"   View at: $(gh repo view --json url -q .url)/releases/tag/{version}")
    else:
        print("❌ Release creation failed", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GitHub Release automation")
    parser.add_argument("--version", help="Release version (e.g., v1.0.0)")
    parser.add_argument("--title", help="Release title")
    parser.add_argument("--notes", help="Release notes (auto-generated if omitted)")
    parser.add_argument("--dry-run", action="store_true", help="Preview without creating")
    parser.add_argument("--prerelease", action="store_true", help="Mark as pre-release")
    parser.add_argument("--suggest-version", action="store_true", help="Suggest next version")
    args = parser.parse_args()

    if args.suggest_version:
        latest = get_latest_tag()
        suggested = suggest_version(latest)
        print(f"Latest tag: {latest or '(none)'}")
        print(f"Suggested version: {suggested}")
        sys.exit(0)

    version = args.version
    if not version:
        latest = get_latest_tag()
        version = suggest_version(latest)
        print(f"ℹ️ No version specified. Using: {version}")

    create_release(
        version=version,
        title=args.title,
        notes=args.notes,
        dry_run=args.dry_run,
        prerelease=args.prerelease,
    )
