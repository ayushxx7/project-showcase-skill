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
- **License Verification (MANDATORY)**:
    - Check if the project has a `LICENSE` file.
    - If missing, the agent **MUST** inform the user: *"Your project is missing a LICENSE. Adding one makes it officially open-source and accessible."*
    - Propose adding an **MIT License** as a default, but allow the user to provide a different license type.
- **Dependency Check (MANDATORY)**:
...
    - Before any capture, the agent **MUST** check if `playwright` (Python) and `vhs` (System) are installed.
    - If missing, the agent **MUST** autonomously run `./scripts/setup.sh` or the equivalent commands (`pip install playwright`, `brew install vhs`) without asking, unless explicitly restricted.
- **Triggers**: "Showcase this project. Start the server and capture the UI.", "Set up a showcase for this project", "Analyze my UI for screenshots".
- **Action**: Look for configuration files to determine the web server type and default ports.

### 2. Automated Capture (`scripts/capture.py` & `scripts/record_cli.tape`)
- **Goal**: Generate and execute scripts to capture the UI or Terminal.
- **Triggers**: "Record a terminal demo of my CLI tool and add it to the README.", "Take screenshots of my app", "Capture the UI", "Record my CLI tool".
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
- **Action**: Use the templates in `references/readme_templates.md` to structure content.
- **Mandatory Sections**:
    - **UX Audit**: Top-level 'Live App' badges.
    - **Hero Section**: Mission statement and value prop.
    - **Visual Gallery**: The captured Web/CLI assets.
    - **How to Use**: Clear instructions on how to run or interact with the project.
    - **Tech Stack**: Iconography-led list of tools.
- **Preservation Policy (CRITICAL)**: 
...
    - **NEVER** overwrite an existing README entirely if it contains custom developer documentation.
    - **Surgical Injection**: Only inject the `Showcase Assets`, `Tech Stack`, or `Visual Gallery` sections.
    - **Verify Before Commit**: Always check if the user has manually written "How it Works" or "Architecture" sections and ensure these are **preserved and merged**, not replaced.
- **UX Audit**: Ensure 'Live App' links are at the very top of the Hero section.

### 4. Elevator Pitch & Social Media
- **Goal**: Summarize the project for external communication.
- **Triggers**: "Write a LinkedIn post and an elevator pitch for this showcase.", "Write a LinkedIn post for this project", "Give me an elevator pitch".
- **Action**: Distill the project into 3 core value propositions, a "why it matters" statement, and a call to action.

## Bundled Resources

- **`scripts/capture.py`**: A generalized Playwright template that can be customized for different frameworks.
- **`references/readme_templates.md`**: A collection of high-converting README structures.

## Best Practices
- **Wait for Load**: Always include `page.wait_for_selector()` or `time.sleep()` to ensure charts and LLM responses are fully rendered.
- **Responsive Captures**: Take screenshots at multiple resolutions (Desktop: 1440x900, Mobile: 375x812).
- **Clean Environment**: Ensure no sensitive data (keys, personal info) is visible in the screenshots.
