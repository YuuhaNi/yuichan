## Yui言語の表示的意味論 (Denotational Semantics)

Yui言語の構文要素をPython言語との対応付けによって形式的に定義します。

### 基本概念

表示的意味論では、以下の意味関数を定義します：

- **ℰ** : Expression → Env → Value （式の意味）
- **𝒮** : Statement → Env → Env （文の意味）
- **ℱ** : Function → Env → (Value* → Value) （関数の意味）

ここで：
- `Env` = 環境（変数名 → 値のマッピング）
- `Value` = 値（整数、浮動小数点数、文字列、配列、関数）
- `Value*` = 値のリスト

---

### 値の定義

```python
Value = int | float | str | list[Value] | Callable
```

#### Yui → Python 値の対応

| Yui | Python | 例 |
|-----|--------|-----|
| 整数 | `int` | `42` |
| 浮動小数点数 | `float` | `3.14` |
| 文字列 | `list[int]` | `"Hello"` → `[72, 101, 108, 108, 111]` |
| 配列 | `list[Value]` | `[1, 2, 3]` |
| 空配列 | `[]` | `[]` |
| 真偽値 | `1` または `0` | `1` (真), `0` (偽) |
| 関数 | `Callable` | `lambda ...` |

**重要**: Yui言語の文字列は、内部的に文字コード（整数）のリストとして表現されます。

---

### 環境 (Environment)

環境 `ρ` は、変数名から値へのマッピングです。

```python
Env = dict[str, Value]

# 空環境
ρ₀ = {}

# 環境の拡張
ρ[x ↦ v] = {**ρ, x: v}

# 環境からの検索
ρ(x) = ρ[x]
```

---

### 式の意味 ℰ⟦e⟧ρ

#### リテラル

```
ℰ⟦n⟧ρ = n                    # 整数リテラル
ℰ⟦f⟧ρ = f                    # 浮動小数点リテラル
ℰ⟦"s"⟧ρ = [ord(c) for c in s]  # 文字列リテラル
```

**Python対応:**
```python
# Yui: 42
42

# Yui: 3.14
3.14

# Yui: "Hello"
[72, 101, 108, 108, 111]  # [ord(c) for c in "Hello"]
```

#### 識別子

```
ℰ⟦x⟧ρ = ρ(x)
```

**Python対応:**
```python
# Yui: count
ρ['count']  # 環境から変数 count の値を取得
```

#### 配列リテラル

```
ℰ⟦[e₁, e₂, ..., eₙ]⟧ρ = [ℰ⟦e₁⟧ρ, ℰ⟦e₂⟧ρ, ..., ℰ⟦eₙ⟧ρ]
```

**Python対応:**
```python
# Yui: [1, 2, 3]
[1, 2, 3]

# Yui: []
[]
```

#### 配列アクセス

```
ℰ⟦arr[i]⟧ρ = (ℰ⟦arr⟧ρ)[ℰ⟦i⟧ρ]
```

**Python対応:**
```python
# Yui: array[i]
ρ['array'][ρ['i']]
```

#### 配列長

```
ℰ⟦|arr|⟧ρ = len(ℰ⟦arr⟧ρ)
```

**Python対応:**
```python
# Yui: |array|
len(ρ['array'])
```

#### 関数呼び出し

```
ℰ⟦f(e₁, e₂, ..., eₙ)⟧ρ = (ℰ⟦f⟧ρ)(ℰ⟦e₁⟧ρ, ℰ⟦e₂⟧ρ, ..., ℰ⟦eₙ⟧ρ)
```

**Python対応:**
```python
# Yui: factorial(5)
ρ['factorial'](5)

# Yui: 和(1, 2, 3)
sum([1, 2, 3])
```

---

### 文の意味 𝒮⟦s⟧ρ

#### 代入

```
𝒮⟦x = e⟧ρ = ρ[x ↦ ℰ⟦e⟧ρ]
```

**Python対応:**
```python
# Yui: count = 0
ρ['count'] = 0
```

#### 配列更新

```
𝒮⟦arr[i] = e⟧ρ = ρ' where
  arr_val = ℰ⟦arr⟧ρ
  arr_val[ℰ⟦i⟧ρ] = ℰ⟦e⟧ρ
  ρ' = ρ[arr ↦ arr_val]
```

**Python対応:**
```python
# Yui: array[i] = value
ρ['array'][ρ['i']] = ρ['value']
```

#### インクリメント

```
𝒮⟦x を増やす⟧ρ = ρ[x ↦ ℰ⟦x⟧ρ + 1]
```

**Python対応:**
```python
# Yui: count を増やす
ρ['count'] += 1
```

#### デクリメント

```
𝒮⟦x を減らす⟧ρ = ρ[x ↦ ℰ⟦x⟧ρ - 1]
```

**Python対応:**
```python
# Yui: count を減らす
ρ['count'] -= 1
```

#### 配列追加

```
𝒮⟦arr の末尾に e を 追加する⟧ρ = ρ' where
  arr_val = ℰ⟦arr⟧ρ
  arr_val.append(ℰ⟦e⟧ρ)
  ρ' = ρ[arr ↦ arr_val]
```

**Python対応:**
```python
# Yui: result の末尾に value を 追加する
ρ['result'].append(ρ['value'])
```

#### 条件分岐

```
𝒮⟦もし c ならば、{ s₁ } そうでなければ { s₂ }⟧ρ =
  if ℰ⟦c⟧ρ then 𝒮⟦s₁⟧ρ else 𝒮⟦s₂⟧ρ
```

**Python対応:**
```python
# Yui:
# もし x が 0 ならば、{
#     result = 1
# }
# そうでなければ {
#     result = 0
# }

if ρ['x'] == 0:
    ρ['result'] = 1
else:
    ρ['result'] = 0
```

#### ループ

```
𝒮⟦n 回、くり返す { s }⟧ρ = ρₙ where
  ρ₀ = ρ
  ρᵢ₊₁ = 𝒮⟦s⟧ρᵢ for i = 0, 1, ..., n-1
```

**Python対応:**
```python
# Yui:
# 10回、くり返す {
#     count を増やす
# }

for _ in range(10):
    ρ['count'] += 1
```

#### ループ制御

```
𝒮⟦くり返しを抜ける⟧ρ = break
```

**Python対応:**
```python
# Yui: くり返しを抜ける
break

```

#### Return文

```
𝒮⟦e が答え⟧ρ = return ℰ⟦e⟧ρ
```

**Python対応:**
```python
# Yui: result が答え
return ρ['result']
```

---

### 関数の意味 ℱ⟦f⟧ρ

#### 関数定義

```
ℱ⟦name = 入力 x₁, x₂, ..., xₙ に対し { s }⟧ρ = λ(v₁, v₂, ..., vₙ).
  let ρ' = ρ[x₁ ↦ v₁][x₂ ↦ v₂]...[xₙ ↦ vₙ]
  in 𝒮⟦s⟧ρ'
```

**Python対応:**
```python
# Yui:
# factorial = 入力 n に対し {
#     もし n が 1 以下 ならば、{
#         1が答え
#     }
#     そうでなければ {
#         prev = 差(n, 1)
#         積(n, factorial(prev))が答え
#     }
# }

def factorial(n):
    if n <= 1:
        return 1
    else:
        prev = n - 1
        return n * factorial(prev)
```

---

### 条件式の意味

#### 比較演算子

```
ℰ⟦x が y⟧ρ = (ℰ⟦x⟧ρ == ℰ⟦y⟧ρ) ? 1 : 0
ℰ⟦x が y より大きい⟧ρ = (ℰ⟦x⟧ρ > ℰ⟦y⟧ρ) ? 1 : 0
ℰ⟦x が y より小さい⟧ρ = (ℰ⟦x⟧ρ < ℰ⟦y⟧ρ) ? 1 : 0
ℰ⟦x が y 以上⟧ρ = (ℰ⟦x⟧ρ >= ℰ⟦y⟧ρ) ? 1 : 0
ℰ⟦x が y 以下⟧ρ = (ℰ⟦x⟧ρ <= ℰ⟦y⟧ρ) ? 1 : 0
ℰ⟦x が y と異なる⟧ρ = (ℰ⟦x⟧ρ != ℰ⟦y⟧ρ) ? 1 : 0
```

**Python対応:**
```python
# Yui: もし x が 10 ならば
if ρ['x'] == 10:

# Yui: もし x が 10 より大きいならば
if ρ['x'] > 10:

# Yui: もし x が 10 より小さいならば
if ρ['x'] < 10:

# Yui: もし x が 10 以上 ならば
if ρ['x'] >= 10:

# Yui: もし x が 10 以下 ならば
if ρ['x'] <= 10:

# Yui: もし x が 10 と異なるならば
if ρ['x'] != 10:
```

---

### 標準ライブラリの意味

#### 算術関数

```
ℰ⟦和(e₁, e₂, ..., eₙ)⟧ρ = ℰ⟦e₁⟧ρ + ℰ⟦e₂⟧ρ + ... + ℰ⟦eₙ⟧ρ
ℰ⟦差(e₁, e₂)⟧ρ = ℰ⟦e₁⟧ρ - ℰ⟦e₂⟧ρ
ℰ⟦積(e₁, e₂, ..., eₙ)⟧ρ = ℰ⟦e₁⟧ρ × ℰ⟦e₂⟧ρ × ... × ℰ⟦eₙ⟧ρ
ℰ⟦商(e₁, e₂)⟧ρ = ⌊ℰ⟦e₁⟧ρ / ℰ⟦e₂⟧ρ⌋  # 整数除算
ℰ⟦剰余(e₁, e₂)⟧ρ = ℰ⟦e₁⟧ρ mod ℰ⟦e₂⟧ρ
ℰ⟦平方根(e)⟧ρ = √(ℰ⟦e⟧ρ)
ℰ⟦絶対値(e)⟧ρ = |ℰ⟦e⟧ρ|
ℰ⟦最大値(e₁, ..., eₙ)⟧ρ = max(ℰ⟦e₁⟧ρ, ..., ℰ⟦eₙ⟧ρ)
ℰ⟦最小値(e₁, ..., eₙ)⟧ρ = min(ℰ⟦e₁⟧ρ, ..., ℰ⟦eₙ⟧ρ)
```

**Python対応:**
```python
# Yui: 和(1, 2, 3)
sum([1, 2, 3])  # または 1 + 2 + 3

# Yui: 差(10, 3)
10 - 3

# Yui: 積(2, 3, 4)
2 * 3 * 4

# Yui: 商(10, 3)
10 // 3  # 整数除算

# Yui: 剰余(10, 3)
10 % 3

# Yui: 平方根(16)
math.sqrt(16)

# Yui: 絶対値(-5)
abs(-5)

# Yui: 最大値(1, 5, 3)
max([1, 5, 3])

# Yui: 最小値(1, 5, 3)
min([1, 5, 3])
```

#### 型変換関数

```
ℰ⟦整数化(e)⟧ρ = int(ℰ⟦e⟧ρ)
ℰ⟦少数化(e)⟧ρ = float(ℰ⟦e⟧ρ)
ℰ⟦文字列化(e)⟧ρ = [ord(c) for c in str(ℰ⟦e⟧ρ)]
```

**Python対応:**
```python
# Yui: 整数化(3.14)
int(3.14)  # 3

# Yui: 少数化(42)
float(42)  # 42.0

# Yui: 文字列化(42)
[ord(c) for c in str(42)]  # [52, 50] ("42" の文字コード)
```

#### 型判定関数

```
ℰ⟦整数判定(e)⟧ρ = isinstance(ℰ⟦e⟧ρ, int) ? 1 : 0
ℰ⟦少数判定(e)⟧ρ = isinstance(ℰ⟦e⟧ρ, float) ? 1 : 0
ℰ⟦文字列判定(e)⟧ρ = (isinstance(ℰ⟦e⟧ρ, list) and all(isinstance(x, int) for x in ℰ⟦e⟧ρ)) ? 1 : 0
```

**Python対応:**
```python
# Yui: 整数判定(x)
1 if isinstance(ρ['x'], int) else 0

# Yui: 少数判定(x)
1 if isinstance(ρ['x'], float) else 0

# Yui: 文字列判定(x)
1 if isinstance(ρ['x'], list) and all(isinstance(c, int) for c in ρ['x']) else 0
```

#### ビット演算関数

```
ℰ⟦論理積(e₁, e₂)⟧ρ = ℰ⟦e₁⟧ρ & ℰ⟦e₂⟧ρ
ℰ⟦論理和(e₁, e₂)⟧ρ = ℰ⟦e₁⟧ρ | ℰ⟦e₂⟧ρ
ℰ⟦排他的論理和(e₁, e₂)⟧ρ = ℰ⟦e₁⟧ρ ^ ℰ⟦e₂⟧ρ
ℰ⟦ビット反転(e)⟧ρ = ~ℰ⟦e⟧ρ
ℰ⟦左シフト(e₁, e₂)⟧ρ = ℰ⟦e₁⟧ρ << ℰ⟦e₂⟧ρ
ℰ⟦右シフト(e₁, e₂)⟧ρ = ℰ⟦e₁⟧ρ >> ℰ⟦e₂⟧ρ
```

**Python対応:**
```python
# Yui: 論理積(12, 10)
12 & 10

# Yui: 論理和(12, 10)
12 | 10

# Yui: 排他的論理和(12, 10)
12 ^ 10

# Yui: ビット反転(12)
~12

# Yui: 左シフト(12, 2)
12 << 2

# Yui: 右シフト(12, 2)
12 >> 2
```

---

### 完全な例: 階乗関数の意味

### Yuiコード

```yui
標準ライブラリを使う

factorial = 入力 n に対し {
    もし n が 1 以下 ならば、{
        1が答え
    }
    そうでなければ {
        prev = 差(n, 1)
        積(n, factorial(prev))が答え
    }
}
```

### 表示的意味論

```
ℱ⟦factorial = 入力 n に対し { ... }⟧ρ₀ = λn.
  let ρ₁ = ρ₀[n ↦ n]
  in if n <= 1 then
       return 1
     else
       let ρ₂ = ρ₁[prev ↦ n - 1]
       in return n × factorial(prev)
```

### Python対応

```python
def factorial(n):
    if n <= 1:
        return 1
    else:
        prev = n - 1
        return n * factorial(prev)
```

---

### 完全な例: 配列の反転

#### Yuiコード

```yui
標準ライブラリを使う

reverse = 入力 array に対し {
    length = |array|
    result = []
    i = 0

    length回、くり返す {
        idx = 差(差(length, i), 1)
        resultの末尾に array[idx] を 追加する
        iを増やす
    }

    resultが答え
}
```

#### 表示的意味論

```
ℱ⟦reverse = 入力 array に対し { ... }⟧ρ₀ = λarray.
  let ρ₁ = ρ₀[array ↦ array]
      ρ₂ = ρ₁[length ↦ len(array)]
      ρ₃ = ρ₂[result ↦ []]
      ρ₄ = ρ₃[i ↦ 0]
  in for _ in range(length):
       let idx = length - i - 1
           ρ₅ = ρ₄[idx ↦ idx]
       in result.append(array[idx])
          i += 1
     return result
```

#### Python対応

```python
def reverse(array):
    length = len(array)
    result = []
    i = 0

    for _ in range(length):
        idx = length - i - 1
        result.append(array[idx])
        i += 1

    return result
```

---

### スコープと環境の動作

#### ローカルスコープ

関数内で定義された変数は、関数のローカル環境に格納されます。

```yui
factorial = 入力 n に対し {
    temp = 差(n, 1)  # temp はローカル変数
    temp が答え
}
# temp は関数外からアクセスできない
```

**Python対応:**
```python
def factorial(n):
    temp = n - 1  # ローカル変数
    return temp
# temp は関数外からアクセスできない
```

#### 再帰とクロージャ

関数は自身を参照できます（再帰）。

```yui
factorial = 入力 n に対し {
    もし n が 1 以下 ならば、{
        1が答え
    }
    そうでなければ {
        prev = 差(n, 1)
        積(n, factorial(prev))が答え  # 自身を参照
    }
}
```

意味論的には、`factorial` は環境 `ρ` に含まれており、関数本体内から `ρ(factorial)` として参照できます。

---

### 意味論的等価性

以下のYuiコードとPythonコードは意味論的に等価です：

#### 例1: ループ

```yui
# Yui
i = 0
10回、くり返す {
    iを増やす
}
```

```python
# Python
i = 0
for _ in range(10):
    i += 1
```

#### 例2: 条件分岐

```yui
# Yui
もし x が 0 より大きいならば、{
    result = "positive"
}
そうでなければ {
    result = "non-positive"
}
```

```python
# Python
if x > 0:
    result = [112, 111, 115, 105, 116, 105, 118, 101]  # "positive"
else:
    result = [110, 111, 110, 45, 112, 111, 115, 105, 116, 105, 118, 101]  # "non-positive"
```

#### 例3: 配列操作

```yui
# Yui
result = []
numbers = [1, 2, 3]
length = |numbers|
i = 0
length回、くり返す {
    resultの末尾に numbers[i] を 追加する
    iを増やす
}
```

```python
# Python
result = []
numbers = [1, 2, 3]
length = len(numbers)
i = 0
for _ in range(length):
    result.append(numbers[i])
    i += 1
```

---

### まとめ

Yui言語の表示的意味論は、以下の特徴を持ちます：

1. **環境ベース**: すべての変数は環境 `ρ` に格納される
2. **値の統一**: すべての値は Python の型として表現可能
3. **文字列の特殊性**: 文字列は整数のリストとして扱われる
4. **関数型的**: 関数は第一級オブジェクト
5. **命令型的**: 代入、ループ、条件分岐などの命令型構文を持つ

この意味論を理解することで：
- Yui言語のインタプリタを正確に実装できる
- Yui→Python のトランスパイラを作成できる
- プログラムの正当性を形式的に証明できる

すべてのYui言語の構文要素は、対応するPythonコードとして明確に定義されています。
