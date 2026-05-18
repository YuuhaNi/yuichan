import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
from matplotlib.patches import Patch

rcParams["font.family"] = ["Hiragino Sans", "Hiragino Maru Gothic Pro", "DejaVu Sans"]
rcParams["axes.unicode_minus"] = False

# (label, gpt_mean, gpt_lo, gpt_hi, haiku_mean, haiku_lo, haiku_hi)
rows = [
    ("EXAMPLES_10",                  35.98, 35.98 - 7.27, 35.98 + 7.27, 22.56, 22.56 - 6.36, 22.56 + 6.36),
    ("apidoc +\nEXAMPLES_10",        42.68, 42.68 - 7.49, 42.68 + 7.49, 34.76, 34.76 - 7.21, 34.76 + 7.21),
    ("ebnf +\nEXAMPLES_10",          46.34, 46.34 - 7.54, 46.34 + 7.54, 31.71, 31.71 - 7.05, 31.71 + 7.05),
    ("spec +\nEXAMPLES_10",          55.49, 55.49 - 7.52, 55.49 + 7.52, 42.07, 42.07 - 7.47, 42.07 + 7.47),
    ("Errdoc_10 +\nEXAMPLES_10",     67.07, 67.07 - 7.12, 67.07 + 7.12, 43.90, 43.90 - 7.51, 43.90 + 7.51),
    ("Errdoc_total +\nEXAMPLES_10",  72.56, 72.56 - 6.77, 72.56 + 6.77, 56.71, 56.71 - 7.50, 56.71 + 7.50),
    # 単体（Wilson 95% CI from summary.json）
    ("Errdoc_10",                    17.07, 12.08, 23.57,  8.54,  5.15, 13.82),
    ("Errdoc_total",                 60.98, 53.34, 68.11, 40.85, 33.62, 48.50),
]

# pass@1 の合計（GPT+Haiku）で昇順ソート
rows.sort(key=lambda r: r[1] + r[4])

# JHumanEval は別カラム（plot_pass_at_k_042811.py の collect ロジックに合わせて
# 同 model×template で問題数最大→timestamp 新しい方を採用）
# GPT-5.4: 20260423_043200 (159/164, CI 93.06–98.69)
# Haiku 4.5: 20260423_031754 (154/164, CI 89.14–96.65)
JHE_LABEL = "JHumanEval"
jhe = (JHE_LABEL, 96.95, 93.06, 98.69, 93.90, 89.14, 96.65)
all_rows = rows + [jhe]

contexts   = [r[0] for r in all_rows]
gpt_mean   = [r[1] for r in all_rows]
gpt_err_lo = [r[1] - r[2] for r in all_rows]
gpt_err_hi = [r[3] - r[1] for r in all_rows]
haiku_mean = [r[4] for r in all_rows]
haiku_err_lo = [r[4] - r[5] for r in all_rows]
haiku_err_hi = [r[6] - r[4] for r in all_rows]

GPT_COLOR = "#12a37f"
CLAUDE_COLOR = "#da7452"
GPT_JHE_COLOR = "#4d4d4d"
CLAUDE_JHE_COLOR = "#b0b0b0"

gpt_colors   = [GPT_JHE_COLOR if c == JHE_LABEL else GPT_COLOR for c in contexts]
haiku_colors = [CLAUDE_JHE_COLOR if c == JHE_LABEL else CLAUDE_COLOR for c in contexts]

x = np.arange(len(contexts))
width = 0.38

fig, ax = plt.subplots(figsize=(13, 6))
bars1 = ax.bar(x - width/2, gpt_mean, width,
               yerr=[gpt_err_lo, gpt_err_hi],
               color=gpt_colors, capsize=4,
               edgecolor="white",
               error_kw={"elinewidth": 1.2, "ecolor": "#111"})
bars2 = ax.bar(x + width/2, haiku_mean, width,
               yerr=[haiku_err_lo, haiku_err_hi],
               color=haiku_colors, capsize=4,
               edgecolor="white",
               error_kw={"elinewidth": 1.2, "ecolor": "#111"})

ax.set_ylabel("Pass@1 (%)", fontsize=12)
ax.set_xlabel("文脈情報", fontsize=12)
ax.set_title("文脈情報を組み合わせた場合のコード生成性能 (95% Wilson CI)", fontsize=13)
ax.set_xticks(x)
ax.set_xticklabels(contexts, rotation=20, ha="right")
ax.set_ylim(0, 105)
ax.yaxis.grid(True, linestyle="--", alpha=0.4)
ax.set_axisbelow(True)

legend_handles = [
    Patch(facecolor=GPT_COLOR, edgecolor="white", label="GPT-5.4"),
    Patch(facecolor=CLAUDE_COLOR, edgecolor="white", label="Haiku 4.5"),
    Patch(facecolor=GPT_JHE_COLOR, edgecolor="white", label="GPT-5.4 (JHumanEval)"),
    Patch(facecolor=CLAUDE_JHE_COLOR, edgecolor="white", label="Haiku 4.5 (JHumanEval)"),
]
ax.legend(handles=legend_handles, title="モデル", loc="upper left", frameon=True, fontsize=9)

for bars, means in [(bars1, gpt_mean), (bars2, haiku_mean)]:
    for bar, m in zip(bars, means):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1.0,
                f"{m:.2f}", ha="center", va="bottom", fontsize=8)

# JHumanEval を区切る点線
if contexts and contexts[-1] == JHE_LABEL and len(contexts) > 1:
    ax.axvline(len(contexts) - 1.5, color="#888", linestyle=":", linewidth=1)

plt.tight_layout()
out_path = "/Users/nishigatayuuha/Git/yuichan-fork/pro159/combined_pass1.png"
plt.savefig(out_path, dpi=150)
print(f"saved: {out_path}")
