#!/usr/bin/env python3
"""results/*/summary.json と results_jhumaneval/*/summary.json を
集計して pass@k をバーで可視化する。

- X軸: 各 md ファイル (template) + 右端に jhumaneval
- Y軸: pass@k (%) ※小数点第2位まで表示
- 色: モデル (GPT=緑 / Claude=赤)。jhumaneval 列のみ灰色の濃淡で区別。
- 信頼区間: 95% Wilson Score (summary.json 内の値を使用)

使い方:
    python3 results/plot_pass_at_k.py
    python3 results/plot_pass_at_k.py --output pass_at_k.png
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


JHUMANEVAL_LABEL = "jhumaneval"


def model_group(model: str) -> str:
    m = model.lower()
    if "gpt" in m:
        return "GPT"
    if "claude" in m:
        return "Claude"
    return model


def template_label(summary: dict, summary_path: Path | None = None) -> str:
    # yuichan 側は template、jhumaneval 側は存在しないので固定ラベル
    t = summary.get("template")
    if t:
        return Path(t).stem
    # jhumaneval は results_jhumaneval/ 配下に置かれる
    if summary_path is not None and summary_path.parent.parent.name == "results_jhumaneval":
        return JHUMANEVAL_LABEL
    # --no-context などで template が無いケースはディレクトリ名末尾をラベル化
    if summary_path is not None:
        parts = summary_path.parent.name.split("_")
        # フォーマット: {timestamp}_{model}_{suffix...}  タイムスタンプは YYYYMMDD_HHMMSS の 2 要素
        if len(parts) >= 4:
            return "_".join(parts[3:])
    return JHUMANEVAL_LABEL


def collect(dirs: list[Path]) -> dict[tuple[str, str], dict]:
    """(group, template_label) -> summary を返す。

    同じ (group, template) に複数 run がある場合は total_problems が
    最大 (= 本番実行) のものを採用する。
    """
    best: dict[tuple[str, str], dict] = {}
    for d in dirs:
        if not d.exists():
            continue
        for summary_path in sorted(d.glob("*/summary.json")):
            with summary_path.open() as f:
                s = json.load(f)
            key = (model_group(s["model"]), template_label(s, summary_path))
            prev = best.get(key)
            if prev is None or s["total_problems"] > prev["total_problems"]:
                best[key] = s
    return best


def plot(data: dict[tuple[str, str], dict], output: Path) -> None:
    # jhumaneval は右端固定、他はアルファベット順
    other = sorted({k[1] for k in data if k[1] != JHUMANEVAL_LABEL})
    templates = other + ([JHUMANEVAL_LABEL] if any(k[1] == JHUMANEVAL_LABEL for k in data) else [])

    groups = ["GPT", "Claude"]
    # md テンプレ列: GPT=緑 / Claude=赤、jhumaneval 列のみ灰色濃淡
    md_colors = {"GPT": "#2ca02c", "Claude": "#d62728"}
    jhe_colors = {"GPT": "#4d4d4d", "Claude": "#b0b0b0"}

    x = np.arange(len(templates))
    width = 0.38

    fig, ax = plt.subplots(figsize=(max(10, len(templates) * 1.15), 6))

    # 凡例用プロキシを先に描画 (色がカテゴリで変わるので)
    from matplotlib.patches import Patch

    legend_handles = [
        Patch(facecolor=md_colors["GPT"], edgecolor="white", label="GPT"),
        Patch(facecolor=md_colors["Claude"], edgecolor="white", label="Claude"),
        Patch(facecolor=jhe_colors["GPT"], edgecolor="white", label="GPT (jhumaneval)"),
        Patch(facecolor=jhe_colors["Claude"], edgecolor="white", label="Claude (jhumaneval)"),
    ]

    for i, g in enumerate(groups):
        vals, lo_err, hi_err, bar_colors = [], [], [], []
        for t in templates:
            s = data.get((g, t))
            if s is None:
                vals.append(np.nan)
                lo_err.append(0.0)
                hi_err.append(0.0)
                bar_colors.append(md_colors[g])
                continue
            p = s["pass_at_k"]
            ci = s["confidence_interval_95"]
            vals.append(p)
            lo_err.append(max(0.0, p - ci["lower"]))
            hi_err.append(max(0.0, ci["upper"] - p))
            bar_colors.append(jhe_colors[g] if t == JHUMANEVAL_LABEL else md_colors[g])

        offset = (i - 0.5) * width
        bars = ax.bar(
            x + offset,
            vals,
            width,
            color=bar_colors,
            yerr=[lo_err, hi_err],
            capsize=4,
            error_kw={"elinewidth": 1.2, "ecolor": "#111"},
            edgecolor="white",
        )
        for bar, v in zip(bars, vals):
            if not np.isnan(v):
                ax.text(
                    bar.get_x() + bar.get_width() / 2,
                    v + 0.8,
                    f"{v:.2f}",
                    ha="center",
                    va="bottom",
                    fontsize=8,
                )

    ax.set_xticks(x)
    ax.set_xticklabels(templates, rotation=30, ha="right")
    ax.set_ylabel("pass@k (%)")
    ax.set_xlabel("prompt template (md) / benchmark")
    ax.set_title("pass@k by prompt template (95% Wilson CI)")
    ax.set_ylim(0, 100)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:.2f}"))
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    ax.legend(handles=legend_handles, title="model", fontsize=8)
    # jhumaneval を視覚的に分離する縦線
    if templates and templates[-1] == JHUMANEVAL_LABEL and len(templates) > 1:
        ax.axvline(len(templates) - 1.5, color="#888", linestyle=":", linewidth=1)
    fig.tight_layout()
    fig.savefig(output, dpi=150)
    print(f"saved: {output}")


def main() -> None:
    repo = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--results-dirs",
        type=Path,
        nargs="+",
        default=[repo / "results", repo / "results_jhumaneval"],
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=repo / "results" / "pass_at_k.png",
    )
    args = parser.parse_args()

    data = collect(args.results_dirs)
    if not data:
        raise SystemExit(f"no summary.json found under {args.results_dirs}")
    plot(data, args.output)


if __name__ == "__main__":
    main()
