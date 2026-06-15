#!/usr/bin/env bash
set -euo pipefail

RAW_BASE="https://raw.githubusercontent.com/Yan-ShiBo/codex-skills-kit/main"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" 2>/dev/null && pwd || true)"

if [[ -n "${SCRIPT_DIR}" && -f "${SCRIPT_DIR}/scripts/install.py" ]]; then
  INSTALLER="${SCRIPT_DIR}/scripts/install.py"
  python3 "${INSTALLER}" "$@"
  exit
fi

TMP_DIR="$(mktemp -d)"
trap 'rm -rf "${TMP_DIR}"' EXIT
curl -fsSL "${RAW_BASE}/scripts/install.py" -o "${TMP_DIR}/install.py"
python3 "${TMP_DIR}/install.py" "$@"
