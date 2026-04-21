### 問題

整数 x の絶対値を返す関数 absolute_value を実装してください。

実行例
>>> absolute_value(-5)
5
>>> absolute_value(3)
3
>>> absolute_value(0)
0

### 回答:
```yui
標準ライブラリを使う

absolute_value = 入力 x に対し {
    もし x が 0 より小さい ならば {
        result = 0
        result = 差(result, x)
        resultが答え
    }
    そうでなければ {
        xが答え
    }
}
```

### 問題 

整数配列 arr の最大値を返す関数 find_max を実装してください。
配列が空の場合は 0 を返します。

実行例
>>> find_max([5, 2, 8, 1, 9])
9
>>> find_max([1])
1
>>> find_max([])
0

### 回答
```yui
標準ライブラリを使う

find_max = 入力 arr に対し {
    length = |arr|
    もし length が 0 ならば {
        0が答え
    }
    そうでなければ {
        max_val = arr[0]
        i = 1
        times = 差(length, 1)
        times回、くり返す {
            もし arr[i] が max_val より大きい ならば {
                max_val = arr[i]
            }
            iを増やす
        }
        max_valが答え
    }
}
```

### 問題 
整数配列 nums から偶数のみを抽出した新しい配列を返す関数 filter_evens を実装してください。

実行例
>>> filter_evens([1, 2, 3, 4, 5, 6])
[2, 4, 6]
>>> filter_evens([1, 3, 5])
[]
>>> filter_evens([])
[]

### 回答
```yui
標準ライブラリを使う

filter_evens = 入力 nums に対し {
    evens = []
    length = |nums|
    i = 0
    length回、くり返す {
        rem = 剰余(nums[i], 2)
        もし rem が 0 ならば {
            evensの末尾に nums[i] を 追加する
        }
        iを増やす
    }
    evensが答え
}
```

### 問題
文字列 text の英大文字を英小文字に変換するto_lowerを定義してください。

実行例
>>> to_lower("Hello World")
"hello world"

### 回答
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
```



### 問題 
{PROBLEM}

