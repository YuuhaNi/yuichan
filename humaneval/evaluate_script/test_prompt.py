#!/usr/bin/env python3
"""
プロンプト生成のテストスクリプト

Usage:
    python test_prompt.py --problem 0 --lang en
    python test_prompt.py --problem 1 --lang ja --context-file doc/CHEATSHEET.md
"""

import argparse
from pathlib import Path


def create_prompt(problem_file_path, context_file='doc/context.md'):
    """
    問題文ファイルからプロンプトを作成

    Args:
        problem_file_path: 問題文ファイルのパス
        context_file: Yui言語リファレンスのパス (Noneの場合はコンテキストなし)

    Returns:
        (system_prompt, user_prompt): システムプロンプトとユーザープロンプト
    """
    # Yui言語リファレンスを読み込む（Noneの場合はスキップ）
    if context_file is not None:
        humaneval_dir = Path(problem_file_path).parent
        doc_path = humaneval_dir.parent / context_file

        with open(doc_path, 'r', encoding='utf-8') as f:
            yui_reference = f.read()
    else:
        yui_reference = None

    # 問題文ファイルを読み込む
    with open(problem_file_path, 'r', encoding='utf-8') as f:
        problem_content = f.read()

    # 言語判定
    is_japanese = '_ja.txt' in str(problem_file_path)

    # システムプロンプト
    if is_japanese:
        system_prompt = "コンテキストを読んで、指示通りに関数を定義してください。"
        instruction = """＜指示＞
次の仕様にあうYui言語の関数定義を完成させてください。"""
    else:
        system_prompt = "Read the context and define functions as instructed."
        instruction = """＜Instruction＞
Complete the Yui language function definition that matches the specification. """

    # ユーザープロンプト
    if yui_reference is not None:
        user_prompt = f"""＜コンテキスト / Context＞
{yui_reference}

{instruction}

{problem_content}"""
    else:
        # コンテキストなしの場合
        user_prompt = f"""{instruction}

{problem_content}"""

    return system_prompt, user_prompt


def main():
    parser = argparse.ArgumentParser(description='プロンプト生成テスト')
    parser.add_argument('--problem', required=True,
                        help='問題ID（例: 0, 1, 2）')
    parser.add_argument('--lang', choices=['en', 'ja'], default='en',
                        help='問題文の言語')
    parser.add_argument('--context-file', default='doc/context.md',
                        help='コンテキストファイルのパス')
    parser.add_argument('--no-context', action='store_true',
                        help='コンテキストなしでプロンプトを生成')
    parser.add_argument('--output', default=None,
                        help='出力ファイル（未指定の場合は標準出力）')
    parser.add_argument('--stats', action='store_true',
                        help='統計情報のみ表示')

    args = parser.parse_args()

    # --no-context が指定された場合、context_file を None に
    context_file = None if args.no_context else args.context_file

    # 問題ファイルを検索
    humaneval_dir = Path(__file__).parent.parent
    pattern = f"{args.problem}_*_{args.lang}.txt"
    problem_files = list(humaneval_dir.glob(pattern))

    if not problem_files:
        print(f"Error: 問題ファイルが見つかりません: {pattern}")
        return 1

    problem_file = problem_files[0]
    print(f"問題ファイル: {problem_file.name}")
    if context_file:
        print(f"コンテキスト: {context_file}")
    else:
        print(f"コンテキスト: なし")
    print("=" * 60)

    # プロンプトを生成
    system_prompt, user_prompt = create_prompt(problem_file, context_file)

    # 統計情報
    system_chars = len(system_prompt)
    user_chars = len(user_prompt)
    total_chars = system_chars + user_chars

    # 簡易的なトークン推定（文字数 / 4）
    estimated_tokens = total_chars // 4

    if args.stats:
        print(f"\n統計情報:")
        print(f"  システムプロンプト: {system_chars:,} 文字")
        print(f"  ユーザープロンプト: {user_chars:,} 文字")
        print(f"  合計: {total_chars:,} 文字")
        print(f"  推定トークン数: ~{estimated_tokens:,} トークン")
    else:
        # プロンプトを出力
        if args.output:
            output_path = Path(args.output)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write("=" * 60 + "\n")
                f.write("SYSTEM PROMPT\n")
                f.write("=" * 60 + "\n")
                f.write(system_prompt + "\n\n")
                f.write("=" * 60 + "\n")
                f.write("USER PROMPT\n")
                f.write("=" * 60 + "\n")
                f.write(user_prompt + "\n")
            print(f"\nプロンプトを保存しました: {output_path}")
        else:
            print("\n" + "=" * 60)
            print("SYSTEM PROMPT")
            print("=" * 60)
            print(system_prompt)
            print("\n" + "=" * 60)
            print("USER PROMPT")
            print("=" * 60)
            print(user_prompt)

        print(f"\n統計: {total_chars:,} 文字、推定 ~{estimated_tokens:,} トークン")

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main())
