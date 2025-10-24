#!/usr/bin/env bash
# Run the Selenium automation once and append the result to log.txt.

set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
LOG_FILE="${SCRIPT_DIR}/log.txt"

touch "${LOG_FILE}"

OUTPUT=$(python3 "${SCRIPT_DIR}/auto_local.py" "$@" 2>&1)
STATUS=$?

printf '%s\n' "${OUTPUT}"

CURRENT_DATE=$(date '+%Y-%m-%d')
if [[ ${STATUS} -eq 0 ]]; then
  printf '%s Successful\n' "${CURRENT_DATE}" >>"${LOG_FILE}"
else
  printf '%s Error\n' "${CURRENT_DATE}" >>"${LOG_FILE}"
fi

exit ${STATUS}
