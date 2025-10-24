#!/usr/bin/env bash
set -euo pipefail

REPO_URL="https://github.com/TouchFishPioneer/SEU-master-thesis.git"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="${SCRIPT_DIR%/scripts}/upstream"

log() {
  printf '[sync] %s\n' "$*"
}

if ! command -v git >/dev/null 2>&1; then
  log "未检测到 git，请先安装 git 再运行本脚本。"
  exit 1
fi

if [ -d "$TARGET_DIR/.git" ]; then
  log "检测到已存在的上游仓库，执行增量更新。"
  git -C "$TARGET_DIR" remote set-url origin "$REPO_URL"
  git -C "$TARGET_DIR" fetch --depth=1 origin main
  git -C "$TARGET_DIR" reset --hard origin/main
else
  log "开始浅克隆上游仓库到 ${TARGET_DIR}。"
  rm -rf "$TARGET_DIR"
  git clone --depth=1 --branch main "$REPO_URL" "$TARGET_DIR"
fi

log "同步完成。可以在 ${TARGET_DIR} 中查看或编译模版。"
