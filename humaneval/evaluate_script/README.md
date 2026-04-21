# HumanEval 評価スクリプト使い方ガイド

Yui言語でのLLMモデルの性能を評価するためのツールです。プログラミング初学者の方でも使えるように、わかりやすく説明します。

## 📋 目次

1. [このツールでできること](#このツールでできること)
2. [必要なもの](#必要なもの)
3. [インストール手順](#インストール手順)
4. [使い方](#使い方)
5. [コマンドラインオプション完全リファレンス](#コマンドラインオプション完全リファレンス)
6. [結果の見方](#結果の見方)
7. [トラブルシューティング](#トラブルシューティング)
8. [よくある質問](#よくある質問)

---

## このツールでできること

このツールは、GPT-4やClaudeなどのAIモデルに「Yui言語でプログラムを書かせて」、その正解率を測定します。

**具体的には:**
1. AIモデルに164個のプログラミング問題を解かせます
2. 生成されたYuiコードが正しく動くかテストします
3. 正解率（pass@k）を計算します

---

## 必要なもの

### 1. Python 3.8以上

確認方法（ターミナル/コマンドプロンプトで実行）:
```bash
python3 --version
```

もし `Python 3.8.0` 以上と表示されればOKです。

### 2. AIモデルのAPIキー（どれか1つ）

以下のいずれかが必要です:

- **OpenAI API キー** (GPT-4など)
  - https://platform.openai.com/api-keys で取得
  - 有料（使った分だけ課金）

- **Anthropic API キー** (Claude)
  - https://console.anthropic.com/ で取得
  - 有料（使った分だけ課金）

- **HuggingFace トークン** (オープンソースモデル)
  - https://huggingface.co/settings/tokens で取得
  - モデルによって無料または有料
  - GPU推奨（CPUでも動作可能だが遅い）

- **Ollama** (ローカルで動くAI)
  - 無料
  - https://ollama.com/ からダウンロード

---

## インストール手順

### ステップ1: 必要なパッケージをインストール

Yuiプロジェクトのルートディレクトリから:

```bash
cd /Users/nishigatayuuha/Git/Yui
pip3 install -r humaneval/evaluate_script/requirements.txt
```

**エラーが出た場合:**
- 「permission denied」と表示されたら: `sudo pip3 install -r humaneval/evaluate_script/requirements.txt` を試してください
- 「pip3: command not found」と表示されたら: `pip install -r humaneval/evaluate_script/requirements.txt` を試してください

### ステップ2: APIキーの設定（推奨: .envファイル）

APIキーを毎回入力するのは面倒なので、`.env`ファイルに保存しておくことをおすすめします。

#### .envファイルの作成

```bash
# Yuiルートディレクトリから
cd /Users/nishigatayuuha/Git/Yui
cp humaneval/evaluate_script/.env.example humaneval/evaluate_script/.env
```

その後、`.env`ファイルを開いて、実際のAPIキーを記入します:

```bash
# テキストエディタで開く
nano humaneval/evaluate_script/.env
# または
vim humaneval/evaluate_script/.env
```

`.env`ファイルの中身（使用するモデルに応じて記入）:

```bash
# OpenAIを使う場合
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxx

# Anthropicを使う場合
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxx

# HuggingFaceを使う場合（プライベートモデルのみ）
HF_TOKEN=hf_xxxxxxxxxxxxxxxx
```

**注意:** `.env`ファイルにはAPIキーという大事な情報が入っているので、Gitにコミットしないように注意してください！（`.gitignore`に設定済み）

---

## 使い方

### 実行場所

**すべてのコマンドはYuiルートディレクトリから実行してください:**

```bash
cd /Users/nishigatayuuha/Git/Yui
```

### 基本的な使い方

#### 1. モデルを指定して評価（最もシンプル）

モデル名だけ指定すれば、プロバイダーは自動判別されます:

```bash
# GPT-5.1で日本語問題を5問評価（コンテキストあり）
python3 humaneval/evaluate_script/evaluate.py \
  --model-name gpt-5.1 \
  --problems 0 1 2 3 4 \
  --lang ja

# GPT-4oで英語問題を3問評価
python3 humaneval/evaluate_script/evaluate.py \
  --model-name gpt-4o \
  --problems 0 1 2 \
  --lang en

# Claude 3.5 Sonnetで日本語問題を1問評価
python3 humaneval/evaluate_script/evaluate.py \
  --model-name claude-3-5-sonnet-20241022 \
  --problems 0 \
  --lang ja
```

**モデル自動判別のルール:**
- `gpt-*`, `o1-*`, `o3-*` → OpenAI
- `claude-*` → Anthropic
- `*/*` (スラッシュ含む) → HuggingFace
- その他 → Ollama

#### 2. コンテキストなしで評価

`--no-context`を付けると、Yui言語のリファレンスなしで評価します:

```bash
# コンテキストなしで評価（モデルがYuiを知らない状態）
python3 humaneval/evaluate_script/evaluate.py \
  --model-name gpt-5.1 \
  --no-context \
  --problems 0 1 2 3 4 \
  --lang ja
```

**コンテキストあり vs なし:**
- **コンテキストあり**（デフォルト）: `doc/context.md`のYui言語リファレンスを含む → 正しい構文を生成しやすい
- **コンテキストなし**: リファレンスなし → モデルの事前学習知識のみで生成 → 構文エラーが多い

#### 3. 全問題を評価

`--problems`を省略すると全164問題を評価します:

```bash
# 全問題を評価（約1-2分、API料金に注意）
python3 humaneval/evaluate_script/evaluate.py \
  --model-name gpt-5.1 \
  --lang ja

# コンテキストなしで全問題評価
python3 humaneval/evaluate_script/evaluate.py \
  --model-name gpt-5.1 \
  --no-context \
  --lang ja
```

**注意:** 164問 × k回生成するので、API料金が高くなる可能性があります！

#### 4. pass@3 を計算（各問題3回生成）

```bash
python3 humaneval/evaluate_script/evaluate.py \
  --model-name gpt-5.1 \
  --k 3 \
  --problems 0 1 2 \
  --lang ja
```

### 各プロバイダーの使い方

#### OpenAI（GPT-4、GPT-5など）

```bash
# .envファイルにOPENAI_API_KEYを設定済みの場合
python3 humaneval/evaluate_script/evaluate.py \
  --model-name gpt-5.1 \
  --problems 0 \
  --lang ja

# 他のGPTモデル
python3 humaneval/evaluate_script/evaluate.py \
  --model-name gpt-4o \
  --problems 0 \
  --lang en

python3 humaneval/evaluate_script/evaluate.py \
  --model-name gpt-4-turbo \
  --problems 0 \
  --lang en
```

**注意: GPT-5系モデル（gpt-5.*, o1-*, o3-*）の制約:**
- `temperature=1`固定（変更不可）
- `max_completion_tokens`を使用（`max_tokens`は使用不可）
- 一部のモデル名は利用できない可能性があります

#### Anthropic（Claude）

```bash
# .envファイルにANTHROPIC_API_KEYを設定済みの場合
python3 humaneval/evaluate_script/evaluate.py \
  --model-name claude-3-5-sonnet-20241022 \
  --problems 0 \
  --lang ja

python3 humaneval/evaluate_script/evaluate.py \
  --model-name claude-3-opus-20240229 \
  --problems 0 \
  --lang en
```

#### Ollama（ローカルAI）

```bash
# まずOllamaを起動（別のターミナルで）
ollama serve

# もう1つのターミナルでモデルをダウンロード
ollama pull codellama

# 評価を実行
python3 humaneval/evaluate_script/evaluate.py \
  --model-name codellama \
  --problems 0 \
  --lang ja

# 他のモデル
python3 humaneval/evaluate_script/evaluate.py \
  --model-name qwen \
  --problems 0 \
  --lang ja
```

#### HuggingFace（オープンソースモデル）

```bash
# .envファイルにHF_TOKENを設定済みの場合（GPU使用）
python3 humaneval/evaluate_script/evaluate.py \
  --model-name meta-llama/CodeLlama-7b-hf \
  --problems 0 \
  --lang ja

# CPU使用（遅いが無料、パブリックモデルならトークン不要）
python3 humaneval/evaluate_script/evaluate.py \
  --model-name bigcode/starcoder \
  --device cpu \
  --problems 0 \
  --lang en
```

**おすすめHuggingFaceモデル:**
- `bigcode/starcoder`: コード生成に特化
- `codellama/CodeLlama-7b-hf`: Meta製コード生成モデル
- `meta-llama/Llama-2-7b-chat-hf`: 汎用モデル（要トークン）
- `Qwen/Qwen2.5-Coder-7B-Instruct`: 高性能コード生成モデル

---

## コマンドラインオプション完全リファレンス

### 🎯 必須オプション

#### `--model-name <モデル名>`

**説明:** 使用するAIモデルを指定します。プロバイダーは自動判別されます。

**デフォルト:** なし（必須）

**使用例:**
```bash
--model-name gpt-5.1                           # OpenAI GPT-5.1
--model-name gpt-4o                            # OpenAI GPT-4o
--model-name claude-3-5-sonnet-20241022        # Anthropic Claude 3.5 Sonnet
--model-name claude-3-5-haiku-20241022         # Anthropic Claude 3.5 Haiku
--model-name codellama                         # Ollama CodeLlama
--model-name meta-llama/Llama-2-7b-chat-hf     # HuggingFace Llama-2
```

**自動判別ルール:**
- `gpt-*`, `o1-*`, `o3-*` → `openai`
- `claude-*` → `anthropic`
- `/` を含む → `huggingface`
- その他 → `ollama`

---

### ⚙️ モデル設定オプション

#### `--model <プロバイダー名>`

**説明:** プロバイダーを手動で指定します。通常は自動判別されるので不要です。

**デフォルト:** 自動判別

**選択肢:** `openai`, `anthropic`, `ollama`, `huggingface`

**使用例:**
```bash
--model openai --model-name gpt-4
```

#### `--api-key <APIキー>`

**説明:** API認証キーを直接指定します。通常は環境変数や.envファイルで設定します。

**デフォルト:** 環境変数から取得
- OpenAI: `OPENAI_API_KEY`
- Anthropic: `ANTHROPIC_API_KEY`

**使用例:**
```bash
--api-key sk-proj-xxxxxxxxxxxxx
```

**セキュリティ注意:** コマンドラインに直接APIキーを入力すると、シェルの履歴に残るため推奨しません。.envファイルまたは環境変数の使用を推奨します。

#### `--hf-token <HuggingFaceトークン>`

**説明:** HuggingFaceのアクセストークンを指定します（プライベートモデル用）。

**デフォルト:** 環境変数 `HF_TOKEN`

**使用例:**
```bash
--hf-token hf_xxxxxxxxxxxxx
```

#### `--device <デバイス>`

**説明:** HuggingFaceモデルの実行デバイスを指定します。

**デフォルト:** `auto`（自動選択）

**選択肢:**
- `auto` - GPUが利用可能なら使用、なければCPU
- `cuda` - GPU強制使用（CUDA対応GPU必須）
- `cpu` - CPU強制使用

**使用例:**
```bash
--device cuda    # GPUを使用
--device cpu     # CPUを使用
```

---

### 📝 評価設定オプション

#### `--lang <言語>`

**説明:** 問題文の言語を指定します。

**デフォルト:** `en`（英語）

**選択肢:**
- `en` - 英語の問題文
- `ja` - 日本語の問題文

**使用例:**
```bash
--lang ja    # 日本語問題を使用
--lang en    # 英語問題を使用
```

**推奨:** 日本語対応モデルには`ja`、その他は`en`を推奨。

#### `--problems <問題番号リスト>`

**説明:** 評価する問題を番号で指定します。空白区切りで複数指定可能。

**デフォルト:** 全164問題

**使用例:**
```bash
--problems 0 1 2 3 4              # 問題0〜4のみ評価
--problems 0                      # 問題0のみ評価
--problems 10 20 30 40 50         # 指定した5問のみ評価
```

**用途:** テスト実行や特定問題の再評価に便利。

#### `--k <サンプル数>`

**説明:** 各問題に対して生成するコードのサンプル数（pass@k のk値）。

**デフォルト:** `1`（pass@1）

**使用例:**
```bash
--k 1     # pass@1: 各問題1回生成
--k 3     # pass@3: 各問題3回生成
--k 5     # pass@5: 各問題5回生成
--k 10    # pass@10: 各問題10回生成（HumanEval標準）
```

**注意:**
- k が大きいほどAPI呼び出し回数が増え、コストが高くなります
- 例: k=3, 164問題 → 492回のAPI呼び出し

---

### 📚 コンテキスト設定オプション

#### `--context-file <ファイルパス>`

**説明:** Yui言語リファレンスのファイルパスを指定します。

**デフォルト:** `doc/context.md`

**利用可能なファイル:**
- `doc/context.md` - 完全なリファレンス（18KB、推奨）
- `doc/CHEATSHEET.md` - 簡潔版（10KB）
- `doc/API.md` - APIリファレンス（15KB）
- `doc/EXAMPLES.md` - コード例重視（21KB）

**使用例:**
```bash
--context-file doc/context.md        # 標準（デフォルト）
--context-file doc/CHEATSHEET.md     # 簡潔版
--context-file doc/API.md            # API重視
--context-file doc/EXAMPLES.md       # 例重視
```

**選択基準:**
- トークン節約が必要 → `CHEATSHEET.md`
- 完全な情報が必要 → `context.md`（デフォルト）
- 関数リファレンス重視 → `API.md`
- コード例で学習させたい → `EXAMPLES.md`

#### `--no-context`

**説明:** コンテキストなしで評価します（Yui言語リファレンスを渡さない）。

**デフォルト:** false（コンテキストあり）

**使用例:**
```bash
--no-context    # コンテキストなしで実行
```

**用途:**
- モデルの事前知識のみでの性能測定
- zero-shot性能の評価
- トークン節約

**注意:** `--no-context` と `--context-file` は同時に使用できません。

---

### 🔧 実行制御オプション

#### `--timeout <秒数>`

**説明:** 各テストケースの最大実行時間（秒）。

**デフォルト:** `10`秒

**使用例:**
```bash
--timeout 30    # 30秒まで待機
--timeout 5     # 5秒でタイムアウト
```

**用途:**
- 複雑な問題で実行時間が長い場合に増やす
- 無限ループ対策

#### `--output-dir <ディレクトリ>`

**説明:** 結果の出力先ディレクトリ。

**デフォルト:** `./results`

**使用例:**
```bash
--output-dir ./my_results       # カスタムディレクトリ
--output-dir /path/to/results   # 絶対パス指定
```

**出力構造:**
```
<output-dir>/
└── YYYYMMDD_HHMMSS_<モデル名>_<コンテキスト>/
    ├── generated/           # 生成されたコード
    ├── result.jsonl         # 詳細結果
    └── summary.json         # サマリー
```

#### `--verbose` または `-v`

**説明:** 詳細な出力を表示します。

**デフォルト:** false（簡潔な出力）

**使用例:**
```bash
--verbose    # 詳細表示
-v           # 同上（短縮形）
```

**出力内容:**
- エラーメッセージの詳細
- 実行時の詳細ログ
- デバッグ情報

---

### 📋 オプション早見表

| オプション | 必須 | デフォルト | 説明 | 使用例 |
|-----------|------|-----------|------|--------|
| `--model-name` | ✓ | なし | モデル名（自動判別） | `--model-name gpt-5.1` |
| `--model` | | 自動 | プロバイダー（手動指定） | `--model openai` |
| `--api-key` | | 環境変数 | APIキー | `--api-key sk-xxx...` |
| `--lang` | | `en` | 問題言語（`en`/`ja`） | `--lang ja` |
| `--problems` | | 全164問 | 評価問題番号 | `--problems 0 1 2` |
| `--k` | | `1` | サンプル数（pass@k） | `--k 3` |
| `--context-file` | | `doc/context.md` | コンテキストファイル | `--context-file doc/CHEATSHEET.md` |
| `--no-context` | | false | コンテキストなし | `--no-context` |
| `--timeout` | | `10` | タイムアウト（秒） | `--timeout 30` |
| `--output-dir` | | `./results` | 出力先 | `--output-dir ./my_results` |
| `--verbose` | | false | 詳細出力 | `--verbose` または `-v` |
| `--hf-token` | | 環境変数 | HFトークン | `--hf-token hf_xxx...` |
| `--device` | | `auto` | 実行デバイス | `--device cuda` |

---

## 結果の見方

### 実行中の表示

```
自動判別: gpt-5.1 → openai
=== HumanEval評価 (pass@1) ===
Model: gpt-5.1
Language: ja
Context: doc/context.md
Total problems: 5

[1/5] 0_has_close_elements
  Sample 1/1... ✓ (0.41s)
  Problem result: ✓ (1/1 samples passed)

[2/5] 1_separate_paren_groups
  Sample 1/1... ✗ (0.33s)
  Problem result: ✗ (0/1 samples passed)

...
```

- **✓** = テスト成功
- **✗** = テスト失敗
- **(0.41s)** = 実行時間

### 最終結果

```
============================================================
評価結果サマリー
============================================================
Total:  5 問題
Passed: 3 問題 (少なくとも1個のサンプルが成功)
Failed: 2 問題 (全サンプルが失敗)
pass@1: 60.00% (3/5)

生成されたコード: results/20251228_053146_gpt-5.1/generated
結果を保存しました: results/20251228_053146_gpt-5.1/result.jsonl
総合結果を保存しました: results/20251228_053146_gpt-5.1/summary.json
============================================================
```

### 出力ファイル

結果は`results/YYYYMMDD_HHMMSS_モデル名/`に保存されます:

```
results/20251228_053146_gpt-5.1/
├── result.jsonl          # 各サンプルの詳細結果（1行1サンプル）
├── summary.json          # 総合結果（pass@k、成功率など）
└── generated/            # 生成されたYuiコード
    ├── 0_0_has_close_elements_sample_0.yui
    ├── 1_1_separate_paren_groups_sample_0.yui
    └── ...
```

#### result.jsonl の形式

各行が1つのサンプルを表します（JSONL形式 = 1行1JSON）:

```json
{
  "problem_id": "0",
  "problem_name": "0_has_close_elements",
  "sample_id": 0,
  "lang": "ja",
  "model": "gpt-5.1",
  "canonical_solution": "標準ライブラリを使う\n\nhas_close_elements = ...",
  "input": "システムプロンプト + ユーザープロンプト（モデルへの入力）",
  "output": "モデルが生成したコード",
  "passed": true,
  "error": null,
  "execution_time": 0.41
}
```

#### summary.json の形式

総合結果:

```json
{
  "model": "gpt-5.1",
  "lang": "ja",
  "context": "doc/context.md",
  "k": 1,
  "total_problems": 5,
  "passed_problems": 3,
  "failed_problems": 2,
  "pass_at_k": 60.0,
  "timestamp": "20251228_053146",
  "total_samples": 5,
  "passed_samples": 3
}
```

---

## トラブルシューティング

### エラー: `Error: OPENAI_API_KEY が設定されていません`

**原因:** APIキーが設定されていません

**解決方法:**
1. `.env`ファイルを確認:
```bash
cat humaneval/evaluate_script/.env
```

2. `.env`ファイルを編集して APIキーを追加:
```bash
nano humaneval/evaluate_script/.env
```

### エラー: `Error: openai パッケージがインストールされていません`

**原因:** 必要なパッケージがインストールされていません

**解決方法:**
```bash
pip3 install -r humaneval/evaluate_script/requirements.txt
```

### エラー: `Unsupported parameter: 'max_tokens' is not supported`

**原因:** GPT-5系モデルで`max_tokens`を使用しようとしています

**解決方法:** これは自動的に処理されているはずですが、もしエラーが出た場合はモデル名を確認してください。`gpt-5.*`、`o1-*`、`o3-*`などのモデルは特別な処理が必要です。

### エラー: `'temperature' does not support 0.8`

**原因:** GPT-5系モデルは`temperature=1`のみサポート

**解決方法:** これは自動的に処理されています。GPT-5系モデルでは`temperature`パラメータが省略され、デフォルト値（1）が使用されます。

### エラー: `subprocess.TimeoutExpired`

**原因:** プログラムの実行に時間がかかりすぎています

**解決方法:**
```bash
# タイムアウト時間を増やす（デフォルト10秒 → 30秒）
python3 humaneval/evaluate_script/evaluate.py \
  --model-name gpt-5.1 \
  --timeout 30 \
  --problems 0 \
  --lang ja
```

### エラー: API rate limit exceeded

**原因:** APIの呼び出し制限に達しました

**解決方法:**
- しばらく待ってから再実行
- `--problems` で評価する問題数を減らす

### 結果を確認する方法

```bash
# 最新の結果ディレクトリを確認
ls -lt results/ | head -5

# summary.jsonを見る（総合結果）
cat results/20251228_053146_gpt-5.1/summary.json | python3 -m json.tool

# result.jsonlの最初のサンプルを見る
head -1 results/20251228_053146_gpt-5.1/result.jsonl | python3 -m json.tool

# 生成されたコードを見る
cat results/20251228_053146_gpt-5.1/generated/0_0_has_close_elements_sample_0.yui
```

---

## よくある質問

### Q: お金はどのくらいかかりますか？

**A:** 使用するモデルと問題数によります:

- **GPT-4o**: 1問あたり約$0.005〜$0.02（50〜200円）
  - 全164問: 約$1〜$3（1000〜3000円）

- **GPT-5.1**: 1問あたり約$0.01〜$0.05（100〜500円）
  - 全164問: 約$2〜$8（2000〜8000円）

- **Claude**: 1問あたり約$0.005〜$0.02（50〜200円）
  - 全164問: 約$1〜$3（1000〜3000円）

- **Ollama**: 無料（ローカルで実行）

**おすすめ:** まず5問だけ試してから全問評価してください！

### Q: pass@k の k ってなんですか？

**A:** 各問題で何回コードを生成するかです:

- **pass@1**: 1回だけ生成（速い、安い）
- **pass@3**: 3回生成して1回でも成功すればOK（遅い、高い）
- **pass@5**: 5回生成して1回でも成功すればOK（さらに遅い、高い）

一般的には **pass@1** で十分です。研究用途では**pass@3**がよく使われます。

### Q: 英語版と日本語版、どちらを使うべきですか？

**A:**

- **英語版** (`--lang en`): AIモデルは英語の方が得意なので、性能が良い傾向
- **日本語版** (`--lang ja`): 日本語でどこまで理解できるかテストしたい場合

研究用途なら両方試すと面白いです！

### Q: コンテキストありとなし、どちらを使うべきですか？

**A:**

- **コンテキストあり**（デフォルト）: Yui言語リファレンスを含む → 正しいコードを生成しやすい → **実用的な評価**
- **コンテキストなし** (`--no-context`): リファレンスなし → モデルの事前学習のみ → **ゼロショット性能の評価**

通常は**コンテキストあり**を推奨します。

### Q: 結果をどう見ればいいですか？

**A:** `pass@1` の値を確認してください:

- **90%以上**: 非常に優秀
- **70-90%**: 良好
- **50-70%**: まあまあ
- **50%未満**: 改善が必要

**注意:** コンテキストなしでは大幅に低くなります（0-20%程度）。

### Q: 利用可能なモデルを確認したい

**A:** 以下のコマンドでOpenAIのモデル一覧を確認できます:

```bash
python3 -c "
import openai, os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path('humaneval/evaluate_script/.env'))
client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
models = client.models.list()

for model in models.data:
    if 'gpt' in model.id.lower():
        print(model.id)
" | grep gpt
```

---

## さらに詳しく知りたい場合

- 詳細な技術仕様: `../CLAUDE.md` を参照
- Yui言語の文法: `../../doc/context.md` を参照
- 問題: GitHub Issues (https://github.com/KuramitsuLab/Yui/issues)

---

## ライセンス

このスクリプトはMITライセンスで提供されています。
