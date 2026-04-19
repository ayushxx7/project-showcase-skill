# Project Showcase Skill 🎬✨
**The Magic Pill for Shipping Professional Project Showcases**

[![Tested on Gemini](https://img.shields.io/badge/Tested_on-Gemini_CLI-8E44AD?style=for-the-badge&logo=google-gemini&logoColor=white)](https://github.com/google/gemini-cli)
[![Works on Claude](https://img.shields.io/badge/Works_on-Claude_Code-D97757?style=for-the-badge&logo=anthropic&logoColor=white)](https://github.com/anthropic/claude-code)
[![Universal Agent Support](https://img.shields.io/badge/Support-Universal_Agents-green?style=for-the-badge)](https://github.com/ayushxx7/project-showcase-skill)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

[![Live App](https://img.shields.io/badge/Live_App-Click_Here_to_Explore-blue?style=for-the-badge&logo=vercel)](https://github.com/ayushxx7/project-showcase-skill)
[![CLI Demo](https://img.shields.io/badge/CLI_Demo-View_Terminal_Recording-green?style=for-the-badge&logo=asciinema)](showcase/cli_power_demo.gif)

**Project Showcase Skill** is the "magic pill" for developers who hate documentation but love showing off. Automate the "last mile" of your workflow—generating high-fidelity visual galleries and surgical README updates in seconds.

## 📦 Installation in 30 Seconds

### 1. Install the Skill
Add it to Gemini CLI, Claude Code, or any agent using the universal installer:
```bash
curl -sSL https://raw.githubusercontent.com/ayushxx7/project-showcase-skill/main/skills.sh | bash
```

### 2. Auto-Setup
The skill is self-configuring. On first trigger, it will autonomously set up **Playwright** and **VHS** for you. Or run it manually:
```bash
./scripts/setup.sh
```

## 🪄 How to Use

Once installed, just talk to your agent (Gemini or Claude) in the terminal. Try these "magic phrases":
- **For Web Apps**: *"Showcase this project. Start the server and capture the UI."*
- **For Repo Health**: *"Audit this project. What is my readiness score?"*
- **For CLI Tools**: *"Record a terminal demo of my CLI tool and add it to the README."*
- **For Socials**: *"Write a LinkedIn post and a Reddit thread for this showcase."*
- **For Galleries**: *"Add a visual gallery to my existing README without overwriting my notes."*

## ✨ The Magic Features
### 🎬 Professional UI Capture (`scripts/capture.py`)
- **📱 Responsive Ready**: Desktop, Tablet, and Mobile viewports in one go.
- **🖼️ Full-Page Screenshots**: Automatically scroll and stitch the entire page.
- **🎭 Visual Privacy**: Mask sensitive data (like API keys or emails) using CSS selectors.
- **🌙 Dark Mode Support**: Capture your UI in both light and dark themes.
- **⚡ Network-Aware**: Waits for `networkidle` to ensure your app is fully hydrated.
- **Privacy-First Security Scan**: Automatically detects and warns about sensitive API keys (OpenAI, Anthropic, etc.) or `.env` leaks before capture.
- **Repo Health & Healing (0-10 Audit)**: Let your "Project Resident Doctor" scan your repo for missing licenses, documentation gaps, and security risks. It assigns a **Health Score** and offers a **Surgical Healing Plan** to get you to 10/10 readiness.
- **Auto-Verification**: Detects 404s, blank screens, and hydration lag.
- **Smart Retries**: If the UI isn't ready, the skill waits, reloads, and fixes the capture autonomously.
- **Video Recording**: High-res `.webm` recordings of your browser interactions.

## 🎬 Showcase Gallery

- **VHS Integration**: Scripted terminal sessions that "type" themselves into high-fidelity GIFs.
- **Zero Effort**: Just tell the agent what commands to run; it generates the `.tape` and the GIF for you.

### 🛡️ Dev-First README Injection
- **Smart License Verification**: Automatically detects missing licenses and proposes an MIT default to keep your project open-source compliant.
- **Preserve & Merge**: It identifies your manual documentation and injects visual galleries around it.
- **UX Audit**: Automatically places high-conversion "Live App" badges at the very top.
- **Auto-Cleanup**: Generates the assets, updates the docs, and deletes the temporary scripts.

## 📊 Repo Health: 100 / 100 (Pristine)
This project "eats its own dog food" and maintains a perfect readiness score.

| Category | Item | Status | Score |
| :--- | :--- | :--- | :--- |
| **Documentation** | README, LICENSE, SKILL.md | ✅ Complete | 15 / 15 |
| **Security** | Secret Scan & .gitignore | ✅ Secure | 15 / 15 |
| **Automation** | setup.sh & Passing Tests | ✅ Working | 20 / 20 |
| **Showcase** | High-res Assets & VHS | ✅ Verified | 20 / 20 |
| **Distribution** | Live App & Official Release | ✅ Distributed | 30 / 30 |

| 🎬 Web Showcase | 📟 CLI Power Demo (GIF) |
| :---: | :---: |
| ![Landing](showcase/landing.png) | ![CLI Demo](showcase/cli_power_demo.gif) |

## 🛠️ Tech Stack
- **Engine**: Python 3.x, Playwright (Browser Automation)
- **Terminal**: VHS (CLI Scripting)
- **Agent Protocol**: Universal Skill Schema (Gemini, Claude, Generic)
- **Design**: Shields.io for modern CTA badges

## 📜 License
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---
*Built with ❤️ for Vibe Coders everywhere. Stop documenting. Start showcasing.*
