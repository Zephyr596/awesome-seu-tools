#!/usr/bin/env bash
set -euo pipefail

REPO_URL="https://github.com/Zephyr596/seuVisitor.git"
TARGET_DIR="$(dirname "$0")/upstream"

if command -v realpath >/dev/null 2>&1; then
  TARGET_DIR="$(realpath "$TARGET_DIR")"
else
  TARGET_DIR="$(cd "$(dirname "$TARGET_DIR")" && pwd)/$(basename "$TARGET_DIR")"
fi

mkdir -p "$TARGET_DIR"

if [ -d "$TARGET_DIR/.git" ]; then
  echo "[seuVisitor] Existing clone detected, fetching latest changes..."
  git -C "$TARGET_DIR" fetch --all --prune
  git -C "$TARGET_DIR" checkout main
  git -C "$TARGET_DIR" pull --ff-only
else
  echo "[seuVisitor] Cloning upstream repository into $TARGET_DIR"
  git clone "$REPO_URL" "$TARGET_DIR"
fi

echo "[seuVisitor] Sync complete."
