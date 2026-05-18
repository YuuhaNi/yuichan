"""
check_yui.py が出力する CSV から各ファイルの syntax / library 出現回数の
最小・最大を集計する。母集団 = check_yui.py が定義する全要素（未登場 = 0）。
"""

import csv
from pathlib import Path

CSV_DIR = Path("/tmp")
FILES = [
    "codesample_10.csv",
    "codesample_10plus_15.csv",
    "codesample_13.csv",
    "codesample_20.csv",
    "codesample_all.csv",
    "codesample_allplus_40.csv",
    "codesample_full_45.csv",
    "codesample_random10.csv",
]


def summarize(csv_path: Path):
    syn_counts = []
    lib_counts = []
    with csv_path.open(encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cat, name, total = row[0], row[1], int(row[2])
            if cat == "syntax":
                syn_counts.append((name, total))
            elif cat == "stdlib":
                lib_counts.append((name, total))

    syn_vals = [t for _, t in syn_counts]
    lib_vals = [t for _, t in lib_counts]
    syn_min = min(syn_vals)
    lib_min = min(lib_vals)
    return {
        "syn_min": syn_min,
        "syn_max": max(syn_vals),
        "lib_min": lib_min,
        "lib_max": max(lib_vals),
        "syn_unused": [n for n, t in syn_counts if t == 0],
        "lib_unused": [n for n, t in lib_counts if t == 0],
        "syn_min_items": [(n, t) for n, t in syn_counts if t == syn_min],
        "lib_min_items": [(n, t) for n, t in lib_counts if t == lib_min],
    }


def main():
    print(f"{'file':32s} {'syn_min':>8s} {'syn_max':>8s} {'lib_min':>8s} {'lib_max':>8s}")
    print("-" * 72)
    rows = []
    for fn in FILES:
        s = summarize(CSV_DIR / fn)
        rows.append((fn, s))
        print(f"{fn[:-4]:32s} {s['syn_min']:>8d} {s['syn_max']:>8d} {s['lib_min']:>8d} {s['lib_max']:>8d}")

    print()
    print("=== 最小値を取った要素（その値で並ぶもの全部）===")
    for fn, s in rows:
        print(f"\n[{fn[:-4]}]")
        print(f"  syntax 最小={s['syn_min']}: {[n for n,_ in s['syn_min_items']]}")
        print(f"  lib    最小={s['lib_min']}: {[n for n,_ in s['lib_min_items']]}")


if __name__ == "__main__":
    main()
