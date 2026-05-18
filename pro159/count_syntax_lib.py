#!/usr/bin/env python3
"""EXAMPLES_10/13/20/33/40 の syntax / lib 使用回数を集計する。

- syntax: Yui の構文要素（キーワード、構文糖、演算記法など）
- lib   : 標準ライブラリ関数（yuistdlib.py で登録されているもの）

対象は ```yui ... ``` で囲まれたブロック全体（テスト行 >>> も含む）。
"""

from __future__ import annotations
import re
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent
FILES = [
    ("EXAMPLES_10", ROOT / "codesample_10.md"),
    ("EXAMPLES_13", ROOT / "codesample_13.md"),
    ("EXAMPLES_20", ROOT / "codesample_20.md"),
    ("EXAMPLES_33", ROOT / "codesample_all.md"),
    ("EXAMPLES_40", ROOT / "codesample_allplus_40.md"),
]

# Yui 構文要素（日本語キーワード／助詞付きパターン）
SYNTAX_PATTERNS = [
    ("入力", r"入力(?![なし])"),         # パラメータ宣言（入力なし は除外）
    ("入力なし", r"入力なし"),
    ("に対し", r"に対し"),
    ("が答え", r"が答え"),
    ("もし", r"もし"),
    ("ならば", r"ならば"),
    ("そうでなければ", r"そうでなければ"),
    ("回くり返す", r"回くり返す"),
    ("くり返しを抜ける", r"くり返しを抜ける"),
    ("何もしない", r"何もしない"),
    ("値なし", r"値なし"),
    ("真", r"(?<![判])真(?![偽])"),       # 真理値リテラル（判定語と衝突回避）
    ("偽", r"(?<![判])偽"),
    ("を増やす", r"を増やす"),
    ("を減らす", r"を減らす"),
    ("を追加する", r"を追加する"),
    ("の大きさ", r"の大きさ"),
    ("のいずれか", r"のいずれか(?!でもない)"),
    ("のいずれでもない", r"のいずれでもない"),
    ("以上", r"以上"),
    ("以下", r"以下"),
    ("より大きい", r"より大きい"),
    ("より小さい", r"より小さい"),
    ("以外", r"以外"),
    ("標準ライブラリを使う", r"標準ライブラリを使う"),
    ("文字列補間 {}", r'"[^"\n]*\{[^}\n]+\}[^"\n]*"'),  # "...{x}..."
]

# 標準ライブラリ関数（日本語名）— yuistdlib.py の register リストから
LIB_NAMES = [
    "絶対値", "平方根", "乱数",
    "和", "差", "積", "商", "剰余",
    "最大値", "最小値",
    "ブール判定", "整数判定", "小数判定", "文字列判定", "配列判定", "オブジェクト判定",
    "整数化", "小数化", "文字列化", "配列化",
]


def extract_yui_blocks(path: Path) -> str:
    """``` yui ... ``` で囲まれた中身を全部つなげて返す"""
    text = path.read_text(encoding="utf-8")
    blocks = re.findall(r"```yui\n(.*?)\n```", text, flags=re.DOTALL)
    return "\n".join(blocks)


def count_syntax(text: str) -> Counter:
    c = Counter()
    for name, pat in SYNTAX_PATTERNS:
        c[name] = len(re.findall(pat, text))
    return c


def count_lib(text: str) -> Counter:
    c = Counter()
    for name in LIB_NAMES:
        # 関数呼び出し形 名前(  だけを数える（説明テキストでの言及は除外）
        c[name] = len(re.findall(rf"{re.escape(name)}\(", text))
    return c


def top_n(counter: Counter, n: int = 10) -> list[tuple[str, int]]:
    return [(k, v) for k, v in counter.most_common() if v > 0][:n]


def render_table(title: str, rows_per_label: dict[str, list[tuple[str, int]]]):
    print(f"\n## {title}\n")
    labels = list(rows_per_label.keys())
    # 横並びの表
    header = "| 順位 | " + " | ".join(f"{l} (項目 / 回数)" for l in labels) + " |"
    sep = "|------|" + "|".join(["----------------------" for _ in labels]) + "|"
    print(header)
    print(sep)
    max_rows = max(len(rows_per_label[l]) for l in labels)
    for i in range(max_rows):
        cells = []
        for l in labels:
            rows = rows_per_label[l]
            if i < len(rows):
                k, v = rows[i]
                cells.append(f"{k} / {v}")
            else:
                cells.append("—")
        print(f"| {i+1} | " + " | ".join(cells) + " |")


def main():
    syntax_per_file = {}
    lib_per_file = {}
    totals = {}
    for label, path in FILES:
        text = extract_yui_blocks(path)
        s = count_syntax(text)
        l = count_lib(text)
        syntax_per_file[label] = top_n(s, 10)
        lib_per_file[label] = top_n(l, 10)
        totals[label] = (sum(s.values()), sum(l.values()), len(text.splitlines()))

    render_table("syntax 使用回数 上位10件", syntax_per_file)
    render_table("lib（標準ライブラリ関数）使用回数 上位10件", lib_per_file)

    print("\n## 参考: 各ファイルの合計\n")
    print("| ファイル | syntax 合計 | lib 合計 | yui ブロック行数 |")
    print("|----------|-------------|----------|------------------|")
    for label, (s, l, n) in totals.items():
        print(f"| {label} | {s} | {l} | {n} |")


if __name__ == "__main__":
    main()
