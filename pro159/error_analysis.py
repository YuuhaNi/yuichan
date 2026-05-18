"""
評価結果ディレクトリ (results/<run>/) を読んで、
失敗した各サンプルを Yui 処理系に再投入し、YuiError.messages[0] を
タグとして集計する。

Usage:
    python3 pro159/error_analysis.py results/<run_dir> [results/<run_dir2> ...]
出力:
    各 <run_dir>/error_tags.csv  と  error_tags.md  を生成
    複数ディレクトリ指定時は標準出力に比較表を出す
"""
from __future__ import annotations
import argparse
import contextlib
import io
import json
import os
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from yuichan.yuiruntime import YuiRuntime
from yuichan.yuierror import YuiError, ERROR_MESSAGES

# yuierror.py の登録名と raise 側のタグ名がずれているケースを補完
TAG_ALIASES = {
    'index-error': 'error-index',
}


def describe(tag: str) -> str:
    return ERROR_MESSAGES.get(tag) or ERROR_MESSAGES.get(TAG_ALIASES.get(tag, ''), '(処理系の登録説明なし)')


def extract_tests(canonical: str) -> str:
    """canonical_solution から '>>> 式' / '期待値' のテストブロックだけ抜き出す。"""
    lines = canonical.splitlines()
    # 最初の '>>>' 行以降をすべて返す
    for i, line in enumerate(lines):
        if line.lstrip().startswith('>>>'):
            return '\n'.join(lines[i:])
    return ''


def classify(code: str, tests: str = '', timeout: int = 10) -> tuple[str, str]:
    """code+tests を yui で実行し、(tag, token) を返す。成功時は ('pass', '')。"""
    full = code if not tests else (code.rstrip() + '\n\n' + tests)
    rt = YuiRuntime()
    buf_out, buf_err = io.StringIO(), io.StringIO()
    try:
        with contextlib.redirect_stdout(buf_out), contextlib.redirect_stderr(buf_err):
            rt.exec(full, syntax='yui', timeout=timeout, eval_mode=False)
        return ('pass', '')
    except YuiError as e:
        msgs = e.messages if isinstance(e.messages, tuple) else (e.messages,)
        tag = msgs[0] if msgs else 'unknown'
        token = msgs[1] if len(msgs) > 1 else ''
        return (str(tag), str(token))
    except Exception as e:
        return (f'non-yui:{type(e).__name__}', str(e)[:80])


def load_run_meta(run_dir: Path) -> dict:
    """summary.json から model / context を拾う。なければ空。"""
    sj = run_dir / 'summary.json'
    if not sj.exists():
        return {}
    try:
        with sj.open() as f:
            d = json.load(f)
        return {
            'model': d.get('model', ''),
            'context': d.get('context', '') or d.get('template', ''),
        }
    except Exception:
        return {}


def load_existing(run_dir: Path) -> dict | None:
    """既存の error_tags.csv を読み込んで result dict を再構成する。"""
    csv_path = run_dir / 'error_tags.csv'
    if not csv_path.exists():
        return None
    tags = {}
    with csv_path.open() as f:
        next(f, None)  # header
        for line in f:
            parts = line.rstrip('\n').split(',')
            if len(parts) < 3:
                continue
            tag = parts[0]
            n = int(parts[-1])
            tags[tag] = n
    meta = load_run_meta(run_dir)
    sj = run_dir / 'summary.json'
    total = passed = failed = 0
    if sj.exists():
        with sj.open() as f:
            d = json.load(f)
        total = d.get('total_problems', 0)
        passed = d.get('passed_problems', 0)
        failed = d.get('failed_problems', 0)
    return {
        'run': run_dir.name,
        'total': total, 'passed': passed, 'failed': failed,
        'tags': tags, 'per_problem': [],
        **meta,
    }


def analyze_run(run_dir: Path) -> dict:
    """1つの結果ディレクトリを解析し、集計を返す。"""
    jsonl = run_dir / 'result.jsonl'
    if not jsonl.exists():
        raise FileNotFoundError(jsonl)

    rows = []
    with jsonl.open() as f:
        for line in f:
            rows.append(json.loads(line))

    failed = [r for r in rows if not r.get('passed')]
    print(f'[{run_dir.name}] total={len(rows)}, failed={len(failed)}', file=sys.stderr)

    tag_counter = Counter()
    per_problem = []
    for i, r in enumerate(failed):
        code = r.get('extracted') or ''
        tests = extract_tests(r.get('canonical_solution') or '')
        if not code.strip():
            tag, token = ('empty-extracted', '')
        else:
            tag, token = classify(code, tests)
        tag_counter[tag] += 1
        per_problem.append({
            'problem_id': r.get('problem_id'),
            'problem_name': r.get('problem_name'),
            'tag': tag,
            'token': token,
        })
        if (i + 1) % 20 == 0:
            print(f'  {i+1}/{len(failed)} processed', file=sys.stderr)

    meta = load_run_meta(run_dir)
    return {
        'run': run_dir.name,
        'total': len(rows),
        'passed': len(rows) - len(failed),
        'failed': len(failed),
        'tags': dict(tag_counter.most_common()),
        'per_problem': per_problem,
        **meta,
    }


def write_outputs(result: dict, run_dir: Path):
    """CSV と Markdown を run_dir に書き出す。"""
    csv_path = run_dir / 'error_tags.csv'
    with csv_path.open('w') as f:
        f.write('tag,description,count\n')
        for tag, n in result['tags'].items():
            desc = describe(tag).replace(',', '、')
            f.write(f'{tag},{desc},{n}\n')

    md_path = run_dir / 'error_tags.md'
    with md_path.open('w') as f:
        f.write(f"# エラータグ分析 — {result['run']}\n\n")
        f.write(f"- 総問題数: {result['total']}\n")
        f.write(f"- 合格: {result['passed']}\n")
        f.write(f"- 失敗: {result['failed']}\n\n")
        f.write("## タグ別集計\n\n")
        f.write("| タグ | 説明 | 件数 | 失敗中の割合 |\n|---|---|---:|---:|\n")
        total_failed = result['failed'] or 1
        for tag, n in result['tags'].items():
            pct = 100.0 * n / total_failed
            f.write(f"| `{tag}` | {describe(tag)} | {n} | {pct:.1f}% |\n")
        f.write("\n## 問題ごとの分類\n\n")
        f.write("| ID | 関数 | タグ | トークン |\n|---|---|---|---|\n")
        for p in result['per_problem']:
            tok = (p['token'] or '').replace('|', '\\|')[:60]
            f.write(f"| {p['problem_id']} | `{p['problem_name']}` | `{p['tag']}` | {tok} |\n")
    print(f'[{result["run"]}] wrote {csv_path.name} / {md_path.name}', file=sys.stderr)


def print_comparison(results: list[dict]):
    """複数 run のタグ分布を横並び表示。"""
    all_tags = sorted({t for r in results for t in r['tags']})
    header = ['tag'] + [r['run'] for r in results]
    print('\n## 比較表 (件数)\n')
    print('| ' + ' | '.join(header) + ' |')
    print('|' + '|'.join(['---'] * len(header)) + '|')
    for tag in all_tags:
        row = [tag] + [str(r['tags'].get(tag, 0)) for r in results]
        print('| ' + ' | '.join(row) + ' |')


def write_summary(results: list[dict], out_path: Path):
    """全 run のタグ件数を1つの CSV と Markdown にまとめる。"""
    all_tags = sorted({t for r in results for t in r['tags']})

    # CSV (long format: 1 row per (run, tag))
    csv_path = out_path.with_suffix('.csv')
    with csv_path.open('w') as f:
        f.write('run,model,context,total,passed,failed,pass_at_1,tag,description,count,share_in_failed\n')
        for r in results:
            model = r.get('model', '')
            context = r.get('context', '')
            total = r['total']
            passed = r['passed']
            failed = r['failed']
            pass1 = 100.0 * passed / total if total else 0.0
            for tag, n in r['tags'].items():
                desc = describe(tag).replace(',', '、')
                share = 100.0 * n / failed if failed else 0.0
                f.write(f'{r["run"]},{model},{context},{total},{passed},{failed},{pass1:.2f},{tag},{desc},{n},{share:.2f}\n')

    # Markdown: pivot table (rows=run, cols=tag)
    md_path = out_path.with_suffix('.md')
    with md_path.open('w') as f:
        f.write('# 全エラータグ集計サマリ\n\n')
        f.write(f'対象 run 数: {len(results)} / タグ種類数: {len(all_tags)}\n\n')

        # 概要表
        f.write('## 概要\n\n')
        f.write('| run | model | context | total | passed | failed | pass@1 |\n')
        f.write('|---|---|---|---:|---:|---:|---:|\n')
        for r in results:
            pass1 = 100.0 * r['passed'] / r['total'] if r['total'] else 0.0
            f.write(f'| `{r["run"]}` | {r.get("model","")} | {r.get("context","")} | {r["total"]} | {r["passed"]} | {r["failed"]} | {pass1:.2f}% |\n')

        # ピボット表
        f.write('\n## タグ別件数 (run × tag)\n\n')
        header = ['run', 'failed'] + all_tags
        f.write('| ' + ' | '.join(header) + ' |\n')
        f.write('|' + '|'.join(['---'] * len(header)) + '|\n')
        for r in results:
            row = [r['run'], str(r['failed'])] + [str(r['tags'].get(t, 0)) for t in all_tags]
            f.write('| ' + ' | '.join(row) + ' |\n')

        # タグ説明
        f.write('\n## タグ説明\n\n')
        f.write('| タグ | 説明 |\n|---|---|\n')
        for t in all_tags:
            f.write(f'| `{t}` | {describe(t)} |\n')

    print(f'wrote summary: {csv_path.name} / {md_path.name}', file=sys.stderr)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('run_dirs', nargs='+', type=Path)
    ap.add_argument('--timeout', type=int, default=10)
    ap.add_argument('--summary', type=Path, default=None,
                    help='全 run の集計を書き出す出力パス (拡張子なし)')
    ap.add_argument('--skip-existing', action='store_true',
                    help='error_tags.csv が既にある run はスキップ')
    args = ap.parse_args()

    results = []
    for d in args.run_dirs:
        if not d.is_dir():
            print(f'skip (not dir): {d}', file=sys.stderr)
            continue
        if args.skip_existing and (d / 'error_tags.csv').exists():
            r = load_existing(d)
            if r:
                print(f'[{d.name}] skip (cached)', file=sys.stderr)
                results.append(r)
                continue
        r = analyze_run(d)
        write_outputs(r, d)
        results.append(r)

    if len(results) > 1:
        print_comparison(results)

    if args.summary:
        write_summary(results, args.summary)


if __name__ == '__main__':
    main()
