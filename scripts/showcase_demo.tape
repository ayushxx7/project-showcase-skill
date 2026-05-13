Output showcase/demo.gif

Set Shell "zsh"
Set FontSize 18
Set Width 1200
Set Height 600
Set Padding 20

Type "cd ~/thevibecoder/projects/self/project-showcase-skill" Enter
Sleep 400ms

Type "clear" Enter
Sleep 300ms

Type "echo '>> Project Showcase Skill <<'" Enter
Sleep 800ms

Type "echo ''" Enter
Sleep 200ms

Type "echo '[1/3] Security Scan'" Enter
Sleep 400ms

Type "python3 scripts/scan.py --dir ." Enter
Sleep 3s

Type "echo ''" Enter
Sleep 200ms

Type "echo '[2/3] Health Audit'" Enter
Sleep 400ms

Type "python3 scripts/audit.py --dir . --json | head -6" Enter
Sleep 3s

Type "echo ''" Enter
Sleep 200ms

Type "echo '[3/3] GitHub Metadata'" Enter
Sleep 400ms

Type "python3 scripts/manage_metadata.py" Enter
Sleep 2s

Type "echo ''" Enter
Sleep 200ms

Type "echo '>> Showcase pipeline complete.'" Enter
Sleep 2s
