import csv
import glob
import json
import os

PRO159_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(PRO159_DIR)
RESULTS_DIR = os.path.join(REPO_ROOT, "results")
TOKEN_CSV = os.path.join(PRO159_DIR, "token_counts.csv")
OUTPUT_CSV = os.path.join(PRO159_DIR, "token_efficiency.csv")


def load_token_counts():
    counts = {}
    with open(TOKEN_CSV, "r", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            counts[row["filename"]] = int(row["token_count"])
    return counts


def collect_results():
    by_key = {}
    for summary_path in sorted(glob.glob(os.path.join(RESULTS_DIR, "*", "summary.json"))):
        with open(summary_path, "r", encoding="utf-8") as f:
            summary = json.load(f)
        template = summary.get("template")
        if not template:
            continue
        rel = template[len("pro159/"):] if template.startswith("pro159/") else template
        model = summary.get("model", "")
        key = (rel, model)
        timestamp = summary.get("timestamp", "")
        prev = by_key.get(key)
        if prev is None or timestamp > prev["timestamp"]:
            by_key[key] = {
                "filename": rel,
                "model": model,
                "pass_at_k": summary.get("pass_at_k", 0.0),
                "passed_problems": summary.get("passed_problems", 0),
                "total_problems": summary.get("total_problems", 0),
                "timestamp": timestamp,
            }
    return list(by_key.values())


def main():
    token_counts = load_token_counts()
    results = collect_results()

    rows = []
    for r in results:
        tokens = token_counts.get(r["filename"])
        if tokens is None:
            print(f"[skip: no token count] {r['filename']}")
            continue
        pass_at_k = float(r["pass_at_k"])
        efficiency = pass_at_k / tokens if tokens > 0 else 0.0
        rows.append({
            "filename": r["filename"],
            "model": r["model"],
            "token_count": tokens,
            "pass_at_k": pass_at_k,
            "passed_problems": r["passed_problems"],
            "total_problems": r["total_problems"],
            "efficiency_per_1k_tokens": round(efficiency * 1000, 4),
            "timestamp": r["timestamp"],
        })

    rows.sort(key=lambda r: r["efficiency_per_1k_tokens"], reverse=True)

    with open(OUTPUT_CSV, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "filename",
                "model",
                "token_count",
                "pass_at_k",
                "passed_problems",
                "total_problems",
                "efficiency_per_1k_tokens",
                "timestamp",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nSaved: {OUTPUT_CSV} ({len(rows)} rows)\n")
    print(f"{'filename':<55} {'model':<22} {'tokens':>7} {'pass@1':>7} {'eff/1k':>8}")
    for r in rows:
        print(f"{r['filename']:<55} {r['model']:<22} {r['token_count']:>7} {r['pass_at_k']:>7.2f} {r['efficiency_per_1k_tokens']:>8.4f}")


if __name__ == "__main__":
    main()
