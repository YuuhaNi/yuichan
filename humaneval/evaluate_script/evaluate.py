#!/usr/bin/env python3
"""
HumanEval評価スクリプト for Yui言語

Usage:
    python evaluate.py --model openai --api-key YOUR_API_KEY
    python evaluate.py --model anthropic --api-key YOUR_API_KEY --k 3
    python evaluate.py --model ollama --model-name codellama
    python evaluate.py --model mlx --model-name mlx-community/Qwen2.5-Coder-7B-Instruct-4bit
    python evaluate.py --model-name mlx-community/Qwen2.5-Coder-7B-Instruct-4bit  # 自動判別
"""

import subprocess
import json
import argparse
import sys
import os
import time
import tempfile
from pathlib import Path
from typing import List, Dict, Any, Tuple
from datetime import datetime, timezone, timedelta

# .envファイルを読み込む（プロジェクトルート優先、なければスクリプトディレクトリ）
try:
    from dotenv import load_dotenv
    # プロジェクトルート（humaneval/evaluate_script の2階層上）の.envを優先
    project_root = Path(__file__).parent.parent.parent
    env_path = project_root / '.env'
    if not env_path.exists():
        # なければスクリプトディレクトリの.envを使用
        env_path = Path(__file__).parent / '.env'
    load_dotenv(dotenv_path=env_path)
except ImportError:
    pass  # python-dotenvがない場合はスキップ


def create_prompt(problem_file_path, context_file='doc/context.md'):
    """
    問題文ファイルまたは.yuiファイルからプロンプトを作成

    Args:
        problem_file_path: 問題文ファイル(.txt)または参照実装(.yui)のパス
        context_file: Yui言語リファレンスのパス (Noneの場合はコンテキストなし)

    Returns:
        (system_prompt, user_prompt): システムプロンプトとユーザープロンプト
    """
    # Yui言語リファレンスを読み込む（Noneの場合はスキップ）
    yui_reference = None
    if context_file is not None:
        humaneval_dir = Path(problem_file_path).parent
        # doc/context.md または docs/API_en.md などを試す
        possible_paths = [
            humaneval_dir.parent / context_file,
            humaneval_dir.parent / 'docs' / 'API_en.md',
            humaneval_dir.parent / 'docs' / 'syntax_en.md',
            humaneval_dir.parent / 'pro159' / 'guide_ja.md',
        ]
        for doc_path in possible_paths:
            if doc_path.exists():
                with open(doc_path, 'r', encoding='utf-8') as f:
                    yui_reference = f.read()
                break

    # 問題ファイルを読み込む
    with open(problem_file_path, 'r', encoding='utf-8') as f:
        problem_content = f.read()

    # .yuiファイルの場合、関数シグネチャとdoctestを抽出してプロンプトを生成
    is_yui_file = str(problem_file_path).endswith('.yui')
    if is_yui_file:
        # 関数名と引数を抽出
        func_name = None
        func_signature = None
        doctest_examples = []

        lines = problem_content.split('\n')
        for line in lines:
            # 関数定義を探す: "関数名 = 入力 引数1, 引数2 に対し {"
            if '= 入力' in line and 'に対し' in line:
                func_signature = line.strip()
                func_name = line.split('=')[0].strip()
            # doctestを抽出
            elif line.strip().startswith('>>>'):
                doctest_examples.append(line.strip())
            elif doctest_examples and not line.strip().startswith('#') and line.strip():
                # 期待される出力
                doctest_examples.append(line.strip())

        # プロンプト用の問題文を生成
        problem_content = f"""関数名: {func_name}

関数シグネチャ:
```yui
{func_signature}
    # ここに実装を書く
}}
```

テスト例:
"""
        for ex in doctest_examples[:4]:  # 最初の数例のみ
            problem_content += f"{ex}\n"

    # 言語判定
    is_japanese = '_ja.txt' in str(problem_file_path) or is_yui_file

    # システムプロンプト
    if is_japanese:
        system_prompt = "コンテキストを読んで、指示通りに関数を定義してください。"
        instruction = """<指示>
次の仕様にあうYui言語の関数定義を完成させてください。"""
    else:
        system_prompt = "Read the context and define functions as instructed."
        instruction = """<Instruction>
Complete the Yui language function definition that matches the specification. """

    # ユーザープロンプト
    if yui_reference is not None:
        user_prompt = f"""<コンテキスト / Context>
{yui_reference}

{instruction}

{problem_content}"""
    else:
        # コンテキストなしの場合
        user_prompt = f"""{instruction}

{problem_content}"""

    return system_prompt, user_prompt


def create_prompt_from_template(problem_file_path, template_file, context_file=None):
    """
    テンプレートファイルからプロンプトを作成

    Args:
        problem_file_path: 問題文ファイルのパス
        template_file: テンプレートファイルのパス（doc/prompt/*.md または NLP2026/docs/PC_*.md）
        context_file: 使用されません（後方互換性のため残されています）

    Returns:
        (system_prompt, user_prompt): システムプロンプトとユーザープロンプト
    """
    # テンプレートを読み込む
    template_path = Path(template_file)
    if not template_path.is_absolute():
        # 相対パスの場合、プロジェクトルートからの相対パスとして解決
        script_dir = Path(__file__).parent
        template_path = script_dir.parent.parent / template_file

    # 問題文ファイルを読み込む
    with open(problem_file_path, 'r', encoding='utf-8') as f:
        problem_content = f.read()

    template_name = template_path.name

    # P_で始まるファイルの場合、PC_.mdを使わず直接テンプレートとして使用
    if template_name.startswith('P_') and not template_name.startswith('PC_'):
        with open(template_path, 'r', encoding='utf-8') as f:
            template = f.read()
        # {PROBLEM}のみ置換（{CONTEXT}は使わない）
        user_prompt = template.replace('{PROBLEM}', problem_content)

    # PC_.md自体の場合、直接テンプレートとして使用（{CONTEXT}は空に）
    elif template_name == 'PC_.md':
        with open(template_path, 'r', encoding='utf-8') as f:
            template = f.read()
        user_prompt = template.replace('{CONTEXT}', '')
        user_prompt = user_prompt.replace('{PROBLEM}', problem_content)

    else:
        # それ以外のファイル（PC_*.mdや任意のファイル）はPC_.mdをベーステンプレートとして使用
        # まず同じディレクトリのPC_.mdを探し、なければdocs/template/PC_.mdを使う
        base_template_path = template_path.parent / 'PC_.md'
        if not base_template_path.exists():
            # プロジェクトルートからの固定パス
            script_dir = Path(__file__).parent
            base_template_path = script_dir.parent.parent / 'docs' / 'template' / 'PC_.md'

        with open(base_template_path, 'r', encoding='utf-8') as f:
            base_template = f.read()

        # 指定されたファイルをコンテキストとして読み込む
        with open(template_path, 'r', encoding='utf-8') as f:
            context_content = f.read()

        # ベーステンプレートの{CONTEXT}と{PROBLEM}を置換
        user_prompt = base_template.replace('{CONTEXT}', context_content)
        user_prompt = user_prompt.replace('{PROBLEM}', problem_content)

    # テンプレート使用時はシステムプロンプトなし（テンプレートに全て含まれる）
    system_prompt = ""

    return system_prompt, user_prompt


def call_openai_api(system_prompt, user_prompt, api_key, model_name='gpt-4', temperature=0.0, k=1):
    """OpenAI APIを呼び出してコードを生成"""
    try:
        import openai
    except ImportError:
        print("Error: openai パッケージがインストールされていません")
        print("pip install openai を実行してください")
        sys.exit(1)

    client = openai.OpenAI(api_key=api_key)

    try:
        # GPT-5以降は max_completion_tokens を使い、temperature=1固定
        # GPT-4以前は max_tokens と任意の temperature を使う
        if 'gpt-5' in model_name.lower() or 'o1' in model_name.lower() or 'o3' in model_name.lower():
            # 新しいモデル用パラメータ（temperature=1固定）
            response = client.chat.completions.create(
                model=model_name,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                n=k,
                max_completion_tokens=1000
            )
        else:
            # 従来のモデル用パラメータ
            response = client.chat.completions.create(
                model=model_name,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=temperature,
                n=k,
                max_tokens=2048
            )

        generated_codes = []
        for choice in response.choices:
            code = choice.message.content
            generated_codes.append(code)

        return generated_codes
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return [None] * k


def call_anthropic_api(system_prompt, user_prompt, api_key, model_name='claude-3-5-sonnet-20241022', temperature=0.0, k=1):
    """Anthropic APIを呼び出してコードを生成"""
    try:
        import anthropic
    except ImportError:
        print("Error: anthropic パッケージがインストールされていません")
        print("pip install anthropic を実行してください")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)
    generated_codes = []

    for i in range(k):
        try:
            response = client.messages.create(
                model=model_name,
                max_tokens=2048,
                temperature=temperature,
                system=system_prompt,
                messages=[
                    {"role": "user", "content": user_prompt}
                ]
            )
            code = response.content[0].text
            generated_codes.append(code)
        except Exception as e:
            print(f"Error calling Anthropic API (sample {i+1}/{k}): {e}")
            generated_codes.append(None)

    return generated_codes


def call_ollama_api(system_prompt, user_prompt, model_name='codellama', temperature=0.0, k=1):
    """Ollama APIを呼び出してコードを生成"""
    try:
        import requests
    except ImportError:
        print("Error: requests パッケージがインストールされていません")
        print("pip install requests を実行してください")
        sys.exit(1)

    full_prompt = f"{system_prompt}\n\n{user_prompt}"
    generated_codes = []

    for i in range(k):
        try:
            response = requests.post('http://localhost:11434/api/generate',
                json={
                    'model': model_name,
                    'prompt': full_prompt,
                    'stream': False,
                    'options': {
                        'temperature': temperature,
                        'num_predict': 1000
                    }
                }
            )
            code = response.json()['response']
            generated_codes.append(code)
        except Exception as e:
            print(f"Error calling Ollama API (sample {i+1}/{k}): {e}")
            generated_codes.append(None)

    return generated_codes


def call_huggingface_api(system_prompt, user_prompt, model_name, hf_token=None, temperature=0.0, k=1, device='auto'):
    """HuggingFace モデルを使ってコードを生成"""
    try:
        from transformers import AutoTokenizer, AutoModelForCausalLM
        import torch
    except ImportError:
        print("Error: transformers または torch パッケージがインストールされていません")
        print("pip install transformers torch を実行してください")
        sys.exit(1)

    print(f"Loading model: {model_name}...")

    try:
        # トークナイザーとモデルを読み込む
        tokenizer = AutoTokenizer.from_pretrained(
            model_name,
            token=hf_token,
            trust_remote_code=True
        )

        # デバイスの自動選択
        if device == 'auto':
            device = 'cuda' if torch.cuda.is_available() else 'cpu'

        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            token=hf_token,
            trust_remote_code=True,
            torch_dtype=torch.float16 if device == 'cuda' else torch.float32,
            device_map=device if device == 'cuda' else None
        )

        if device == 'cpu':
            model = model.to(device)

        print(f"Model loaded on {device}")

    except Exception as e:
        print(f"Error loading HuggingFace model: {e}")
        return [None] * k

    # プロンプトを結合
    full_prompt = f"{system_prompt}\n\n{user_prompt}"

    generated_codes = []

    for i in range(k):
        try:
            # トークン化
            inputs = tokenizer(full_prompt, return_tensors="pt").to(device)

            # 生成
            with torch.no_grad():
                outputs = model.generate(
                    **inputs,
                    max_new_tokens=1000,
                    temperature=temperature,
                    do_sample=True,
                    pad_token_id=tokenizer.eos_token_id
                )

            # デコード
            generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

            # プロンプト部分を除去
            if full_prompt in generated_text:
                code = generated_text[len(full_prompt):].strip()
            else:
                code = generated_text.strip()

            generated_codes.append(code)

        except Exception as e:
            print(f"Error generating with HuggingFace model (sample {i+1}/{k}): {e}")
            generated_codes.append(None)

    return generated_codes


# MLXモデルのグローバルキャッシュ（毎回ロードを避けるため）
_mlx_model_cache = {}


def call_mlx_api(system_prompt, user_prompt, model_name, hf_token=None, temperature=0.0, k=1):
    """MLX（Apple Silicon）モデルを使ってコードを生成

    Args:
        system_prompt: システムプロンプト
        user_prompt: ユーザープロンプト
        model_name: HuggingFaceのモデル名（例: mlx-community/Qwen2.5-Coder-7B-Instruct-4bit）
        hf_token: HuggingFaceトークン（プライベートモデル用）
        temperature: 生成時の温度パラメータ
        k: 生成するサンプル数

    Returns:
        list: 生成されたコードのリスト
    """
    try:
        from mlx_lm import load, generate
    except ImportError:
        print("Error: mlx-lm パッケージがインストールされていません")
        print("pip install mlx mlx-lm を実行してください")
        sys.exit(1)

    global _mlx_model_cache

    # モデルをキャッシュから取得、またはロード
    if model_name not in _mlx_model_cache:
        print(f"Loading MLX model: {model_name}...")
        try:
            model, tokenizer = load(model_name, tokenizer_config={"trust_remote_code": True})
            _mlx_model_cache[model_name] = (model, tokenizer)
            print(f"Model loaded successfully on Apple Silicon (MLX)")
        except Exception as e:
            print(f"Error loading MLX model: {e}")
            return [None] * k
    else:
        model, tokenizer = _mlx_model_cache[model_name]

    generated_codes = []

    for i in range(k):
        try:
            # チャット形式のプロンプトを構築
            if hasattr(tokenizer, 'apply_chat_template'):
                messages = []
                if system_prompt:
                    messages.append({"role": "system", "content": system_prompt})
                messages.append({"role": "user", "content": user_prompt})

                prompt = tokenizer.apply_chat_template(
                    messages,
                    tokenize=False,
                    add_generation_prompt=True
                )
            else:
                # チャットテンプレートがない場合はシンプルに結合
                prompt = f"{system_prompt}\n\n{user_prompt}" if system_prompt else user_prompt

            # 生成
            response = generate(
                model,
                tokenizer,
                prompt=prompt,
                max_tokens=2048,
                verbose=False
            )

            generated_codes.append(response)

        except Exception as e:
            print(f"Error generating with MLX model (sample {i+1}/{k}): {e}")
            generated_codes.append(None)

    return generated_codes


def extract_and_complete_code(generated_text, problem_file_path):
    """
    生成されたコード（関数本体）と問題文を結合して完全なコードを作成

    Args:
        generated_text: モデルが生成したコード
        problem_file_path: 問題文ファイル(.txt)または参照実装(.yui)のパス

    Returns:
        str: 完全なYuiコード
    """
    if generated_text is None:
        return None

    # 問題ファイルを読み込む
    with open(problem_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # .yuiファイルの場合は参照実装なので、base_codeは使わない
    is_yui_file = str(problem_file_path).endswith('.yui')

    # ```yui 以降の部分を抽出（.txtファイルの場合）
    if not is_yui_file and '```yui' in content:
        code_start = content.find('```yui') + len('```yui\n')
        base_code = content[code_start:]
    else:
        base_code = ""  # .yuiファイルの場合は生成コードをそのまま使う

    # 生成されたテキストからコードのみを抽出
    clean_generated = generated_text.strip()

    # マークダウンコードブロック全体を抽出（```yui ... ```）
    code_blocks = []
    in_code_block = False
    current_block = []

    for line in clean_generated.split('\n'):
        if line.strip().startswith('```yui') or line.strip() == '```':
            if in_code_block:
                # ブロック終了
                code_blocks.append('\n'.join(current_block))
                current_block = []
                in_code_block = False
            else:
                # ブロック開始
                in_code_block = True
        elif in_code_block:
            current_block.append(line)

    # コードブロックが見つかった場合
    if code_blocks:
        clean_generated = '\n'.join(code_blocks).strip()
    else:
        # コードブロックがない場合、「標準ライブラリを使う」から始まる行を見つける
        lines = clean_generated.split('\n')
        start_idx = -1
        end_idx = len(lines)

        for i, line in enumerate(lines):
            if '標準ライブラリを使う' in line or '= 入力' in line:
                if start_idx == -1:
                    start_idx = i
            # 説明文の開始を検出（「この実装では」「テストケースを実行すると」など）
            elif start_idx != -1 and (
                line.strip().startswith('この') or
                line.strip().startswith('テスト') or
                line.strip().startswith('1.') or
                line.strip().startswith('2.') or
                (line.strip() and not line.strip().startswith('#') and '=' not in line and 'を' not in line and 'ならば' not in line and 'くり返す' not in line and 'が答え' not in line and '}' not in line and '{' not in line)
            ):
                end_idx = i
                break

        if start_idx != -1:
            clean_generated = '\n'.join(lines[start_idx:end_idx]).strip()

    # 末尾のテストケース例（>>> で始まる行）を除去
    lines = clean_generated.split('\n')
    code_lines = []
    for line in lines:
        if line.strip().startswith('>>>'):
            break
        code_lines.append(line)
    clean_generated = '\n'.join(code_lines).strip()

    # モデルが完全なコードを返したかチェック
    # "標準ライブラリを使う" や関数名が含まれていれば完全なコード
    if '標準ライブラリを使う' in clean_generated or 'import' in clean_generated:
        # 完全なコードが返された場合はそのまま使用
        return clean_generated

    # base_codeがない場合（.yuiファイルの場合）は生成コードをそのまま返す
    if not base_code:
        return clean_generated

    # 関数本体のみが返された場合は問題ファイルと結合
    full_code = base_code + '\n' + clean_generated

    return full_code


def test_generated_code(generated_code, doctest_path, timeout=10):
    """
    生成されたコードにテストケースを追加して実行

    Returns:
        (success, stdout, stderr, execution_time)
    """
    if generated_code is None:
        return False, '', 'Code generation failed', 0.0

    start_time = time.time()

    try:
        # doctestを読み込む
        with open(doctest_path, 'r', encoding='utf-8') as f:
            tests = f.read()

        # コードとテストを結合
        full_code = generated_code + '\n\n' + tests

        # 一時ファイルに保存して実行
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yui', delete=False, encoding='utf-8') as f:
            f.write(full_code)
            temp_file = f.name

        try:
            # yuichanで実行
            project_root = Path(__file__).parent.parent.parent
            result = subprocess.run(
                ['python3', '-m', 'yuichan.main', temp_file],
                capture_output=True,
                text=True,
                timeout=timeout,
                cwd=str(project_root)
            )
            success = result.returncode == 0
            execution_time = time.time() - start_time
            return success, result.stdout, result.stderr, execution_time
        finally:
            Path(temp_file).unlink()

    except subprocess.TimeoutExpired:
        execution_time = time.time() - start_time
        return False, '', f'Timeout ({timeout}s)', execution_time
    except Exception as e:
        execution_time = time.time() - start_time
        return False, '', str(e), execution_time


def extract_problem_id(file_path):
    """ファイル名から問題IDを抽出"""
    return file_path.stem.split('_')[0]


def find_problem_files(humaneval_dir, lang='en'):
    """問題ファイルを検索

    まず *_{lang}.txt 形式を探し、見つからなければ *.yui ファイル（doctest除く）を使用
    """
    # 従来の問題文ファイル形式を検索
    pattern = f'*_{lang}.txt'
    files = list(humaneval_dir.glob(pattern))

    if files:
        return sorted(files, key=lambda p: int(extract_problem_id(p)))

    # 問題文ファイルがない場合、.yuiファイル（参照実装）を使用
    yui_files = [f for f in humaneval_dir.glob('*.yui') if not f.name.endswith('_doctest.yui')]
    return sorted(yui_files, key=lambda p: int(extract_problem_id(p)))


def get_doctest_file(humaneval_dir, problem_id):
    """問題IDからdoctestファイルを取得"""
    files = list(humaneval_dir.glob(f'{problem_id}_*_doctest.yui'))
    return files[0] if files else None


def calculate_pass_at_k(results_by_problem, k):
    """pass@kを計算"""
    total_problems = len(results_by_problem)
    if total_problems == 0:
        return 0.0

    passed_problems = 0
    for problem_id, results in results_by_problem.items():
        if any(results):
            passed_problems += 1

    return (passed_problems / total_problems) * 100


def wilson_confidence_interval(passed, total, confidence=0.95):
    """
    Wilson Score信頼区間を計算

    Args:
        passed: 成功数
        total: 総数
        confidence: 信頼水準（デフォルト: 0.95 = 95%）

    Returns:
        (lower, upper): 信頼区間の下限と上限（0-1の範囲）
    """
    from math import sqrt

    if total == 0:
        return 0.0, 0.0

    # 信頼水準に対応するz値（95% → 1.96, 99% → 2.576）
    z = 1.96 if confidence == 0.95 else 2.576

    p = passed / total
    n = total

    denominator = 1 + z**2 / n
    center = (p + z**2 / (2 * n)) / denominator
    margin = z * sqrt((p * (1 - p) + z**2 / (4 * n)) / n) / denominator

    lower = max(0.0, center - margin)
    upper = min(1.0, center + margin)

    return lower, upper


def detect_model_provider(model_name):
    """
    モデル名から自動的にプロバイダーを判別

    Args:
        model_name: モデル名（例: gpt-4, claude-3-5-sonnet, meta-llama/Llama-2, mlx-community/Qwen2.5-Coder）

    Returns:
        str: プロバイダー名 ('openai', 'anthropic', 'mlx', 'huggingface', 'ollama')
    """
    if not model_name:
        return None

    model_lower = model_name.lower()

    # GPTで始まる、またはo1/o3を含む → OpenAI
    if model_lower.startswith('gpt') or model_lower.startswith('o1') or model_lower.startswith('o3'):
        return 'openai'

    # claudeで始まる → Anthropic
    if model_lower.startswith('claude'):
        return 'anthropic'

    # mlx-community/ で始まる → MLX（Apple Silicon）
    if model_lower.startswith('mlx-community/') or model_lower.startswith('mlx/'):
        return 'mlx'

    # スラッシュを含む → HuggingFace（例: meta-llama/Llama-2）
    if '/' in model_name:
        return 'huggingface'

    # それ以外 → Ollama（codellama, qwen など）
    return 'ollama'


def main():
    parser = argparse.ArgumentParser(description='HumanEval評価スクリプト')
    parser.add_argument('--model', default=None, choices=['openai', 'anthropic', 'ollama', 'huggingface', 'mlx'],
                        help='使用するモデルプロバイダー（省略時は--model-nameから自動判別）')
    parser.add_argument('--model-name', default=None,
                        help='モデル名（例: gpt-5-mini-2025-08-07, claude-3-5-sonnet, meta-llama/Llama-2-7b）')
    parser.add_argument('--api-key', default=None,
                        help='APIキー')
    parser.add_argument('--hf-token', default=None,
                        help='HuggingFace token（プライベートモデル用）')
    parser.add_argument('--device', default='auto', choices=['auto', 'cuda', 'cpu'],
                        help='HuggingFaceモデルの実行デバイス')
    parser.add_argument('--k', type=int, default=1,
                        help='pass@k のk値')
    parser.add_argument('--temperature', type=float, default=0.2,
                        help='生成時のtemperature（0.0〜2.0、デフォルト: 0.2）。GPT-5系では無視されます。')
    parser.add_argument('--lang', choices=['en', 'ja'], default='ja',
                        help='問題文の言語')
    parser.add_argument('--template', default='docs/template/PC_.md',
                        help='プロンプトテンプレートファイルのパス（デフォルト: docs/template/PC_.md）。PC_*.mdはコンテキスト付き、P_*.mdはコンテキストなし。')
    parser.add_argument('--context-file', default='docs/API_en.md',
                        help='コンテキストファイルのパス（--templateが指定されていない場合のみ使用）')
    parser.add_argument('--no-context', action='store_true',
                        help='コンテキストなしで評価（--templateが指定されていない場合のみ有効）')
    parser.add_argument('--problems', nargs='*', default=None,
                        help='評価する問題ID')
    parser.add_argument('--timeout', type=int, default=10,
                        help='各テストのタイムアウト秒数')
    parser.add_argument('--output-dir', default='./results',
                        help='結果の出力ディレクトリ')
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='詳細な出力を表示')
    parser.add_argument('--show-prompt', action='store_true',
                        help='最初の1問のプロンプトを表示して終了（デバッグ用）')

    args = parser.parse_args()

    # --model が指定されていない場合、--model-name から自動判別
    # ただし --show-prompt の場合はモデル指定不要
    if not args.model and not args.show_prompt:
        if args.model_name:
            args.model = detect_model_provider(args.model_name)
            print(f"自動判別: {args.model_name} → {args.model}")
        else:
            print("Error: --model または --model-name のいずれかを指定してください")
            print("\n例:")
            print("  python evaluate.py --model-name gpt-5-mini-2025-08-07")
            print("  python evaluate.py --model-name claude-3-5-sonnet-20241022")
            print("  python evaluate.py --model-name meta-llama/Llama-2-7b")
            print("  python evaluate.py --model ollama --model-name codellama")
            return 1

    # --template が指定された場合、または --no-context が指定された場合、context_file を None に
    if args.template:
        context_file = None
    elif args.no_context:
        context_file = None
    else:
        context_file = args.context_file

    # --show-prompt: プロンプトを表示して終了（APIキー不要）
    if args.show_prompt:
        humaneval_dir = Path(__file__).parent.parent
        all_problem_files = find_problem_files(humaneval_dir, args.lang)
        if not all_problem_files:
            print("Error: 問題ファイルが見つかりません")
            return 1

        problem_file = all_problem_files[0]
        problem_name = problem_file.stem.replace(f'_{args.lang}', '')

        print(f"=== プロンプトプレビュー ===")
        print(f"問題: {problem_name}")
        print(f"テンプレート: {args.template}")
        print()

        if args.template:
            system_prompt, user_prompt = create_prompt_from_template(problem_file, args.template, context_file)
        else:
            system_prompt, user_prompt = create_prompt(problem_file, context_file)

        print("--- System Prompt ---")
        print(system_prompt if system_prompt else "(なし)")
        print()
        print("--- User Prompt ---")
        print(user_prompt)
        print()
        print(f"--- プロンプト長: {len(user_prompt)} 文字 ---")
        return 0

    # API keyの取得
    if args.model == 'openai':
        api_key = args.api_key or os.getenv('OPENAI_API_KEY')
        model_name = args.model_name or 'gpt-4'
        if not api_key:
            print("Error: OpenAI API keyが設定されていません")
            print("--api-key で指定するか、OPENAI_API_KEY 環境変数を設定してください")
            return 1
    elif args.model == 'anthropic':
        api_key = args.api_key or os.getenv('ANTHROPIC_API_KEY')
        model_name = args.model_name or 'claude-3-5-sonnet-20241022'
        if not api_key:
            print("Error: Anthropic API keyが設定されていません")
            print("--api-key で指定するか、ANTHROPIC_API_KEY 環境変数を設定してください")
            return 1
    elif args.model == 'huggingface':
        api_key = None
        hf_token = args.hf_token or os.getenv('HF_TOKEN')
        model_name = args.model_name
        if not model_name:
            print("Error: HuggingFaceモデル名が指定されていません")
            print("--model-name でモデル名を指定してください（例: meta-llama/Llama-2-7b-chat-hf）")
            return 1
    elif args.model == 'mlx':
        api_key = None
        hf_token = args.hf_token or os.getenv('HF_TOKEN')
        model_name = args.model_name
        if not model_name:
            print("Error: MLXモデル名が指定されていません")
            print("--model-name でモデル名を指定してください（例: mlx-community/Qwen2.5-Coder-7B-Instruct-4bit）")
            return 1
    else:  # ollama
        api_key = None
        model_name = args.model_name or 'codellama'

    # ディレクトリ設定
    humaneval_dir = Path(__file__).parent.parent

    # 日本時刻を取得（JST = UTC+9）
    jst = timezone(timedelta(hours=9))
    now_jst = datetime.now(jst)
    timestamp = now_jst.strftime('%Y%m%d_%H%M%S')

    # モデル名からファイル名に使えない文字を削除
    safe_model_name = model_name.replace('/', '_').replace(':', '_')

    # MLXモデルの場合はプレフィックスを追加
    model_prefix = "MLX_" if args.model == 'mlx' else ""

    # テンプレート/コンテキスト情報をディレクトリ名に追加
    if args.template:
        # テンプレートが指定された場合（doc/prompt/*.md）
        template_name = Path(args.template).stem  # 例: "ONESHOT.md" → "ONESHOT"
        context_suffix = f"_{template_name}"
    elif args.no_context:
        context_suffix = "_no_context"
    else:
        # コンテキストファイル名から拡張子を除いた部分を取得
        context_name = Path(args.context_file).stem  # 例: "context.md" → "context"
        context_suffix = f"_with_{context_name}"

    # 出力ディレクトリ名: [MLX_]YYYYMMDD_HHMMSS_モデル名_コンテキスト/テンプレート
    output_dirname = f"{model_prefix}{timestamp}_{safe_model_name}{context_suffix}"
    output_dir = Path(args.output_dir) / output_dirname
    output_dir.mkdir(parents=True, exist_ok=True)
    generated_dir = output_dir / 'generated'
    generated_dir.mkdir(parents=True, exist_ok=True)

    # ログファイルを設定
    log_file = output_dir / 'log.txt'
    log_handle = open(log_file, 'w', encoding='utf-8')

    def log(message):
        """標準出力とログファイルの両方に出力"""
        print(message)
        log_handle.write(message + '\n')
        log_handle.flush()

    # 問題ファイルを検索
    all_problem_files = find_problem_files(humaneval_dir, args.lang)

    if not all_problem_files:
        print(f"Error: 問題ファイルが見つかりません")
        return 1

    # 特定の問題のみ評価
    if args.problems:
        problem_ids = set(args.problems)
        problem_files = [
            f for f in all_problem_files
            if extract_problem_id(f) in problem_ids
        ]
    else:
        problem_files = all_problem_files

    if not problem_files:
        print(f"Error: 指定された問題が見つかりませんでした")
        return 1

    # 評価開始
    print(f"=== HumanEval評価 (pass@{args.k}) ===")
    print(f"Model: {model_name}")
    print(f"Language: {args.lang}")
    if args.template:
        print(f"Prompt Template: {args.template}")
    else:
        print(f"Context: {context_file if context_file else 'なし'}")
    print(f"Total problems: {len(problem_files)}")
    print()

    results_by_problem = {}
    all_results = []

    for i, problem_file in enumerate(problem_files, 1):
        problem_start_time = time.time()
        problem_id = extract_problem_id(problem_file)
        problem_name = problem_file.stem.replace(f'_{args.lang}', '')

        print(f"[{i}/{len(problem_files)}] {problem_name}")

        # プロンプトを作成（テンプレート使用 or 従来方式）
        if args.template:
            system_prompt, user_prompt = create_prompt_from_template(problem_file, args.template, context_file)
        else:
            system_prompt, user_prompt = create_prompt(problem_file, context_file)

        # doctestファイルを取得
        doctest_file = get_doctest_file(humaneval_dir, problem_id)
        if not doctest_file:
            print(f"  Warning: doctestファイルが見つかりません")
            continue

        # k個のサンプルを生成
        if args.model == 'openai':
            generated_codes = call_openai_api(system_prompt, user_prompt, api_key, model_name, temperature=args.temperature, k=args.k)
        elif args.model == 'anthropic':
            generated_codes = call_anthropic_api(system_prompt, user_prompt, api_key, model_name, temperature=args.temperature, k=args.k)
        elif args.model == 'huggingface':
            generated_codes = call_huggingface_api(system_prompt, user_prompt, model_name, hf_token, temperature=args.temperature, k=args.k, device=args.device)
        elif args.model == 'mlx':
            generated_codes = call_mlx_api(system_prompt, user_prompt, model_name, hf_token, temperature=args.temperature, k=args.k)
        else:  # ollama
            generated_codes = call_ollama_api(system_prompt, user_prompt, model_name, temperature=args.temperature, k=args.k)

        # 参照実装（canonical_solution）を読み込む
        # problem_name には既に problem_id が含まれている（例: "0_has_close_elements"）
        canonical_solution_file = humaneval_dir / f"{problem_name}.yui"
        canonical_solution = ""
        if canonical_solution_file.exists():
            with open(canonical_solution_file, 'r', encoding='utf-8') as f:
                canonical_solution = f.read()

        samples_passed = 0

        for j, generated_code in enumerate(generated_codes):
            # コードを完成させる
            full_code = extract_and_complete_code(generated_code, problem_file)

            # 生成されたコードを保存
            if full_code:
                code_file = generated_dir / f"{problem_id}_{problem_name}_sample_{j}.yui"
                with open(code_file, 'w', encoding='utf-8') as f:
                    f.write(full_code)

            # 生成結果をログに出力
            log_handle.write(f"\n{'='*60}\n")
            log_handle.write(f"[{i}/{len(problem_files)}] {problem_name} - Sample {j+1}/{args.k}\n")
            log_handle.write(f"{'='*60}\n")
            log_handle.write(f"--- Generated Code ---\n")
            log_handle.write(f"{generated_code}\n")
            log_handle.write(f"--- Extracted Code ---\n")
            log_handle.write(f"{full_code}\n")
            log_handle.flush()

            # テスト実行
            success, stdout, stderr, exec_time = test_generated_code(full_code, doctest_file, args.timeout)

            if success:
                print(f"  Sample {j+1}/{args.k}... ✓ ({exec_time:.2f}s)")
                log_handle.write(f"--- Result: ✓ PASSED ({exec_time:.2f}s) ---\n")
                samples_passed += 1
            else:
                print(f"  Sample {j+1}/{args.k}... ✗ ({exec_time:.2f}s)")
                log_handle.write(f"--- Result: ✗ FAILED ({exec_time:.2f}s) ---\n")
                log_handle.write(f"Error: {stderr}\n")
                if args.verbose and stderr:
                    print(f"    Error: {stderr[:200]}")
            log_handle.flush()

            # フラットな結果を記録（各サンプルを1行として）
            all_results.append({
                'problem_id': problem_id,
                'problem_name': problem_name,
                'sample_id': j,
                'lang': args.lang,
                'model': model_name,
                'canonical_solution': canonical_solution,
                'input': system_prompt + '\n\n' + user_prompt,
                'output': generated_code,  # 生のAPI出力
                'extracted': full_code,     # 抽出・クリーンアップ後のコード
                'passed': success,
                'error': stderr if not success else None,
                'execution_time': exec_time
            })

            # 問題ごとの結果も記録（pass@k計算用）
            if problem_id not in results_by_problem:
                results_by_problem[problem_id] = []
            results_by_problem[problem_id].append(success)

        # 問題ごとの結果表示
        problem_passed = any(results_by_problem[problem_id])
        problem_elapsed_time = time.time() - problem_start_time

        if problem_passed:
            print(f"  Problem result: ✓ ({samples_passed}/{args.k} samples passed) [{problem_elapsed_time:.2f}s]")
        else:
            print(f"  Problem result: ✗ (0/{args.k} samples passed) [{problem_elapsed_time:.2f}s]")

        print()

    # pass@kを計算
    pass_rate = calculate_pass_at_k(results_by_problem, args.k)

    total = len(results_by_problem)
    passed = sum(1 for results in results_by_problem.values() if any(results))
    failed = total - passed

    # 95%信頼区間を計算（Wilson Score法）
    ci_lower, ci_upper = wilson_confidence_interval(passed, total, confidence=0.95)

    # サマリーを表示
    print("=" * 60)
    print("評価結果サマリー")
    print("=" * 60)
    print(f"Total:  {total} 問題")
    print(f"Passed: {passed} 問題")
    print(f"Failed: {failed} 問題")
    print(f"pass@{args.k}: {pass_rate:.2f}% ({passed}/{total})")
    print(f"95% CI: [{ci_lower*100:.2f}%, {ci_upper*100:.2f}%] (Wilson Score)")
    print(f"\n生成されたコード: {generated_dir}")

    # 結果をJSONLで保存（フラット構造）
    result_file = output_dir / 'result.jsonl'
    with open(result_file, 'w', encoding='utf-8') as f:
        for result in all_results:
            json.dump(result, f, ensure_ascii=False)
            f.write('\n')

    # 総合結果をsummary.jsonで保存
    summary_file = output_dir / 'summary.json'
    summary = {
        'model': model_name,
        'lang': args.lang,
        'template': args.template if args.template else None,
        'context': args.template if args.template else context_file,  # テンプレート優先、なければcontext_file
        'temperature': args.temperature,
        'k': args.k,
        'total_problems': total,
        'passed_problems': passed,
        'failed_problems': failed,
        'pass_at_k': round(pass_rate, 2),
        'confidence_interval_95': {
            'lower': round(ci_lower * 100, 2),
            'upper': round(ci_upper * 100, 2),
            'method': 'Wilson Score'
        },
        'timestamp': timestamp,
        'total_samples': len(all_results),
        'passed_samples': sum(1 for r in all_results if r['passed']),
    }
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    print(f"結果を保存しました: {result_file}")
    print(f"総合結果を保存しました: {summary_file}")
    print(f"ログを保存しました: {log_file}")
    print("=" * 60)

    # サマリーをログにも出力
    log_handle.write(f"\n{'='*60}\n")
    log_handle.write(f"評価結果サマリー\n")
    log_handle.write(f"{'='*60}\n")
    log_handle.write(f"Total:  {total} 問題\n")
    log_handle.write(f"Passed: {passed} 問題\n")
    log_handle.write(f"Failed: {failed} 問題\n")
    log_handle.write(f"pass@{args.k}: {pass_rate:.2f}% ({passed}/{total})\n")
    log_handle.write(f"95% CI: [{ci_lower*100:.2f}%, {ci_upper*100:.2f}%] (Wilson Score)\n")
    log_handle.close()

    # 失敗した問題の一覧
    if failed > 0 and not args.verbose:
        print("\n失敗した問題:")
        failed_problems = set()
        for problem_id, results in results_by_problem.items():
            if not any(results):
                # 問題名を取得（all_resultsから）
                problem_name = next((r['problem_name'] for r in all_results if r['problem_id'] == problem_id), problem_id)
                failed_problems.add(problem_name)

        for problem_name in sorted(failed_problems):
            print(f"  - {problem_name}")
        print("\n詳細を見るには --verbose オプションを使用してください")

    return 0


if __name__ == '__main__':
    sys.exit(main())
