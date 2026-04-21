# Prerequisites 🛠️

To use the Project Showcase Skill, you'll need a few dependencies installed. The skill can usually set these up for you automatically, but here's the manual checklist.

## Web Recording (Playwright)
The skill uses [Playwright](https://playwright.dev/python/) for automated browser captures.

- **Requirement**: Python 3.7+
- **Install**:
  ```bash
  pip install playwright
  playwright install chromium
  ```

## Terminal Recording (VHS)
Terminal recording is powered by [VHS](https://github.com/charmbracelet/vhs) from Charmbracelet.

- **Platform**: macOS/Linux (optimized for Unix-like environments).
- **Install (macOS)**:
  ```bash
  brew install vhs
  ```
- **Install (Linux)**: Follow the [VHS installation guide](https://github.com/charmbracelet/vhs#installation).

## Other Tools
- **FFmpeg**: Required by Playwright and VHS for video/GIF processing.
- **GitHub CLI (`gh`)**: Optional but recommended for automated metadata fetching and release creation.
