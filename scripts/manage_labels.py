import subprocess
import json
import argparse
import os

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

def update_gh_topics(topics, commit=False, push=False):
    topic_str = ",".join(topics)
    print(f"🏷️ Detected Topics: {topic_str}")
    try:
        # Check if gh is installed and logged in
        subprocess.run(["gh", "auth", "status"], check=True, capture_output=True)
        
        print(f"🚀 Updating GitHub topics...")
        subprocess.run(["gh", "repo", "edit", "--add-topic", topic_str], check=True)
        print("✅ GitHub topics updated successfully.")
        
        if commit:
            print("📝 Committing topic updates...")
            # We don't actually change files with topics, but the user might want a record
            # Or this script could be extended to update a config file. 
            # For now, let's assume we are committing the meta-change or any other changes made.
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", f"chore: update github topics to {topic_str}"], check=True)
            
            if push:
                print("📤 Pushing changes...")
                subprocess.run(["git", "push"], check=True)
                print("✅ Pushed to remote.")
                
    except Exception as e:
        print(f"⚠️ Git/GitHub operation failed: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Apply detected topics to the repo")
    parser.add_argument("--commit", action="store_true", help="Commit the changes (optional)")
    parser.add_argument("--push", action="store_true", help="Push the changes (optional)")
    args = parser.parse_args()
    
    topics = detect_topics()
    if args.apply:
        update_gh_topics(topics, commit=args.commit, push=args.push)
    else:
        print(f"🔍 Suggested topics: {', '.join(topics)}")
        print("Run with --apply to update the repository.")
