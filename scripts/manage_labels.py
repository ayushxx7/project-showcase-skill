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

def update_gh_topics(topics):
    topic_str = ",".join(topics)
    print(f"🏷️ Detected Topics: {topic_str}")
    try:
        # Check if gh is installed and logged in
        subprocess.run(["gh", "auth", "status"], check=True, capture_output=True)
        
        print(f"🚀 Updating GitHub topics...")
        subprocess.run(["gh", "repo", "edit", "--add-topic", topic_str], check=True)
        print("✅ GitHub topics updated successfully.")
    except Exception as e:
        print(f"⚠️ Could not update GitHub topics: {e}")
        print("Make sure 'gh' CLI is installed and authenticated.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Apply detected topics to the repo")
    args = parser.parse_args()
    
    topics = detect_topics()
    if args.apply:
        update_gh_topics(topics)
    else:
        print(f"🔍 Suggested topics: {', '.join(topics)}")
        print("Run with --apply to update the repository.")
