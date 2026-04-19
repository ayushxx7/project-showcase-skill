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

### 1. Initial Analysis
- **Goal**: Identify project type and key routes.
- **Triggers**: "Set up a showcase for this project", "Analyze my UI for screenshots".
- **Action**: Look for configuration files (e.g., `.streamlit/config.toml`, `package.json`, `app.py`) to determine the web server type and default ports.

### 2. Automated Capture (`scripts/capture.py` & `scripts/record_cli.tape`)
- **Goal**: Generate and execute scripts to capture the UI or Terminal.
- **Triggers**: "Take screenshots of my app", "Capture the UI", "Record my CLI tool".
- **Action**: 
    - **Web**: Create or update a `capture_ui.py` script. **Execute it** to generate screenshots and videos.
    - **CLI**: Create a `.tape` file for [VHS](https://github.com/charmbracelet/vhs). **Execute `vhs < your_file.tape`** to generate GIFs/MP4s.
- **Verification & Auto-Fix (MANDATORY)**:
    - After capture, **inspect the generated assets**. 
    - **Failure Detection**: Look for 404 pages, blank screens, or `vhs` parser errors.
    - **Auto-Fix**: If a failure is detected, diagnose the cause (e.g., port mismatch, server not started, hydration lag) and **retry once** with adjusted parameters (e.g., longer `wait_for_timeout`).
    - **User Bridge**: If the second attempt fails or the "intended outcome" is ambiguous, ask the user: *"The capture shows [X], but is that what you wanted? Give me a quick prompt (e.g., 'go to /dashboard') to guide me."*
- **Cleanup (MANDATORY)**:
    - Once the showcase is verified and the README is updated, **delete all temporary files**.
    - This includes temporary `.tape` files, `capture_ui.py` scripts, and redundant screenshots not used in the final README.
    - Ensure only the final high-quality assets (e.g., `landing.png`, `demo.gif`) remain in the `showcase/` folder.

### 3. README Documentation
- **Goal**: Build a professional README with a visual gallery.
- **Triggers**: "Generate a README for this project", "Add a UI gallery to my README".
- **Action**: Use the templates in `references/readme_templates.md` to structure:
    - **UX Audit**: Ensure 'Live App' links are at the very top of the Hero section using the `for-the-badge` style with a call-to-action like 'Click Here to Explore'.
    - Hero section with high-level mission.
    - Feature breakdown with emojis.
    - **UI Gallery**: A responsive Markdown table displaying screenshots.
    - Tech Stack with icons/badges.
    - Verified Quality section (tests, coverage).

### 4. Elevator Pitch & Social Media
- **Goal**: Summarize the project for external communication.
- **Triggers**: "Write a LinkedIn post for this project", "Give me an elevator pitch".
- **Action**: Distill the project into 3 core value propositions, a "why it matters" statement, and a call to action.

## Bundled Resources

- **`scripts/capture.py`**: A generalized Playwright template that can be customized for different frameworks.
- **`references/readme_templates.md`**: A collection of high-converting README structures.

## Best Practices
- **Wait for Load**: Always include `page.wait_for_selector()` or `time.sleep()` to ensure charts and LLM responses are fully rendered.
- **Responsive Captures**: Take screenshots at multiple resolutions (Desktop: 1440x900, Mobile: 375x812).
- **Clean Environment**: Ensure no sensitive data (keys, personal info) is visible in the screenshots.
