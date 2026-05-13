# UI Capture (`capture.py`)

Playwright-based browser automation for high-quality screenshots and video.

## Features

- **Responsive viewports**: Desktop (1920x1080), Tablet (768x1024), Mobile (375x667)
- **Full-page screenshots**: Scroll and capture entire pages
- **Visual masking**: Hide sensitive elements via CSS selectors
- **Dark mode**: Capture in light or dark theme
- **Video recording**: `.webm` output converted to optimized GIF
- **Hydration awareness**: Waits for `networkidle` and framework selectors (React, Streamlit)
- **Interaction flows**: Click, fill, hover sequences with per-step screenshots

## Usage

```bash
# Basic landing page capture
python3 scripts/capture.py --url http://localhost:3000

# Responsive (desktop + tablet + mobile)
python3 scripts/capture.py --url http://localhost:3000 --responsive

# With video recording
python3 scripts/capture.py --url http://localhost:3000 --record-video

# Dark mode + full page
python3 scripts/capture.py --url http://localhost:3000 --theme dark --full-page

# Mask sensitive elements
python3 scripts/capture.py --url http://localhost:3000 --mask ".api-key,.user-email"

# Custom interactions (JSON)
python3 scripts/capture.py --url http://localhost:3000 --interactions '[{"action":"fill","selector":"#search","value":"test","filename":"search.png"}]'
```

## Options

| Flag | Default | Description |
|---|---|---|
| `--url` | `http://localhost:8501` | Target URL |
| `--dir` | `showcase` | Output directory |
| `--responsive` | off | Capture all 3 viewports |
| `--full-page` | off | Full scrollable page |
| `--theme` | `light` | `light` or `dark` |
| `--mask` | — | Comma-separated CSS selectors to hide |
| `--record-video` | off | Record .webm + convert to GIF |
| `--interactions` | — | JSON interaction sequence |
| `--hydration-delay` | 5 | Seconds to wait for UI hydration |
| `--ab-mode` | off | A/B comparison capture |
