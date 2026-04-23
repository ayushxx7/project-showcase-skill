import os
import re
import argparse

# Common patterns for secrets
SECRET_PATTERNS = {
    "OpenAI Key": r"sk-[a-zA-Z0-9]{48}",
    "Anthropic Key": r"sk-ant-api03-[a-zA-Z0-9_-]{93}A",
    "Generic API Key": r"(?:api|secret|key|password)[-_ ]?[\'\"]?[:=][\'\"]?\s*([a-zA-Z0-9]{16,})[\'\"]?",
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "AWS Secret Key": r"(?i)aws_secret_access_key\s*[:=]\s*([a-zA-Z0-9/+=]{40})",
    "Google API Key": r"AIza[0-9A-Za-z-_]{35}",
    "Firebase API Key": r"AIza[0-9A-Za-z-_]{35}",
    "Stripe Secret Key": r"sk_live_[0-9a-zA-Z]{24}",
    "Stripe Publishable Key": r"pk_live_[0-9a-zA-Z]{24}",
    "GitHub Personal Access Token": r"ghp_[a-zA-Z0-9]{36}",
}

def scan_files(directory="."):
    findings = []
    
    # Files/Dirs to ignore
    ignore_dirs = [".git", "node_modules", ".venv", ".venv_capture", "env", "__pycache__", "dist", "build", "showcase"]
    ignore_files = [".gitignore", "LICENSE", "package-lock.json", "yarn.lock"]
    
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        
        for file in files:
            if file in ignore_files or any(file.endswith(ext) for ext in [".png", ".jpg", ".gif", ".pdf", ".zip"]):
                continue
                
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    
                    for name, pattern in SECRET_PATTERNS.items():
                        matches = re.finditer(pattern, content)
                        for match in matches:
                            # Avoid false positives for empty or generic strings
                            secret = match.group(0)
                            if secret:
                                line_no = content.count('\n', 0, match.start()) + 1
                                findings.append({
                                    "type": name,
                                    "file": file_path,
                                    "line": line_no,
                                    "snippet": secret[:4] + "*" * (len(secret) - 8) + secret[-4:]
                                })
                                
            except Exception as e:
                print(f"⚠️ Failed to read {file_path}: {e}")
                
    return findings

def check_gitignore():
    if not os.path.exists(".gitignore"):
        return False, "❌ .gitignore is missing!"
    
    with open(".gitignore", "r") as f:
        content = f.read()
        
    sensitive_patterns = [".env", "secrets.toml", ".streamlit/secrets.toml", "node_modules"]
    missing = [p for p in sensitive_patterns if p not in content]
    
    if missing:
        return False, f"⚠️ .gitignore is missing: {', '.join(missing)}"
    
    return True, "✅ .gitignore looks healthy."

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Privacy-first security scan for secrets and leaks.")
    parser.add_argument("--dir", default=".", help="Directory to scan")
    args = parser.parse_args()
    
    print("🛡️ Starting Privacy-First Security Scan...")
    
    findings = scan_files(args.dir)
    healthy, gitignore_msg = check_gitignore()
    
    print(gitignore_msg)
    
    if findings:
        print(f"🚨 Found {len(findings)} potential secrets:")
        for f in findings:
            print(f"  - [{f['type']}] in {f['file']}:{f['line']} -> {f['snippet']}")
        print("\n❌ SECURITY SCAN FAILED: Please remove secrets and add them to .gitignore.")
        exit(1)
    else:
        print("✅ No secrets found in source code.")
        if healthy:
            print("✨ Your project is ready for a professional showcase!")
        else:
            print("⚠️ Improve your .gitignore before sharing.")
        exit(0)
