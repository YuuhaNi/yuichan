#!/usr/bin/env python3
"""
.md (内部に ```yui ブロックを含む) を解析し、

  - feature(行) × sample(列) の出現回数行列  (counts.csv)
  - syntax / stdlib それぞれのカバレッジ・多様性指標   (metrics.csv)
  - ヒートマップ                                   (heatmap.png)

を出力する。check_yui.py の解析ロジックを再利用する。

使い方:
    python3 pro159/coverage/analyze.py pro159/codesample_10.md
    python3 pro159/coverage/analyze.py pro159/codesample_10.md -o pro159/coverage/out
"""

import argparse
import csv
import math
import os
import sys
from collections import Counter

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib  # noqa: F401  (import するだけで日本語フォントが効く)

# プロジェクトルート (= pro159 の親) を sys.path に追加して check_yui を import
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)

from check_yui import (  # noqa: E402
    SYNTAX_FEATURES,
    analyze_path,
    get_stdlib_aliases,
)


# ─────────────────────────────────────────────
# 行列構築
# ─────────────────────────────────────────────

def build_matrices(path):
    """analyze_path の結果から syntax / stdlib それぞれの DataFrame を作る。

    返り値:
        syntax_df : index=SYNTAX_FEATURES, columns=sample names, values=count
        stdlib_df : index=stdlib 代表名,    columns=sample names, values=count
    """
    samples = analyze_path(path)
    sample_names = [s[0] for s in samples]

    # syntax: 定義済みの全要素を行に持つ
    syntax_data = {
        name: [feat.get(f, 0) for f in SYNTAX_FEATURES]
        for name, feat, _ in samples
    }
    syntax_df = pd.DataFrame(syntax_data, index=SYNTAX_FEATURES)

    # stdlib: 全エイリアスのカウント合計を、代表名行にまとめる
    aliases = get_stdlib_aliases()
    stdlib_index = [rep for rep, _ in aliases]
    stdlib_data = {}
    for name, _, names_counter in samples:
        row = []
        for _, parts in aliases:
            row.append(sum(names_counter.get(p, 0) for p in parts))
        stdlib_data[name] = row
    stdlib_df = pd.DataFrame(stdlib_data, index=stdlib_index)

    return sample_names, syntax_df, stdlib_df


# ─────────────────────────────────────────────
# 指標計算
# ─────────────────────────────────────────────

def compute_metrics(df, label):
    """feature × sample の出現回数 DataFrame から集合全体の指標を計算する。

    - n_features_total   : 行数（定義済み要素数）
    - n_features_used    : 1 度以上出現した要素数
    - coverage           : used / total
    - total_occurrences  : 全セルの合計
    - shannon_entropy    : H = -Σ p_i log p_i  (p は要素 i の出現割合, 自然対数)
    - normalized_entropy : H / log(n_features_used)  (0..1)
    - gini_simpson       : 1 - Σ p_i^2
    - effective_n        : exp(H)  (Hill number, q=1)

    sample ごとの指標 (per-sample) も返す。
    """
    counts = df.sum(axis=1).values.astype(float)  # 各 feature の総出現数
    total = counts.sum()
    n_total = len(counts)
    n_used = int((counts > 0).sum())

    if total > 0 and n_used > 0:
        p = counts[counts > 0] / total
        H = float(-(p * np.log(p)).sum())
        H_norm = H / math.log(n_used) if n_used > 1 else 0.0
        gs = float(1.0 - (p ** 2).sum())
        eff = float(math.exp(H))
    else:
        H = H_norm = gs = eff = 0.0

    overall = {
        'category': label,
        'n_samples': df.shape[1],
        'n_features_total': n_total,
        'n_features_used': n_used,
        'coverage': n_used / n_total if n_total else 0.0,
        'total_occurrences': int(total),
        'shannon_entropy': H,
        'normalized_entropy': H_norm,
        'gini_simpson': gs,
        'effective_n': eff,
    }

    # サンプルごとの指標
    per_sample_rows = []
    for col in df.columns:
        c = df[col].values.astype(float)
        t = c.sum()
        used = int((c > 0).sum())
        if t > 0 and used > 0:
            p = c[c > 0] / t
            h = float(-(p * np.log(p)).sum())
            h_norm = h / math.log(used) if used > 1 else 0.0
            g = float(1.0 - (p ** 2).sum())
            e = float(math.exp(h))
        else:
            h = h_norm = g = e = 0.0
        per_sample_rows.append({
            'category': label,
            'sample': col,
            'n_features_used': used,
            'coverage': used / n_total if n_total else 0.0,
            'total_occurrences': int(t),
            'shannon_entropy': h,
            'normalized_entropy': h_norm,
            'gini_simpson': g,
            'effective_n': e,
        })

    return overall, per_sample_rows


# ─────────────────────────────────────────────
# ヒートマップ
# ─────────────────────────────────────────────

def draw_heatmap(df, title, out_path, drop_zero_rows=True, annotate=True):
    """feature × sample の出現回数ヒートマップを描く。色は log1p, 注釈は生の数。"""
    if drop_zero_rows:
        df_plot = df.loc[(df.sum(axis=1) > 0)]
        if df_plot.empty:
            df_plot = df
    else:
        df_plot = df

    data = df_plot.values
    color = np.log1p(data)

    n_rows, n_cols = df_plot.shape
    fig_w = max(6, 0.6 * n_cols + 3)
    fig_h = max(4, 0.28 * n_rows + 2)
    fig, ax = plt.subplots(figsize=(fig_w, fig_h))

    im = ax.imshow(color, aspect='auto', cmap='YlGnBu')
    ax.set_xticks(range(n_cols))
    ax.set_xticklabels(df_plot.columns, rotation=45, ha='right', fontsize=8)
    ax.set_yticks(range(n_rows))
    ax.set_yticklabels(df_plot.index, fontsize=7)
    ax.set_title(title)

    if annotate:
        for i in range(n_rows):
            for j in range(n_cols):
                v = int(data[i, j])
                if v == 0:
                    continue
                # 背景の濃さで文字色を切り替える
                norm = color[i, j] / (color.max() if color.max() > 0 else 1)
                ax.text(j, i, str(v), ha='center', va='center',
                        fontsize=6, color='white' if norm > 0.55 else 'black')

    cbar = fig.colorbar(im, ax=ax, shrink=0.6)
    cbar.set_label('log(1 + count)', fontsize=8)

    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


# ─────────────────────────────────────────────
# メイン
# ─────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('path', help='対象 .md または .yui ファイル')
    ap.add_argument('-o', '--out-dir',
                    default=os.path.join(os.path.dirname(__file__), 'out'),
                    help='出力ディレクトリ (default: pro159/coverage/out)')
    args = ap.parse_args()

    base = os.path.splitext(os.path.basename(args.path))[0]
    out_dir = args.out_dir
    os.makedirs(out_dir, exist_ok=True)

    sample_names, syntax_df, stdlib_df = build_matrices(args.path)
    print(f'parsed {len(sample_names)} samples from {args.path}', file=sys.stderr)

    # counts.csv (syntax と stdlib を縦に連結 + category 列)
    syn = syntax_df.copy()
    syn.insert(0, 'category', 'syntax')
    syn.insert(1, 'name', syn.index)
    std = stdlib_df.copy()
    std.insert(0, 'category', 'stdlib')
    std.insert(1, 'name', std.index)
    counts_path = os.path.join(out_dir, f'{base}_counts.csv')
    pd.concat([syn, std], ignore_index=True).to_csv(counts_path, index=False)

    # metrics.csv
    overall_syn, per_syn = compute_metrics(syntax_df, 'syntax')
    overall_std, per_std = compute_metrics(stdlib_df, 'stdlib')
    overall_path = os.path.join(out_dir, f'{base}_metrics_overall.csv')
    per_sample_path = os.path.join(out_dir, f'{base}_metrics_per_sample.csv')
    pd.DataFrame([overall_syn, overall_std]).to_csv(overall_path, index=False)
    pd.DataFrame(per_syn + per_std).to_csv(per_sample_path, index=False)

    # heatmap
    syn_heatmap = os.path.join(out_dir, f'{base}_syntax_heatmap.png')
    std_heatmap = os.path.join(out_dir, f'{base}_stdlib_heatmap.png')
    draw_heatmap(syntax_df,
                 f'{base} — syntax features (count)', syn_heatmap)
    draw_heatmap(stdlib_df,
                 f'{base} — stdlib functions (count, used only)', std_heatmap)

    # コンソールサマリ
    print()
    print('=== overall ===')
    print(pd.DataFrame([overall_syn, overall_std]).to_string(index=False))
    print()
    print('outputs:')
    for p in [counts_path, overall_path, per_sample_path, syn_heatmap, std_heatmap]:
        print(f'  {p}')


if __name__ == '__main__':
    main()
