#!/usr/bin/env python3
"""
build_index.py

Walks all 5 tracked category folders and regenerates:
  - <category>/README.md  (problem table for that category)
  - README.md             (root stats + links to each category)

Run automatically by GitHub Actions on every push, or manually:
  python 0-scripts/build_index.py
"""

import re
import pathlib

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent

CATEGORIES = [
    "data-structures",
    "databases",
    "linux-shell",
    "python",
    "sql",
]

CATEGORY_LABELS = {
    "data-structures": "Data Structures",
    "databases":       "Databases",
    "linux-shell":     "Linux Shell",
    "python":          "Python",
    "sql":             "SQL",
}


def build_category_index(category: str) -> int:
    base = REPO_ROOT / category
    if not base.exists():
        return 0

    rows = []
    for entry in sorted(base.iterdir()):
        if not entry.is_dir():
            continue
        readme = entry / "README.md"
        if not readme.exists():
            continue

        text = readme.read_text(encoding="utf-8")
        title_line = text.splitlines()[0].lstrip("# ").strip()
        diff_match = re.search(r"\*\*Difficulty:\*\*\s*(.+)", text)
        link_match = re.search(r"\*\*Link:\*\*\s*(\S+)", text)
        difficulty = diff_match.group(1).strip() if diff_match else "—"
        link = link_match.group(1).strip() if link_match else ""
        rows.append((title_line, difficulty, link, entry.name))

    label = CATEGORY_LABELS.get(category, category.title())
    lines = [
        f"# {label} Problems\n",
        "| # | Problem | Difficulty |",
        "|---|---------|------------|",
    ]
    for i, (title_line, difficulty, link, folder) in enumerate(rows, 1):
        if link:
            lines.append(f"| {i} | [{title_line}]({folder}/) | {difficulty} |")
        else:
            lines.append(f"| {i} | {title_line} | {difficulty} |")

    (base / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return len(rows)


def build_root_index(counts: dict):
    total = sum(counts.values())
    lines = [
        "# HackerRank Solutions\n",
        "Auto-synced from my HackerRank submissions.\n",
        "## 📊 Stats\n",
        f"**Total solved: {total}**\n",
    ]
    for cat in CATEGORIES:
        label = CATEGORY_LABELS.get(cat, cat.title())
        lines.append(f"- {label}: {counts.get(cat, 0)}")

    lines += [
        "\n## 📁 Categories\n",
    ]
    for cat in CATEGORIES:
        label = CATEGORY_LABELS.get(cat, cat.title())
        lines.append(f"- [{label}]({cat}/README.md)")

    (REPO_ROOT / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    counts = {}
    for cat in CATEGORIES:
        count = build_category_index(cat)
        counts[cat] = count
        print(f"  {cat}: {count} problems")

    build_root_index(counts)
    print(f"Done. Total: {sum(counts.values())} problems.")


if __name__ == "__main__":
    main()
