# Metadata (`manage_metadata.py`)

Auto-detects and updates GitHub repository metadata.

## Features

- **Topic detection** — scans file patterns to suggest GitHub topics (e.g., `requirements.txt` → `python`)
- **Description extraction** — pulls elevator pitch from README
- **Auto-apply** — uses `gh repo edit` to update GitHub directly

## Usage

```bash
# Preview suggested topics + description
python3 scripts/manage_metadata.py

# Apply to GitHub
python3 scripts/manage_metadata.py --apply

# Apply + commit + push
python3 scripts/manage_metadata.py --apply --commit --push
```

## Topic Detection

| File Pattern | Topics Added |
|---|---|
| `requirements.txt` | `python` |
| `package.json` | `javascript`, `nodejs` |
| `go.mod` | `go` |
| `Cargo.toml` | `rust` |
| `Dockerfile` / `docker-compose` | `docker` |
| `pytest` / `jest` | `testing` |
| `tailwind` | `tailwindcss` |
| `react` | `react` |
| `next` | `nextjs` |
| `github/workflows` | `github-actions`, `automation` |

Base topics `showcase` and `automation` are always included.
