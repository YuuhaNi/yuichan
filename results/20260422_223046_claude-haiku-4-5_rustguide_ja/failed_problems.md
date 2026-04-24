# 失敗問題一覧 — 20260422_223046_claude-haiku-4-5_rustguide_ja

- モデル: claude-haiku-4-5
- 言語: ja / テンプレート: pro159/rustguide_ja.md
- 合計: **164問中 119問失敗** (pass@1 = 27.44%)

## 失敗原因サマリ

| 原因 | 件数 |
|------|------|
| テスト失敗(出力不一致) | 63 |
| 構文エラー | 31 |
| 構文認識不可(Yui非準拠) | 25 |

### 原因の意味

- **構文認識不可(Yui非準拠)**: Yuiパーサが文法として受理できず、そもそもコードとして実行されなかった
- **構文エラー**: パース自体は通ったが実行中に文法エラーで停止
- **テスト失敗(出力不一致)**: 実行は完了したがテストの期待値と異なる

## 失敗問題リスト

| タスクID | 関数 | 問題概要 | 失敗原因 | エラー詳細 |
|---------|------|---------|---------|-----------|
| 0 | `has_close_elements` | リストnumbersの中に、与えられたthresholdより近い２つの数値が存在するか判定する | テスト失敗(出力不一致) | テストを失敗 🔍has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) ❌true ✅1 line 22, column 1: |
| 1 | `separate_paren_groups` | この関数への入力は、入れ子になった括弧が複数含まれる文字列である。 | テスト失敗(出力不一致) | テストを失敗 🔍separate_paren_groups("(()()) ((())) () ((())()())") ❌[] ✅["(()())", "((()))", "()", "((())()())"] line 44, column 1: |
| 3 | `below_zero` | 銀行口座に対する入出金操作のリストが与えられます。あなたのタスクは、残高ゼロから | テスト失敗(出力不一致) | テストを失敗 🔍below_zero([]) ❌false ✅0 line 61, column 1: |
| 6 | `parse_nested_parens` | この関数の入力は、空白で区切られた複数の入れ子になった括弧のグループを表す文字列です。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 8 | `sum_product` | 与えられた整数リストに対して、リスト内のすべての整数の和と積からなるタプルを返す。 | テスト失敗(出力不一致) | テストを失敗 🔍sum_product([]) ❌{"numbers": [], "s": 0, "p": 1, "i": 0, "sum": 0, "product": 1} ✅[0, 1] line 17, column 1: |
| 10 | `make_palindrome` | 与えられた文字列が回文かどうかをテストします。 | 構文エラー | 関数が定義されていません ❌make_palindrome line 20, column 5: |
| 11 | `string_xor` | 引数は1と0のみからなる文字列aとbである。 | 構文エラー | データの種類（型）が違っています ✅<🔢number> ❌"" line 16, column 16: |
| 12 | `longest` | 文字列のリストのうち、最も長いものを返す。同じ長さの文字列が | テスト失敗(出力不一致) | テストを失敗 🔍longest([]) ❌null ✅"" line 26, column 1: |
| 15 | `string_sequence` | 0からnまでの数字を空白区切りで連結した文字列で返す。 | 構文エラー | 関数が定義されていません ❌足す line 6, column 4: |
| 17 | `parse_music` | この関数の引数は、特別なASCII形式の音符を表す文字列である。あなたの仕事は、この文字列を解析して、それぞれの音符が何拍続くかに対応する整数のリストを返すことである。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 18 | `how_many_times` | 部分文字列substringが文字列stringの中で何回見つかるか数える。 | 構文エラー | index-error ✅<9 ❌9 🔍[99, 97, 99, 97, 99, 97, 99, 97, 99] line 25, column 12: |
| 19 | `sort_numbers` | 引数は'zero'から'nine'までの英単語の数を空白で区切った文字列である。 | 構文エラー | データの種類（型）が違っています ✅<🔢number> ❌"" line 21, column 25: |
| 20 | `find_closest_elements` | （少なくとも長さ2以上の）リストnumbersから、互いに最も近いものを2つ選び、 | テスト失敗(出力不一致) | テストを失敗 🔍find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) ❌{"numbers": [1.000000, 2.000000, 3.900000, 4.000000, 5.000000, 2.200000], "min_diff": 0.100000, " |
| 24 | `largest_divisor` | 与えられた数nについて、nの約数のうち、nより小さい最大の数を求める | テスト失敗(出力不一致) | テストを失敗 🔍largest_divisor(3) ❌3 ✅1 line 19, column 1: |
| 25 | `factorize` | 与えられた整数の素因数のリストを小さいものから大きいものの順に返す。各因数は、 | テスト失敗(出力不一致) | テストを失敗 🔍factorize(2) ❌{"n": 1, "factors": [2], "divisor": 2} ✅[2] line 26, column 1: |
| 26 | `remove_duplicates` | 整数のリストから、複数回出現する要素をすべて取り除く。 | テスト失敗(出力不一致) | テストを失敗 🔍remove_duplicates([1, 2, 3, 2, 4, 3, 5]) ❌[1, 2, 3, 2, 4, 3, 5] ✅[1, 4, 5] line 39, column 1: |
| 27 | `flip_case` | 与えられた文字列に対して、英小文字を英大文字に、英大文字を英小文字に変換する。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 28 | `concatenate` | 文字列のリストを1つの文字列に連結する | 構文エラー | データの種類（型）が違っています ✅<🔢number> ❌"" line 7, column 16: |
| 31 | `is_prime` | 与えられた数が素数であれば真を、そうでなければ偽を返す。 | テスト失敗(出力不一致) | テストを失敗 🔍is_prime(6) ❌false ✅0 line 27, column 1: |
| 32 | `find_zero` | 点xにおける係数xsを持つ多項式の値を計算する。 | 構文エラー | 関数が定義されていません ❌approx_zero line 16, column 5: |
| 33 | `sort_third` | この関数はリストlを受け取り、l'を返す。l'は、インデックスが3で割り | 構文エラー | index-error ✅>=0 ❌-1 line 19, column 33: |
| 34 | `unique` | リスト内のユニークな要素をソートして返す | 構文エラー | index-error ✅>=0 ❌-1 line 19, column 22: |
| 37 | `sort_even` | この関数はリスト l を受け取り、l' を返す。l'は、インデックスが奇数の | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 38 | `decode_cyclic` | 3文字ごとに循環させてエンコードした文字列を返す。 | テスト失敗(出力不一致) | テストを失敗 🔍decode_cyclic("axdhhixdexrvsncacbgh") ❌"axhhxdxrsnacgh" ✅"daxihhexdvxrcsnbacgh" line 20, column 1: |
| 39 | `prime_fib` | prime_fib はフィボナッチ数で、かつ素数であるn番目の数を返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 40 | `triples_sum_to_zero` | triples_sum_to_zero は整数のリストを引数に取り、 | テスト失敗(出力不一致) | テストを失敗 🔍triples_sum_to_zero([1, 3, 5, 0]) ❌false ✅0 line 51, column 1: |
| 42 | `incr_list` | 要素を1ずつ増やしたリストを返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 43 | `pairs_sum_to_zero` | pairs_sum_to_zero は整数のリストを引数にとる。 | テスト失敗(出力不一致) | テストを失敗 🔍pairs_sum_to_zero([1, 3, 5, 0]) ❌false ✅0 line 28, column 1: |
| 44 | `change_base` | 引数xの基数をbaseに変換する。 | 構文エラー | サポートされていない演算子です 🔍+ line 14, column 16: |
| 45 | `triangle_area` | 三角形の一辺の長さと高さが与えられたとき、面積を返す。 | テスト失敗(出力不一致) | テストを失敗 🔍triangle_area(5, 3) ❌7 ✅7.500000 line 8, column 1: |
| 47 | `median` | リスト l の要素の中央値を返す。 | 構文エラー | index-error ✅>=0 ❌-1 line 10, column 20: |
| 48 | `is_palindrome` | 与えられた文字列が回文かどうかを判定する | テスト失敗(出力不一致) | テストを失敗 🔍is_palindrome("") ❌true ✅1 line 16, column 1: |
| 50 | `decode_shift` | アルファベットの各文字を5ずつずらしてエンコードした文字列を返す。 | テスト失敗(出力不一致) | テストを失敗 🔍decode_shift("ifcnmmjciacwhxsgfhlm") ❌"nkhsrrohnfh\|m}xlkmqr" ✅"daxihhexdvxrcsnbacgh" line 17, column 1: |
| 52 | `below_threshold` | リスト l 内の全ての数値が閾値 t 以下の場合、Trueを返す。 | テスト失敗(出力不一致) | テストを失敗 🔍below_threshold([1, 2, 4, 10], 100) ❌true ✅1 line 30, column 1: |
| 54 | `same_chars` | 2つの単語が同じ文字セットから構成されるかどうか判定する。 | テスト失敗(出力不一致) | テストを失敗 🔍same_chars("eabcdzzzz", "dddzzzzzzzddeddabc") ❌false ✅1 line 57, column 1: |
| 56 | `correct_bracketing` | 引数bracketsは"<"と">"の文字列である。 | テスト失敗(出力不一致) | テストを失敗 🔍correct_bracketing("<>") ❌true ✅1 line 28, column 1: |
| 57 | `monotonic` | リストの要素が単調増加または単調減少する場合にTrueを返す。 | 構文エラー | index-error ✅>=0 ❌-1 line 13, column 14: |
| 58 | `common` | 2つのリストについて、ユニークな共通要素をソートして返す。 | テスト失敗(出力不一致) | テストを失敗 🔍common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) ❌{"l1": [1, 4, 3, 34, 653, 2, 5], "l2": [5, 7, 1, 5, 9, 653, 121], "result": [1, 5, 653], "i |
| 61 | `correct_bracketing` | 引数bracketsは"("と") "からなる文字列である。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 62 | `derivative` | xsは多項式の係数列を表す。 | 構文エラー | ここは変数が必要です ❌xsの大きさ line 6, column 4: |
| 64 | `vowels_count` | Add more test cases. | テスト失敗(出力不一致) | テストを失敗 🔍vowels_count("Alone") ❌2 ✅3 line 35, column 1: |
| 67 | `fruit_distribution` | この課題では、果物の入ったカゴに配られたリンゴとオレンジの数を表す文字列が | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 69 | `search` | 正の整数の空でないリストが与えられる。0より大きく、その整数自身の値以上の頻度を | テスト失敗(出力不一致) | テストを失敗 🔍search([5, 5, 5, 5, 1]) ❌5 ✅1 line 73, column 1: |
| 71 | `triangle_area` | 三角形の3辺の長さが与えられた。3辺が有効な三角形を形成していれば、 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 72 | `will_it_fly` | 物体qが飛べばTrueを、そうでなければFalseを返す関数を書け。 | テスト失敗(出力不一致) | テストを失敗 🔍will_it_fly([3, 2, 3], 9) ❌false ✅1 line 43, column 1: |
| 73 | `smallest_change` | 整数の配列arrが与えられたとき、その配列を回文配列にするために | テスト失敗(出力不一致) | テストを失敗 🔍smallest_change([1,2,3,5,4,7,9,6]) ❌8 ✅4 line 22, column 1: |
| 74 | `total_match` | ２つの文字列リストを受け取り、リストの全文字数の合計がもう一方 | テスト失敗(出力不一致) | テストを失敗 🔍total_match(["hi", "admin"], ["hi", "hi"]) ❌["hi", "admin"] ✅["hi", "hi"] line 55, column 1: |
| 75 | `is_multiply_prime` | 与えられた数が3つの素数の掛け算であればTrueを、そうでなければFalseを返す | テスト失敗(出力不一致) | テストを失敗 🔍is_multiply_prime(5) ❌false ✅0 line 36, column 1: |
| 76 | `is_simple_power` | あなたのタスクは、ある数xがnの単純なべき乗である場合にtrueを、 | テスト失敗(出力不一致) | テストを失敗 🔍is_simple_power(16, 2) ❌true ✅1 line 23, column 1: |
| 77 | `iscube` | 整数aを受け取り、この整数がある整数の3乗である場合にTrue | テスト失敗(出力不一致) | テストを失敗 🔍iscube(1) ❌true ✅1 line 24, column 1: |
| 78 | `hex_key` | 16進数の数字を文字列として受け取り、その中に含まれる素数である16進数の桁数を | テスト失敗(出力不一致) | テストを失敗 🔍hex_key("AB") ❌0 ✅1 line 25, column 1: |
| 79 | `decimal_to_binary` | 10進数形式の数値が与えられ、あなたのタスクはそれを2進数形式に変換することである。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 80 | `is_happy` | あなたは文字列sが与えられる。 | テスト失敗(出力不一致) | テストを失敗 🔍is_happy("a") ❌false ✅0 line 35, column 1: |
| 82 | `prime_length` | 文字列を受け取り、文字列の長さが素数であればTrueを、そうでなければFalseを返す関数を書く。 | テスト失敗(出力不一致) | テストを失敗 🔍prime_length("Hello") ❌false ✅1 line 29, column 1: |
| 83 | `starts_one_ends` | 正の整数 n が与えられたとき、n 桁の正の整数で 1 で始まるか | 構文エラー | 変数が定義されていません ❌min line 7, column 7: |
| 84 | `solve` | 正の整数 N が与えられた時、その桁の総和を2進数で返す。 | 構文エラー | データの種類（型）が違っています ✅<🔢number> ❌"1" line 33, column 19: |
| 86 | `anti_shuffle` | 文字列を引数として受け取り、その「順序付けられたバージョン」を返す関数を作成してください。 | 構文エラー | データの種類（型）が違っています ✅<🔢number> ❌"" line 21, column 25: |
| 87 | `get_row` | 2次元のデータがネストされたリストとして与えられる。これは行列に似ているが、 | 構文エラー | データの種類（型）が違っています ✅<🔢int> ❌"row" line 29, column 16: |
| 89 | `encrypt` | 文字列を引数にとり、アルファベットを回転させて暗号化した | テスト失敗(出力不一致) | テストを失敗 🔍encrypt("hi") ❌"ÒÔ" ✅"lm" line 17, column 1: |
| 90 | `next_smallest` | 整数のリストが与えられる。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 91 | `is_bored` | 単語の文字列が与えられ、あなたのタスクは退屈指数を数える | 構文エラー | 関数が定義されていません ❌足 line 11, column 24: |
| 92 | `any_int` | 3つの数値を受け取る関数を作る。 | テスト失敗(出力不一致) | テストを失敗 🔍any_int(2, 3, 1) ❌true ✅1 line 30, column 1: |
| 93 | `encode` | メッセージを受け取り、すべての文字の大文字と小文字を入れ替え、 | テスト失敗(出力不一致) | テストを失敗 🔍encode("TEST") ❌"tCst" ✅"tgst" line 83, column 1: |
| 94 | `skjkasdkd` | 整数のリストが与えらる。 | テスト失敗(出力不一致) | テストを失敗 🔍skjkasdkd([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]) ❌53 ✅10 line 53, column 1: |
| 95 | `check_dict_case` | 辞書が与えられたとき、すべてのキーが小文字であればTrueを、 | テスト失敗(出力不一致) | テストを失敗 🔍check_dict_case({"p":"pineapple", "b":"banana"}) ❌true ✅1 line 93, column 1: |
| 96 | `count_up_to` | 非負整数を受け取り、素数でnより小さい最初のn個の | テスト失敗(出力不一致) | テストを失敗 🔍count_up_to(5) ❌{"n": 5, "primes": [2, 3], "candidate": 5, "is_prime": false, "i": 0, "divisor": 2} ✅[2, 3] line 35, column 1: |
| 99 | `closest_integer` | 数値を表す文字列valueを受け取り、それに最も近い整数を返す関数を作る。 | テスト失敗(出力不一致) | テストを失敗 🔍closest_integer("-15.5") ❌-15 ✅-16 line 33, column 1: |
| 101 | `words_string` | カンマまたは空白で区切られた単語の文字列が与えられる。あなたのタスクは、 | 構文エラー | データの種類（型）が違っています ✅<🔢number> ❌"" line 24, column 20: |
| 102 | `choose_num` | この関数は2つの正の数xとyを受け取り、範囲[x, y]（両端を含む）に含まれる | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 103 | `rounded_avg` | 2つの正の整数nとmが与えられており、あなたのタスクはnからmまでの | 構文エラー | サポートされていない演算子です 🔍+ line 42, column 19: |
| 104 | `unique_digits` | 正の整数xのリストが与えられたとき、偶数桁の要素を持たない全ての | テスト失敗(出力不一致) | テストを失敗 🔍unique_digits([15, 33, 1422, 1]) ❌{"x": [15, 33, 1422, 1], "result": [], "i": 1, "num": 15, "digits": "15", "digit_count": 2, "is_unique": true, "j": 2, |
| 106 | `f` | iは1から始まる。iの階乗は1からiまでの数の掛け算（1 * 2 * ... * i）である。 | テスト失敗(出力不一致) | テストを失敗 🔍f(5) ❌[1, 2, 6, 24, 120] ✅[1, 2, 6, 24, 15] line 16, column 1: |
| 107 | `even_odd_palindrome` | 与えられた正の整数 nに対して、範囲 1 から n まで（両端を含む）に存在する | テスト失敗(出力不一致) | テストを失敗 🔍even_odd_palindrome(123) ❌{"n": 123, "even_count": 8, "odd_count": 13, "i": 124, "s": "123", "s_len": 3, "is_palindrome": false, "j": 0} ✅[8, 13] line 4 |
| 108 | `count_nums` | count_nums 関数は、整数の配列を引数として受け取り、その配列内の各整数の各桁の合計が | テスト失敗(出力不一致) | テストを失敗 🔍count_nums([1, 1, 2, -2, 3, 4, 5]) ❌7 ✅6 line 40, column 1: |
| 109 | `move_one_ball` | N個の整数arr[1], arr[2], ..., arr[N]なる配列 'arr' があります。 | テスト失敗(出力不一致) | テストを失敗 🔍move_one_ball([3, 4, 5, 1, 2]) ❌true ✅1 line 53, column 1: |
| 110 | `exchange` | この問題では、2つの数のリストを受け取り、lst1を偶数のみのリストに | 構文エラー | 変数が定義されていません ❌needed line 25, column 7: |
| 111 | `histogram` | 空白で区切られた小文字を表す文字列が与えられる。最も出現回数が多い文字と | テスト失敗(出力不一致) | テストを失敗 🔍histogram([97, 32, 98, 32, 98, 32, 97]) ❌{"97": 1, "98": 1} ✅[[[97], 2], [[98], 2]] line 67, column 1: |
| 112 | `reverse_delete` | 課題 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 113 | `odd_count` | 数字のみで構成された文字列のリストを引数として受け取り、新しいリストを返します。 | 構文エラー | データの種類（型）が違っています ✅<🔢number> ❌"" line 26, column 27: |
| 114 | `minSubArraySum` | 整数の配列 nums が与えられたとき、nums の空でない部分配列の最小和を求めよ。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 115 | `max_fill` | 長方形のグリッド状(grid)の井戸が与えられる。各行が1つの井戸を表し、 | 構文エラー | 変数が定義されていません ❌buckets line 50, column 7: |
| 116 | `sort_array` | この問題では、非負整数の配列を2進数表現における"1"の個数を昇順でソートする。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 118 | `get_closest_vowel` | 単語が与えられる。あなたの仕事は、単語の右側から2つの子音（大文字と | テスト失敗(出力不一致) | テストを失敗 🔍get_closest_vowel("yogurt") ❌"117" ✅"u" line 48, column 1: |
| 119 | `match_parens` | 2つの文字列からなるリストが与えられます。両方の文字列は開き括弧 '(' または | 構文エラー | 変数が定義されていません ❌combined line 13, column 7: |
| 120 | `maximum` | 整数の配列 arr と正の整数 k が与えられる。arr に含まれる大きい方から k 個の数を含む | 構文エラー | サポートされていない演算子です 🔍+ line 45, column 29: |
| 121 | `solution` | 整数の空でないリストが与えられた時、偶数の位置にある奇数の要素の合計を返す。 | テスト失敗(出力不一致) | テストを失敗 🔍solution([5, 8, 7, 1]) ❌2 ✅12 line 19, column 1: |
| 123 | `get_odd_collatz` | 正の整数nが与えられたとき、コラッツ数列の奇数を持つソートされたリストを返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 124 | `valid_date` | 与えられた日付文字列を検証し、その日付が有効であればTrueを、そうでなければFalseを返す関数を書く必要がある。 | テスト失敗(出力不一致) | テストを失敗 🔍valid_date("03-11-2000") ❌false ✅1 line 84, column 1: |
| 125 | `split_words` | 単語の文字列が与えられた場合、空白で分割された単語のリストを返す。 | テスト失敗(出力不一致) | テストを失敗 🔍split_words("Hello world!") ❌5 ✅["Hello", "world!"] line 76, column 1: |
| 126 | `is_sorted` | 数字のリストが与えられたとき、昇順に整列されているかどうかを返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 127 | `intersection` | 2つの区間が与えられます。 | テスト失敗(出力不一致) | テストを失敗 🔍intersection([-1, 1], [0, 4]) ❌"YES" ✅"NO" line 58, column 1: |
| 128 | `prod_signs` | 整数の配列 arr が与えられます。この配列に含まれる各数値の絶対値の合計と、 | テスト失敗(出力不一致) | テストを失敗 🔍prod_signs([1, 2, 2, -4]) ❌-9 ✅[-9] line 69, column 1: |
| 129 | `minPath` | N行とN列 (N >= 2)) のグリッドと正の整数kが与えられた場合、各セルには値が含まれている。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 131 | `digits` | 正の整数 n が与えられた時、奇数桁数の積を返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 132 | `is_nested` | この関数は、角括弧だけを含む文字列を入力として受け取ります。括弧が有効な順序で | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 134 | `check_if_last_char_is_a_letter` | 与えられた文字列の最後の文字がアルファベットであり、かつ単語の一部でなければTrueを、 | テスト失敗(出力不一致) | テストを失敗 🔍check_if_last_char_is_a_letter("apple") ❌false ✅0 line 68, column 1: |
| 136 | `largest_smallest_integers` | リストから最も大きな負の整数と最も小さな正の整数を見つけ、それらをタプル（a, b） | テスト失敗(出力不一致) | テストを失敗 🔍largest_smallest_integers([2, 4, 1, 3, 5, 7]) ❌{"lst": [2, 4, 1, 3, 5, 7], "largest_negative": null, "smallest_positive": 1, "i": 6, "num": 7} ✅[[], 1] |
| 137 | `compare_one` | 整数、浮動小数点数、または実数を表す文字列を引数として受け取り、その中で最も大きい値を | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 138 | `is_equal_to_sum_even` | 与えられた数値nが、ちょうど4つの正の偶数の合計として表現できるかどうかを評価してください。 | テスト失敗(出力不一致) | テストを失敗 🔍is_equal_to_sum_even(4) ❌false ✅0 line 45, column 1: |
| 140 | `fix_spaces` | 文字列テキストが与えられた場合、その中のすべての空白をアンダースコアに置換し、 | 構文エラー | データの種類（型）が違っています ✅<🔢number> ❌"" line 43, column 19: |
| 141 | `file_name_check` | ファイル名を表す文字列を受け取り、そのファイル名が有効であれば'Yes'を返し、そうでなければ'No' | テスト失敗(出力不一致) | テストを失敗 🔍file_name_check("example.txt") ❌"No" ✅"Yes" line 120, column 1: |
| 143 | `words_in_sentence` | 文を表す文字列が与えられ、その文には空白で区切られたいくつかの単語が含まれている。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 144 | `simplify` | あなたの仕事は、式 x * n を簡単にする関数を実装することです。 | 構文エラー | index-error ✅>=0 ❌-1 line 28, column 51: |
| 145 | `order_by_points` | 各数字の桁の合計に基づいて、与えられた整数のリストを昇順に並べる | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 146 | `specialFilter` | 数値の配列を入力とし、配列中の要素のうち、10より大きく、 | テスト失敗(出力不一致) | テストを失敗 🔍specialFilter([33, -2, -3, 45, 21, 109]) ❌1 ✅2 line 68, column 1: |
| 147 | `get_max_triples` | 正の整数 n が与えられるので、長さ n の整数配列 a を作成せよ。 | テスト失敗(出力不一致) | テストを失敗 🔍get_max_triples(5) ❌0 ✅1 line 55, column 1: |
| 148 | `bf` | 私たちの太陽系には8つの惑星があります：太陽に最も近いのはVenus, Earth, Mars, Jupiter, Saturn, | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 149 | `sorted_list_sum` | 文字列のリストを引数として受け取る関数を作成してください。 | 構文エラー | index-error ✅>=0 ❌-1 line 27, column 21: |
| 150 | `x_or_y` | 素数である場合はxの値を返し、それ以外の場合はyの値を返す簡単なプログラム。 | テスト失敗(出力不一致) | テストを失敗 🔍x_or_y(7, 34, 12) ❌12 ✅34 line 23, column 1: |
| 153 | `Strongest_Extension` | クラスの名前（文字列）と拡張子のリストが与えられます。 | 構文エラー | 変数が定義されていません ❌j line 14, column 31: |
| 154 | `cycpattern_check` | 2つの単語が与えられる。2番目の単語またはその回転させた文字列が最初の単語の部分文字列である場合、Trueを返す必要がある。 | テスト失敗(出力不一致) | テストを失敗 🔍cycpattern_check("xyzw","xyw") ❌false ✅0 line 93, column 1: |
| 155 | `even_odd_count` | 整数が与えられた場合、偶数桁数と奇数桁数をそれぞれ持つタプルを返す。 | テスト失敗(出力不一致) | テストを失敗 🔍even_odd_count(7) ❌{"num": 7, "s": "7", "even": 0, "odd": 1, "i": 1, "digit": 55, "d": 7, "even_count": 0, "odd_count": 1} ✅[0, 1] line 45, column 1: |
| 157 | `right_angle_triangle` | 三角形の3辺の長さを与える。三角形が直角三角形ならTrueを、そうでなければFalseを返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 158 | `find_max` | 文字列のリストを受け取る関数を書きなさい。 | テスト失敗(出力不一致) | テストを失敗 🔍find_max(["name", "of", "string"]) ❌"name" ✅"string" line 52, column 1: |
| 159 | `eat` | あなたはお腹を空かせたウサギです。すでに一定数のニンジンを食べました。 | テスト失敗(出力不一致) | テストを失敗 🔍eat(5, 6, 10) ❌{"number": 5, "need": 6, "remaining": 10, "eaten": 6, "total_eaten": 11, "left": 4, "result": [11, 4]} ✅[11, 4] line 18, column 1: |
| 160 | `do_algebra` | 演算子(operator)とオペランド(operand)の2つのリストが与えられる。ひとつ目のリストは | 構文エラー | 関数が定義されていません ❌累乗 line 96, column 23: |
| 161 | `solve` | 文字列sが与えられます。 | テスト失敗(出力不一致) | テストを失敗 🔍solve("AsDf") ❌[97] ✅"aSdF" line 69, column 1: |
| 162 | `string_to_md5` | 文字列 text が与えられたとき、その md5 ハッシュと等価な文字列を返す。 | 構文エラー | 関数が定義されていません ❌md5 line 8, column 7: |
| 163 | `generate_integers` | 正の整数aとbが与えられたとき、aとbの間にある偶数の数字を昇順で返してください。 | テスト失敗(出力不一致) | テストを失敗 🔍generate_integers(2, 10) ❌{"a": 2, "b": 10, "min_val": 10, "max_val": 10, "result": [4, 6, 8, 10]} ✅[2, 4, 6, 8] line 23, column 1: |
