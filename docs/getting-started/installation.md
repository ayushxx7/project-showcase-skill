# Installation

## 1. Install the Skill

Add it to your AI agent using the universal installer:

```bash
curl -sSL https://raw.githubusercontent.com/ayushxx7/project-showcase-skill/main/skills.sh | bash
```

This detects and installs into:
- Gemini CLI (`~/.gemini/skills/`)
- Claude Code (`~/.claude/skills/`)
- Hermes Agent (`~/.hermes/profiles/*/skills/`)
- Generic agents (`~/.agents/skills/`)

## 2. Setup Dependencies

```bash
./scripts/setup.sh
```

This installs system deps (VHS, ffmpeg) and Python packages (Playwright + Chromium).

## 3. Verify

```bash
python3 scripts/audit.py --dir . --heal
python3 scripts/scan.py --dir .
python3 scripts/capture.py --url http://localhost:8501 --responsive
```
