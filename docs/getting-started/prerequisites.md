# Prerequisites

## Required

| Tool | Purpose | Install |
|---|---|---|
| Python 3.8+ | Scripts runtime | [python.org](https://www.python.org/) |
| Playwright | UI capture | `pip install playwright && playwright install chromium` |
| ffmpeg | Video/GIF processing | `brew install ffmpeg` (macOS) |

## Optional

| Tool | Purpose | Install |
|---|---|---|
| VHS | Terminal GIF recording | `brew install vhs` (macOS) |
| GitHub CLI (`gh`) | Releases, metadata | [cli.github.com](https://cli.github.com/) |
| MkDocs Material | Local docs site | `pip install mkdocs-material` |

## Run the Docs Site Locally

```bash
pip install mkdocs-material
mkdocs serve
```
