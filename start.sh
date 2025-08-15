#!/usr/bin/env bash
set -euo pipefail

: "${JEKYLL_ENV:=development}"
: "${HOST:=0.0.0.0}"
: "${PORT:=4000}"

echo "==> JEKYLL_ENV=$JEKYLL_ENV"

# Ensure gems are present
bundle check || bundle install --jobs 4 --retry 3

# 1) Auto-generate event pages from speakers.yml (idempotent)
if [ -f scripts/generate_events_md.py ]; then
  echo "==> Generating event pages from _data/speakers.yml ..."
  python3 scripts/generate_events_md.py --out events --base-permalink /events/
fi

# 2) Build and serve
echo "==> Building site..."
bundle exec jekyll build

echo "==> Serving on http://$HOST:$PORT"
exec bundle exec jekyll serve --host "$HOST" --port "$PORT" --watch --livereload
