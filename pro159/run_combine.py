#!/usr/bin/env python3
"""combine_list.csv の定義に従って、複数の md ファイルを結合する。

CSV 形式 (ヘッダ必須):
    output_name,file1,file2[,file3,...]

使い方:
    python3 run_combine.py                       # combine_list.csv を読んで combined/ に出力
    python3 run_combine.py --csv my_list.csv     # 別の CSV を指定
    python3 run_combine.py --dry-run             # 実行せず内容だけ表示
"""
import argparse
import csv
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
COMBINE_SCRIPT = HERE / "combine_md.py"
DEFAULT_CSV = HERE / "combine_list.csv"
OUTPUT_DIR = HERE / "combined"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV,
                        help=f"CSV ファイル (default: {DEFAULT_CSV.name})")
    parser.add_argument("--output-dir", type=Path, default=OUTPUT_DIR,
                        help=f"出力先 (default: {OUTPUT_DIR.name}/)")
    parser.add_argument("--dry-run", action="store_true",
                        help="実行せず処理内容だけ表示")
    parser.add_argument("--overwrite", action="store_true",
                        help="既存ファイルを上書き (default: スキップ)")
    args = parser.parse_args()

    if not args.csv.is_file():
        print(f"Error: CSV が見つかりません: {args.csv}", file=sys.stderr)
        return 1

    args.output_dir.mkdir(parents=True, exist_ok=True)

    rows = []
    with open(args.csv, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)

    if not rows:
        print("Warning: CSV にエントリがありません", file=sys.stderr)
        return 0

    # 入力ファイルの存在確認
    file_cols = [c for c in rows[0].keys() if c.startswith("file")]
    missing = set()
    for r in rows:
        for col in file_cols:
            v = (r.get(col) or "").strip()
            if v and not (HERE / v).is_file():
                missing.add(v)
    if missing:
        print("Error: 以下の入力ファイルが見つかりません:", file=sys.stderr)
        for m in sorted(missing):
            print(f"  - {m}", file=sys.stderr)
        return 1

    def _rel(p: Path) -> str:
        try:
            return str(p.relative_to(HERE))
        except ValueError:
            return str(p)

    print(f"=== Combine Runner ===")
    print(f"CSV: {_rel(args.csv)}")
    print(f"出力: {_rel(args.output_dir)}/")
    print(f"件数: {len(rows)}")
    print()

    skipped = 0
    created = 0
    for i, r in enumerate(rows, 1):
        name = (r.get("output_name") or "").strip()
        if not name:
            print(f"[{i}/{len(rows)}] ⚠ output_name が空 - スキップ")
            continue

        files = []
        for col in file_cols:
            v = (r.get(col) or "").strip()
            if v:
                files.append(v)

        out = args.output_dir / f"{name}.md"
        rel_out = _rel(out)

        if out.exists() and not args.overwrite:
            print(f"[{i}/{len(rows)}] - skip (exists): {rel_out}")
            skipped += 1
            continue

        cmd = ["python3", str(COMBINE_SCRIPT), *files, "-o", str(out)]
        print(f"[{i}/{len(rows)}] {name}.md  ←  {' + '.join(files)}")

        if args.dry_run:
            continue

        try:
            subprocess.run(cmd, check=True, cwd=str(HERE))
            created += 1
        except subprocess.CalledProcessError as e:
            print(f"\n❌ 失敗: {name} (exit={e.returncode})", file=sys.stderr)
            return e.returncode

    print()
    print(f"作成: {created} 件 / スキップ: {skipped} 件 / 合計: {len(rows)} 件")
    return 0


if __name__ == "__main__":
    sys.exit(main())
