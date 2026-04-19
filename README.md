# Project Showcase Skill 🎬✨
**Automated Documentation | CLI Recording | Playwright Showcases**

[![Tested on Gemini](https://img.shields.io/badge/Tested_on-Gemini_CLI-8E44AD?style=for-the-badge&logo=google-gemini&logoColor=white)](https://github.com/google/gemini-cli)
[![Works on Claude](https://img.shields.io/badge/Works_on-Claude_Code-D97757?style=for-the-badge&logo=anthropic&logoColor=white)](https://github.com/anthropic/claude-code)
[![Universal Agent Support](https://img.shields.io/badge/Support-Universal_Agents-green?style=for-the-badge)](https://github.com/ayushxx7/project-showcase-skill)

[![Live App](https://img.shields.io/badge/Live_App-Click_Here_to_Explore-blue?style=for-the-badge&logo=vercel)](https://github.com/ayushxx7/project-showcase-skill)
[![CLI Demo](https://img.shields.io/badge/CLI_Demo-View_Terminal_Recording-green?style=for-the-badge&logo=asciinema)](showcase/cli_power_demo.gif)

**Project Showcase Skill** automates the "last mile" of development: showcasing your work to the world. It is a high-performance **developer tool** for **workflow automation**, creating professional **visual galleries** and **automated documentation** for your projects.

## 📦 Installation

### 1. Install the Skill
Use the universal installer to add this to your Gemini CLI or Claude Code:
```bash
curl -sSL https://raw.githubusercontent.com/ayushxx7/project-showcase-skill/main/skills.sh | bash
```

### 2. Setup Dependencies
Once installed, navigate to the skill directory and run the environment setup (installs Playwright & VHS):
```bash
./scripts/setup.sh
```

## 🚀 Overview
Stop sending boring READMEs. This skill identifies key UI and CLI components, captures them automatically using **Playwright** and **VHS**, and generates professional, high-conversion documentation.

- 📟 **Automated CLI Recording**: Generate high-fidelity GIFs of your terminal sessions with VHS.
- 🎬 **Smart Browser Capture**: Automated Playwright videos and screenshots with built-in verification.
- 🛠️ **Workflow Automation**: One-command documentation that cleans up after itself.

## 🎬 Showcase Assets
| 🎬 Web Demo | 📟 CLI Demo (GIF) |
| :---: | :---: |
| ![Landing](showcase/landing.png) | ![CLI Demo](showcase/cli_power_demo.gif) |

## 🛠️ Tools Used
- **Playwright**: For high-res UI screenshots and screen recordings.
- **VHS**: For automated terminal session recording and GIF generation.
- **Shields.io**: For professional `for-the-badge` call-to-action links.

## ⚙️ Quick Start
1. **Record Terminal**: `vhs < showcase/record_cli.tape`
2. **Capture UI**: `python3 showcase/capture_ui.py`
3. **Generate README**: Use the templates in `references/readme_templates.md`.
