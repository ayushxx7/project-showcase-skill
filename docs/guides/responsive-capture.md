# Responsive Capture

Capture your UI across desktop, tablet, and mobile in one command.

## Viewports

| Device | Dimensions |
|---|---|
| Desktop | 1920 x 1080 |
| Tablet | 768 x 1024 |
| Mobile | 375 x 667 |

## Usage

```bash
python3 scripts/capture.py --url http://localhost:3000 --responsive
```

This produces:
- `showcase/landing_desktop.png`
- `showcase/landing_tablet.png`
- `showcase/landing_mobile.png`

## Why It Matters

- **Portfolio quality**: Shows you considered responsive design
- **Feature discovery**: Some features (mobile menus) only appear on small screens
- **Visual verification**: Ensures layout doesn't break across devices
