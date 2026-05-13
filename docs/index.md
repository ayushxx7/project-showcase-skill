# Project Showcase Skill

**Automate the "last mile" of development** — generate visual galleries, audit repo health, inject professional READMEs, and launch on social media.

## What It Does

| Script | Purpose |
|---|---|
| `scripts/capture.py` | Playwright-based UI screenshots (desktop, tablet, mobile) |
| `scripts/scan.py` | Security scan for hardcoded secrets and .env leaks |
| `scripts/audit.py` | Repo health scoring (0-100) with healing plan |
| `scripts/inject_readme.py` | Surgical README gallery injection |
| `scripts/release.py` | GitHub release creation with auto-changelog |
| `scripts/manage_metadata.py` | Auto-detect and update GitHub topics/description |
| `scripts/setup.sh` | One-shot dependency installer |

## Quick Start

```bash
# 1. Install the skill
curl -sSL https://raw.githubusercontent.com/ayushxx7/project-showcase-skill/main/skills.sh | bash

# 2. Setup dependencies
./scripts/setup.sh

# 3. Run a health audit
python3 scripts/audit.py --dir /path/to/your/project --heal

# 4. Capture UI
python3 scripts/capture.py --url http://localhost:3000 --responsive

# 5. Scan for secrets
python3 scripts/scan.py --dir /path/to/your/project
```

## Agent Commands

When installed as a skill, tell your agent:

- *"Showcase this project"* — Full pipeline: capture + audit + README + release
- *"Audit this project"* — Health score + healing plan
- *"Capture the UI"* — Screenshots across viewports
- *"Scan for secrets"* — Pre-publish security check
- *"Update the README"* — Surgical gallery injection
- *"Create a release"* — GitHub release with changelog
- *"Launch on LinkedIn"* — Post templates + asset bundling

## Sub-Skills

- **LinkedIn Magic** (`linkedin-magic/`) — Post templates, asset bundling, hashtag strategy

## License

MIT — see [LICENSE](../LICENSE)
