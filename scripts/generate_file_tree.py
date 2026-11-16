#!/usr/bin/env python3
"""File: scripts/generate_file_tree.py
Purpose: Generate FILE-TREE.md from the current repository filesystem.
Layer: Repository / Navigation Tool
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "FILE-TREE.md"
IGNORED_DIRS = {
    ".git", ".venv", "venv", "__pycache__", ".pytest_cache",
    ".mypy_cache", ".ruff_cache", "node_modules", "dist", "build",
}
IGNORED_FILES = {".DS_Store", "Thumbs.db"}


def render_tree(directory: Path, prefix: str = "") -> list[str]:
    entries = [
        entry for entry in directory.iterdir()
        if entry.name not in IGNORED_FILES
        and not (entry.is_dir() and entry.name in IGNORED_DIRS)
    ]
    entries.sort(key=lambda item: (not item.is_dir(), item.name.lower()))
    lines: list[str] = []
    for index, entry in enumerate(entries):
        is_last = index == len(entries) - 1
        branch = "└── " if is_last else "├── "
        label = entry.name + ("/" if entry.is_dir() else "")
        lines.append(prefix + branch + label)
        if entry.is_dir():
            extension = "    " if is_last else "│   "
            lines.extend(render_tree(entry, prefix + extension))
    return lines


def main() -> None:
    header = (
        "<!--\n"
        "File: FILE-TREE.md\n"
        "Purpose: 提供由当前仓库文件系统生成的目录树，帮助 AI Agent 和协作者定位文件。\n"
        "Layer: Repository / Navigation\n"
        "-->\n\n"
    )
    body = (
        "# Repository File Tree\n\n"
        "> 本文件由 `python scripts/generate_file_tree.py` 生成。"
        "新增、删除、移动或重命名文件后必须重新生成。\n>\n"
        "> 文件树仅用于定位；文件内容、权限和实际存在状态以当前工作区为准。\n\n"
        "```text\n"
        "zeki-brand/\n"
        + "\n".join(render_tree(ROOT))
        + "\n```\n"
    )
    OUTPUT.write_text(header + body, encoding="utf-8", newline="\n")
    print(f"Generated {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
