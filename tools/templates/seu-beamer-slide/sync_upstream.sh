#!/usr/bin/env bash
set -euo pipefail

REPO_URL="https://github.com/TouchFishPioneer/SEU-Beamer-Slide.git"
TARGET_DIR="$(dirname "$0")/upstream"

mkdir -p "$TARGET_DIR"
cd "$TARGET_DIR"

if [ -d "SEU-Beamer-Slide/.git" ]; then
  echo "[INFO] Updating existing SEU-Beamer-Slide repository..."
  git -C SEU-Beamer-Slide pull --ff-only
else
  echo "[INFO] Cloning SEU-Beamer-Slide repository..."
  git clone "$REPO_URL"
fi

echo "[INFO] Done. Repository stored in: $TARGET_DIR/SEU-Beamer-Slide"
