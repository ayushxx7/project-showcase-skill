# Scripts Overview

The skill is powered by 6 Python scripts and 2 shell scripts:

| Script | Language | Purpose |
|---|---|---|
| `scripts/capture.py` | Python | Playwright UI screenshots |
| `scripts/scan.py` | Python | Secret leak detection |
| `scripts/audit.py` | Python | Repo health scoring |
| `scripts/inject_readme.py` | Python | README gallery injection |
| `scripts/release.py` | Python | GitHub release automation |
| `scripts/manage_metadata.py` | Python | GitHub topics/description |
| `scripts/setup.sh` | Bash | Dependency installer |
| `skills.sh` | Bash | Universal skill installer |

All Python scripts support `--help` for options.
