#!/usr/bin/env python3
"""File: scripts/check_file_headers.py
Purpose: Check required File, Purpose and Layer metadata on supported text files.
Layer: Repository / Validation Tool
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IGNORED_DIRS = {
    ".git", ".venv", "venv", "__pycache__", ".pytest_cache",
    ".mypy_cache", ".ruff_cache", "node_modules", "dist", "build",
}
SPECIAL_TEXT_FILES = {".editorconfig", ".gitattributes", ".gitignore"}


def is_supported(path: Path) -> bool:
    return path.suffix.lower() in {
        ".md", ".yaml", ".yml", ".json", ".py", ".txt"
    } or path.name in SPECIAL_TEXT_FILES


def check(path: Path) -> str | None:
    relative = path.relative_to(ROOT).as_posix()
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    if path.suffix.lower() == ".md":
        if relative == ".github/ISSUE_TEMPLATE/product-proposal.md":
            head = "\n".join(lines[:8])
            valid = (
                lines and lines[0] == "---"
                and any(line.startswith("# File: ") for line in lines[:8])
                and any(line.startswith("# Purpose: ") for line in lines[:8])
                and any(line.startswith("# Layer: ") for line in lines[:8])
            )
        else:
            head = "\n".join(lines[:7])
            valid = (
                text.startswith("<!--\n")
                and "File: " in head
                and "Purpose: " in head
                and "Layer: " in head
                and "-->" in head
            )
    elif path.suffix.lower() == ".json":
        try:
            data = json.loads(text)
            metadata = data.get("$comment", "")
            valid = all(token in metadata for token in ("File: ", "Purpose: ", "Layer: "))
        except (json.JSONDecodeError, AttributeError):
            return "invalid JSON or missing object root"
    elif path.suffix.lower() == ".py":
        python_header_lines = lines[1:8] if lines and lines[0].startswith("#!") else lines[:7]
        head = "\n".join(python_header_lines)
        valid = (
            python_header_lines
            and python_header_lines[0].startswith('"""')
            and "File: " in head
            and "Purpose: " in head
            and "Layer: " in head
        )
    else:
        head = "\n".join(lines[:5])
        valid = (
            lines[:1] and lines[0].startswith("# File: ")
            and any(line.startswith("# Purpose: ") for line in lines[:5])
            and any(line.startswith("# Layer: ") for line in lines[:5])
        )

    if not valid:
        return "missing or malformed File / Purpose / Layer header"
    if f"File: {relative}" not in text[:1000]:
        return f"header path does not match actual path ({relative})"
    return None


def walk_files():
    for path in ROOT.rglob("*"):
        if any(part in IGNORED_DIRS for part in path.relative_to(ROOT).parts):
            continue
        if path.is_file() and is_supported(path):
            yield path


def main() -> int:
    failures = []
    checked = 0
    for path in sorted(walk_files()):
        checked += 1
        error = check(path)
        if error:
            failures.append((path.relative_to(ROOT).as_posix(), error))

    if failures:
        print("File header check failed:")
        for name, error in failures:
            print(f"- {name}: {error}")
        return 1

    print(f"File header check passed. Text files checked: {checked}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
