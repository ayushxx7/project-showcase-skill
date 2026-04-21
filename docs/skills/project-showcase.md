# Project Showcase Skill 🎬

This skill automates the "last mile" of development: showcasing your work to the world. It identifies key UI components, captures them automatically, and generates professional documentation.

## Core Workflows

### 1. Initial Analysis & Auto-Setup
- **Goal**: Identify project type and ensure the environment is ready.
- **Security Scan**: Scans for common API key patterns (OpenAI, Anthropic, Google, AWS, etc.) before any capture.
- **License Verification**: Checks for a `LICENSE` file. Proposes MIT if missing.

### 2. Automated Capture
- **Web UI**: Executes `scripts/capture.py` to capture screenshots and videos.
- **Terminal CLI**: Executes `scripts/record_cli.tape` using VHS to record terminal sessions.
- **Verification & Auto-Fix**: Inspects assets for 404s, blank screens, or recording errors. If a failure is detected, it diagnoses the cause (e.g., port mismatch, hydration lag) and retries once with adjusted parameters.

### 3. GitHub Discoverability
- **Topics**: The skill scans your tech stack and purpose to suggest relevant GitHub Topics.
- **Automation**: Uses `gh repo edit --add-topic` to improve your project's searchability on GitHub.

### 3. README Documentation & Hygiene
- **Vibe-First README**: Prioritizes "Showing" over "Telling."
- **Surgical Injection**: Injects visual galleries without overwriting your manual notes.
- **UX Audit**: Adds high-conversion badges (e.g., "Live App").
- **Deduplication**: Ensures sections like "Features" or "Installation" are not duplicated.

### 4. Repo Health & Healing (Audit & Fix)
- **Scoring**: Assigns a weighted score on a 0-100 scale.
- **Healing Plan**: Presents a diagnostic report and offers surgical improvements.

---
*Built for Vibe Coders everywhere.*
