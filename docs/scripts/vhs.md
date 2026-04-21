# CLI Recording (VHS) 📟

The Project Showcase Skill uses [VHS](https://github.com/charmbracelet/vhs) from the Charmbracelet team to generate high-fidelity GIFs of terminal sessions.

## How it Works

1. **Tape Generation**: The agent dynamically generates a `.tape` script based on the CLI commands you want to demo.
2. **VHS Execution**: VHS reads the script, spawns a virtual terminal, "types" the commands, and records the output.
3. **GIF Generation**: VHS then processes the recording into a high-quality GIF, perfectly sized for the GitHub README.

## VHS Script (`record_cli.tape`)

A sample script for VHS might look like this:

```vhs
Output showcase/cli_power_demo.gif

Set Shell "zsh"
Set FontSize 24
Set Width 1200
Set Height 600

Type "pip install project-showcase" Enter
Sleep 1s
Type "project-showcase --audit" Enter
Sleep 5s
```

## Best Practices

- **Sleep Intervals**: Use `Sleep` to give the viewer time to read the output.
- **Set Dimensions**: Explicitly set the width and height to ensure the GIF fits the README perfectly.
- **Font Size**: Use a large font size (e.g., 22+) so the recording is readable on mobile screens.
