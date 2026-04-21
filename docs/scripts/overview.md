# Scripts Overview 🛠️

The Project Showcase Skill is powered by a set of specialized Python and Shell scripts that handle everything from environment setup to high-fidelity UI capture.

## Core Scripts

- **`scripts/capture.py`**: The heart of the skill. Handles Playwright-based browser automation to capture screenshots and videos of web applications.
- **`scripts/manage_metadata.py`**: Manages the metadata and configuration for the showcase, ensuring consistent naming and tagging.
- **`scripts/setup.sh`**: A comprehensive setup script that installs system dependencies (like VHS and FFmpeg) and Python packages.
- **`scripts/record_cli.tape`**: A template for VHS recordings, defining how the terminal "types" out commands for the GIF demo.

## Helper Scripts
- **`linkedin-magic/scripts/bundle_assets.py`**: A specialized tool for social media launches that selects and prepares the best assets for LinkedIn/Twitter.
- **`skills.sh`**: The universal installer script used to add this skill to various AI agent environments.
