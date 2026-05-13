# Security & Privacy

## Secret Scanning

Before any capture or publish, run the security scanner:

```bash
python3 scripts/scan.py --dir /path/to/project
```

This prevents:
- Hardcoded API keys in source code
- `.env` files committed to git
- Secrets visible in UI screenshots

## Visual Masking

If your UI displays sensitive data (emails, API keys, personal info), use masking:

```bash
python3 scripts/capture.py --url http://localhost:3000 --mask ".api-key,.user-email,#secret-field"
```

This hides matching elements via `visibility: hidden` before taking screenshots.

## License

If a project is missing a license, the skill proposes MIT. This ensures open-source compliance.

## Health Score

The audit (`scripts/audit.py`) assigns a security score based on:
- No hardcoded secrets detected
- `.gitignore` covers `.env`, `secrets.toml`, `node_modules`, `__pycache__`
