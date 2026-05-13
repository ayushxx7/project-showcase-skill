# README Injection (`inject_readme.py`)

Surgically injects showcase galleries into READMEs without destroying manual docs.

## Strategy

1. **If a Showcase Gallery section exists** → replace it
2. **If no gallery section** → insert after the first paragraph, before the first `##` heading
3. **Never duplicates** — checks for existing markers
4. **Badge injection** — places shields.io badges after the `#` title line
5. **Deduplication** — warns on and removes duplicate section headings

## Usage

```bash
# Inject a gallery block
python3 scripts/inject_readme.py --readme README.md --gallery "## 🎬 Showcase Gallery\n![Demo](showcase/demo.gif)"

# Inject badges
python3 scripts/inject_readme.py --readme README.md --badges "[![Live App](...)](...)"

# Check for issues without modifying
python3 scripts/inject_readme.py --readme README.md --check

# Preview changes
python3 scripts/inject_readme.py --readme README.md --gallery "..." --dry-run
```

## Options

| Flag | Description |
|---|---|
| `--readme` | Path to README (default: `README.md`) |
| `--gallery` | Gallery markdown block to inject |
| `--badges` | Badge markdown block to inject |
| `--check` | Check for duplicate sections only |
| `--dry-run` | Preview without writing |
| `--no-backup` | Skip `.bak.timestamp` backup |

## Safety

- Always creates a backup before modifying (unless `--no-backup`)
- Preserves all existing manual documentation
- Idempotent — running twice won't duplicate content
