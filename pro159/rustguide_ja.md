# Yui プログラミングガイド（Rust ユーザ向け）

Yui は日本語で書ける教育用プログラミング言語です。
本ガイドでは、各機能を **まず Rust で示し、同じ処理を Yui でどう書くか** を対比しながら紹介します。
Rust にある概念・ない概念の両方を明確にすることで、Rust 経験者がすばやく Yui を習得できるようにします。

---

## 1. はじめてのプログラム

Rust の `println!` に相当する「式を単独で書くとその値が表示される」動作が Yui にもあります。

**Rust**

```rust
fn main() {
    println!("Hello, world!");
}
```

**Yui**

```yui
# "Hello, world!" と表示する
"Hello, world!"
```

- Yui では、代入・制御文以外の**単独の式**は自動的に印字されます（REPL 的挙動）。
- 行頭から `#`（または `＃`）以降はコメントです。
- `fn main()` のようなエントリーポイントは不要です。

---

## 2. 変数と増減

**Rust**

```rust
fn main() {
    let mut x = 1;
    let mut y = -2;
    x += 1;
    y -= 1;
    assert_eq!(x, 2);
    assert_eq!(y, -3);
}
```

**Yui**

```yui
x = 1
y = -2
xを増やす
yを減らす

>>> x
2
>>> y
-3
```

- Yui の `>>> 式` + 期待値は Rust の `assert_eq!` と同様で、プログラム内にテストを埋め込めます。
- `xを増やす` は `x += 1` に、`yを減らす` は `y -= 1` に相当します。
- Yui には `let` や `mut` のような宣言は不要です。変数は代入時に自動的に作成されます。

---

## 3. 型とリテラル

Rust と Yui の型の対応は以下のとおりです。

| Rust | Yui | Yui リテラル |
|------|-----|----------|
| `()` / `Option::None` | ヌル | `値なし` |
| `bool` | 論理値 | `真` / `偽` |
| `i64` | 整数 | `42` |
| `f64` | 小数 | `3.14`（表示は小数点以下 6 桁固定） |
| `String` / `&str` | 文字列 | `"あ"` |
| `Vec<T>` | 配列 | `[1, 2, 3]` |
| `HashMap<String, T>` | オブジェクト | `{"x": 1, "y": 2}` |

注意点:

- Yui は**動的型付け**です。型宣言は不要で、同じ変数に異なる型の値を代入できます。
- Yui の **文字列は内部的に文字コード（int）の配列**です。`Vec` と同じ操作（要素追加・長さ取得）が使えます。
- Yui の小数は表示上、常に 6 桁の小数点以下が付きます（`3.000000`）。
- 所有権・借用・ライフタイムの概念はありません。

---

## 4. 文字列補間

**Rust**

```rust
fn main() {
    let name = "ゆい";
    let age = 12;
    let msg = format!("こんにちは、{}さん！あなたは{}歳です。", name, age);
    assert_eq!(msg, "こんにちは、ゆいさん！あなたは12歳です。");
}
```

**Yui**

```yui
name = "ゆい"
age  = 12
msg  = "こんにちは、{name}さん！あなたは{age}歳です。"

>>> msg
"こんにちは、ゆいさん！あなたは12歳です。"
```

- Rust の `format!` マクロのような特別な構文は不要です。**通常の文字列に `{変数名}` を書けば展開されます**。
- `{` や `"` を文字として書きたいときは `\{` `\"`。`\\`, `\n`, `\t` も使えます。

---

## 5. 配列（ベクタ）

**Rust**

```rust
fn main() {
    let mut a = vec![1, 2, 3];
    a.push(0);
    a[0] += 1;
    if a.contains(&2) {
        a[0] = a[3];
    }
    assert_eq!(a.len(), 4);
}
```

**Yui**

```yui
A = [1, 2, 3]
Aに0を追加する
A[0]を増やす
もし2がAのいずれかならば{
   A[0] = A[3]
}

>>> Aの大きさ
4
```

対応表:

| Rust | Yui |
|------|-----|
| `a.push(x)` | `Aにxを追加する` |
| `a.len()` | `Aの大きさ` |
| `a[i]` | `A[i]`（同じ） |
| `a.contains(&x)` | `もしxがAのいずれかならば` |
| `!a.contains(&x)` | `もしxがAのいずれでもないならば` |

### 5.1 インデックスと長さ

**Rust**

```rust
fn main() {
    let mut a = vec![10, 20, 30];
    let n = a.len();
    let first = a[0];
    let last = a[n - 1];
    a[1] = 200;
}
```

**Yui**

```yui
標準ライブラリを使う
A = [10, 20, 30]
n = Aの大きさ
first = A[0]
last  = A[差(n,1)]
A[1] = 200
```

- Yui には `-` の中置演算がないため、`n - 1` は `差(n, 1)` と書きます。

---

## 6. オブジェクト（ハッシュマップ）

**Rust**

```rust
use std::collections::HashMap;

fn main() {
    let mut o: HashMap<&str, i32> = HashMap::new();
    o.insert("x", 0);
    o.insert("y", 0);
    o.insert("x", 1);
    o.insert("y", 2);
    assert_eq!(o.get("x"), Some(&1));
}
```

**Yui**

```yui
O = {"x": 0, "y": 0}
O["x"] = 1
O["y"] = 2

>>> O["x"]
1
```

- Yui のオブジェクトは JSON 風のリテラルで簡潔に書けます。
- キーは文字列を使います。

---

## 7. 文字列は配列

Rust では `String` と `Vec<u8>` は別物ですが、Yui では文字列 = 文字コード配列です。

**Rust**

```rust
fn main() {
    let mut s: Vec<char> = "hello".chars().collect();
    s[0] = 'H';
    for c in " world".chars() {
        s.push(c);
    }
    let result: String = s.into_iter().collect();
    assert_eq!(result, "Hello world");
}
```

**Yui**

```yui
s = "hello"
s[0] = "H"[0]

t = " world"
i = 0
tの大きさ回くり返す{
   sにt[i]を追加する
   iを増やす
}

>>> s
"Hello world"
```

- `"H"[0]` は文字コードで、配列の要素と同じ型です。
- Rust の `chars()` や `collect()` のような変換は不要です。

---

## 8. 条件分岐

**Rust**

```rust
fn main() {
    let flag = true;
    let result = if flag { 1 } else { 2 };
    assert_eq!(result, 1);
}
```

**Yui**

```yui
flag   = 真
result = 0
もしflagが真ならば{
   result = 1
}
そうでなければ{
   result = 2
}
```

### 8.1 比較演算子 → 接尾辞

Yui は `==` `!=` `<` `>` などの**記号を使いません**。`もし A が B <接尾辞> ならば` と書きます。

| Rust | Yui |
|------|-----|
| `a == b` | `もしaがbならば` |
| `a != b` | `もしaがb以外ならば` |
| `a < b`  | `もしaがbより小さいならば` |
| `a > b`  | `もしaがbより大きいならば` |
| `a <= b` | `もしaがb以下ならば` |
| `a >= b` | `もしaがb以上ならば` |
| `xs.contains(&a)` | `もしaがxsのいずれかならば` |
| `!xs.contains(&a)` | `もしaがxsのいずれでもないならば` |

**Rust**

```rust
fn main() {
    let fruits = vec!["apple", "banana", "cherry"];
    let found = if fruits.contains(&"banana") { 1 } else { 0 };
    let missing = if !fruits.contains(&"grape") { 1 } else { 0 };
}
```

**Yui**

```yui
fruits = ["apple", "banana", "cherry"]
found   = 0
missing = 0
もし"banana"がfruitsのいずれかならば{ foundを増やす }
もし"grape"がfruitsのいずれでもないならば{ missingを増やす }
```

### 8.2 多段分岐

Yui には `else if` がありません。`そうでなければ { もし ... }` をネストします。

---

## 9. 繰り返し

Yui のループは **回数指定の `N回くり返す`** のみです。`while` や `for x in xs` はありません。

**Rust**

```rust
fn main() {
    let mut count = 0;
    for _ in 0..10 {
        count += 1;
        if count == 5 {
            break;
        }
    }
    assert_eq!(count, 5);
}
```

**Yui**

```yui
count = 0
10回くり返す{
   countを増やす
   もしcountが5ならば{
      くり返しを抜ける
   }
}

>>> count
5
```

| Rust | Yui |
|------|-----|
| `for _ in 0..N { }` | `N回くり返す{ ... }` |
| `break` | `くり返しを抜ける` |

配列の全要素に順にアクセスしたいときは、インデックス変数を自分で増やします（`7. 文字列は配列` の例を参照）。

---

## 10. 関数

### 10.1 定義と戻り値

**Rust**

```rust
fn succ(n: i32) -> i32 {
    n + 1
}

fn main() {
    assert_eq!(succ(0), 1);
}
```

**Yui**

```yui
標準ライブラリを使う

succ = 入力nに対し{
   nを増やす
   nが答え
}

>>> succ(0)
1
```

| Rust | Yui |
|------|-----|
| `fn f(a: T, b: U) -> R` | `f = 入力 a, b に対し { ... }` |
| `fn f() -> R` | `f = 入力なしに対し { ... }` |
| `return x` / 末尾式 | `xが答え` |

- 型注釈は不要です。
- 関数内で作った変数は**ローカルスコープ**（Rust と同じ）。

### 10.2 暗黙の戻り値（構造体風）

Rust では戻り値の型を明示しますが、Yui では**戻り値を書かないとローカル変数をまとめたオブジェクトが返ります**。
Rust の構造体のように使えます。

**Rust**

```rust
struct Point {
    x: i32,
    y: i32,
}

fn point(x: i32, y: i32) -> Point {
    Point { x, y }
}

fn main() {
    let o = point(3, 5);
    assert_eq!(o.x, 3);
}
```

**Yui**

```yui
point = 入力x,yに対し{
   # 何も返さない → {"x": ..., "y": ...} が返る
}
O = point(3, 5)

>>> O["x"]
3
```

### 10.3 再帰

**Rust**

```rust
fn fact(n: i64) -> i64 {
    if n == 0 {
        1
    } else {
        n * fact(n - 1)
    }
}

fn main() {
    assert_eq!(fact(5), 120);
}
```

**Yui**

```yui
標準ライブラリを使う

fact = 入力nに対し{
   もしnが0ならば{
      1が答え
   }
   そうでなければ{
      積(n, fact(差(n,1)))が答え
   }
}

>>> fact(5)
120
```

Yui には `*` `-` の中置演算がないので、`積` `差` を使います。

---

## 11. 標準ライブラリ

Rust は演算子やトレイトが豊富ですが、Yui は**記号を使わず、関数で演算する**のが特徴です。
ソース先頭で `標準ライブラリを使う` と宣言してから関数を呼びます。

### 11.1 四則演算

| Rust | Yui |
|------|-----|
| `a + b + c` | `和(a, b, c)`（配列も可: `和([a,b,c])`） |
| `a - b` | `差(a, b)` |
| `a * b` | `積(a, b)` |
| `a / b`（整数除算） | `商(a, b)` |
| `a % b` | `剰余(a, b)` |

**Rust**

```rust
fn gcd(mut a: i64, mut b: i64) -> i64 {
    while b != 0 {
        let r = a % b;
        a = b;
        b = r;
    }
    a
}

fn main() {
    assert_eq!(gcd(12, 18), 6);
}
```

**Yui**

```yui
標準ライブラリを使う

gcd = 入力a,bに対し{
   a回くり返す{
      もしbが0ならば{
         くり返しを抜ける
      }
      r = 剰余(a, b)
      a = b
      b = r
   }
   aが答え
}

>>> gcd(12, 18)
6
```

Yui には `while` がないので、**十分大きい回数のループ + break** で `while` を模倣します。

### 11.2 数学関数

| Rust | Yui |
|------|-----|
| `x.abs()` / `i64::abs(x)` | `絶対値(x)` |
| `(x as f64).sqrt()` | `平方根(x)` |
| `std::cmp::max(a, b)` | `最大値(a, b, ...)` / `最大値(xs)` |
| `std::cmp::min(a, b)` | `最小値(a, b, ...)` / `最小値(xs)` |
| `rand::random::<f64>()` | `乱数()` |

**Rust**

```rust
fn main() {
    assert_eq!((-7_i64).abs(), 7);
    assert_eq!(std::cmp::max(3, 5), 5);
}
```

**Yui**

```yui
標準ライブラリを使う

>>> 絶対値(-7)
7
>>> 平方根(9)
3.000000
>>> 最大値(3, 1, 4, 1, 5)
5
>>> 最小値([10, 20, 30])
10
```

### 11.3 型変換

| Rust | Yui |
|------|-----|
| `x as i64` / `x.parse::<i64>()` | `整数化(x)` |
| `x as f64` | `小数化(x)` |
| `x.to_string()` / `format!("{}", x)` | `文字列化(x)` |
| `s.bytes().collect()` | `配列化(x)` |

**Rust**

```rust
fn main() {
    assert_eq!("42".parse::<i64>().unwrap(), 42);
    assert_eq!(3.7_f64 as i64, 3);
    assert_eq!(42.to_string(), "42");
}
```

**Yui**

```yui
標準ライブラリを使う

>>> 整数化("42")
42
>>> 整数化(3.700000)
3
>>> 文字列化(42)
"42"
>>> 配列化("Hi")
[72,105]
```

### 11.4 型判定

| Rust | Yui |
|------|-----|
| `TypeId::of::<bool>()` 比較 | `ブール判定(x)` |
| `TypeId::of::<i64>()` 比較 | `整数判定(x)` |
| `TypeId::of::<f64>()` 比較 | `小数判定(x)` |
| `TypeId::of::<String>()` 比較 | `文字列判定(x)` |
| `TypeId::of::<Vec<_>>()` 比較 | `配列判定(x)` |
| `TypeId::of::<HashMap<_,_>>()` 比較 | `オブジェクト判定(x)` |

Rust では静的型なので実行時の型判定は稀ですが、Yui は動的型なので型判定関数があります。

```yui
標準ライブラリを使う

>>> 整数判定(42)
真
>>> 文字列判定("hello")
真
>>> 整数判定("42")
偽
```

---

## 12. 総合例: FizzBuzz

**Rust**

```rust
fn main() {
    let mut result: Vec<String> = Vec::new();
    for i in 1..=100 {
        if i % 15 == 0 {
            result.push("FizzBuzz".to_string());
        } else if i % 3 == 0 {
            result.push("Fizz".to_string());
        } else if i % 5 == 0 {
            result.push("Buzz".to_string());
        } else {
            result.push(i.to_string());
        }
    }
    assert_eq!(result.len(), 100);
}
```

**Yui**

剰余を使わずにカウンタで Fizz/Buzz を判定できます。

```yui
result = []
i    = 0
fizz = 0
buzz = 0

100回くり返す{
   iを増やす
   fizzを増やす
   buzzを増やす
   もしfizzが3ならば{ fizz = 0 }
   もしbuzzが5ならば{ buzz = 0 }

   もしfizzが0ならば{
      もしbuzzが0ならば{
         resultに"FizzBuzz"を追加する
      }そうでなければ{
         resultに"Fizz"を追加する
      }
   }そうでなければ{
      もしbuzzが0ならば{
         resultに"Buzz"を追加する
      }そうでなければ{
         resultにiを追加する
      }
   }
}

>>> resultの大きさ
100
>>> result[2]
"Fizz"
>>> result[4]
"Buzz"
>>> result[14]
"FizzBuzz"
```

---

## 13. 総合例: モンテカルロ法で π を推定

**Rust**

```rust
use rand::Rng;

fn monte_carlo(n: i64) -> f64 {
    let mut rng = rand::thread_rng();
    let mut hits = 0;
    for _ in 0..n {
        let x: f64 = rng.gen();
        let y: f64 = rng.gen();
        if (x * x + y * y).sqrt() <= 1.0 {
            hits += 1;
        }
    }
    4.0 * hits as f64 / n as f64
}

fn main() {
    println!("{}", monte_carlo(1000));
}
```

**Yui**

```yui
標準ライブラリを使う

monte_carlo = 入力nに対し{
   hits = 0
   n回くり返す{
      x = 乱数()
      y = 乱数()
      dist = 平方根(和(積(x,x), 積(y,y)))
      もしdistが1以下ならば{
         hitsを増やす
      }
   }
   商(積(小数化(hits), 4), 小数化(n))が答え
}

monte_carlo(1000)
```

---

## 14. Rust にあって Yui にないもの（要注意）

Rust 経験者がつまずきやすいポイントです。

- **型宣言・型注釈が無い**: Yui は動的型付けです。`let x: i32` のような宣言は不要。
- **所有権・借用・ライフタイムが無い**: メモリ管理は自動です。`&`, `&mut`, `'a` は存在しません。
- **中置演算子が無い**: `+ - * / % == != < <= > >=` すべて使えません。算術は `和/差/積/商/剰余`、比較は `が〜ならば` 構文で書きます。
- **`while` / `for x in xs` が無い**: `N回くり返す { ... くり返しを抜ける }` のみ。
- **`else if` が無い**: `そうでなければ { もし ... }` をネストして書く。
- **`match` / パターンマッチが無い**: 条件分岐は `もし〜ならば` のみ。
- **ローカルだけの関数本体**: `return` を書かないと**ローカル変数のオブジェクト**が返る（Rust にない挙動）。
- **構造体・enum・トレイト・ジェネリクスは無い**: Yui は教育用の最小構文のみ。
- **エラーハンドリング（Result/Option）が無い**: 例外やパニックの概念もありません。

---

## 15. まとめ

Rust と比較した Yui の特徴は次のとおりです。

- **記号を減らし、日本語の語順で書く**。
- 型宣言・所有権・ライフタイムは不要（動的型付け・自動メモリ管理）。
- 比較は `が〜ならば`、四則演算は `和/差/積/商/剰余`。
- 文字列は文字コード配列で、`Vec` と統一的に扱える。
- 関数は `入力...に対し{ ...が答え }`、戻り値なしはローカル変数を辞書化して返す。
- `>>> 式` と期待値を書くと assert 互換のテストをプログラム内に残せる。

