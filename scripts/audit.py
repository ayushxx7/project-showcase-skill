#!/usr/bin/env python3
"""
Repo Health Audit — scores a project on a 0-100 scale.

Usage:
    python3 scripts/audit.py [--dir .] [--heal]
"""

import os
import argparse
import json
import subprocess
import sys

# Scoring weights
WEIGHTS = {
    "documentation": 15,
    "security": 15,
    "automation": 20,
    "showcase": 20,
    "distribution": 30,
}

def check_documentation(directory):
    """README, LICENSE, meaningful content."""
    score = 0
    findings = []

    # README exists and has content
    readme_path = os.path.join(directory, "README.md")
    if os.path.exists(readme_path):
        with open(readme_path) as f:
            content = f.read().strip()
        if len(content) > 200:
            score += 5
            findings.append(("✅", "README.md present with substantial content"))
        elif len(content) > 50:
            score += 3
            findings.append(("⚠️", "README.md present but thin"))
        else:
            findings.append(("❌", "README.md is nearly empty"))
    else:
        findings.append(("❌", "README.md missing"))

    # LICENSE exists
    license_files = ["LICENSE", "LICENSE.md", "LICENSE.txt", "LICENCE"]
    has_license = any(os.path.exists(os.path.join(directory, f)) for f in license_files)
    if has_license:
        score += 5
        findings.append(("✅", "LICENSE file present"))
    else:
        findings.append(("❌", "LICENSE file missing — propose MIT"))

    # Setup/install instructions
    if os.path.exists(readme_path):
        with open(readme_path) as f:
            content = f.read().lower()
        if "install" in content or "setup" in content or "getting started" in content:
            score += 5
            findings.append(("✅", "Installation/setup instructions found"))
        else:
            findings.append(("⚠️", "No installation instructions in README"))
    else:
        findings.append(("⚠️", "Cannot check install instructions (no README)"))

    return score, findings


def check_security(directory):
    """Secrets scan, .gitignore validation."""
    score = 0
    findings = []

    # Run scan.py
    scan_script = os.path.join(directory, "scripts", "scan.py")
    if os.path.exists(scan_script):
        try:
            result = subprocess.run(
                [sys.executable, scan_script, "--dir", directory],
                capture_output=True, text=True, timeout=30
            )
            if result.returncode == 0:
                score += 10
                findings.append(("✅", "No hardcoded secrets detected"))
            else:
                findings.append(("❌", f"Secrets detected:\n{result.stdout.strip()}"))
        except Exception as e:
            findings.append(("⚠️", f"Could not run scan.py: {e}"))
    else:
        findings.append(("⚠️", "scripts/scan.py not found — skipping secret scan"))

    # .gitignore exists
    gitignore = os.path.join(directory, ".gitignore")
    if os.path.exists(gitignore):
        with open(gitignore) as f:
            content = f.read()
        critical = [".env", "secrets.toml", "node_modules", "__pycache__"]
        missing = [p for p in critical if p not in content]
        if not missing:
            score += 5
            findings.append(("✅", "gitignore covers critical patterns"))
        else:
            score += 2
            findings.append(("⚠️", f"gitignore missing: {', '.join(missing)}"))
    else:
        findings.append(("❌", ".gitignore missing"))

    return score, findings


def check_automation(directory):
    """setup.sh, tests, CI."""
    score = 0
    findings = []

    # setup.sh exists
    setup = os.path.join(directory, "scripts", "setup.sh")
    if os.path.exists(setup):
        score += 5
        findings.append(("✅", "scripts/setup.sh present"))
    else:
        findings.append(("⚠️", "scripts/setup.sh missing"))

    # Tests exist
    test_dir = os.path.join(directory, "tests")
    test_files = []
    if os.path.isdir(test_dir):
        test_files = [f for f in os.listdir(test_dir) if f.startswith("test_") and f.endswith(".py")]
    if test_files:
        score += 5
        findings.append(("✅", f"Test files found: {', '.join(test_files)}"))
    else:
        findings.append(("⚠️", "No test files in tests/"))

    # CI config
    ci_paths = [
        os.path.join(directory, ".github", "workflows"),
        os.path.join(directory, ".travis.yml"),
        os.path.join(directory, "Makefile"),
    ]
    has_ci = any(os.path.exists(p) for p in ci_paths)
    if has_ci:
        score += 5
        findings.append(("✅", "CI/CD configuration detected"))
    else:
        findings.append(("⚠️", "No CI/CD configuration found"))

    # requirements.txt or package.json
    has_deps = (
        os.path.exists(os.path.join(directory, "requirements.txt")) or
        os.path.exists(os.path.join(directory, "package.json")) or
        os.path.exists(os.path.join(directory, "pyproject.toml"))
    )
    if has_deps:
        score += 5
        findings.append(("✅", "Dependency manifest present"))
    else:
        findings.append(("⚠️", "No dependency manifest found"))

    return score, findings


def check_showcase(directory):
    """Screenshots, GIFs, visual assets."""
    score = 0
    findings = []

    showcase_dir = os.path.join(directory, "showcase")
    assets_dir = os.path.join(directory, "assets")

    # Check for visual assets
    image_files = []
    for d in [showcase_dir, assets_dir, directory]:
        if os.path.isdir(d):
            for f in os.listdir(d):
                if f.lower().endswith((".png", ".jpg", ".gif", ".webp", ".svg")):
                    image_files.append(os.path.join(d, f))

    if len(image_files) >= 3:
        score += 10
        findings.append(("✅", f"{len(image_files)} visual assets found"))
    elif len(image_files) >= 1:
        score += 5
        findings.append(("⚠️", f"Only {len(image_files)} visual asset(s) — aim for 3+"))
    else:
        findings.append(("❌", "No visual assets (screenshots/GIFs) found"))

    # VHS tape file
    tape_files = []
    for root, _, files in os.walk(directory):
        for f in files:
            if f.endswith(".tape"):
                tape_files.append(os.path.join(root, f))
    if tape_files:
        score += 5
        findings.append(("✅", f"VHS tape file(s) found: {len(tape_files)}"))
    else:
        findings.append(("⚠️", "No VHS tape files for terminal demos"))

    # capture.py exists
    capture = os.path.join(directory, "scripts", "capture.py")
    if os.path.exists(capture):
        score += 5
        findings.append(("✅", "scripts/capture.py present"))
    else:
        findings.append(("⚠️", "scripts/capture.py missing"))

    return score, findings


def check_distribution(directory):
    """GitHub metadata, topics, releases."""
    score = 0
    findings = []

    # Check if it's a git repo
    git_dir = os.path.join(directory, ".git")
    if not os.path.isdir(git_dir):
        findings.append(("❌", "Not a git repository"))
        return score, findings
    score += 5
    findings.append(("✅", "Git repository initialized"))

    # Check for remote
    try:
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            capture_output=True, text=True, cwd=directory, timeout=10
        )
        if result.returncode == 0 and result.stdout.strip():
            score += 5
            findings.append(("✅", f"Remote configured: {result.stdout.strip()}"))
        else:
            findings.append(("⚠️", "No remote configured"))
    except Exception:
        findings.append(("⚠️", "Could not check git remote"))

    # Check for GitHub topics via gh
    try:
        result = subprocess.run(
            ["gh", "repo", "view", "--json", "repositoryTopics"],
            capture_output=True, text=True, cwd=directory, timeout=10
        )
        if result.returncode == 0:
            data = json.loads(result.stdout)
            topics = data.get("repositoryTopics", [])
            topic_names = [t.get("name", "") for t in topics]
            if topic_names:
                score += 10
                findings.append(("✅", f"GitHub topics: {', '.join(topic_names)}"))
            else:
                findings.append(("⚠️", "No GitHub topics set"))
        else:
            findings.append(("⚠️", "Could not fetch GitHub topics (gh auth?)"))
    except Exception:
        findings.append(("⚠️", "gh CLI not available for topic check"))

    # Check for releases
    try:
        result = subprocess.run(
            ["gh", "release", "list", "--limit", "1"],
            capture_output=True, text=True, cwd=directory, timeout=10
        )
        if result.returncode == 0 and result.stdout.strip():
            score += 10
            findings.append(("✅", "GitHub release exists"))
        else:
            findings.append(("⚠️", "No GitHub releases yet"))
    except Exception:
        findings.append(("⚠️", "Could not check releases"))

    return score, findings


def run_audit(directory):
    """Run all checks and compute total score."""
    categories = {
        "Documentation": check_documentation,
        "Security": check_security,
        "Automation": check_automation,
        "Showcase": check_showcase,
        "Distribution": check_distribution,
    }

    total_score = 0
    max_score = sum(WEIGHTS.values())
    report = {}

    for category, check_fn in categories.items():
        score, findings = check_fn(directory)
        # Normalize to category weight
        cat_key = category.lower()
        cat_max = WEIGHTS.get(cat_key, 20)
        normalized = min(score, cat_max)
        total_score += normalized
        report[category] = {
            "score": normalized,
            "max": cat_max,
            "findings": findings,
        }

    return total_score, max_score, report


def print_report(total, maximum, report):
    """Print a formatted health report."""
    print("\n" + "=" * 60)
    print("🩺  REPO HEALTH AUDIT REPORT")
    print("=" * 60)

    for category, data in report.items():
        score = data["score"]
        max_s = data["max"]
        pct = int(score / max_s * 100) if max_s > 0 else 0
        bar = "█" * (pct // 10) + "░" * (10 - pct // 10)
        print(f"\n{category}: {score}/{max_s} [{bar}] {pct}%")
        for icon, finding in data["findings"]:
            print(f"  {icon} {finding}")

    print("\n" + "-" * 60)
    pct = int(total / maximum * 100) if maximum > 0 else 0
    if pct >= 90:
        emoji = "🌟"
    elif pct >= 70:
        emoji = "✅"
    elif pct >= 50:
        emoji = "⚠️"
    else:
        emoji = "❌"
    print(f"\n{emoji}  TOTAL SCORE: {total}/{maximum} ({pct}%)")

    if pct == 100:
        print("   Pristine! This repo is showcase-ready. 🚀")
    elif pct >= 70:
        print("   Good shape. Address the ❌ items to reach 100%.")
    else:
        print("   Needs work. Focus on the ❌ items first.")
    print()


def generate_heal_plan(report):
    """Generate a prioritized healing plan from failed checks."""
    plan = []
    for category, data in report.items():
        for icon, finding in data["findings"]:
            if "❌" in icon:
                plan.append(f"[{category}] {finding}")
    return plan


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Repo Health Audit — score and healing plan")
    parser.add_argument("--dir", default=".", help="Directory to audit")
    parser.add_argument("--heal", action="store_true", help="Show healing plan")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    total, maximum, report = run_audit(args.dir)

    if args.json:
        output = {
            "score": total,
            "max": maximum,
            "pct": int(total / maximum * 100) if maximum > 0 else 0,
            "categories": {
                cat: {"score": d["score"], "max": d["max"], "findings": d["findings"]}
                for cat, d in report.items()
            },
        }
        if args.heal:
            output["heal_plan"] = generate_heal_plan(report)
        print(json.dumps(output, indent=2))
    else:
        print_report(total, maximum, report)
        if args.heal:
            plan = generate_heal_plan(report)
            if plan:
                print("💊 HEALING PLAN (prioritized):")
                for i, item in enumerate(plan, 1):
                    print(f"   {i}. {item}")
                print()
            else:
                print("✨ No critical issues found. Nothing to heal!\n")
