import subprocess
import json
import argparse
import os
import re

# Mapping of file patterns/keywords to GitHub topics
TOPIC_MAP = {
    "playwright": ["playwright", "browser-automation"],
    "vhs": ["vhs", "cli-recording"],
    "package.json": ["javascript", "nodejs"],
    "requirements.txt": ["python"],
    "go.mod": ["go"],
    "Cargo.toml": ["rust"],
    "docker-compose": ["docker"],
    "Dockerfile": ["docker"],
    "README.md": ["documentation"],
    "jest": ["testing", "jest"],
    "pytest": ["testing", "pytest"],
    "terraform": ["infrastructure-as-code", "terraform"],
    "github/workflows": ["github-actions", "automation"],
    "tailwind": ["tailwindcss"],
    "react": ["react"],
    "next": ["nextjs"],
    "vue": ["vuejs"],
    "sqlite": ["sqlite", "database"],
    "postgresql": ["postgresql", "database"],
    "mongodb": ["mongodb", "database"]
}

def detect_topics():
    detected = set(["showcase", "automation"]) # Base topics
    
    # Simple file-based detection
    files = []
    for root, _, filenames in os.walk('.'):
        if '.git' in root or '.venv' in root or 'node_modules' in root:
            continue
        for f in filenames:
            files.append(os.path.join(root, f))
            
    for pattern, topics in TOPIC_MAP.items():
        if any(pattern in f for f in files):
            detected.update(topics)
            
    return sorted(list(detected))

def detect_description():
    """Detect a concise GitHub description from the README."""
    try:
        if not os.path.exists("README.md"):
            return None
            
        with open("README.md", "r") as f:
            content = f.read()
            
        # Try to find the elevator pitch (usually the first paragraph after the header or badges)
        # Skip the header (# ...)
        lines = content.splitlines()
        pitch = None
        for line in lines:
            line = line.strip()
            if not line or line.startswith("#") or line.startswith("[!") or line.startswith("<"):
                continue
            # First line that isn't a header, badge, or empty is likely the pitch
            pitch = line
            break
            
        if pitch:
            # Strip markdown bold/italic
            pitch = re.sub(r'[*_]{1,2}', '', pitch)
            # Trim to 160 chars
            if len(pitch) > 160:
                pitch = pitch[:157] + "..."
            return pitch
            
    except Exception as e:
        print(f"⚠️ Failed to detect description: {e}")
    return None

def update_gh_metadata(topics=None, description=None, commit=False, push=False):
    try:
        # Check if gh is installed and logged in
        subprocess.run(["gh", "auth", "status"], check=True, capture_output=True)
        
        if description:
            print(f"📝 Updating Description: {description}")
            try:
                subprocess.run(["gh", "repo", "edit", "--description", description], check=True)
                print("✅ GitHub description updated successfully.")
            except Exception as e:
                print(f"⚠️ Failed to update description: {e}")
                
        if topics:
            topic_str = ",".join(topics)
            print(f"🏷️ Updating Topics: {topic_str}")
            try:
                subprocess.run(["gh", "repo", "edit", "--add-topic", topic_str], check=True)
                print("✅ GitHub topics updated successfully.")
            except Exception as e:
                print(f"⚠️ Failed to update topics: {e}")
        
        if commit:
            print("📝 Committing metadata updates record...")
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", "chore: update github metadata (topics/description)"], check=True)
            
            if push:
                print("📤 Pushing changes...")
                subprocess.run(["git", "push"], check=True)
                print("✅ Pushed to remote.")
                
    except Exception as e:
        print(f"⚠️ Git/GitHub operation failed: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Apply detected metadata to the repo")
    parser.add_argument("--commit", action="store_true", help="Commit any changes (optional)")
    parser.add_argument("--push", action="store_true", help="Push any changes (optional)")
    args = parser.parse_args()
    
    topics = detect_topics()
    description = detect_description()
    
    if args.apply:
        update_gh_metadata(topics=topics, description=description, commit=args.commit, push=args.push)
    else:
        print(f"🔍 Suggested topics: {', '.join(topics)}")
        if description:
            print(f"🔍 Suggested description: {description}")
        else:
            print("🔍 No description detected from README.md.")
        print("\nRun with --apply to update the repository.")
