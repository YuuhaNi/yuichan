# 失敗問題一覧 — 20260422_171055_gpt-5.4-2026-03-05_rustguide_ja

- モデル: gpt-5.4-2026-03-05
- 言語: ja / テンプレート: pro159/rustguide_ja.md
- 合計: **164問中 79問失敗** (pass@1 = 51.83%)

## 失敗原因サマリ

| 原因 | 件数 |
|------|------|
| テスト失敗(出力不一致) | 60 |
| 構文認識不可(Yui非準拠) | 11 |
| 構文エラー | 7 |
| タイムアウト | 1 |

### 原因の意味

- **構文認識不可(Yui非準拠)**: Yuiパーサが文法として受理できず、そもそもコードとして実行されなかった
- **構文エラー**: パース自体は通ったが実行中に文法エラーで停止
- **テスト失敗(出力不一致)**: 実行は完了したがテストの期待値と異なる

## 失敗問題リスト

| タスクID | 関数 | 問題概要 | 失敗原因 | エラー詳細 |
|---------|------|---------|---------|-----------|
| 0 | `has_close_elements` | リストnumbersの中に、与えられたthresholdより近い２つの数値が存在するか判定する | テスト失敗(出力不一致) | テストを失敗 🔍has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) ❌true ✅1 line 23, column 1: |
| 1 | `separate_paren_groups` | この関数への入力は、入れ子になった括弧が複数含まれる文字列である。 | テスト失敗(出力不一致) | テストを失敗 🔍separate_paren_groups("(()()) ((())) () ((())()())") ❌["(()())", " ((()))", " ()", " ((())()())"] ✅["(()())", "((()))", "()", "((())()())"] line 36, col |
| 3 | `below_zero` | 銀行口座に対する入出金操作のリストが与えられます。あなたのタスクは、残高ゼロから | テスト失敗(出力不一致) | テストを失敗 🔍below_zero([]) ❌false ✅0 line 19, column 1: |
| 10 | `make_palindrome` | 与えられた文字列が回文かどうかをテストします。 | テスト失敗(出力不一致) | テストを失敗 🔍make_palindrome("") ❌true ✅"" line 19, column 1: |
| 12 | `longest` | 文字列のリストのうち、最も長いものを返す。同じ長さの文字列が | テスト失敗(出力不一致) | テストを失敗 🔍longest([]) ❌null ✅"" line 20, column 1: |
| 14 | `all_prefixes` | 引数で与えられた文字列に対して、短いものから長いものへ、全ての接頭辞のリストを返す | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 19 | `sort_numbers` | 引数は'zero'から'nine'までの英単語の数を空白で区切った文字列である。 | テスト失敗(出力不一致) | テストを失敗 🔍sort_numbers("three") ❌"" ✅"three" line 26, column 1: |
| 27 | `flip_case` | 与えられた文字列に対して、英小文字を英大文字に、英大文字を英小文字に変換する。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 31 | `is_prime` | 与えられた数が素数であれば真を、そうでなければ偽を返す。 | テスト失敗(出力不一致) | テストを失敗 🔍is_prime(6) ❌false ✅0 line 23, column 1: |
| 32 | `find_zero` | 点xにおける係数xsを持つ多項式の値を計算する。 | 構文エラー | 関数が定義されていません ❌approx_zero line 18, column 5: |
| 38 | `decode_cyclic` | 3文字ごとに循環させてエンコードした文字列を返す。 | テスト失敗(出力不一致) | テストを失敗 🔍decode_cyclic("axdhhixdexrvsncacbgh") ❌"cwcjghzcdzquumbcbaig" ✅"daxihhexdvxrcsnbacgh" line 22, column 1: |
| 39 | `prime_fib` | prime_fib はフィボナッチ数で、かつ素数であるn番目の数を返す。 | タイムアウト | Timeout (10s) |
| 40 | `triples_sum_to_zero` | triples_sum_to_zero は整数のリストを引数に取り、 | テスト失敗(出力不一致) | テストを失敗 🔍triples_sum_to_zero([1, 3, 5, 0]) ❌false ✅0 line 39, column 1: |
| 42 | `incr_list` | 要素を1ずつ増やしたリストを返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 43 | `pairs_sum_to_zero` | pairs_sum_to_zero は整数のリストを引数にとる。 | テスト失敗(出力不一致) | テストを失敗 🔍pairs_sum_to_zero([1, 3, 5, 0]) ❌false ✅0 line 22, column 1: |
| 45 | `triangle_area` | 三角形の一辺の長さと高さが与えられたとき、面積を返す。 | テスト失敗(出力不一致) | テストを失敗 🔍triangle_area(5, 3) ❌7 ✅7.500000 line 8, column 1: |
| 47 | `median` | リスト l の要素の中央値を返す。 | テスト失敗(出力不一致) | テストを失敗 🔍median([-10, 4, 6, 1000, 10, 20]) ❌16 ✅8.000000 line 33, column 1: |
| 48 | `is_palindrome` | 与えられた文字列が回文かどうかを判定する | テスト失敗(出力不一致) | テストを失敗 🔍is_palindrome("") ❌true ✅1 line 23, column 1: |
| 50 | `decode_shift` | アルファベットの各文字を5ずつずらしてエンコードした文字列を返す。 | テスト失敗(出力不一致) | テストを失敗 🔍decode_shift("ifcnmmjciacwhxsgfhlm") ❌"ifcnmmjciacwhxsgfhlm" ✅"daxihhexdvxrcsnbacgh" line 30, column 1: |
| 52 | `below_threshold` | リスト l 内の全ての数値が閾値 t 以下の場合、Trueを返す。 | テスト失敗(出力不一致) | テストを失敗 🔍below_threshold([1, 2, 4, 10], 100) ❌true ✅1 line 15, column 1: |
| 54 | `same_chars` | 2つの単語が同じ文字セットから構成されるかどうか判定する。 | テスト失敗(出力不一致) | テストを失敗 🔍same_chars("eabcdzzzz", "dddzzzzzzzddeddabc") ❌true ✅1 line 46, column 1: |
| 56 | `correct_bracketing` | 引数bracketsは"<"と">"の文字列である。 | テスト失敗(出力不一致) | テストを失敗 🔍correct_bracketing("<>") ❌true ✅1 line 28, column 1: |
| 57 | `monotonic` | リストの要素が単調増加または単調減少する場合にTrueを返す。 | テスト失敗(出力不一致) | テストを失敗 🔍monotonic([1, 2, 4, 10]) ❌true ✅1 line 35, column 1: |
| 61 | `correct_bracketing` | 引数bracketsは"("と") "からなる文字列である。 | テスト失敗(出力不一致) | テストを失敗 🔍correct_bracketing("()") ❌true ✅1 line 27, column 1: |
| 62 | `derivative` | xsは多項式の係数列を表す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 64 | `vowels_count` | Add more test cases. | テスト失敗(出力不一致) | テストを失敗 🔍vowels_count("Alone") ❌2 ✅3 line 21, column 1: |
| 67 | `fruit_distribution` | この課題では、果物の入ったカゴに配られたリンゴとオレンジの数を表す文字列が | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 69 | `search` | 正の整数の空でないリストが与えられる。0より大きく、その整数自身の値以上の頻度を | 構文エラー | index-error ✅<0 ❌5 🔍[] line 12, column 10: |
| 71 | `triangle_area` | 三角形の3辺の長さが与えられた。3辺が有効な三角形を形成していれば、 | テスト失敗(出力不一致) | テストを失敗 🔍triangle_area(4, 8, 5) ❌8 ✅8.180000 line 22, column 1: |
| 72 | `will_it_fly` | 物体qが飛べばTrueを、そうでなければFalseを返す関数を書け。 | テスト失敗(出力不一致) | テストを失敗 🔍will_it_fly([3, 2, 3], 9) ❌true ✅1 line 31, column 1: |
| 75 | `is_multiply_prime` | 与えられた数が3つの素数の掛け算であればTrueを、そうでなければFalseを返す | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 76 | `is_simple_power` | あなたのタスクは、ある数xがnの単純なべき乗である場合にtrueを、 | テスト失敗(出力不一致) | テストを失敗 🔍is_simple_power(16, 2) ❌true ✅1 line 29, column 1: |
| 77 | `iscube` | 整数aを受け取り、この整数がある整数の3乗である場合にTrue | テスト失敗(出力不一致) | テストを失敗 🔍iscube(1) ❌true ✅1 line 26, column 1: |
| 80 | `is_happy` | あなたは文字列sが与えられる。 | テスト失敗(出力不一致) | テストを失敗 🔍is_happy("a") ❌false ✅0 line 28, column 1: |
| 82 | `prime_length` | 文字列を受け取り、文字列の長さが素数であればTrueを、そうでなければFalseを返す関数を書く。 | テスト失敗(出力不一致) | テストを失敗 🔍prime_length("Hello") ❌true ✅1 line 25, column 1: |
| 83 | `starts_one_ends` | 正の整数 n が与えられたとき、n 桁の正の整数で 1 で始まるか | 構文エラー | 関数が定義されていません ❌冪 line 8, column 14: |
| 84 | `solve` | 正の整数 N が与えられた時、その桁の総和を2進数で返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 90 | `next_smallest` | 整数のリストが与えられる。 | テスト失敗(出力不一致) | テストを失敗 🔍next_smallest([1, 2, 3, 4, 5]) ❌2 ✅[2] line 30, column 1: |
| 92 | `any_int` | 3つの数値を受け取る関数を作る。 | テスト失敗(出力不一致) | テストを失敗 🔍any_int(2, 3, 1) ❌true ✅1 line 28, column 1: |
| 93 | `encode` | メッセージを受け取り、すべての文字の大文字と小文字を入れ替え、 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 95 | `check_dict_case` | 辞書が与えられたとき、すべてのキーが小文字であればTrueを、 | テスト失敗(出力不一致) | テストを失敗 🔍check_dict_case({"p":"pineapple", "b":"banana"}) ❌false ✅1 line 44, column 1: |
| 102 | `choose_num` | この関数は2つの正の数xとyを受け取り、範囲[x, y]（両端を含む）に含まれる | テスト失敗(出力不一致) | テストを失敗 🔍choose_num(7, 7) ❌6 ✅-1 line 28, column 1: |
| 103 | `rounded_avg` | 2つの正の整数nとmが与えられており、あなたのタスクはnからmまでの | テスト失敗(出力不一致) | テストを失敗 🔍rounded_avg(964,977) ❌"0b1111001011" ✅"0b1111001010" line 67, column 1: |
| 104 | `unique_digits` | 正の整数xのリストが与えられたとき、偶数桁の要素を持たない全ての | テスト失敗(出力不一致) | テストを失敗 🔍unique_digits([15, 33, 1422, 1]) ❌[1, 15] ✅[1, 15, 33] line 53, column 1: |
| 106 | `f` | iは1から始まる。iの階乗は1からiまでの数の掛け算（1 * 2 * ... * i）である。 | テスト失敗(出力不一致) | テストを失敗 🔍f(5) ❌[1, 2, 6, 24, 120] ✅[1, 2, 6, 24, 15] line 18, column 1: |
| 108 | `count_nums` | count_nums 関数は、整数の配列を引数として受け取り、その配列内の各整数の各桁の合計が | 構文エラー | index-error ✅<2 ❌2 🔍[45, 49] line 14, column 14: |
| 109 | `move_one_ball` | N個の整数arr[1], arr[2], ..., arr[N]なる配列 'arr' があります。 | テスト失敗(出力不一致) | テストを失敗 🔍move_one_ball([3, 4, 5, 1, 2]) ❌true ✅1 line 33, column 1: |
| 111 | `histogram` | 空白で区切られた小文字を表す文字列が与えられる。最も出現回数が多い文字と | テスト失敗(出力不一致) | テストを失敗 🔍histogram([97, 32, 98, 32, 98, 32, 97]) ❌{"97": 1, "98": 1} ✅[[[97], 2], [[98], 2]] line 48, column 1: |
| 113 | `odd_count` | 数字のみで構成された文字列のリストを引数として受け取り、新しいリストを返します。 | テスト失敗(出力不一致) | テストを失敗 🔍odd_count(["1234567"]) ❌["the number of odd elements 0n the str0ng 0 of the 0nput."] ✅["the number of odd elements 4n the str4ng 4 of the 4nput."] line |
| 116 | `sort_array` | この問題では、非負整数の配列を2進数表現における"1"の個数を昇順でソートする。 | テスト失敗(出力不一致) | テストを失敗 🔍sort_array([-2,-3,-4,-5,-6]) ❌[-2, -4, -3, -6, -5] ✅[-4, -2, -6, -5, -3] line 69, column 1: |
| 117 | `select_words` | ある文字列sと自然数nが与えらる。あなたに課せられたタスクは、文字列s | テスト失敗(出力不一致) | テストを失敗 🔍select_words("Mary had a little lamb", 4) ❌["Mary", "lamb"] ✅["little"] line 42, column 1: |
| 123 | `get_odd_collatz` | 正の整数nが与えられたとき、コラッツ数列の奇数を持つソートされたリストを返す。 | テスト失敗(出力不一致) | テストを失敗 🔍get_odd_collatz(14) ❌[5, 7, 11, 13, 17] ✅[1, 5, 7, 11, 13, 17] line 51, column 1: |
| 124 | `valid_date` | 与えられた日付文字列を検証し、その日付が有効であればTrueを、そうでなければFalseを返す関数を書く必要がある。 | テスト失敗(出力不一致) | テストを失敗 🔍valid_date("03-11-2000") ❌true ✅1 line 111, column 1: |
| 125 | `split_words` | 単語の文字列が与えられた場合、空白で分割された単語のリストを返す。 | テスト失敗(出力不一致) | テストを失敗 🔍split_words("Hello world!") ❌5 ✅["Hello", "world!"] line 63, column 1: |
| 126 | `is_sorted` | 数字のリストが与えられたとき、昇順に整列されているかどうかを返す。 | テスト失敗(出力不一致) | テストを失敗 🔍is_sorted([5]) ❌true ✅1 line 36, column 1: |
| 127 | `intersection` | 2つの区間が与えられます。 | テスト失敗(出力不一致) | テストを失敗 🔍intersection([-1, 1], [0, 4]) ❌"YES" ✅"NO" line 47, column 1: |
| 128 | `prod_signs` | 整数の配列 arr が与えられます。この配列に含まれる各数値の絶対値の合計と、 | テスト失敗(出力不一致) | テストを失敗 🔍prod_signs([1, 2, 2, -4]) ❌-9 ✅[-9] line 33, column 1: |
| 129 | `minPath` | N行とN列 (N >= 2)) のグリッドと正の整数kが与えられた場合、各セルには値が含まれている。 | 構文エラー | index-error ✅<0 ❌0 🔍[] line 48, column 33: |
| 130 | `tri` | フィボナッチ数列は、ここ数世紀の間に数学者によって深く研究され、誰もが知っている。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 132 | `is_nested` | この関数は、角括弧だけを含む文字列を入力として受け取ります。括弧が有効な順序で | テスト失敗(出力不一致) | テストを失敗 🔍is_nested("[[]]") ❌true ✅1 line 35, column 1: |
| 133 | `sum_squares` | 数字のリストが与えられます。 | 構文エラー | 関数が定義されていません ❌切り上げ line 7, column 11: |
| 134 | `check_if_last_char_is_a_letter` | 与えられた文字列の最後の文字がアルファベットであり、かつ単語の一部でなければTrueを、 | テスト失敗(出力不一致) | テストを失敗 🔍check_if_last_char_is_a_letter("apple") ❌false ✅0 line 41, column 1: |
| 136 | `largest_smallest_integers` | リストから最も大きな負の整数と最も小さな正の整数を見つけ、それらをタプル（a, b） | テスト失敗(出力不一致) | テストを失敗 🔍largest_smallest_integers([2, 4, 1, 3, 5, 7]) ❌[null, 1] ✅[[], 1] line 38, column 1: |
| 137 | `compare_one` | 整数、浮動小数点数、または実数を表す文字列を引数として受け取り、その中で最も大きい値を | テスト失敗(出力不一致) | テストを失敗 🔍compare_one(1, "2,3") ❌"2.3" ✅"2,3" line 51, column 1: |
| 138 | `is_equal_to_sum_even` | 与えられた数値nが、ちょうど4つの正の偶数の合計として表現できるかどうかを評価してください。 | テスト失敗(出力不一致) | テストを失敗 🔍is_equal_to_sum_even(4) ❌false ✅0 line 13, column 1: |
| 139 | `special_factorial` | ブラジリアン階乗は次のように定義される： | テスト失敗(出力不一致) | テストを失敗 🔍special_factorial(4) ❌27648 ✅288 line 15, column 1: |
| 140 | `fix_spaces` | 文字列テキストが与えられた場合、その中のすべての空白をアンダースコアに置換し、 | テスト失敗(出力不一致) | テストを失敗 🔍fix_spaces("Yellow Yellow Dirty Fellow") ❌"Yellow_Yellow-Dirty-Fellow" ✅"Yellow_Yellow__Dirty__Fellow" line 48, column 1: |
| 141 | `file_name_check` | ファイル名を表す文字列を受け取り、そのファイル名が有効であれば'Yes'を返し、そうでなければ'No' | テスト失敗(出力不一致) | テストを失敗 🔍file_name_check("His12FILE94.exe") ❌"Yes" ✅"No" line 114, column 1: |
| 144 | `simplify` | あなたの仕事は、式 x * n を簡単にする関数を実装することです。 | テスト失敗(出力不一致) | テストを失敗 🔍simplify("1/5", "5/1") ❌true ✅1 line 53, column 1: |
| 145 | `order_by_points` | 各数字の桁の合計に基づいて、与えられた整数のリストを昇順に並べる | テスト失敗(出力不一致) | テストを失敗 🔍order_by_points([1, 11, -1, -11, -12]) ❌[1, -1, 11, -11, -12] ✅[-1, -11, 1, -12, 11] line 55, column 1: |
| 147 | `get_max_triples` | 正の整数 n が与えられるので、長さ n の整数配列 a を作成せよ。 | テスト失敗(出力不一致) | テストを失敗 🔍get_max_triples(5) ❌[[1, 7, 13]] ✅1 line 40, column 1: |
| 148 | `bf` | 私たちの太陽系には8つの惑星があります：太陽に最も近いのはVenus, Earth, Mars, Jupiter, Saturn, | テスト失敗(出力不一致) | テストを失敗 🔍bf("Earth", "Earth") ❌["Mars"] ✅[] line 52, column 1: |
| 152 | `compare` | 待ち望んでいた出来事の結果がようやく判明したときの感覚は、誰もが覚えていると思う。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 154 | `cycpattern_check` | 2つの単語が与えられる。2番目の単語またはその回転させた文字列が最初の単語の部分文字列である場合、Trueを返す必要がある。 | テスト失敗(出力不一致) | テストを失敗 🔍cycpattern_check("xyzw","xyw") ❌false ✅0 line 52, column 1: |
| 157 | `right_angle_triangle` | 三角形の3辺の長さを与える。三角形が直角三角形ならTrueを、そうでなければFalseを返す。 | テスト失敗(出力不一致) | テストを失敗 🔍right_angle_triangle(3, 4, 5) ❌true ✅1 line 27, column 1: |
| 160 | `do_algebra` | 演算子(operator)とオペランド(operand)の2つのリストが与えられる。ひとつ目のリストは | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 161 | `solve` | 文字列sが与えられます。 | テスト失敗(出力不一致) | テストを失敗 🔍solve("AsDf") ❌"asdf" ✅"aSdF" line 41, column 1: |
| 162 | `string_to_md5` | 文字列 text が与えられたとき、その md5 ハッシュと等価な文字列を返す。 | 構文エラー | 関数が定義されていません ❌md5 line 7, column 4: |
| 163 | `generate_integers` | 正の整数aとbが与えられたとき、aとbの間にある偶数の数字を昇順で返してください。 | テスト失敗(出力不一致) | テストを失敗 🔍generate_integers(2, 10) ❌[2, 4, 6, 8, 10] ✅[2, 4, 6, 8] line 29, column 1: |
