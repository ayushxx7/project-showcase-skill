# Repo Audit (`audit.py`)

Scores a project's showcase readiness on a 0-100 scale.

## Scoring

| Category | Max | Criteria |
|---|---|---|
| Documentation | 15 | README quality, LICENSE, install instructions |
| Security | 15 | No secrets, proper .gitignore |
| Automation | 20 | setup.sh, tests, CI/CD, dependency manifest |
| Showcase | 20 | Screenshots, VHS tapes, capture.py |
| Distribution | 30 | Git remote, GitHub topics, releases |

## Usage

```bash
# Score a project
python3 scripts/audit.py --dir /path/to/project

# Score + healing plan
python3 scripts/audit.py --dir /path/to/project --heal

# JSON output (for automation)
python3 scripts/audit.py --dir /path/to/project --json
```

## Healing Plan

When run with `--heal`, lists all failed checks prioritized by category. Fix the ❌ items first to reach 100%.

## Integration

The audit is automatically run as part of the `/showcase` agent workflow. Results can be written to `REPO_HEALTH.md`:

```bash
python3 scripts/audit.py --dir . > REPO_HEALTH.md
```
