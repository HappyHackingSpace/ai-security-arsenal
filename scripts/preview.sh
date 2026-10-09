#!/bin/sh
# Render README.md with GitHub's own markdown API and open it in the browser.
set -e
cd "$(dirname "$0")/.."
out="${TMPDIR:-/tmp}/ai-security-arsenal-preview.html"
{
  echo '<!doctype html><meta charset="utf-8"><title>ai-security-arsenal preview</title>'
  echo '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/github-markdown-css@5.8.1/github-markdown.min.css">'
  echo '<body style="max-width:1100px;margin:32px auto;padding:0 16px"><article class="markdown-body">'
  gh api markdown -f mode=gfm -f context=omarkurt/ai-security-arsenal -f text="$(cat README.md)"
  echo '</article></body>'
} > "$out"
echo "$out"
open "$out"
