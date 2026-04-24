#!/usr/bin/env python3
"""LLM プロンプト用に複数の Markdown を列挙順に結合する。

使い方:
    python combine_md.py hamari_ja.md codesample_random10.md -o prompt.md
    python combine_md.py a.md b.md c.md           # stdout に出力
"""
import argparse
import sys
from pathlib import Path


def combine(paths: list[Path]) -> str:
    parts = []
    for p in paths:
        parts.append(p.read_text(encoding="utf-8").rstrip())
    return "\n\n".join(parts) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path, help="結合する .md ファイル (列挙順に連結)")
    parser.add_argument("-o", "--output", type=Path, help="出力先 (省略時は stdout)")
    args = parser.parse_args()

    missing = [p for p in args.files if not p.is_file()]
    if missing:
        for p in missing:
            print(f"error: not a file: {p}", file=sys.stderr)
        return 1

    result = combine(args.files)

    if args.output:
        args.output.write_text(result, encoding="utf-8")
    else:
        sys.stdout.write(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
