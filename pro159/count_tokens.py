import csv
import glob
import os

import anthropic
from dotenv import load_dotenv

PRO159_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(PRO159_DIR)
load_dotenv(os.path.join(REPO_ROOT, ".env"))

MODEL = "claude-haiku-4-5"
OUTPUT_CSV = os.path.join(PRO159_DIR, "token_counts.csv")


def main():
    client = anthropic.Anthropic()
    md_files = sorted(
        glob.glob(os.path.join(PRO159_DIR, "*.md"))
        + glob.glob(os.path.join(PRO159_DIR, "combined", "*.md"))
    )

    rows = []
    for path in md_files:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        char_count = len(content)
        result = client.messages.count_tokens(
            model=MODEL,
            messages=[{"role": "user", "content": content}],
        )
        token_count = result.input_tokens
        filename = os.path.relpath(path, PRO159_DIR)
        print(f"{filename}: {char_count} chars, {token_count} tokens")
        rows.append({
            "filename": filename,
            "char_count": char_count,
            "token_count": token_count,
            "model": MODEL,
        })

    with open(OUTPUT_CSV, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=["filename", "char_count", "token_count", "model"]
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nSaved: {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
