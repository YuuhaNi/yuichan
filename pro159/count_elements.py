"""
pro159 配下の codesample_*.md / hamari_codesample_*.md を走査し、
各ファイルで使われている syntax 要素 / library 要素のユニーク種類数を集計する。
"""

import re
from pathlib import Path

SYNTAX_PATTERNS = {
    # yuichan/syntax/yui.json で定義されたキーワード／記号
    # --- リテラル ---
    "null(値なし)":       r"値なし|null",
    "boolean-true(真)":   r"(?<![\w])真(?![\w判])",
    "boolean-false(偽)":  r"(?<![\w])偽(?![\w判])",
    # --- コレクション ---
    "array[]":            r"\[[^\]\n]*\]",
    "object{}":           r'\{"[^"]+"\s*:',
    # --- 属性 ---
    "property-length(の大きさ)": r"の大きさ",
    # --- import ---
    "import-standard(標準ライブラリを使う)": r"標準ライブラリを使う",
    "import-operator(四則演算子を使う)":     r"四則演算子を使う",
    # --- 二項演算子 ---
    "binary +":  r"(?<![+])\+(?![+=])",
    "binary -":  r"(?<=\d)\-(?=\d)|(?<=\))\-",
    "binary *":  r"\*(?![*=])",
    "binary /":  r"(?<![/])/(?![/=])",
    "binary %":  r"%(?![=])",
    "binary ==": r"==",
    "binary !=": r"!=",
    "binary <=": r"<=",
    "binary >=": r">=",
    "binary <":  r"(?<![<=!])<(?![=])",
    "binary >":  r"(?<![>=!])>(?![=])",
    # --- 配列インデックス ---
    "array-indexer(添字アクセス)": r"\w\[",
    # --- 代入／インクリメント ---
    "assignment(=)":           r"(?<![=!<>])=(?![=])",
    "increment(を増やす)":      r"を増やす",
    "decrement(を減らす)":      r"を減らす",
    # --- 配列追加 ---
    "append(を追加する)":       r"を追加する",
    "append2(に追加する)":      r"に追加する",
    # --- 制御 ---
    "break(くり返しを抜ける)":  r"くり返しを抜ける",
    "pass(何もしない)":         r"何もしない",
    "return-end(が答え)":       r"が[、]?答え",
    "return-none(関数から抜ける)": r"関数から抜ける",
    # --- 繰り返し ---
    "repeat(N回くり返す)":      r"回[、]?\s*くり返す",
    # --- 条件 ---
    "if-begin(もし)":           r"もし",
    "if-suffix!=(以外)":        r"以外",
    "if-suffix<(より小さい)":    r"より小さい",
    "if-suffix<=(以下)":        r"以下",
    "if-suffix>(より大きい)":    r"より大きい",
    "if-suffix>=(以上)":        r"以上",
    "if-suffixin(のいずれか)":   r"のいずれか(?!でもない)",
    "if-suffixnotin(のいずれでもない)": r"のいずれでもない",
    "if-then(ならば)":          r"ならば[、]?",
    "if-else(そうでなければ)":   r"そうでなければ[、]?",
    # --- 関数定義 ---
    "funcdef-args-begin(入力)": r"入力(?!なし)",
    "funcdef-noarg(入力なし)":  r"入力なし",
    "funcdef-block(に対し)":    r"に対し[て]?[、]?",
    # --- 文字列補間 ---
    "string-interpolation": r'"[^"]*\{[^}]+\}[^"]*"',
}

LIB_PATTERNS = {
    # yuichan/yuistdlib.py に登録されている関数（日本語名）20 種
    "絶対値": r"絶対値\(",
    "平方根": r"平方根\(",
    "乱数": r"乱数\(",
    "和": r"和\(",
    "差": r"差\(",
    "積": r"積\(",
    "商": r"商\(",
    "剰余": r"剰余\(",
    "最大値": r"最大値\(",
    "最小値": r"最小値\(",
    "ブール判定": r"ブール判定\(",
    "整数判定": r"整数判定\(",
    "小数判定": r"小数判定\(",
    "文字列判定": r"文字列判定\(",
    "配列判定": r"配列判定\(",
    "オブジェクト判定": r"オブジェクト判定\(",
    "整数化": r"整数化\(",
    "小数化": r"小数化\(",
    "文字列化": r"文字列化\(",
    "配列化": r"配列化\(",
}


def strip_comments(src: str) -> str:
    # `#` から行末までをコメントとして除去（文字列内 # は素朴に無視）
    out = []
    for line in src.splitlines():
        # 行頭インデントを残す
        idx = line.find("#")
        # ただし文字列の中にある # は無視 → 簡易的に "..." の中にあるかを判定
        if idx >= 0:
            # 文字列内かどうかをざっくり判定
            before = line[:idx]
            if before.count('"') % 2 == 0:
                line = before
        out.append(line)
    return "\n".join(out)


def extract_yui_blocks(md: str) -> str:
    """ ```yui ... ``` または ``` ... ``` のコードブロックを連結して返す """
    blocks = re.findall(r"```(?:yui)?\n(.*?)```", md, re.DOTALL)
    return "\n".join(blocks)


def extract_yui_blocks_list(md: str) -> list:
    """ コードブロックをリストで返す（ブロック単位の集計用） """
    return re.findall(r"```(?:yui)?\n(.*?)```", md, re.DOTALL)


def count_unique(src: str, patterns: dict) -> list:
    used = []
    for name, pat in patterns.items():
        if re.search(pat, src):
            used.append(name)
    return used


def count_occurrences(src: str, patterns: dict) -> dict:
    """ 各要素について出現回数を返す（0 のものは含めない） """
    counts = {}
    for name, pat in patterns.items():
        n = len(re.findall(pat, src))
        if n > 0:
            counts[name] = n
    return counts


def main():
    root = Path("/Users/nishigatayuuha/Git/yuichan-fork/pro159")
    files = sorted(root.glob("*codesample*.md"))

    rows = []
    for f in files:
        md = f.read_text(encoding="utf-8")
        yui = strip_comments(extract_yui_blocks(md))

        # 定義済み全要素について出現回数（未使用は 0）
        syn_all = {name: len(re.findall(pat, yui)) for name, pat in SYNTAX_PATTERNS.items()}
        lib_all = {name: len(re.findall(pat, yui)) for name, pat in LIB_PATTERNS.items()}

        syn_min = min(syn_all.values())
        lib_min = min(lib_all.values())
        syn_max = max(syn_all.values())
        lib_max = max(lib_all.values())

        # 0 回の要素 = 「ファイルに未登場の要素」
        syn_unused = [k for k, v in syn_all.items() if v == 0]
        lib_unused = [k for k, v in lib_all.items() if v == 0]

        rows.append((f.name, syn_min, syn_max, lib_min, lib_max, syn_unused, lib_unused))

    # 表示
    print(f"{'file':32s} {'syn_min':>8s} {'syn_max':>8s} {'lib_min':>8s} {'lib_max':>8s}")
    print("-" * 72)
    for name, sm, sx, lm, lx, *_ in rows:
        print(f"{name:32s} {sm:>8d} {sx:>8d} {lm:>8d} {lx:>8d}")

    print()
    print("=== 未登場要素 (0 回のもの) ===")
    for name, sm, sx, lm, lx, su, lu in rows:
        print(f"\n[{name}]")
        print(f"  未使用 syntax ({len(su)}): {su}")
        print(f"  未使用 lib    ({len(lu)}): {lu}")


if __name__ == "__main__":
    main()
