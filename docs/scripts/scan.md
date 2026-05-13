# Security Scan (`scan.py`)

Prevents accidental secret leaks before publishing.

## Features

- Detects 10+ secret patterns: OpenAI, Anthropic, Google, AWS, Stripe, GitHub tokens
- Validates `.gitignore` covers critical files (`.env`, `secrets.toml`, etc.)
- Safe snippet display — only shows first/last 4 chars of found secrets
- Exit code 1 on findings (CI-friendly)

## Usage

```bash
python3 scripts/scan.py
python3 scripts/scan.py --dir /path/to/project
```

## Detected Patterns

| Pattern | Example |
|---|---|
| OpenAI Key | `sk-...` (48 chars) |
| Anthropic Key | `sk-ant-...` (93 chars) |
| Google API Key | `AIza...` (35 chars) |
| AWS Access Key | `AKIA...` (16 chars) |
| Stripe Secret Key | `sk_live_...` (24 chars) |
| GitHub PAT | `ghp_...` (36 chars) |
| Firebase URL | `*.firebaseapp.com` |
| Generic API Key | `api_key = "..."` |
