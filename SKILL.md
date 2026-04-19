---
name: project-showcase
description: "Automate the creation of high-quality project showcases, including UI captures using Playwright, professional README galleries, and feature summaries for portfolios or social media."
---

# Project Showcase Skill

This skill automates the "last mile" of development: showcasing your work to the world. It identifies key UI components, captures them automatically, and generates professional documentation.

## Prerequisites
- **Web Recording**: `playwright` (Python/JS). Run `playwright install chromium`.
- **Terminal Recording (macOS/Linux)**: [VHS](https://github.com/charmbracelet/vhs). Install via `brew install vhs`. 
    - *Note*: Terminal recording is currently optimized for Unix-like environments.

## Core Workflows
### 1. Initial Analysis & Auto-Setup
- **Goal**: Identify project type and ensure the environment is ready.
- **Framework Detection & Secret Management**:
    - **Streamlit Projects**: Detect via `streamlit_app.py` or `streamlit` in `requirements.txt`.
    - **Secret Migration**: If detected, propose migrating `.env` keys to `.streamlit/secrets.toml` to align with Streamlit Cloud standards.
    - **Cloud Readiness**: Provide instructions for the user to update their Cloud Dashboard secrets after migration.
- **TOML Support**: Prefer `.toml` (e.g., `pyproject.toml`, `secrets.toml`) for configuration in modern frameworks, while maintaining fallback support for `.env`.
- **Security & Privacy Scan**:
    - Before any capture, the agent should scan the project for common API key patterns (OpenAI, Anthropic, Google, AWS, etc.).
    - If secrets are found in the source code or `.env` files, the agent should warn the user and propose adding them to `.gitignore`.
    - **Visual Privacy**: During UI capture, ensure no sensitive keys are visible in the rendered UI. If detected, the agent should blur or mask them before saving the screenshot.
- **License Verification**:
...
    - Check if the project has a `LICENSE` file.
    - If missing, inform the user: *"Your project is missing a LICENSE. Adding one makes it officially open-source and accessible."*
    - Propose adding an MIT License as a default, but allow the user to provide a different license type.
- **GitHub Discoverability (Labels)**:
    - Always scan the `requirements.txt`, `package.json`, and project structure to identify the tech stack.
    - Propose and apply GitHub Topics using a single comma-separated command: `gh repo edit --add-topic "topic1,topic2,topic3"`.
    - **Priority Topics**: Include the framework (e.g., `streamlit`, `react`), database (e.g., `neondb`, `mongodb`), and core feature (e.g., `ai-agent`, `scraper`).
- **Dependency Check**:
    - Before any capture, the agent should check if `playwright` (Python), `vhs` (System), and `ffmpeg` (for Video-to-GIF) are installed.
    - If missing, the agent should run `./scripts/setup.sh` or the equivalent commands (`pip install playwright`, `brew install vhs`, `brew install ffmpeg`) to ensure the environment is ready.
- **Triggers**: "Showcase this project. Start the server and capture the UI.", "Set up a showcase for this project", "Analyze my UI for screenshots".
- **Action**: Look for configuration files to determine the web server type and default ports.

### 2. Automated Capture (`scripts/capture.py` & `scripts/record_cli.tape`)
- **Goal**: Generate and execute scripts to capture the UI or Terminal with surgical precision.
- **Safety & Precision Protocols**:
    - **Protocol 1: Selector Discovery Phase**: 
        - Before interaction, the agent MUST list all interactive labels, placeholders, and buttons on the page.
        - Use this to distinguish between similar elements (e.g., search bars vs. filters) to avoid "blind guessing."
    - **Protocol 2: Two-Phase Hydration**: 
        - **Pre-load Phase**: Navigate to the URL and wait for a "Stable State" (e.g., specific H1 appearance or removal of loading spinners).
        - **Recording Phase**: Start video recording ONLY after the app is confirmed to be interactive.
    - **Protocol 3: Automated Video Post-Processing (The "Clean Cut")**:
        - Use `ffmpeg` to trim the start of recordings (e.g., `-ss 2`) to remove residual loading frames.
        - Optimize the GIF palette for high-clarity/low-filesize to ensure README performance.
    - **Protocol 4: Visual Audit & Verification**:
        - After generation, the agent MUST perform a "Verification Step."
        - Describe the intended flow and confirm the logs show the exact selectors used matched that intent.
        - If a fallback selector was used, re-verify if the intended element was missed.
- **Rich Media & Video-to-GIF**: 
    - Support video recording via Playwright (`record_video_dir`).
    - Use `ffmpeg` to transform `.webm` recordings into optimized `.gif` files for GitHub README compatibility.
    - Target `demo.gif` for the visual gallery.
- **Hydration-Aware Captures**: 
    - Include configurable "hydration delays" (e.g., 10-20 seconds) for JS-heavy frameworks like Streamlit or Dash to ensure the UI is fully interactive before taking screenshots.
- **Comparative Demonstration (A/B Mode)**:
    - Perform a default action (e.g., a standard search), capture it, toggle a feature (e.g., enable "AI Assistant"), and capture the improved result in a single continuous flow to demonstrate the value proposition.
- **Triggers**: "Record a terminal demo of my CLI tool and add it to the README.", "Take screenshots of my app", "Capture the UI", "Record my CLI tool", "Create an A/B demo".
- **Action**: 
    - **Web**: Create or update a `capture_ui.py` script. Execute it to generate screenshots and videos.
    - **CLI**: Create a `.tape` file for [VHS](https://github.com/charmbracelet/vhs). Execute `vhs < your_file.tape` to generate GIFs/MP4s.
- **Verification & Auto-Fix**:
    - After capture, inspect the generated assets. 
    - **Failure Detection**: Look for 404 pages, blank screens, or `vhs` parser errors.
    - **Auto-Fix**: If a failure is detected, diagnose the cause (e.g., port mismatch, server not started, hydration lag) and retry once with adjusted parameters (e.g., longer `wait_for_timeout`).
    - **User Bridge**: If the second attempt fails or the "intended outcome" is ambiguous, ask the user: *"The capture shows [X], but is that what you wanted? Give me a quick prompt (e.g., 'go to /dashboard') to guide me."*
- **Cleanup**:
    - Once the showcase is verified and the README is updated, delete all temporary files.
    - This includes temporary `.tape` files, `capture_ui.py` scripts, and redundant screenshots not used in the final README.
    - Ensure only the final high-quality assets (e.g., `landing.png`, `demo.gif`) remain in the `showcase/` folder.

### 3. README Documentation
- **Goal**: Build a professional README with a visual gallery.
- **Triggers**: "Add a visual gallery to my existing README without overwriting my notes.", "Generate a README for this project".
- **Action**: Use the templates in `references/readme_templates.md` to structure content.
- **Mandatory Sections**:
    - **UX Audit**: Top-level 'Live App' badges.
    - **Hero Section**: Mission statement and value prop.
    - **Visual Gallery**: The captured Web/CLI assets.
    - **Repo Health Score**: A diagnostic table showing the 0-10 readiness score across Documentation, Security, Automation, and Showcase categories.
    - **How to Use**: Clear instructions on how to run or interact with the project.
    - **Tech Stack**: Iconography-led list of tools.
    - **License**: Clear statement of the project's open-source license.
- **Preservation Policy**: 
    - Do not overwrite an existing README entirely if it contains custom developer documentation.
    - **Surgical Injection**: Only inject the `Showcase Assets`, `Tech Stack`, or `Visual Gallery` sections.
    - **Verify Before Commit**: Check if the user has manually written "How it Works" or "Architecture" sections and ensure these are preserved and merged, not replaced.
- **UX Audit**: Ensure 'Live App' links are at the very top of the Hero section.

### 4. Professional Delivery & Release
- **Goal**: Package the project for official discovery and distribution.
- **Professional GitHub Release**:
    - Create an automated **"Alpha Release" (v0.1.0-alpha)** upon completion of the showcase.
    - **Title Format**: `v0.1.0-alpha: [High-Impact Feature Name]` (e.g., `v0.1.0-alpha: AI-Powered Search`).
    - **Notes Preparation**: NEVER pass notes as raw strings with `\n` to the CLI. Always create a temporary `release_notes.md` and use `gh release create <tag> --notes-file release_notes.md`.
    - **Release Structure**:
        - 🚀 **Live App**: Prominent link at the very top.
        - 🌟 **Highlights**: Bulleted list of core value propositions (AI features, DB integration, Security, etc.).
        - 🛠️ **Tech Stack**: Brief mention of the engines used.
- **Verification & Validation**:
    - **URL Check**: Verify the release formatting by checking the output URL.
    - **Clean State**: If a force-push was required to clean secrets, ensure the release is re-associated with the latest clean commit hash.
    - **Repo Health Sync**: Ensure the Repo Health Score table in the README reflects the new Release status.

### 5. Repo Health & Healing (Audit & Fix)
- **Goal**: Diagnose the project's "Readiness" and offer surgical improvements.
- **Triggers**: "Audit this repository", "How healthy is my project?", "Heal this repo".
- **Action**:
    - **Diagnosis**: Perform a scan for:
        - **Documentation**: README, LICENSE, `.env.example`.
        - **Security**: Leaked API keys, un-ignored `.env` files.
        - **Automation**: Presence of `setup.sh` or installation scripts.
        - **Showcase**: Presence of `showcase/` assets and `.tape` files.
        - **Quality (TDD)**: Presence of `tests/` directory and passing test status.
    - **Scoring**: Assign a weighted score on a **0-100+ Scale** (Bonus points allowed):
        - **Documentation (20 pts)**: README, LICENSE, `.env.example`.
        - **Security (20 pts)**: No leaked keys, `.env` in `.gitignore`.
        - **Automation (20 pts)**: Working setup and install scripts.
        - **Quality/TDD (20 pts)**: Tests present and passing.
        - **Showcase (20 pts)**: High-res screenshots and VHS demos.
        - **Bonus (+5-10 pts)**: GitHub Actions, multi-platform support, or interactive demos.
    - **Thoughtful Prescription**: Before fixing, the agent should present a **"Healing Plan"**:
        - List the specific missing or broken items.
        - Explain *why* they matter (e.g., "Missing LICENSE prevents open-source contribution").
        - Describe exactly what files will be created or modified.
    - **The Heal**: Only after user approval, apply the fixes surgically and re-audit to show the improved score.

### 6. Elevator Pitch & Social Media
- **Goal**: Summarize the project for external communication.
- **Triggers**: "Write a LinkedIn post and an elevator pitch for this showcase.", "Write a Reddit post for this project", "Give me an elevator pitch".
- **Action**: Distill the project into 3 core value propositions, a "why it matters" statement, and a call to action.
- **Formats**:
    - **LinkedIn**: Professional, value-driven, and badge-focused.
    - **Reddit**: Technical, developer-to-developer, and GIF-centric (targeting `r/webdev`, `r/programming`).
    - **Elevator Pitch**: A 30-second high-impact verbal summary.

## Bundled Resources
## Bundled Resources

- **`scripts/capture.py`**: A generalized Playwright template that can be customized for different frameworks.
- **`references/readme_templates.md`**: A collection of high-converting README structures.

## Mandatory Execution Checklist
Before finalizing any showcase or delivery, the agent MUST go through this checklist one-by-one to verify completion:

- [ ] **Analysis**: Framework detected (Streamlit/React/etc.) and Secrets scanned?
- [ ] **Security**: `.env` migrated/ignored and UI masks applied?
- [ ] **Environment**: `setup.sh` run and all dependencies (Playwright, VHS, ffmpeg) verified?
- [ ] **Capture**: Selector Discovery performed and Stability confirmed?
- [ ] **Assets**: Clean-cut GIF and high-res screenshots generated?
- [ ] **Audit**: Visual verification performed against intended flow?
- [ ] **Documentation**: README surgically updated with Visual Gallery and Repo Health Score?
- [ ] **Discoverability**: GitHub Topics applied via `gh repo edit`?
- [ ] **Release**: v0.1.0-alpha created with `--notes-file` and verified via URL?

*Note: All items have equal priority and must be completed unless explicitly confirmed as out of scope.*

## Best Practices
- **Wait for Load**: Always include `page.wait_for_selector()` or `time.sleep()` to ensure charts and LLM responses are fully rendered.
- **Verified Quality**: After performing surgical README updates, the agent should run `python3 tests/test_readme_injection.py` to confirm the injection logic is still sound.
- **Responsive Captures**: Take screenshots at multiple resolutions (Desktop: 1440x900, Mobile: 375x812).
- **Clean Environment**: Ensure no sensitive data (keys, personal info) is visible in the screenshots.
