---
name: project-showcase
description: "Automate the creation of high-quality project showcases, including UI captures using Playwright, professional README galleries, and feature summaries for portfolios or social media."
---

# Project Showcase Skill

This skill automates the "last mile" of development: showcasing your work to the world. It identifies key UI components, captures them automatically, and generates professional documentation.

## Core Workflows

### 1. Initial Analysis
- **Goal**: Identify project type and key routes.
- **Triggers**: "Set up a showcase for this project", "Analyze my UI for screenshots".
- **Action**: Look for configuration files (e.g., `.streamlit/config.toml`, `package.json`, `app.py`) to determine the web server type and default ports.

### 2. Automated Capture (`scripts/capture.py`)
- **Goal**: Generate and execute a Playwright script to capture the UI.
- **Triggers**: "Take screenshots of my app", "Capture the UI for the showcase".
- **Action**: Create or update a `capture_ui.py` script. It should:
    - Launch a browser (headless or headed).
    - Navigate to local or remote URLs.
    - Interact with key elements (fill inputs, click buttons).
    - Save high-res screenshots to the `showcase/` folder.

### 3. README Documentation
- **Goal**: Build a professional README with a visual gallery.
- **Triggers**: "Generate a README for this project", "Add a UI gallery to my README".
- **Action**: Use the templates in `references/readme_templates.md` to structure:
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
