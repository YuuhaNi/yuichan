```yui
標準ライブラリを使う
# 複利計算
#
# 元本 P を年利 r で n 年運用したときの最終金額は、いわゆる複利の公式で
#   A は P と (1+r) の n 乗の積
# になる。yui には べき乗 が無いので、毎年 balance を (1+r) 倍するループで実装する。
#
# 利率 r は小数で渡す (例: 5% なら 0.05)。
# 結果は小数で返る。

# === 1. n 年後の元利合計 ===
compound=入力P,r,nに対し{
   balance=小数化(P)
   factor=和(小数化(1),r)
   n回くり返す{
      balance=積(balance,factor)
   }
   balanceが答え
}

# === 2. 元本が 2 倍になるのに何年かかるか (年単位の切り上げ) ===
# 利率 r で運用したとき、balance が初めて元本の 2 倍以上になる年を返す
years_to_double=入力rに対し{
   balance=小数化(1)
   factor=和(小数化(1),r)
   n=0
   # 念のため上限 1000 年でガード
   1000回くり返す{
      もしbalanceが2以上ならば{
         くり返しを抜ける
      }
      balance=積(balance,factor)
      nを増やす
   }
   nが答え
}

# === テスト: 1 年目 ===
>>> compound(1000,0.05,1)
1050.000000
# === テスト: 2 年目 (1000 × 1.05 × 1.05) ===
>>> compound(1000,0.05,2)
1102.500000
# === テスト: 3 年目 (1.10 を 3 回かける) ===
>>> compound(1000,0.10,3)
1331.000000
# === テスト: 利率 0 なら元本のまま ===
>>> compound(100,0.0,5)
100.000000
# === テスト: 0 年なら元本のまま ===
>>> compound(1000,0.05,0)
1000.000000

# === テスト: 年利 10 パーセントなら、8 年目に元本が 2 倍を超える ===
>>> years_to_double(0.10)
8
# === テスト: 年利 7 パーセントなら 11 年 ===
>>> years_to_double(0.07)
11
# === テスト: 年利 5 パーセントなら 15 年 (いわゆる 72 の法則) ===
>>> years_to_double(0.05)
15
```

```yui
# ビット加算: 1 ビット全加算器を桁上がり c と共に繰り返して整数の和を求める
# Yui では整数が内部的に 2 進数のビット配列 (LSB 先頭) として保持される。
# そのため a[i] で i ビット目が取れ、aの大きさ でビット長が得られる。
#
# 例: 6 は二進で 110 → [0, 1, 1] (LSB 先頭)
#     6[0] = 0, 6[1] = 1, 6[2] = 1, 6の大きさ = 3
#
# 各桁で a + b + c の和 sum を見て、出力 x と次の桁上がり c を決める。
#   sum=0: x=0 c=0     sum=1: x=1 c=0
#   sum=2: x=0 c=1     sum=3: x=1 c=1
# 桁あふれに備えて、長い方の長さに +1 して走査する。
bits_add=入力A,Bに対し{
   max=Aの大きさ
   もしBの大きさがmaxより大きいならば{
      max=Bの大きさ
   }
   maxを増やす
   c=0
   X=0
   index=0
   max回くり返す{
      もしindexがAの大きさより小さいならば{
         a=A[index]
      }
      そうでなければ{
         a=0
      }
      もしindexがBの大きさより小さいならば{
         b=B[index]
      }
      そうでなければ{
         b=0
      }
      sum=0
      もしaが1ならば{
         sumを増やす
      }
      もしbが1ならば{
         sumを増やす
      }
      もしcが1ならば{
         sumを増やす
      }
      もしsumが0ならば{
         x=0
         c=0
      }
      もしsumが1ならば{
         x=1
         c=0
      }
      もしsumが2ならば{
         x=0
         c=1
      }
      もしsumが3ならば{
         x=1
         c=1
      }
      Xにxを追加する
      indexを増やす
   }
   Xが答え
}

>>> bits_add(3,5)
8
>>> bits_add(1,1)
2
>>> bits_add(15,1)
16
```

```yui
標準ライブラリを使う
# 配列を反転する: 先頭と末尾を入れ替えながら中央へ進む
reverse=入力Aに対し{
   n=Aの大きさ
   # 入れ替え回数は n/2 回 (奇数長の場合、真ん中はそのまま)
   half=商(n,2)
   i=0
   half回くり返す{
      # i 番目と (n-1-i) 番目を入れ替える
      j=差(差(n,1),i)
      tmp=A[i]
      A[i]=A[j]
      A[j]=tmp
      iを増やす
   }
   Aが答え
}

# テスト: 奇数長
>>> reverse([1,2,3,4,5])
[5,4,3,2,1]
# テスト: 偶数長
>>> reverse([1,2,3,4])
[4,3,2,1]
# テスト: 要素が 1 つ
>>> reverse([42])
[42]
# テスト: 空配列
>>> reverse([])
[]
# テスト: 文字列 (内部は文字コード配列なので同じ操作で反転できる)
>>> reverse("hello")
"olleh"
```

```yui
標準ライブラリを使う
# 母音を数える / 最初の母音で抜ける
# 文字列は文字コード配列なので、「のいずれか」で母音判定ができる。

# 母音を数える
count_vowels=入力sに対し{
   vowels="aeiouAEIOU"
   count=0
   i=0
   sの大きさ回くり返す{
      c=s[i]
      もしcがvowelsのいずれかならば{
         countを増やす
      }
      iを増やす
   }
   countが答え
}

>>> count_vowels("hello")
2
>>> count_vowels("programming")
3
>>> count_vowels("xyz")
0
>>> count_vowels("AEIOU")
5

# 最初の母音を見つけたら くり返しを抜ける (break)
first_vowel=入力sに対し{
   vowels="aeiouAEIOU"
   result=""
   i=0
   sの大きさ回くり返す{
      c=s[i]
      もしcがvowelsのいずれかならば{
         resultにcを追加する
         くり返しを抜ける
      }
      iを増やす
   }
   resultが答え
}

>>> first_vowel("hello")
"e"
>>> first_vowel("sky")
""
>>> first_vowel("Apple")
"A"
```

```yui
# 文字列からユニークな文字だけを取り出す
# 文字列は文字コード配列なので、配列と同じ「のいずれか / のいずれでもない」で
# 既出判定ができる。先頭から順に見て、まだ結果に含まれていない文字だけを追加する。

unique_chars=入力sに対し{
   result=""
   i=0
   sの大きさ回くり返す{
      c=s[i]
      もしcがresultのいずれでもないならば{
         resultにcを追加する
      }
      iを増やす
   }
   resultが答え
}

# テスト: 重複を 1 つにまとめる
>>> unique_chars("banana")
"ban"
>>> unique_chars("mississippi")
"misp"
# テスト: 出現順は保たれる
>>> unique_chars("abcabc")
"abc"
>>> unique_chars("programming")
"progamin"
# テスト: すべて同じ文字
>>> unique_chars("aaaa")
"a"
# テスト: 空文字列
>>> unique_chars("")
""
# テスト: 日本語もそのまま動く (文字列は文字コード配列)
>>> unique_chars("さくらさくら")
"さくら"
```

```yui
標準ライブラリを使う
# 文字列 s の中の old を全て new で置換した新しい文字列を返す
# old が空文字列の場合は s をそのまま返す (無限ループ防止)
# 文字列は文字コード配列なので、追加 (`に〜を追加する`) で組み立てられる

replace=入力s,old,newに対し{
   result=""
   n=sの大きさ
   m=oldの大きさ
   newlen=newの大きさ
   もしmが0ならば{
      sが答え
   }
   i=0
   # 各反復で i は最低 1 進むので n+1 回回せば必ず終わる
   limit=和(n,1)
   limit回くり返す{
      もしiがn以上ならば{
         くり返しを抜ける
      }
      # i から始まる m 文字が old と一致するか調べる
      match=0
      tail=和(i,m)
      もしtailがn以下ならば{
         match=1
         j=0
         m回くり返す{
            ij=和(i,j)
            cs=s[ij]
            co=old[j]
            もしcsがco以外ならば{
               match=0
            }
            jを増やす
         }
      }
      もしmatchが1ならば{
         # new を追記して i を m 進める
         k=0
         newlen回くり返す{
            resultにnew[k]を追加する
            kを増やす
         }
         i=和(i,m)
      }
      そうでなければ{
         # 一致しなければ s[i] を 1 文字コピー
         resultにs[i]を追加する
         iを増やす
      }
   }
   resultが答え
}

# テスト: 単純な置換
>>> replace("hello world","world","Yui")
"hello Yui"
# テスト: 複数箇所を一括置換
>>> replace("ababab","a","X")
"XbXbXb"
# テスト: 置換結果が元より短い
>>> replace("hello hello","hello","hi")
"hi hi"
# テスト: 置換結果が元より長い
>>> replace("abc","b","BBB")
"aBBBc"
# テスト: 一致しないなら原文のまま
>>> replace("hello","xyz","ABC")
"hello"
# テスト: 全体が一致
>>> replace("foo","foo","bar")
"bar"
# テスト: 削除 (new が空文字列)
>>> replace("a-b-c","-","")
"abc"
# テスト: old が空なら原文を返す
>>> replace("hello","","X")
"hello"
```

```yui
標準ライブラリを使う
# BMI (Body Mass Index) 分類
#
# BMI は 体重(kg) を 身長(m) の 2 乗で割った値。WHO 基準で次のように分類:
#
#   BMI が 18.5 未満           → "痩せ"
#   18.5 以上 25 未満           → "普通"
#   25 以上 30 未満             → "過体重"
#   30 以上                     → "肥満"
#
# 範囲分類は しきい値の昇順に並べた 早期 return パターンで書ける。
# 各しきい値ごとに「ここまでなら〜〜」と書けば、AND を使わず排他的に分類できる。

bmi_category=入力w,hに対し{
   # BMI を float で計算する
   weight=小数化(w)
   h2=積(h,h)
   bmi=商(weight,h2)

   もしbmiが18.5より小さいならば{
      "痩せ"が答え
   }
   もしbmiが25より小さいならば{
      "普通"が答え
   }
   もしbmiが30より小さいならば{
      "過体重"が答え
   }
   "肥満"が答え
}

# === テスト: 痩せ (身長 1.70m, 体重 50kg → BMI 約 17.3) ===
>>> bmi_category(50,1.70)
"痩せ"
# === テスト: 普通 (身長 1.70m, 体重 65kg → BMI 約 22.5) ===
>>> bmi_category(65,1.70)
"普通"
# === テスト: 過体重 (身長 1.70m, 体重 80kg → BMI 約 27.7) ===
>>> bmi_category(80,1.70)
"過体重"
# === テスト: 肥満 (身長 1.70m, 体重 100kg → BMI 約 34.6) ===
>>> bmi_category(100,1.70)
"肥満"
# === テスト: 別の身長でも分類されること ===
>>> bmi_category(55,1.60)
"普通"
>>> bmi_category(90,1.65)
"肥満"
# === テスト: 痩せ寄りの境界 ===
>>> bmi_category(45,1.70)
"痩せ"
```

```yui
標準ライブラリを使う
# 3 辺の長さから三角形を分類する
#
#   "not_triangle" : 三角不等式を満たさない (a+b > c などが成り立たない)
#   "equilateral"  : 正三角形 (3 辺すべて等しい)
#   "isosceles"    : 二等辺三角形 (ちょうど 2 辺が等しい)
#   "scalene"      : 不等辺三角形 (3 辺すべて異なる)
#
# yui には AND / OR が無いので、複数条件は **フラグ** か **ネスト もし** で組む。
# 三角不等式は 3 本の比較すべてが成り立つ必要があるので、ここではフラグで集約する。

classify=入力a,b,cに対し{
   # === ステップ 1: 三角不等式チェック ===
   # a+b > c, a+c > b, b+c > a がすべて成り立つかを ok フラグで集約
   ok=1
   ab=和(a,b)
   ac=和(a,c)
   bc=和(b,c)
   もしabがc以下ならば{ ok=0 }
   もしacがb以下ならば{ ok=0 }
   もしbcがa以下ならば{ ok=0 }
   もしokが0ならば{
      "not_triangle"が答え
   }

   # === ステップ 2: 何辺が等しいかを数える ===
   # eq == 3 なら正三角形、eq == 1 なら二等辺、eq == 0 なら不等辺
   # 等しさは「差が 0」で判定する
   # (もし <変数> が <変数> ならば の形は yui パーサが嫌うので避ける)
   eq=0
   dab=差(a,b)
   dbc=差(b,c)
   dac=差(a,c)
   もしdabが0ならば{
      eqを増やす
   }
   もしdbcが0ならば{
      eqを増やす
   }
   もしdacが0ならば{
      eqを増やす
   }

   もしeqが3ならば{
      "equilateral"が答え
   }
   もしeqが1ならば{
      "isosceles"が答え
   }
   "scalene"が答え
}

# === テスト: 正三角形 ===
>>> classify(5,5,5)
"equilateral"
# === テスト: 二等辺 ===
>>> classify(5,5,8)
"isosceles"
>>> classify(8,5,5)
"isosceles"
>>> classify(5,8,5)
"isosceles"
# === テスト: 不等辺 ===
>>> classify(3,4,5)
"scalene"
>>> classify(7,8,9)
"scalene"
# === テスト: 三角不等式違反 ===
>>> classify(1,2,3)
"not_triangle"
>>> classify(1,1,5)
"not_triangle"
>>> classify(10,1,1)
"not_triangle"
# === テスト: 退化した三角形 (面積ゼロ、ちょうど一直線) も三角形ではない ===
>>> classify(2,2,4)
"not_triangle"
```

```yui
標準ライブラリを使う
# 整数のビットシフト
# bits.yui ではビット列 (LSB ファーストの配列) を加工していたが、
# ここでは整数を直接、2 のべき乗で乗除する素朴な実装にする。
#
#   左シフト lshift(n,k)  ↔  n を 2 倍を k 回   ↔  n * 2^k
#   右シフト rshift(n,k)  ↔  n を 2 で割るを k 回 (床除算) ↔  n // 2^k
#
# yui には算術記号がないので 積() / 商() を使う。
# 商() は整数同士なら床除算なので右シフトもこれでよい。

lshift=入力n,kに対し{
   result=n
   k回くり返す{
      result=積(result,2)
   }
   resultが答え
}

rshift=入力n,kに対し{
   result=n
   k回くり返す{
      result=商(result,2)
   }
   resultが答え
}

# テスト: 左シフト
>>> lshift(1,3)
8
>>> lshift(3,2)
12
>>> lshift(5,1)
10
# テスト: 0 シフトは恒等
>>> lshift(7,0)
7
>>> rshift(7,0)
7
# テスト: 右シフト (床除算)
>>> rshift(8,3)
1
>>> rshift(12,2)
3
# テスト: 端数は切り捨てられる
>>> rshift(13,2)
3
# テスト: シフト幅が大きすぎると 0 になる
>>> rshift(5,3)
0
# テスト: 0 をシフトしても 0
>>> lshift(0,5)
0
>>> rshift(0,5)
0
# テスト: 左→右で元に戻る (端数切り捨てが起きない範囲で)
>>> rshift(lshift(11,4),4)
11
```

```yui
標準ライブラリを使う
# 二次方程式 ax^2 + bx + c = 0 の実数解を求める (実数解 2 つを想定)
# 解の公式:  x = (-b ± √D) / 2a    ただし D = b^2 - 4ac
# 結果は [大きい解, 小さい解] の配列で返す

solve=入力a,b,cに対し{
   D=差(積(b,b),積(4,積(a,c)))
   sqrtD=平方根(D)
   # 整数同士の 商() は床除算になるので、すべて小数化してから割る
   denom=小数化(積(2,a))
   mb=小数化(差(0,b))
   x1=商(和(mb,sqrtD),denom)
   x2=商(差(mb,sqrtD),denom)
   [x1,x2]が答え
}

# テスト: x^2 - 3x + 2 = 0 → x = 2, 1
>>> solve(1,-3,2)
[2.000000,1.000000]
# テスト: x^2 - 1 = 0 → x = 1, -1
>>> solve(1,0,-1)
[1.000000,-1.000000]
# テスト: x^2 - 4 = 0 → x = 2, -2
>>> solve(1,0,-4)
[2.000000,-2.000000]
# テスト: x^2 - 5x + 6 = 0 → x = 3, 2
>>> solve(1,-5,6)
[3.000000,2.000000]
```
