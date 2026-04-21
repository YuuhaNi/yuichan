#!/usr/bin/env python3
"""
JHumanEval 評価スクリプト

Usage:
    # HuggingFace からデータセットを取得して評価
    python evaluate_jhumaneval.py --model-name gpt-4o --k 1

    # ローカルファイルを使用
    python evaluate_jhumaneval.py --model-name claude-3-5-sonnet-20241022 --dataset ./jhuman-eval.jsonl.gz

    # Ollama ローカルモデルを使用
    python evaluate_jhumaneval.py --model-name codellama --k 3
"""

import json
import argparse
import sys
import os
import gzip
import tempfile
import subprocess
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime, timezone, timedelta

# .envファイルを読み込む
try:
    from dotenv import load_dotenv
    env_path = Path(__file__).resolve().parent / '.env'
    print(f"DEBUG: env_path = {env_path}, exists = {env_path.exists()}")
    if env_path.exists():
        result = load_dotenv(dotenv_path=env_path)
        print(f"DEBUG: load_dotenv result = {result}")
        print(f"DEBUG: OPENAI_API_KEY set = {os.getenv('OPENAI_API_KEY') is not None}")
except ImportError:
    print("DEBUG: dotenv not installed")


def load_jhumaneval_dataset(dataset_path: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    JHumanEval データセットを読み込む

    Args:
        dataset_path: ローカルファイルパス（None の場合は HuggingFace から取得）

    Returns:
        データセットのリスト
    """
    if dataset_path:
        # ローカルファイルから読み込み
        path = Path(dataset_path)
        if path.suffix == '.gz':
            with gzip.open(path, 'rt', encoding='utf-8') as f:
                return [json.loads(line) for line in f]
        else:
            with open(path, 'r', encoding='utf-8') as f:
                return [json.loads(line) for line in f]
    else:
        # HuggingFace から取得
        try:
            from datasets import load_dataset
            ds = load_dataset('kogi-jwu/jhumaneval', split='test')
            return [dict(item) for item in ds]
        except ImportError:
            print("Error: datasets パッケージがインストールされていません")
            print("pip install datasets を実行してください")
            sys.exit(1)
        except Exception as e:
            print(f"Error loading dataset from HuggingFace: {e}")
            sys.exit(1)


def detect_model_provider(model_name: str) -> str:
    """モデル名からプロバイダーを自動判別"""
    if not model_name:
        return None

    model_lower = model_name.lower()

    if model_lower.startswith('gpt') or model_lower.startswith('o1') or model_lower.startswith('o3') or model_lower.startswith('o4'):
        return 'openai'
    if model_lower.startswith('claude'):
        return 'anthropic'
    if model_lower.startswith('mlx-community/') or model_lower.startswith('mlx/'):
        return 'mlx'
    if '/' in model_name:
        return 'huggingface'
    return 'ollama'


def call_openai_api(prompt: str, api_key: str, model_name: str, temperature: float = 0.2, k: int = 1) -> List[str]:
    """OpenAI API を呼び出してコードを生成"""
    try:
        import openai
    except ImportError:
        print("Error: openai パッケージがインストールされていません")
        sys.exit(1)

    client = openai.OpenAI(api_key=api_key)

    try:
        # GPT-5/o1/o3/o4 系は max_completion_tokens を使用
        if any(x in model_name.lower() for x in ['gpt-5', 'o1', 'o3', 'o4']):
            # o1/o3/o4 は temperature 指定不可
            if any(x in model_name.lower() for x in ['o1', 'o3', 'o4']):
                response = client.chat.completions.create(
                    model=model_name,
                    messages=[{"role": "user", "content": prompt}],
                    n=k,
                    max_completion_tokens=2000
                )
            else:
                response = client.chat.completions.create(
                    model=model_name,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=temperature,
                    n=k,
                    max_completion_tokens=2000
                )
        else:
            response = client.chat.completions.create(
                model=model_name,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                n=k,
                max_tokens=2000
            )
        return [choice.message.content for choice in response.choices]
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return [None] * k


def call_anthropic_api(prompt: str, api_key: str, model_name: str, temperature: float = 0.2, k: int = 1) -> List[str]:
    """Anthropic API を呼び出してコードを生成"""
    try:
        import anthropic
    except ImportError:
        print("Error: anthropic パッケージがインストールされていません")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)
    generated = []

    for _ in range(k):
        try:
            response = client.messages.create(
                model=model_name,
                max_tokens=2000,
                temperature=temperature,
                messages=[{"role": "user", "content": prompt}]
            )
            generated.append(response.content[0].text)
        except Exception as e:
            print(f"Error calling Anthropic API: {e}")
            generated.append(None)

    return generated


def call_ollama_api(prompt: str, model_name: str, temperature: float = 0.2, k: int = 1) -> List[str]:
    """Ollama API を呼び出してコードを生成"""
    try:
        import requests
    except ImportError:
        print("Error: requests パッケージがインストールされていません")
        sys.exit(1)

    generated = []
    for _ in range(k):
        try:
            response = requests.post(
                'http://localhost:11434/api/generate',
                json={
                    'model': model_name,
                    'prompt': prompt,
                    'stream': False,
                    'options': {'temperature': temperature, 'num_predict': 2000}
                }
            )
            generated.append(response.json()['response'])
        except Exception as e:
            print(f"Error calling Ollama API: {e}")
            generated.append(None)

    return generated


def call_huggingface_api(prompt: str, model_name: str, hf_token: Optional[str] = None,
                         temperature: float = 0.2, k: int = 1, device: str = 'auto') -> List[str]:
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
        tokenizer = AutoTokenizer.from_pretrained(
            model_name, token=hf_token, trust_remote_code=True
        )

        if device == 'auto':
            device = 'cuda' if torch.cuda.is_available() else 'cpu'

        model = AutoModelForCausalLM.from_pretrained(
            model_name, token=hf_token, trust_remote_code=True,
            torch_dtype=torch.float16 if device == 'cuda' else torch.float32,
            device_map=device if device == 'cuda' else None
        )

        if device == 'cpu':
            model = model.to(device)

        print(f"Model loaded on {device}")
    except Exception as e:
        print(f"Error loading HuggingFace model: {e}")
        return [None] * k

    generated = []
    for i in range(k):
        try:
            inputs = tokenizer(prompt, return_tensors="pt").to(device)
            with torch.no_grad():
                outputs = model.generate(
                    **inputs, max_new_tokens=2000, temperature=temperature,
                    do_sample=True, pad_token_id=tokenizer.eos_token_id
                )
            generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
            if prompt in generated_text:
                code = generated_text[len(prompt):].strip()
            else:
                code = generated_text.strip()
            generated.append(code)
        except Exception as e:
            print(f"Error generating with HuggingFace model (sample {i+1}/{k}): {e}")
            generated.append(None)

    return generated


# MLX モデルキャッシュ
_mlx_model_cache = {}

def call_mlx_api(prompt: str, model_name: str, hf_token: Optional[str] = None,  # noqa: ARG001
                 temperature: float = 0.2, k: int = 1) -> List[str]:  # noqa: ARG001
    """MLX (Apple Silicon) モデルを使用"""
    try:
        from mlx_lm import load, generate
    except ImportError:
        print("Error: mlx-lm パッケージがインストールされていません")
        sys.exit(1)

    global _mlx_model_cache

    if model_name not in _mlx_model_cache:
        print(f"Loading MLX model: {model_name}...")
        model, tokenizer = load(model_name, tokenizer_config={"trust_remote_code": True})
        _mlx_model_cache[model_name] = (model, tokenizer)

    model, tokenizer = _mlx_model_cache[model_name]
    generated = []

    for _ in range(k):
        try:
            if hasattr(tokenizer, 'apply_chat_template'):
                formatted_prompt = tokenizer.apply_chat_template(
                    [{"role": "user", "content": prompt}],
                    tokenize=False,
                    add_generation_prompt=True
                )
            else:
                formatted_prompt = prompt

            response = generate(model, tokenizer, prompt=formatted_prompt, max_tokens=2000, verbose=False)
            generated.append(response)
        except Exception as e:
            print(f"Error generating with MLX: {e}")
            generated.append(None)

    return generated


def extract_python_code(generated_text: str) -> str:
    """生成されたテキストから Python コードを抽出"""
    if not generated_text:
        return ""

    text = generated_text.strip()

    # ```python ... ``` ブロックを抽出
    if '```python' in text:
        start = text.find('```python') + len('```python')
        end = text.find('```', start)
        if end != -1:
            return text[start:end].strip()

    # ``` ... ``` ブロックを抽出
    if '```' in text:
        start = text.find('```') + 3
        # 言語指定があれば改行まで読み飛ばす
        if text[start:start+10].strip() and '\n' in text[start:start+20]:
            start = text.find('\n', start) + 1
        end = text.find('```', start)
        if end != -1:
            return text[start:end].strip()

    # コードブロックがない場合、def/class から始まる部分を探す
    lines = text.split('\n')
    code_lines = []
    in_code = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith('def ') or stripped.startswith('class ') or stripped.startswith('import ') or stripped.startswith('from '):
            in_code = True
        if in_code:
            # 説明文と思われる行で終了
            if stripped and not stripped.startswith('#') and not any(c in stripped for c in '(){}[].:=+-*/<>'):
                if len(stripped) > 50 and ' ' in stripped:
                    break
            code_lines.append(line)

    if code_lines:
        return '\n'.join(code_lines).strip()

    return text


def run_python_test(code: str, test: str, entry_point: str, timeout: int = 10) -> Tuple[bool, str]:
    """
    生成されたコードをテストで検証

    Args:
        code: 生成された Python コード（prompt + completion）
        test: テストコード
        entry_point: テストのエントリーポイント関数名
        timeout: タイムアウト秒数

    Returns:
        (success, error_message)
    """
    # テストコードを組み立て
    full_code = f"{code}\n\n{test}\n\ncheck({entry_point})"

    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as f:
        f.write(full_code)
        temp_file = f.name

    try:
        result = subprocess.run(
            [sys.executable, temp_file],
            capture_output=True,
            text=True,
            timeout=timeout
        )
        if result.returncode == 0:
            return True, ""
        else:
            return False, result.stderr or result.stdout
    except subprocess.TimeoutExpired:
        return False, f"Timeout ({timeout}s)"
    except Exception as e:
        return False, str(e)
    finally:
        Path(temp_file).unlink(missing_ok=True)


def wilson_confidence_interval(passed: int, total: int, confidence: float = 0.95) -> Tuple[float, float]:
    """Wilson Score 信頼区間を計算"""
    from math import sqrt

    if total == 0:
        return 0.0, 0.0

    z = 1.96 if confidence == 0.95 else 2.576
    p = passed / total
    n = total

    denominator = 1 + z**2 / n
    center = (p + z**2 / (2 * n)) / denominator
    margin = z * sqrt((p * (1 - p) + z**2 / (4 * n)) / n) / denominator

    return max(0.0, center - margin), min(1.0, center + margin)


def create_prompt(item: Dict[str, Any], lang: str = 'ja', prompt_style: str = 'completion') -> str:
    """
    問題からプロンプトを作成

    Args:
        item: JHumanEval のデータ項目
        lang: 言語 ('ja' or 'en')
        prompt_style: プロンプトスタイル ('completion' or 'instruction')

    Returns:
        プロンプト文字列
    """
    prompt = item['prompt'] if lang == 'ja' else item.get('prompt_en', item['prompt'])

    if prompt_style == 'completion':
        # コード補完形式（そのまま続きを生成）
        return prompt
    else:
        # 指示形式
        instruction = "以下の関数を完成させてください。" if lang == 'ja' else "Complete the following function."
        return f"{instruction}\n\n```python\n{prompt}\n```\n\n関数の実装のみを出力してください。" if lang == 'ja' else f"{instruction}\n\n```python\n{prompt}\n```\n\nOutput only the function implementation."


def main():
    parser = argparse.ArgumentParser(description='JHumanEval 評価スクリプト')
    parser.add_argument('--model', default=None, choices=['openai', 'anthropic', 'ollama', 'huggingface', 'mlx'],
                        help='モデルプロバイダー（省略時は --model-name から自動判別）')
    parser.add_argument('--model-name', default=None,
                        help='モデル名（例: gpt-4o, claude-3-5-sonnet-20241022, meta-llama/Llama-2-7b）')
    parser.add_argument('--api-key', default=None, help='API キー')
    parser.add_argument('--hf-token', default=None, help='HuggingFace token（プライベートモデル用）')
    parser.add_argument('--device', default='auto', choices=['auto', 'cuda', 'cpu'],
                        help='HuggingFace モデルの実行デバイス')
    parser.add_argument('--dataset', default=None, help='データセットのパス（省略時は HuggingFace から取得）')
    parser.add_argument('--k', type=int, default=1, help='pass@k の k 値')
    parser.add_argument('--temperature', type=float, default=0.2, help='生成時の temperature')
    parser.add_argument('--lang', choices=['en', 'ja'], default='en', help='プロンプトの言語')
    parser.add_argument('--prompt-style', choices=['completion', 'instruction'], default='instruction',
                        help='プロンプトスタイル')
    parser.add_argument('--problems', nargs='*', default=None, help='評価する問題 ID（例: 0 1 2）')
    parser.add_argument('--timeout', type=int, default=10, help='各テストのタイムアウト秒数')
    parser.add_argument('--output-dir', default='./results_jhumaneval', help='結果の出力ディレクトリ')
    parser.add_argument('--verbose', '-v', action='store_true', help='詳細出力')

    args = parser.parse_args()

    # プロバイダー自動判別
    if not args.model:
        if args.model_name:
            args.model = detect_model_provider(args.model_name)
            print(f"自動判別: {args.model_name} → {args.model}")
        else:
            print("Error: --model または --model-name のいずれかを指定してください")
            print("\n例:")
            print("  python evaluate_jhumaneval.py --model-name gpt-4o")
            print("  python evaluate_jhumaneval.py --model-name claude-3-5-sonnet-20241022")
            print("  python evaluate_jhumaneval.py --model-name meta-llama/Llama-2-7b")
            print("  python evaluate_jhumaneval.py --model ollama --model-name codellama")
            return 1

    # API キー・モデル名取得
    api_key = None
    hf_token = None
    model_name = args.model_name

    if args.model == 'openai':
        api_key = args.api_key or os.getenv('OPENAI_API_KEY')
        model_name = model_name or 'gpt-4'
        if not api_key:
            print("Error: OPENAI_API_KEY が設定されていません")
            print("--api-key で指定するか、OPENAI_API_KEY 環境変数を設定してください")
            return 1
    elif args.model == 'anthropic':
        api_key = args.api_key or os.getenv('ANTHROPIC_API_KEY')
        model_name = model_name or 'claude-3-5-sonnet-20241022'
        if not api_key:
            print("Error: ANTHROPIC_API_KEY が設定されていません")
            print("--api-key で指定するか、ANTHROPIC_API_KEY 環境変数を設定してください")
            return 1
    elif args.model == 'huggingface':
        hf_token = args.hf_token or os.getenv('HF_TOKEN')
        if not model_name:
            print("Error: HuggingFace モデル名が指定されていません")
            print("--model-name でモデル名を指定してください（例: meta-llama/Llama-2-7b-chat-hf）")
            return 1
    elif args.model == 'mlx':
        hf_token = args.hf_token or os.getenv('HF_TOKEN')
        if not model_name:
            print("Error: MLX モデル名が指定されていません")
            print("--model-name でモデル名を指定してください（例: mlx-community/Qwen2.5-Coder-7B-Instruct-4bit）")
            return 1
    else:  # ollama
        model_name = model_name or 'codellama'

    # データセット読み込み
    print("データセットを読み込み中...")
    dataset = load_jhumaneval_dataset(args.dataset)
    print(f"読み込み完了: {len(dataset)} 問題")

    # 問題フィルタリング
    if args.problems:
        problem_ids = set(args.problems)
        dataset = [item for item in dataset if item['task_id'].split('/')[-1] in problem_ids]

    if not dataset:
        print("Error: 評価対象の問題がありません")
        return 1

    # 出力ディレクトリ作成
    jst = timezone(timedelta(hours=9))
    timestamp = datetime.now(jst).strftime('%Y%m%d_%H%M%S')
    safe_model_name = args.model_name.replace('/', '_').replace(':', '_')
    output_dir = Path(args.output_dir) / f"{timestamp}_{safe_model_name}_{args.lang}"
    output_dir.mkdir(parents=True, exist_ok=True)

    log_file = output_dir / 'log.txt'
    log_handle = open(log_file, 'w', encoding='utf-8')

    def log(msg):
        print(msg)
        log_handle.write(msg + '\n')
        log_handle.flush()

    # 評価開始
    log(f"=== JHumanEval 評価 (pass@{args.k}) ===")
    log(f"Model: {args.model_name}")
    log(f"Language: {args.lang}")
    log(f"Prompt style: {args.prompt_style}")
    log(f"Problems: {len(dataset)}")
    log("")

    results_by_problem = {}
    all_results = []

    for i, item in enumerate(dataset, 1):
        task_id = item['task_id']
        entry_point = item['entry_point']

        log(f"[{i}/{len(dataset)}] {task_id}")

        # プロンプト作成
        prompt = create_prompt(item, args.lang, args.prompt_style)

        # コード生成
        if args.model == 'openai':
            generated_codes = call_openai_api(prompt, api_key, model_name, args.temperature, args.k)
        elif args.model == 'anthropic':
            generated_codes = call_anthropic_api(prompt, api_key, model_name, args.temperature, args.k)
        elif args.model == 'huggingface':
            generated_codes = call_huggingface_api(prompt, model_name, hf_token, args.temperature, args.k, args.device)
        elif args.model == 'mlx':
            generated_codes = call_mlx_api(prompt, model_name, hf_token, args.temperature, args.k)
        else:  # ollama
            generated_codes = call_ollama_api(prompt, model_name, args.temperature, args.k)

        samples_passed = 0
        problem_results = []

        for j, generated in enumerate(generated_codes):
            # コード抽出
            if args.prompt_style == 'completion':
                # completion 形式: prompt + 生成結果
                full_code = item['prompt'] + (generated or "")
            else:
                # instruction 形式: 生成結果からコードを抽出して prompt と結合
                extracted = extract_python_code(generated) if generated else ""
                full_code = item['prompt'] + "\n" + extracted

            # 生成結果をログに出力
            log_handle.write(f"\n{'='*60}\n")
            log_handle.write(f"[{i}/{len(dataset)}] {task_id} - Sample {j+1}/{args.k}\n")
            log_handle.write(f"{'='*60}\n")
            log_handle.write(f"--- Generated Code ---\n")
            log_handle.write(f"{generated}\n")
            log_handle.write(f"--- Full Code ---\n")
            log_handle.write(f"{full_code}\n")
            log_handle.flush()

            # テスト実行
            success, error = run_python_test(full_code, item['test'], entry_point, args.timeout)

            if success:
                log(f"  Sample {j+1}/{args.k}: ✓")
                log_handle.write(f"--- Result: ✓ PASSED ---\n")
                samples_passed += 1
            else:
                log(f"  Sample {j+1}/{args.k}: ✗")
                log_handle.write(f"--- Result: ✗ FAILED ---\n")
                log_handle.write(f"Error: {error}\n")
                if args.verbose and error:
                    log(f"    Error: {error[:200]}")
            log_handle.flush()

            problem_results.append(success)
            all_results.append({
                'task_id': task_id,
                'sample_id': j,
                'prompt': prompt,
                'generated': generated,
                'full_code': full_code,
                'passed': success,
                'error': error if not success else None
            })

        results_by_problem[task_id] = problem_results
        problem_passed = any(problem_results)
        status = "✓" if problem_passed else "✗"
        log(f"  Result: {status} ({samples_passed}/{args.k})")
        log("")

    # 結果集計
    total = len(results_by_problem)
    passed = sum(1 for results in results_by_problem.values() if any(results))
    pass_rate = (passed / total * 100) if total > 0 else 0.0
    ci_lower, ci_upper = wilson_confidence_interval(passed, total)

    log("=" * 60)
    log("評価結果サマリー")
    log("=" * 60)
    log(f"Total:  {total} 問題")
    log(f"Passed: {passed} 問題")
    log(f"Failed: {total - passed} 問題")
    log(f"pass@{args.k}: {pass_rate:.2f}% ({passed}/{total})")
    log(f"95% CI: [{ci_lower*100:.2f}%, {ci_upper*100:.2f}%]")

    # 結果保存
    result_file = output_dir / 'result.jsonl'
    with open(result_file, 'w', encoding='utf-8') as f:
        for result in all_results:
            json.dump(result, f, ensure_ascii=False)
            f.write('\n')

    summary = {
        'model': args.model_name,
        'lang': args.lang,
        'prompt_style': args.prompt_style,
        'k': args.k,
        'temperature': args.temperature,
        'total_problems': total,
        'passed_problems': passed,
        'pass_at_k': round(pass_rate, 2),
        'confidence_interval_95': {
            'lower': round(ci_lower * 100, 2),
            'upper': round(ci_upper * 100, 2)
        },
        'timestamp': timestamp
    }

    summary_file = output_dir / 'summary.json'
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    log(f"\n結果: {result_file}")
    log(f"サマリー: {summary_file}")

    log_handle.close()
    return 0


if __name__ == '__main__':
    sys.exit(main())
