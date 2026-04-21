# プロンプトテンプレート

このディレクトリには、HumanEval評価で使用するプロンプトテンプレートが含まれています。

## テンプレートの種類

### 1. zero_shot.md
**Zero-shot prompting**: コンテキストなし、問題文のみを提示

- Yui言語リファレンスを含まない
- モデルが事前学習で獲得した知識のみで回答
- 最も軽量（トークン数が少ない）

**使用例:**
```bash
python evaluate.py --model-name gpt-4 --template templates/zero_shot.md
```

### 2. one_shot.md
**One-shot prompting**: 1つの例示を提示してから問題を提示

- absolute_value関数の実装例を1つ提示
- 例示からYui言語の文法とスタイルを学習
- Few-shot learningの簡易版

**使用例:**
```bash
python evaluate.py --model-name gpt-4 --template templates/one_shot.md
```

### 3. full_context.md
**Full context prompting**: Yui言語リファレンス全体を提示

- doc/context.md（またはその他のドキュメント）を含む
- 最も詳細な情報を提供
- トークン数が多い

**使用例:**
```bash
python evaluate.py --model-name gpt-4 --template templates/full_context.md --context-file doc/context.md
```

## テンプレート変数

テンプレートでは以下の変数を使用できます:

- `{CONTEXT}`: Yui言語リファレンス（--context-fileで指定）
- `{PROBLEM}`: HumanEval問題文
- `{INSTRUCTION}`: 指示文（言語に応じて自動生成）

## カスタムテンプレートの作成

独自のテンプレートを作成することもできます:

1. このディレクトリに新しい `.md` ファイルを作成
2. 上記の変数を使ってプロンプトを構成
3. `--template` オプションでファイルパスを指定

例: `templates/my_template.md`
```markdown
あなたはYui言語のエキスパートです。

以下の問題を解いてください:
{PROBLEM}

{INSTRUCTION}
```

使用:
```bash
python evaluate.py --model-name gpt-4 --template templates/my_template.md
```

## テンプレート比較実験

複数のテンプレートで性能を比較:

```bash
# Zero-shot
python evaluate.py --model-name gpt-4 --template templates/zero_shot.md

# One-shot
python evaluate.py --model-name gpt-4 --template templates/one_shot.md

# Full context
python evaluate.py --model-name gpt-4 --template templates/full_context.md --context-file doc/context.md
```

結果は `NLP2026/results/` に保存され、ディレクトリ名にテンプレート情報が含まれます。
