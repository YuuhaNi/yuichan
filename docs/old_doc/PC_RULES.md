## 変換ルール

PythonからYui言語への変換ルールをまとめました

### 1. 基本構文
- Python: `def function_name(x):` → Yui: `function_name = 入力 x に対し {`
- Python: `def function_name(x, y):` → Yui: `function_name = 入力 x, y に対し {`
- Python: `def function_name():` → Yui: `function_name = 入力なしに対し {`
- Python: `return value` → Yui: `valueが答え`

### 2. 演算子 → 関数呼び出し
- Python: `a + b` → Yui: `和(a, b)`
- Python: `a - b` → Yui: `差(a, b)`
- Python: `a * b` → Yui: `積(a, b)`
- Python: `a / b` or `a // b` → Yui: `商(a, b)`
- Python: `a % b` → Yui: `剰余(a, b)`
- Python: `abs(x)` → Yui: `絶対値(x)`
- Python: `max(...)` → Yui: `最大値(...)`
- Python: `min(...)` → Yui: `最小値(...)`

### 3. 条件分岐
- Python: `if x == 1:` → Yui: `もし x が 1 ならば {`
- Python: `if x != 1:` → Yui: `もし x が 1 以外 ならば {`
- Python: `if x >= 1:` → Yui: `もし x が 1 以上 ならば {`
- Python: `if x <= 1:` → Yui: `もし x が 1 以下 ならば {`
- Python: `if x > 1:` → Yui: `もし x が 1 より大きい ならば {`
- Python: `if x < 1:` → Yui: `もし x が 1 より小さい ならば {`
- Python: `else:` → Yui: `そうでなければ {`

### 4. ループ
- Python: `for i in range(n):` → Yui: `i = 0` + `n回、くり返す { ... iを増やす }`
- Python: `for item in array:` → Yui: `i = 0` + `length = |array|` + `length回、くり返す { item = array[i] ... iを増やす }`
- Python: `while` → Yui: 固定回数ループに変換（最大反復回数を設定）
- Python: `break` → Yui: `くり返しを抜ける`
- Python: `continue` → Yui: 条件分岐で代用（continueは存在しない）

### 5. 配列操作
- Python: `len(arr)` → Yui: `|arr|`
- Python: `arr.append(x)` → Yui: `arrの末尾に x を 追加する`
- Python: `x += 1` → Yui: `xを増やす`
- Python: `x -= 1` → Yui: `xを減らす`

### 6. 文字列
- Python: `len(s)` → Yui: `|s|`
- Python: `ord('A')` → Yui: `"A"[0]`
- Python: `s == "text"` → Yui: 文字ごとに比較（直接比較不可）

### 7. 型変換
- Python: `int(x)` → Yui: `整数化(x)`
- Python: `float(x)` → Yui: `少数化(x)`
- Python: `str(x)` → Yui: `文字列化(x)`

### 8. その他（注意事項）
- ファイル先頭に `標準ライブラリを使う` を追加（算術演算を使う場合）
- すべての `{` の後に改行
- テストケースは `>>>` 形式で記述
