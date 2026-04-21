## Yui Language Survival Guide for Python Programmers

**5分でYuiを理解する** - Pythonプログラマーのための最速ガイド

## TL;DR (超クイックスタート)

```python
# Python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

```yui
# Yui
標準ライブラリを使う

factorial = 入力 n に対し {
    もし n が 1 以下 ならば {
        1が答え
    }
    そうでなければ {
        prev = 差(n, 1)
        積(n, factorial(prev))が答え
    }
}

>>> factorial(5)
120
```

**重要な違い**:
- 四則演算は関数呼び出し: `a + b` → `和(a, b)`
- ブロックは `{` で始まり、**必ず改行**が必要
- テストケースは `>>>` で書く（doctest風）

---

## データ型の対比

### 基本型

| Python | Yui | 備考 |
|--------|-----|------|
| `x = 42` | `x = 42` | 整数 |
| `x = 3.14` | `x = 3.14` | 浮動小数点数 |
| `x = True` | `x = 1` | 真偽値は 1/0 |
| `x = False` | `x = 0` | 真偽値は 1/0 |
| `x = "Hello"` | `x = "Hello"` | 文字列（内部は文字コード配列） |
| `x = 'A'` | `x = "A"[0]` | 文字コード（65） |

### コレクション

```python
# Python
nums = [1, 2, 3]
matrix = [[1, 2], [3, 4]]
text = "ABC"
```

```yui
# Yui
nums = [1, 2, 3]
matrix = [[1, 2], [3, 4]]
text = "ABC"  # 内部は [65, 66, 67]
```

**重要**: Yuiの文字列は**ミュータブル**（変更可能）

```python
# Python
s = "ABC"
# s[0] = 'Z'  # エラー！文字列は不変
```

```yui
# Yui
s = "ABC"
s[0] = "Z"[0]  # OK！ → "ZBC"
```

---

## 制御構造の対比

### 条件分岐

```python
# Python
if x == 1:
    print("one")
elif x == 2:
    print("two")
else:
    print("other")
```

```yui-snippet
# Yui (説明用スニペット - xは事前に定義が必要)
もし x が 1 ならば {
    # one
}
そうでなければ {
    もし x が 2 ならば {
        # two
    }
    そうでなければ {
        # other
    }
}
```

### 比較演算子

| Python | Yui |
|--------|-----|
| `x == 1` | `x が 1` |
| `x != 1` | `x が 1 以外` |
| `x >= 1` | `x が 1 以上` |
| `x <= 1` | `x が 1 以下` |
| `x > 1` | `x が 1 より大きい` |
| `x < 1` | `x が 1 より小さい` |

### ループ

```python
# Python: for loop
for i in range(10):
    print(i)
```

```yui
# Yui: 固定回数ループ
i = 0
10回、くり返す {
    # iを使った処理
    iを増やす
}
```

```python
# Python: while loop
while x < 10:
    x += 1
```

```yui-snippet
# Yui: 十分大きい回数でループ (説明用 - xは事前に定義が必要)
1000回、くり返す {
    もし x が 10 より小さい ならば {
        xを増やす
    }
}
```

**重要**: Yuiには `while` がない。十分大きい回数でループして条件チェック。

### Break文

```python
# Python
for i in range(100):
    if i == 5:
        break
```

```yui
# Yui
i = 0
100回、くり返す {
    もし i が 5 ならば {
        くり返しを抜ける
    }
    iを増やす
}
```

---

## 関数定義の対比

```python
# Python
def add(x, y):
    return x + y

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def get_answer():
    return 42
```

```yui
# Yui
標準ライブラリを使う

add = 入力 x, y に対し {
    和(x, y)が答え
}

factorial = 入力 n に対し {
    もし n が 1 以下 ならば {
        1が答え
    }
    そうでなければ {
        prev = 差(n, 1)
        積(n, factorial(prev))が答え
    }
}

get_answer = 入力なしに対し {
    42が答え
}
```

**Yuiの関数定義パターン**:
```yui-snippet
# 引数ありの関数 (説明用パターン)
関数名 = 入力 引数1, 引数2 に対し {
    # 処理
    戻り値 が答え
}

# 引数なしの関数 (説明用パターン)
関数名 = 入力なしに対し {
    # 処理
    戻り値 が答え
}
```

---

## 演算子の変換表

### 算術演算

| Python | Yui | 備考 |
|--------|-----|------|
| `a + b` | `和(a, b)` | 可変長引数: `和(a, b, c)` |
| `a - b` | `差(a, b)` | |
| `a * b` | `積(a, b)` | 可変長引数: `積(a, b, c)` |
| `a / b` | `商(a, b)` | 整数÷整数=整数（切り捨て） |
| `a % b` | `剰余(a, b)` | |
| `abs(a)` | `絶対値(a)` | |
| `max(a, b)` | `最大値(a, b)` | 可変長引数 |
| `min(a, b)` | `最小値(a, b)` | 可変長引数 |

### 型変換・判定

| Python | Yui |
|--------|-----|
| `int(x)` | `整数化(x)` |
| `float(x)` | `少数化(x)` |
| `str(x)` | `文字列化(x)` |
| `isinstance(x, int)` | `整数判定(x)` |
| `isinstance(x, float)` | `少数判定(x)` |
| `isinstance(x, str)` | `文字列判定(x)` |

### ビット演算

| Python | Yui |
|--------|-----|
| `a & b` | `論理積(a, b)` |
| `a \| b` | `論理和(a, b)` |
| `a ^ b` | `排他的論理和(a, b)` |
| `~a` | `ビット反転(a)` |
| `a << b` | `左シフト(a, b)` |
| `a >> b` | `右シフト(a, b)` |

### インクリメント・デクリメント

| Python | Yui |
|--------|-----|
| `x += 1` | `xを増やす` |
| `x -= 1` | `xを減らす` |
| `arr[i] += 1` | `arr[i]を増やす` |

---

## よくあるPythonパターン

### リスト内包表記 → ループ

```python
# Python
squares = [x**2 for x in range(10)]
```

```yui
# Yui
標準ライブラリを使う

squares = []
x = 0
10回、くり返す {
    sq = 積(x, x)
    squaresの末尾に sq を 追加する
    xを増やす
}
```

### filter → 条件付きappend

```python
# Python
evens = [x for x in range(10) if x % 2 == 0]
```

```yui
# Yui
標準ライブラリを使う

evens = []
x = 0
10回、くり返す {
    rem = 剰余(x, 2)
    もし rem が 0 ならば {
        evensの末尾に x を 追加する
    }
    xを増やす
}
```

### map → ループで変換

```python
# Python
doubled = list(map(lambda x: x * 2, nums))
```

```yui-snippet
# Yui (説明用 - numsは事前に定義が必要)
標準ライブラリを使う

doubled = []
i = 0
nums_len = |nums|
nums_len回、くり返す {
    val = nums[i]
    doubled_val = 積(val, 2)
    doubledの末尾に doubled_val を 追加する
    iを増やす
}
```

### enumerate → インデックスカウンター

```python
# Python
for i, val in enumerate(arr):
    print(f"{i}: {val}")
```

```yui-snippet
# Yui (説明用 - arrは事前に定義が必要)
i = 0
arr_len = |arr|
arr_len回、くり返す {
    val = arr[i]
    # i と val を使った処理
    iを増やす
}
```

### 文字列の連結

```python
# Python
result = "Hello" + " " + "World"
```

```yui
# Yui
result = "Hello"
resultの末尾に 32 を 追加する  # スペース
world = "World"
resultの末尾に world[0] を 追加する  # W
resultの末尾に world[1] を 追加する  # o
resultの末尾に world[2] を 追加する  # r
resultの末尾に world[3] を 追加する  # l
resultの末尾に world[4] を 追加する  # d
# または
i = 0
5回、くり返す {
    resultの末尾に world[i] を 追加する
    iを増やす
}
```

### スライス → ループでコピー

```python
# Python
sub = arr[2:5]
```

```yui-snippet
# Yui (説明用 - arrは事前に定義が必要)
sub = []
i = 2
3回、くり返す {  # 5 - 2 = 3
    subの末尾に arr[i] を 追加する
    iを増やす
}
```

---

## 標準ライブラリ

### 必須のインポート

```yui
標準ライブラリを使う
```

算術関数を使う前に**必ず**記述！

### 可変長引数

```python
# Python
sum([1, 2, 3, 4, 5])  # 15
```

```yui
# Yui - 2つの方法
標準ライブラリを使う

# 方法1: 可変長引数（推奨）
sum = 和(1, 2, 3, 4, 5)

# 方法2: 配列を渡す
nums = [1, 2, 3, 4, 5]
sum = 和(nums)
```

### よく使う関数

```yui
標準ライブラリを使う

# 算術
sum = 和(1, 2, 3, 4, 5)        # 15
diff = 差(10, 3)                # 7
prod = 積(2, 3, 4)              # 24
quot = 商(7, 2)                 # 3 (整数除算)
quot_f = 商(7.0, 2.0)           # 3.5 (浮動小数点除算)
rem = 剰余(17, 5)               # 2

# 比較・統計
max_val = 最大値(5, 2, 8, 1)    # 8
min_val = 最小値(5, 2, 8, 1)    # 1
abs_val = 絶対値(-5)            # 5

# 型変換
n = 整数化("123")               # 123
n = 整数化(1.7)                 # 1
f = 少数化(5)                   # 5.0
s = 文字列化(123)               # "123"

# 型判定
is_int = 整数判定(42)           # 1 (True)
is_float = 少数判定(3.14)       # 1 (True)
is_str = 文字列判定("hello")    # 1 (True)

# その他
rand = 乱数生成()               # 0.0 ~ 1.0
```

---

## 落とし穴と回避策

### 1. 演算子を使わない

```yui-snippet
# ❌ NG (構文エラー)
x = a + b

# ✅ OK
標準ライブラリを使う
x = 和(a, b)
```

### 2. ブロックの後は必ず改行

```yui-snippet
# ❌ NG (構文エラー)
もし x が 1 ならば { xを増やす }

# ✅ OK
もし x が 1 ならば {
    xを増やす
}
```

### 3. while ループは存在しない

```yui-snippet
# ❌ NG (構文エラー)
while x < 10:
    x += 1

# ✅ OK - 十分大きい回数でループ (xは事前に定義が必要)
1000回、くり返す {
    もし x が 10 より小さい ならば {
        xを増やす
    }
}
```

### 4. リスト内包表記は使えない

```python
# Python
squares = [x**2 for x in range(10)]
```

```yui
# Yui - ループで構築
標準ライブラリを使う

squares = []
x = 0
10回、くり返す {
    sq = 積(x, x)
    squaresの末尾に sq を 追加する
    xを増やす
}
```

### 5. 浮動小数点演算は明示的に

```yui
標準ライブラリを使う

# ❌ 整数除算 (切り捨て)
avg = 商(10, 3)  # 3

# ✅ 浮動小数点除算
avg = 商(少数化(10), 少数化(3))  # 3.333...
# または
avg = 商(10.0, 3.0)
```

### 6. 配列の長さは変数に保存

```yui-snippet
# ❌ 毎回計算するのは非効率 (arrは事前に定義が必要)
10回、くり返す {
    length = |arr|  # 毎回計算
}

# ✅ 事前に計算 (arrは事前に定義が必要)
length = |arr|
length回、くり返す {
    # ...
}
```

