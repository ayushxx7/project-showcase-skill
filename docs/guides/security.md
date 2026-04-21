# Security & Privacy 🛡️

Security is a top priority for the Project Showcase Skill. Before any capture or documentation update, the skill performs a several automated checks.

## 🛡️ Secret Scan & Privacy Check

Before any UI capture or terminal recording, the agent:
1. **Scans for API Keys**: Searches for OpenAI, Anthropic, AWS, and other common key patterns in the source code.
2. **Visual Privacy**: During UI capture, the agent ensures no sensitive keys are visible in the rendered UI. If detected, the agent autonomously blurs or masks them before saving the screenshot to prevent accidental leaks in the showcase.
3. **Masking Sensitive UI**: The `capture.py` script can be configured with CSS selectors to hide specific elements (like API key fields or email addresses) before taking screenshots.

## 📜 MIT License by Default

If a project is missing a license, the skill will propose adding an **MIT License**. This ensures your project is open-source compliant and ready for the community.

## 🩺 Repo Health Score

The skill assigns a **Repo Health Score** (0-100) based on:
- **Documentation**: Presence of README and LICENSE.
- **Security**: Secret scan results.
- **Visuals**: High-res screenshots and terminal recordings.
- **Distribution**: Presence of "Live App" links and GitHub metadata.
