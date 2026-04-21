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
{PROBLEM}


