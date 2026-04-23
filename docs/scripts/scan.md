# Security Scan (`scan.py`) 🛡️

`scan.py` is a privacy-first security scanner designed to prevent accidental leaks of sensitive information before a project is showcased.

## Key Features

- **🔍 Pattern Matching**: Detects 10+ common hardcoded secrets, including OpenAI, Anthropic, Google, AWS, Stripe, and GitHub keys.
- **🛡️ .gitignore Validation**: Verifies that critical files like `.env`, `secrets.toml`, and `.streamlit/secrets.toml` are listed in `.gitignore`.
- **🚀 Pre-Capture Verification**: Integrated into the `/showcase` and `/capture` workflows to ensure a "Clean State" before screenshots are taken.
- **✨ Safe Snippets**: When a secret is found, the script only shows the first and last few characters (e.g., `sk-a...b123`) to help you identify the leak without logging the full secret.
- **✅ Readiness Scoring**: Contributes directly to the security component of the Repo Health Score.

## Usage

The script is invoked automatically by the agent before any visual capture, but can be run manually:

```bash
python3 scripts/scan.py
```

### Options
- `--dir`: The directory to scan (defaults to the current directory).

## Why This Matters

When showcasing a project, it's easy to accidentally include a `.env` file or a hardcoded key in a screenshot. `scan.py` acts as a "safety net," ensuring that your public showcase remains professional and secure.
