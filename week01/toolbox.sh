#!/usr/bin/env bash
# toolbox.sh — which of this term's tools does this machine have?
#
#   bash toolbox.sh
#
# Paste the whole output into toolbox.txt. A MISSING line is not your
# problem to fix today — tell the instructor; the lab image is their job.
# Read the script too: it is a shell script, which is what Part 3 asks you
# to write (a much shorter one).

for tool in bash git ssh docker code uv ollama nvidia-smi claude opencode; do
    if command -v "$tool" >/dev/null 2>&1; then
        printf '%-11s %s\n' "$tool" "$(command -v "$tool")"
    else
        printf '%-11s MISSING\n' "$tool"
    fi
done

echo
bash --version | head -1
git --version
docker --version 2>/dev/null || echo "docker: not installed, or not running"
uv --version 2>/dev/null || true
ollama --version 2>/dev/null || true
claude --version 2>/dev/null || true
