#!/bin/bash

# Project Showcase Skill - Universal Installer
# Targets: Gemini CLI, Claude Code, Cursor

REPO_URL="https://github.com/ayushxx7/project-showcase-skill"
SKILL_NAME="project-showcase"

echo "🎬 Installing Project Showcase Skill..."

# 1. Detect Gemini CLI
if [ -d "$HOME/.gemini/skills" ]; then
    echo "🤖 Gemini CLI detected. Installing..."
    cd "$HOME/.gemini/skills" && git clone $REPO_URL $SKILL_NAME 2>/dev/null || (cd $SKILL_NAME && git pull)
fi

# 2. Detect Claude Code
if [ -d "$HOME/.claude/skills" ]; then
    echo "🧠 Claude Code detected. Installing..."
    cd "$HOME/.claude/skills" && git clone $REPO_URL $SKILL_NAME 2>/dev/null || (cd $SKILL_NAME && git pull)
fi

# 3. Detect Generic Agents folder
if [ -d "$HOME/.agents/skills" ]; then
    echo "🕵️ Generic Agent Skills folder detected. Installing..."
    cd "$HOME/.agents/skills" && git clone $REPO_URL $SKILL_NAME 2>/dev/null || (cd $SKILL_NAME && git pull)
fi

echo "✅ Installation complete. Restart your agent to activate the skill."
