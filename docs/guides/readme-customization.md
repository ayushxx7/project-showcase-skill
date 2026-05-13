# README Customization

The skill's README injection is designed to be **surgical** — it enhances without destroying.

## Principles

1. **Show first, tell second** — Visual gallery goes at the top, before any `##` section
2. **Never duplicate** — If a section exists, it's replaced or merged, not duplicated
3. **Preserve manual docs** — Your hand-written content is never deleted
4. **Vibe-first** — No diagnostic tables or health scores in the main README. Those go in `REPO_HEALTH.md`

## README Structure (Recommended)

```
# Project Title
[badges]

Elevator pitch — one sentence.

## 🎬 Showcase Gallery
[screenshots, GIFs, architecture diagrams]

## ✨ Features
[what it does]

## 🛠️ Installation
[how to set up]

## 📖 Usage
[how to use it]

## 📜 License
```

## Health Score Separation

The main README should NOT contain:
- Health score tables (✅ Secure | 92/100)
- Diagnostic checkmark lists
- Audit percentages

Move these to `REPO_HEALTH.md` and link to it from the README if needed.

## Badge Guidelines

- **"Tested on Gemini CLI"** — Only for agentic projects (skills, MCP servers, agent tools)
- **"Live App"** — Only if there's a deployed URL
- **License badge** — Always include if LICENSE exists
