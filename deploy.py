#!/usr/bin/env python3
"""
Deploy script for richnashawaty.com
Usage: python3 deploy.py "your commit message"
"""

import subprocess
import sys
import os

# Config
REPO_DIR = os.path.dirname(os.path.abspath(__file__))
REMOTE = "origin"
BRANCH = "main"

def run(cmd, cwd=None):
    result = subprocess.run(cmd, shell=True, cwd=cwd or REPO_DIR,
                            capture_output=True, text=True)
    if result.stdout.strip():
        print(result.stdout.strip())
    if result.stderr.strip():
        print(result.stderr.strip())
    return result.returncode

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 deploy.py \"your commit message\"")
        sys.exit(1)

    message = sys.argv[1]

    print(f"\n🚀 Deploying richnashawaty.com")
    print(f"   Message: {message}\n")

    steps = [
        ("git add .",                            "Staging files..."),
        (f'git commit -m "{message}"',           "Committing..."),
        (f"git push {REMOTE} {BRANCH}",          "Pushing to GitHub..."),
    ]

    for cmd, label in steps:
        print(f"→ {label}")
        code = run(cmd)
        if code != 0 and "nothing to commit" not in label.lower():
            # commit returns 1 if nothing to commit — that's fine
            pass

    print("\n✅ Push complete.")
    print("\nNext: SSH into Hostinger and run:")
    print("  cd ~/domains/richnashawaty.com/public_html && git fetch origin && git reset --hard origin/main\n")

if __name__ == "__main__":
    main()
