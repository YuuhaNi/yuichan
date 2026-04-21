### 問題
整数 x の絶対値を返す関数 absolute_value を実装してください。

実行例
>>> absolute_value(-5)
5
>>> absolute_value(3)
3
>>> absolute_value(0)
0

### 回答
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
{PROBLEM}



