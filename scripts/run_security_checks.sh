#!/usr/bin/env bash
set -uo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

passed=0
failed=0
skipped=0

run_check() {
    local label="$1"
    shift

    printf '\n===== %s =====\n' "$label"

    if "$@"; then
        echo "[PASS] $label"
        passed=$((passed + 1))
    else
        local status=$?
        echo "[FAIL] $label (exit $status)"
        failed=$((failed + 1))
    fi
}

optional_check() {
    local label="$1"
    local command_name="$2"
    shift 2

    if ! command -v "$command_name" >/dev/null 2>&1; then
        echo "[SKIP] $label: $command_name is not installed"
        skipped=$((skipped + 1))
        return
    fi

    run_check "$label" "$@"
}

if python -c "import pytest" >/dev/null 2>&1; then
    run_check "Unit tests" python -m pytest -q
else
    echo "[SKIP] Unit tests: pytest is not installed"
    skipped=$((skipped + 1))
fi

optional_check "Bandit SAST" bandit bandit -r app
optional_check "Semgrep SAST" semgrep semgrep scan --config p/python app
optional_check "Dependency audit" pip-audit pip-audit -r requirements.txt
optional_check "Secret scan" gitleaks gitleaks dir .

printf '\nSummary: passed=%s failed=%s skipped=%s\n' \
    "$passed" "$failed" "$skipped"

echo "Skipped checks are not passes."

(( failed == 0 ))
