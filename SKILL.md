---
name: project-showcase
description: "Automate the creation of high-quality project showcases, including UI captures using Playwright, professional README galleries, and feature summaries for portfolios or social media."
---

# Project Showcase Skill

This skill automates the "last mile" of development: showcasing your work to the world. It identifies key UI components, captures them automatically, and generates professional documentation.

## Commands
- `/showcase`: **The Magic Pill** (Default). Runs UI Capture + Terminal Record + README Update + GitHub Release + Metadata (About/Labels).
- `/select`: Opens an interactive UI to select specific features to run.
- `/capture`: Trigger high-fidelity UI captures using Playwright.
- `/record`: Record a terminal demo using VHS.
- `/audit`: Perform a Repo Health Audit (Scoring & Healing Plan).
- `/readme`: Surgically update the README with visual galleries and badges.
- `/release`: Create an official GitHub Release (v0.1.0-alpha).
- `/metadata`: Auto-detect and update GitHub "About" and "Topics".
- `/socials`: Generate ready-to-post content for LinkedIn and Reddit.
- `/scan`: Run a privacy-first security scan for secrets and `.env` leaks.
- `/license`: Verify or add an MIT License.
- `/setup`: Ensure all dependencies (Playwright, VHS, ffmpeg) are installed.

## Core Workflows
### 1. Initial Analysis & Auto-Setup
- **Goal**: Identify project type and ensure the environment is ready.
- **Autonomous Asset Generation**:
    - If UI captures or Terminal recordings are missing, the agent **MUST NOT** skip them or leave broken links.
    - **Step 1**: Attempt real capture via Playwright/VHS.
    - **Step 2**: If Step 1 fails, generate a high-fidelity "Visual Architecture" diagram or a stylized SVG that represents the project's logic.
    - **Outcome**: Every showcased repo MUST have a visual element, real or generated.
- **Framework Detection & Secret Management**:
    - **Streamlit Projects**: Detect via `streamlit_app.py` or `streamlit` in `requirements.txt`.
    - **Secret Migration**: If detected, propose migrating `.env` keys to `.streamlit/secrets.toml` to align with Streamlit Cloud standards.
- **Security & Privacy Scan (`/scan`)**:
    - Before any capture, the agent should scan the project for common API key patterns (OpenAI, Anthropic, Google, AWS, etc.).
    - If secrets are found in the source code or `.env` files, the agent should warn the user and propose adding them to `.gitignore`.
- **License Verification (`/license`)**:
    - Check if the project has a `LICENSE` file. If missing, propose adding an MIT License.
- **Dependency Check (`/setup`)**:
    - Before any capture, the agent should check if `playwright` (Python), `vhs` (System), and `ffmpeg` are installed.

### 2. Automated Capture (`/capture`, `/record`)
- **UI Capture**: Uses `scripts/capture.py`. Supports responsive, full-page, masking, and dark mode.
- **Terminal Record**: Uses `scripts/record_cli.tape` and VHS.
- **Verification & Auto-Fix**:
    - After capture, inspect the generated assets. 
    - **Failure Detection**: Look for 404 pages, blank screens, or `vhs` parser errors.
- **Cleanup**:
    - Once the showcase is verified and the README is updated, delete all temporary files.
    - Ensure only the final high-quality assets (e.g., `landing.png`, `demo.gif`) remain in the `showcase/` folder.

### 3. README Documentation & Hygiene (`/readme`)
- **Goal**: Build a professional README that "Shows first, tells second."
- **Read the Docs (Optional / Non-UI Focus)**:
    - **Detection**: If the project is a CLI tool, library, or back-end API (non-UI), the agent SHOULD suggest setting up "Read the Docs" using MkDocs.
    - **Action**: Propose creating a basic `mkdocs.yml` and `docs/` structure.
    - **User Choice**: Always ask: *"Since this is a [CLI/Library], would you like me to set up a 'Read the Docs' style documentation site as well?"*
- **Asset Integrity**: 
    - **NEVER** include broken image links or placeholders (like `landing.png` if it doesn't exist). 
    - If a real capture is impossible, the agent **MUST** generate a high-fidelity alternative (e.g., a Mermaid diagram).
- **The "Vibe-First" README**:
    - **No Metadata Bloat**: Remove the diagnostic health table and the checkmark/percentage lines (e.g., `✅ Secure | ✅ 92/100`). These feel robotic and cluttered.
    - **Natural Context Sentence**: Instead of keywords, generate a single, high-signal sentence that naturally blends the project's essence, tech stack, and purpose. 
        - *Example*: "A privacy-first AI agent built with React and TypeScript for automated UI auditing."
        - *Rule*: This sentence should feel like a human-written subtitle, not an audit report.
    - **External Health Audit**: All detailed scoring, health tables, and diagnostic data MUST be moved to a dedicated external repository/file (e.g., `ayush-repos-health`) or kept at the very bottom of a separate `REPO_HEALTH.md`. The main README remains focused strictly on the product and the "Vibe".
- **Surgical Injection & Deduplication**:
    - **Never Duplicate**: If a section already exists (e.g., "Architecture", "Features", "Installation"), the agent **MUST NOT** add a second version.
    - **Superiority Choice**: Compare existing content with generated content. If the generated version is better (clearer, more visual), **replace** the old one.
    - **Hybrid Merge**: If both contain unique value, merge them into a single cohesive section.
    - **Zero Redundancy**: A single, streamlined source of truth for every project aspect. No redundant headers.
- **Top Fold Placement**: Always aim to place the Visual Gallery immediately after the elevator pitch to maximize initial impact.
- **Agentic Badges**: 
    - **"Tested on Gemini CLI"**: This badge MUST ONLY be applied to agentic projects (e.g., Skills, MCP Servers, Agent-specific tools). 
    - **DO NOT** add this badge to general web apps, CLIs, or libraries that are not specifically built for or tested as AI agent extensions.

### 4. Professional Delivery & Release (`/release`, `/metadata`)
- **Goal**: Package the project for official distribution.
- **Professional GitHub Release (`/release`)**:
    - Create an automated **Release (e.g., v0.1.0-alpha/beta/stable)** upon completion of the showcase.
- **GitHub Metadata (`/metadata`)**:
    - Detect and update the "About" description and "Topics" (labels) using `scripts/manage_metadata.py`.
- **Verification & Validation**:
    - **Live Repository Audit**: 
        - Before finalizing, visually confirm that the **README**, **Badges**, **Visual Gallery**, and **GitHub Topics** are rendered correctly.
    - **Clean State**: If a force-push was required to clean secrets, ensure the release is re-associated with the latest clean commit hash.

### 5. Repo Health & Healing (`/audit`)
- **Goal**: Diagnose the project's "Readiness" and offer surgical improvements.
- **Scoring**: Assign a weighted score on a **0-100 Scale**.
- **Checklist Items**:
    - Documentation (README, LICENSE).
    - Security (Secrets, `.gitignore`).
    - Automation (`setup.sh`, Tests).
    - Showcase (Screenshots, VHS).
    - **Bonus (+5 pts)**: Extended Documentation (MkDocs/Read the Docs) - *Especially recommended for non-UI apps*.
- **Thoughtful Prescription**: Before fixing, the agent should present a **"Healing Plan"**.
- **The Heal**: Only after user approval, apply the fixes surgically and re-audit to show the improved score.

### 6. Social Media & PR (`/socials`)
- **Goal**: Summarize the project for external communication.
- **Formats**:
    - **LinkedIn**: Professional, value-driven, and badge-focused.
    - **Reddit**: Technical, developer-to-developer, and GIF-centric.

## Best Practices
- **Wait for Load**: Always include `page.wait_for_selector()` or `time.sleep()` to ensure charts and LLM responses are rendered.
- **Verified Quality**: Run `python3 tests/test_readme_injection.py` to confirm the injection logic is still sound.
- **Documentation Hygiene**: Never sacrifice README beauty for diagnostic data. Keep the README for the "Vibe" and move the "Audit" to `REPO_HEALTH.md`.

---
*Built with ❤️ for Vibe Coders everywhere.*
