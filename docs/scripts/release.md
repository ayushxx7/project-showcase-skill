# GitHub Release (`release.py`)

Creates GitHub releases with auto-generated changelogs from commit history.

## Features

- **Auto-versioning** — suggests next semver based on commit prefixes (`feat:`, `fix:`, `BREAKING`)
- **Auto-changelog** — groups commits by type (Features, Bug Fixes, Docs, etc.)
- **Pre-release support** — flag for alpha/beta releases
- **Dry-run mode** — preview before creating

## Usage

```bash
# Auto-version + auto-changelog
python3 scripts/release.py

# Specific version
python3 scripts/release.py --version v1.2.0

# Pre-release
python3 scripts/release.py --version v1.0.0-beta.1 --prerelease

# Custom title + notes
python3 scripts/release.py --version v1.0.0 --title "First Stable Release" --notes "..."

# Preview without creating
python3 scripts/release.py --dry-run

# Just suggest a version
python3 scripts/release.py --suggest-version
```

## Changelog Format

Commits are grouped by conventional prefix:

| Prefix | Category |
|---|---|
| `feat:` | ✨ Features |
| `fix:` | 🐛 Bug Fixes |
| `docs:` | 📝 Documentation |
| `refactor:` | ♻️ Refactoring |
| `perf:` | ⚡ Performance |
| `test:` | ✅ Tests |
| `chore:` | 🔧 Chores |
| `security:` | 🛡️ Security |

## Prerequisites

- `gh` CLI installed and authenticated (`gh auth login`)
- Git repository with remote configured
