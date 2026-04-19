# VHS Terminal Recording Template
# 🎬 Automate your CLI demos with this .tape file.
# Install VHS: brew install vhs (macOS/Linux) or go install github.com/charmbracelet/vhs@latest

# Output settings (generates a GIF or MP4)
Output showcase/cli_demo.gif

# Window settings
Set FontSize 22
Set Width 1200
Set Height 600
Set Padding 40
Set WindowBar Rounded

# Type your demo commands below
Type "ls -la"
Sleep 500ms
Enter

Sleep 1s

Type "echo '🚀 Showcase your CLI tool with project-showcase-skill!'"
Sleep 500ms
Enter

Sleep 2s

# Capture the final state
Screenshot showcase/cli_final_state.png
