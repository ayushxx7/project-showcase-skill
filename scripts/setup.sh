#!/bin/bash
set -e

echo "🎬 Setting up Project Showcase dependencies..."

# Check Python version (need 3.8+)
PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")' 2>/dev/null || echo "0.0")
REQUIRED="3.8"
if [ "$(printf '%s\n' "$REQUIRED" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED" ]; then
    echo "❌ Python 3.8+ required. Found: $PYTHON_VERSION"
    exit 1
fi
echo "✅ Python $PYTHON_VERSION detected."

# Detect OS
OS="$(uname)"
case "${OS}" in
    Darwin*)    PLATFORM="mac" ;;
    Linux*)     PLATFORM="linux" ;;
    *)          echo "Unsupported OS: ${OS}"; exit 1 ;;
esac

# 1. Install System Dependencies
if [ "$PLATFORM" == "mac" ]; then
    echo "🍎 Mac detected. Checking for Homebrew..."
    if ! command -v brew &> /dev/null; then
        echo "❌ Homebrew not found. Please install it: https://brew.sh/"
    else
        echo "📦 Installing VHS and ffmpeg..."
        brew install vhs ffmpeg
    fi
elif [ "$PLATFORM" == "linux" ]; then
    echo "🐧 Linux detected. Checking for VHS and ffmpeg..."
    if ! command -v vhs &> /dev/null; then
        echo "📦 Please install VHS: https://github.com/charmbracelet/vhs#installation"
    fi
    if ! command -v ffmpeg &> /dev/null; then
        echo "📦 Please install ffmpeg using your package manager (e.g., sudo apt install ffmpeg)"
    fi
fi

# 2. Setup Python Virtual Environment
echo "🐍 Setting up Python environment..."
python3 -m venv .venv
source .venv/bin/activate

echo "pip install dependencies..."
python3 -m pip install --upgrade pip
if [ -f "requirements.txt" ]; then
    python3 -m pip install -r requirements.txt
else
    python3 -m pip install playwright
fi

echo "Installing Playwright browsers..."
python3 -m playwright install chromium

echo "✅ Environment ready!"
echo "To use, run: source .venv/bin/activate"
