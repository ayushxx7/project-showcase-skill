# UI Capture (`capture.py`) 📸

`capture.py` is a robust Python script leveraging [Playwright](https://playwright.dev/python/) to automate the process of capturing high-quality visual assets from any web application.

## Key Features

- **📱 Responsive Viewports**: Automatically captures Desktop (1920x1080), Tablet (768x1024), and Mobile (375x667) screenshots.
- **🖼️ Full-Page Stitches**: Intelligently scrolls and stitches the entire page for long landing pages.
- **🎭 Element Masking**: Uses CSS selectors to hide sensitive data (emails, API keys, etc.) before taking the shot.
- **🌙 Theme Switching**: If supported by the app, it can trigger dark/light mode for comparative captures.
- **⚡ Hydration Awareness**: Waits for `networkidle` and specific selectors to ensure the UI is fully loaded.
- **🎥 Video Recording**: Optionally records a `.webm` video of interactions (scrolling, clicking).

## Usage

The script is typically invoked by the agent, but can be run manually:

```bash
python3 scripts/capture.py --url http://localhost:3000 --output showcase/landing.png
```

### Common Arguments
- `--url`: The target application URL.
- `--output`: The destination path for the screenshot.
- `--mask`: A comma-separated list of CSS selectors to hide.
- `--full-page`: Boolean flag to capture the entire scrollable area.
- `--mobile`: Boolean flag to simulate a mobile device.
