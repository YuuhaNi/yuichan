## Yui言語 サンプルコード集

Yui言語の主要な機能と書き方を理解するための実践的なサンプルコードです。

### 基礎編

#### 1. Hello World (文字列の返却)

```yui
標準ライブラリを使う

hello = 入力なしに対し {
    "Hello, World!"が答え
}

>>> hello()
"Hello, World!"
```

#### 2. 算術演算の基礎

```yui
標準ライブラリを使う

arithmetic = 入力 a, b に対し {
    sum = 和(a, b)
    diff = 差(a, b)
    prod = 積(a, b)
    quot = 商(a, b)
    rem = 剰余(a, b)

    result = []
    resultの末尾に sum を 追加する
    resultの末尾に diff を 追加する
    resultの末尾に prod を 追加する
    resultの末尾に quot を 追加する
    resultの末尾に rem を 追加する

    resultが答え
}

>>> arithmetic(10, 3)
[13, 7, 30, 3, 1]
```

#### 3. 絶対値の計算

```yui
標準ライブラリを使う

my_abs = 入力 x に対し {
    もし x が 0 より小さいならば、{
        差(0, x)が答え
    }
    そうでなければ {
        xが答え
    }
}

>>> my_abs(-5)
5
>>> my_abs(3)
3
```

---

### 制御構造

#### 4. FizzBuzz

```yui
標準ライブラリを使う

fizzbuzz = 入力 n に対し {
    result = []
    i = 1

    n回、くり返す {
        mod3 = 剰余(i, 3)
        mod5 = 剰余(i, 5)

        もし mod3 が 0 ならば、{
            もし mod5 が 0 ならば、{
                resultの末尾に "FizzBuzz" を 追加する
            }
            そうでなければ {
                resultの末尾に "Fizz" を 追加する
            }
        }
        そうでなければ {
            もし mod5 が 0 ならば、{
                resultの末尾に "Buzz" を 追加する
            }
            そうでなければ {
                resultの末尾に i を 追加する
            }
        }

        iを増やす
    }

    resultが答え
}

>>> fizzbuzz(15)
[1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]
```

#### 5. 最大値と最小値

```yui
標準ライブラリを使う

find_min_max = 入力 numbers に対し {
    length = |numbers|
    もし length が 0 ならば、{
        []が答え
    }

    min_val = numbers[0]
    max_val = numbers[0]

    i = 1
    times = 差(length, 1)
    times回、くり返す {
        current = numbers[i]
        もし current が min_val より小さいならば、{
            min_val = current
        }
        もし current が max_val より大きいならば、{
            max_val = current
        }
        iを増やす
    }

    result = []
    resultの末尾に min_val を 追加する
    resultの末尾に max_val を 追加する
    resultが答え
}

>>> find_min_max([3, 7, 2, 9, 1, 5])
[1, 9]
```

---

### 配列操作

#### 6. 配列の反転

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

>>> reverse([1, 2, 3, 4, 5])
[5, 4, 3, 2, 1]
```

#### 7. 配列のフィルタリング（偶数のみ）

```yui
標準ライブラリを使う

filter_even = 入力 numbers に対し {
    length = |numbers|
    result = []
    i = 0

    length回、くり返す {
        num = numbers[i]
        remainder = 剰余(num, 2)
        もし remainder が 0 ならば、{
            resultの末尾に num を 追加する
        }
        iを増やす
    }

    resultが答え
}

>>> filter_even([1, 2, 3, 4, 5, 6, 7, 8])
[2, 4, 6, 8]
```

#### 8. 配列の合計

```yui
標準ライブラリを使う

array_sum = 入力 numbers に対し {
    length = |numbers|
    sum = 0
    i = 0

    length回、くり返す {
        sum = 和(sum, numbers[i])
        iを増やす
    }

    sumが答え
}

>>> array_sum([1, 2, 3, 4, 5])
15
```

#### 9. 配列の連結

```yui
標準ライブラリを使う

concat = 入力 arr1, arr2 に対し {
    result = []

    len1 = |arr1|
    i = 0
    len1回、くり返す {
        resultの末尾に arr1[i] を 追加する
        iを増やす
    }

    len2 = |arr2|
    i = 0
    len2回、くり返す {
        resultの末尾に arr2[i] を 追加する
        iを増やす
    }

    resultが答え
}

>>> concat([1, 2, 3], [4, 5, 6])
[1, 2, 3, 4, 5, 6]
```

---

### 文字列処理

#### 10. 文字列の長さ

```yui
標準ライブラリを使う

string_length = 入力 text に対し {
    |text|が答え
}

>>> string_length("Hello")
5
```

#### 11. 文字列の連結

```yui
標準ライブラリを使う

string_concat = 入力 str1, str2 に対し {
    result = []

    len1 = |str1|
    i = 0
    len1回、くり返す {
        resultの末尾に str1[i] を 追加する
        iを増やす
    }

    len2 = |str2|
    i = 0
    len2回、くり返す {
        resultの末尾に str2[i] を 追加する
        iを増やす
    }

    resultが答え
}

>>> string_concat("Hello", "World")
"HelloWorld"
```

#### 12. 回文判定

```yui
標準ライブラリを使う

is_palindrome = 入力 text に対し {
    length = |text|
    half = 商(length, 2)
    i = 0

    half回、くり返す {
        right_idx = 差(差(length, i), 1)
        もし text[i] が text[right_idx] と異なるならば、{
            0が答え
        }
        iを増やす
    }

    1が答え
}

>>> is_palindrome("racecar")
1
>>> is_palindrome("hello")
0
```

#### 13. 文字カウント

```yui
標準ライブラリを使う

count_char = 入力 text, target に対し {
    target_code = target[0]
    length = |text|
    count = 0
    i = 0

    length回、くり返す {
        もし text[i] が target_code ならば、{
            countを増やす
        }
        iを増やす
    }

    countが答え
}

>>> count_char("hello world", "l")
3
```

#### 14. 大文字を小文字に変換

```yui
標準ライブラリを使う

to_lower = 入力 text に対し {
    length = |text|
    result = []
    i = 0

    length回、くり返す {
        char = text[i]
        # 'A'(65) ~ 'Z'(90)
        もし char が 64 より大きいならば、{
            もし char が 91 より小さいならば、{
                # Convert to lowercase by adding 32
                char = 和(char, 32)
            }
        }
        resultの末尾に char を 追加する
        iを増やす
    }

    resultが答え
}

>>> to_lower("Hello World")
"hello world"
```

### 型変換と型判定

### 15. 型判定の例

```yui
標準ライブラリを使う

get_type = 入力 value に対し {
    is_int = 整数判定(value)
    もし is_int が 1 ならば、{
        "integer"が答え
    }

    is_float = 少数判定(value)
    もし is_float が 1 ならば、{
        "float"が答え
    }

    is_str = 文字列判定(value)
    もし is_str が 1 ならば、{
        "string"が答え
    }

    "unknown"が答え
}

>>> get_type(42)
"integer"
>>> get_type(3.14)
"float"
>>> get_type("hello")
"string"
```

#### 16. 型変換の例

```yui
標準ライブラリを使う

convert_types = 入力 value に対し {
    as_int = 整数化(value)
    as_float = 少数化(value)
    as_str = 文字列化(value)

    result = []
    resultの末尾に as_int を 追加する
    resultの末尾に as_float を 追加する
    resultの末尾に as_str を 追加する

    resultが答え
}

>>> convert_types(42)
[42, 42.0, "42"]
```

---

### ビット演算

#### 17. ビット演算の基礎

```yui
標準ライブラリを使う

bit_operations = 入力 a, b に対し {
    and_result = 論理積(a, b)
    or_result = 論理和(a, b)
    xor_result = 排他的論理和(a, b)
    not_a = ビット反転(a)
    left = 左シフト(a, 2)
    right = 右シフト(a, 2)

    result = []
    resultの末尾に and_result を 追加する
    resultの末尾に or_result を 追加する
    resultの末尾に xor_result を 追加する
    resultの末尾に 剰余(not_a, 256) を 追加する
    resultの末尾に left を 追加する
    resultの末尾に right を 追加する

    resultが答え
}

>>> bit_operations(12, 10)
[8, 14, 6, 243, 48, 3]
```

#### 18. ビットカウント（1の個数）

```yui
標準ライブラリを使う

count_bits = 入力 n に対し {
    count = 0
    i = 0

    32回、くり返す {
        bit = 論理積(n, 1)
        もし bit が 1 ならば、{
            countを増やす
        }
        n = 右シフト(n, 1)
        iを増やす
    }

    countが答え
}

>>> count_bits(7)
3
>>> count_bits(15)
4
```
