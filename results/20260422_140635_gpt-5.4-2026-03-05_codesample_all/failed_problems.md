# 失敗問題一覧 — 20260422_140635_gpt-5.4-2026-03-05_codesample_all

- モデル: gpt-5.4-2026-03-05
- 言語: ja / テンプレート: pro159/codesample_all.md
- 合計: **164問中 79問失敗** (pass@1 = 51.83%)

## 失敗原因サマリ

| 原因 | 件数 |
|------|------|
| テスト失敗(出力不一致) | 38 |
| 構文エラー | 25 |
| 構文認識不可(Yui非準拠) | 16 |

### 原因の意味

- **構文認識不可(Yui非準拠)**: Yuiパーサが文法として受理できず、そもそもコードとして実行されなかった
- **構文エラー**: パース自体は通ったが実行中に文法エラーで停止
- **テスト失敗(出力不一致)**: 実行は完了したがテストの期待値と異なる

## 失敗問題リスト

| タスクID | 関数 | 問題概要 | 失敗原因 | エラー詳細 |
|---------|------|---------|---------|-----------|
| 0 | `has_close_elements` | リストnumbersの中に、与えられたthresholdより近い２つの数値が存在するか判定する | テスト失敗(出力不一致) | テストを失敗 🔍has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) ❌true ✅1 line 22, column 1: |
| 3 | `below_zero` | 銀行口座に対する入出金操作のリストが与えられます。あなたのタスクは、残高ゼロから | テスト失敗(出力不一致) | テストを失敗 🔍below_zero([]) ❌false ✅0 line 17, column 1: |
| 7 | `filter_by_substring` | 文字列リストstringsを、与えれた部分文字列substringを含むものだけにフィルタする | 構文エラー | 関数が定義されていません ❌find line 9, column 11: |
| 10 | `make_palindrome` | 与えられた文字列が回文かどうかをテストします。 | テスト失敗(出力不一致) | テストを失敗 🔍make_palindrome("") ❌true ✅"" line 18, column 1: |
| 11 | `string_xor` | 引数は1と0のみからなる文字列aとbである。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 12 | `longest` | 文字列のリストのうち、最も長いものを返す。同じ長さの文字列が | テスト失敗(出力不一致) | テストを失敗 🔍longest([]) ❌null ✅"" line 25, column 1: |
| 20 | `find_closest_elements` | （少なくとも長さ2以上の）リストnumbersから、互いに最も近いものを2つ選び、 | 構文エラー | index-error ✅<6 ❌6 🔍[1.0, 2.0, 2.2, 3.9, 4.0, 5.0] line 14, column 9: |
| 22 | `filter_integers` | 任意の種類の値が含まれるリストから整数値のみ抽出する | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 31 | `is_prime` | 与えられた数が素数であれば真を、そうでなければ偽を返す。 | テスト失敗(出力不一致) | テストを失敗 🔍is_prime(6) ❌false ✅0 line 23, column 1: |
| 32 | `find_zero` | 点xにおける係数xsを持つ多項式の値を計算する。 | 構文エラー | 関数が定義されていません ❌approx_zero line 17, column 5: |
| 38 | `decode_cyclic` | 3文字ごとに循環させてエンコードした文字列を返す。 | 構文エラー | サポートされていない演算子です 🔍+ line 14, column 17: |
| 39 | `prime_fib` | prime_fib はフィボナッチ数で、かつ素数であるn番目の数を返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 40 | `triples_sum_to_zero` | triples_sum_to_zero は整数のリストを引数に取り、 | テスト失敗(出力不一致) | テストを失敗 🔍triples_sum_to_zero([1, 3, 5, 0]) ❌false ✅0 line 31, column 1: |
| 42 | `incr_list` | 要素を1ずつ増やしたリストを返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 43 | `pairs_sum_to_zero` | pairs_sum_to_zero は整数のリストを引数にとる。 | テスト失敗(出力不一致) | テストを失敗 🔍pairs_sum_to_zero([1, 3, 5, 0]) ❌false ✅0 line 20, column 1: |
| 44 | `change_base` | 引数xの基数をbaseに変換する。 | 構文エラー | データの種類（型）が違っています ✅<🔢number> ❌"2" line 16, column 14: |
| 47 | `median` | リスト l の要素の中央値を返す。 | 構文エラー | 関数が定義されていません ❌bubble_sort line 4, column 6: |
| 48 | `is_palindrome` | 与えられた文字列が回文かどうかを判定する | テスト失敗(出力不一致) | テストを失敗 🔍is_palindrome("") ❌true ✅1 line 19, column 1: |
| 50 | `decode_shift` | アルファベットの各文字を5ずつずらしてエンコードした文字列を返す。 | テスト失敗(出力不一致) | テストを失敗 🔍decode_shift("ifcnmmjciacwhxsgfhlm") ❌"nkhsrrohnfhbmcxlkmqr" ✅"daxihhexdvxrcsnbacgh" line 37, column 1: |
| 52 | `below_threshold` | リスト l 内の全ての数値が閾値 t 以下の場合、Trueを返す。 | テスト失敗(出力不一致) | テストを失敗 🔍below_threshold([1, 2, 4, 10], 100) ❌true ✅1 line 15, column 1: |
| 54 | `same_chars` | 2つの単語が同じ文字セットから構成されるかどうか判定する。 | 構文エラー | 関数が定義されていません ❌unique_chars line 4, column 7: |
| 56 | `correct_bracketing` | 引数bracketsは"<"と">"の文字列である。 | テスト失敗(出力不一致) | テストを失敗 🔍correct_bracketing("<>") ❌true ✅1 line 29, column 1: |
| 57 | `monotonic` | リストの要素が単調増加または単調減少する場合にTrueを返す。 | テスト失敗(出力不一致) | テストを失敗 🔍monotonic([1, 2, 4, 10]) ❌true ✅1 line 34, column 1: |
| 58 | `common` | 2つのリストについて、ユニークな共通要素をソートして返す。 | 構文エラー | 関数が定義されていません ❌bubble_sort line 15, column 4: |
| 59 | `largest_prime_factor` | nの最大となる素因数を返す。ただし、 n > 1 を前提とし、素数ではないものとする。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 61 | `correct_bracketing` | 引数bracketsは"("と") "からなる文字列である。 | テスト失敗(出力不一致) | テストを失敗 🔍correct_bracketing("()") ❌true ✅1 line 33, column 1: |
| 62 | `derivative` | xsは多項式の係数列を表す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 64 | `vowels_count` | Add more test cases. | テスト失敗(出力不一致) | テストを失敗 🔍vowels_count("key") ❌1 ✅2 line 24, column 1: |
| 65 | `circular_shift` | 整数 x の桁を循環シフトする。shift 分だけ桁を右にシフトし、結果を文字列として返す。 | 構文エラー | 関数が定義されていません ❌reverse line 8, column 7: |
| 67 | `fruit_distribution` | この課題では、果物の入ったカゴに配られたリンゴとオレンジの数を表す文字列が | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 72 | `will_it_fly` | 物体qが飛べばTrueを、そうでなければFalseを返す関数を書け。 | テスト失敗(出力不一致) | テストを失敗 🔍will_it_fly([3, 2, 3], 9) ❌true ✅1 line 29, column 1: |
| 75 | `is_multiply_prime` | 与えられた数が3つの素数の掛け算であればTrueを、そうでなければFalseを返す | テスト失敗(出力不一致) | テストを失敗 🔍is_multiply_prime(5) ❌false ✅0 line 74, column 1: |
| 76 | `is_simple_power` | あなたのタスクは、ある数xがnの単純なべき乗である場合にtrueを、 | テスト失敗(出力不一致) | テストを失敗 🔍is_simple_power(16, 2) ❌true ✅1 line 25, column 1: |
| 77 | `iscube` | 整数aを受け取り、この整数がある整数の3乗である場合にTrue | テスト失敗(出力不一致) | テストを失敗 🔍iscube(1) ❌true ✅1 line 20, column 1: |
| 79 | `decimal_to_binary` | 10進数形式の数値が与えられ、あなたのタスクはそれを2進数形式に変換することである。 | 構文エラー | データの種類（型）が違っています ✅<🔢number> ❌"0" line 17, column 15: |
| 80 | `is_happy` | あなたは文字列sが与えられる。 | テスト失敗(出力不一致) | テストを失敗 🔍is_happy("a") ❌false ✅0 line 28, column 1: |
| 82 | `prime_length` | 文字列を受け取り、文字列の長さが素数であればTrueを、そうでなければFalseを返す関数を書く。 | テスト失敗(出力不一致) | テストを失敗 🔍prime_length("Hello") ❌true ✅1 line 25, column 1: |
| 83 | `starts_one_ends` | 正の整数 n が与えられたとき、n 桁の正の整数で 1 で始まるか | テスト失敗(出力不一致) | テストを失敗 🔍starts_one_ends(2) ❌19 ✅18 line 32, column 1: |
| 84 | `solve` | 正の整数 N が与えられた時、その桁の総和を2進数で返す。 | 構文エラー | 関数が定義されていません ❌reverse line 28, column 4: |
| 90 | `next_smallest` | 整数のリストが与えられる。 | テスト失敗(出力不一致) | テストを失敗 🔍next_smallest([1, 2, 3, 4, 5]) ❌2 ✅[2] line 36, column 1: |
| 92 | `any_int` | 3つの数値を受け取る関数を作る。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 94 | `skjkasdkd` | 整数のリストが与えらる。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 95 | `check_dict_case` | 辞書が与えられたとき、すべてのキーが小文字であればTrueを、 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 102 | `choose_num` | この関数は2つの正の数xとyを受け取り、範囲[x, y]（両端を含む）に含まれる | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 103 | `rounded_avg` | 2つの正の整数nとmが与えられており、あなたのタスクはnからmまでの | 構文エラー | 関数が定義されていません ❌文字列補間 line 34, column 24: |
| 104 | `unique_digits` | 正の整数xのリストが与えられたとき、偶数桁の要素を持たない全ての | テスト失敗(出力不一致) | テストを失敗 🔍unique_digits([15, 33, 1422, 1]) ❌[1] ✅[1, 15, 33] line 38, column 1: |
| 105 | `by_length` | 整数の配列が与えられたとき、1から9までの整数をソートし、 | 構文エラー | 関数が定義されていません ❌bubble_sort line 4, column 11: |
| 106 | `f` | iは1から始まる。iの階乗は1からiまでの数の掛け算（1 * 2 * ... * i）である。 | テスト失敗(出力不一致) | テストを失敗 🔍f(5) ❌[1, 2, 6, 24, 120] ✅[1, 2, 6, 24, 15] line 16, column 1: |
| 107 | `even_odd_palindrome` | 与えられた正の整数 nに対して、範囲 1 から n まで（両端を含む）に存在する | 構文エラー | 関数が定義されていません ❌reverse line 9, column 10: |
| 108 | `count_nums` | count_nums 関数は、整数の配列を引数として受け取り、その配列内の各整数の各桁の合計が | テスト失敗(出力不一致) | テストを失敗 🔍count_nums([12, 23, 34, -45, -56, 0]) ❌3 ✅5 line 48, column 1: |
| 109 | `move_one_ball` | N個の整数arr[1], arr[2], ..., arr[N]なる配列 'arr' があります。 | テスト失敗(出力不一致) | テストを失敗 🔍move_one_ball([3, 4, 5, 1, 2]) ❌true ✅1 line 32, column 1: |
| 111 | `histogram` | 空白で区切られた小文字を表す文字列が与えられる。最も出現回数が多い文字と | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 116 | `sort_array` | この問題では、非負整数の配列を2進数表現における"1"の個数を昇順でソートする。 | 構文エラー | 関数が定義されていません ❌rshift line 17, column 9: |
| 123 | `get_odd_collatz` | 正の整数nが与えられたとき、コラッツ数列の奇数を持つソートされたリストを返す。 | 構文エラー | 関数が定義されていません ❌bubble_sort line 27, column 4: |
| 124 | `valid_date` | 与えられた日付文字列を検証し、その日付が有効であればTrueを、そうでなければFalseを返す関数を書く必要がある。 | テスト失敗(出力不一致) | テストを失敗 🔍valid_date("03-11-2000") ❌true ✅1 line 117, column 1: |
| 125 | `split_words` | 単語の文字列が与えられた場合、空白で分割された単語のリストを返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 126 | `is_sorted` | 数字のリストが与えられたとき、昇順に整列されているかどうかを返す。 | テスト失敗(出力不一致) | テストを失敗 🔍is_sorted([5]) ❌true ✅1 line 36, column 1: |
| 128 | `prod_signs` | 整数の配列 arr が与えられます。この配列に含まれる各数値の絶対値の合計と、 | テスト失敗(出力不一致) | テストを失敗 🔍prod_signs([1, 2, 2, -4]) ❌-9 ✅[-9] line 31, column 1: |
| 129 | `minPath` | N行とN列 (N >= 2)) のグリッドと正の整数kが与えられた場合、各セルには値が含まれている。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 131 | `digits` | 正の整数 n が与えられた時、奇数桁数の積を返す。 | テスト失敗(出力不一致) | テストを失敗 🔍digits(5) ❌53 ✅5 line 23, column 1: |
| 132 | `is_nested` | この関数は、角括弧だけを含む文字列を入力として受け取ります。括弧が有効な順序で | テスト失敗(出力不一致) | テストを失敗 🔍is_nested("[[]]") ❌true ✅1 line 30, column 1: |
| 133 | `sum_squares` | 数字のリストが与えられます。 | 構文エラー | 関数が定義されていません ❌天井 line 8, column 9: |
| 134 | `check_if_last_char_is_a_letter` | 与えられた文字列の最後の文字がアルファベットであり、かつ単語の一部でなければTrueを、 | テスト失敗(出力不一致) | テストを失敗 🔍check_if_last_char_is_a_letter("apple") ❌false ✅0 line 40, column 1: |
| 135 | `can_arrange` | 直前の要素よりも大きくない要素の中で、最も大きなインデックスを持つ要素を探して | 構文エラー | index-error ✅<0 ❌1 🔍[] line 9, column 9: |
| 136 | `largest_smallest_integers` | リストから最も大きな負の整数と最も小さな正の整数を見つけ、それらをタプル（a, b） | テスト失敗(出力不一致) | テストを失敗 🔍largest_smallest_integers([2, 4, 1, 3, 5, 7]) ❌[null, 1] ✅[[], 1] line 38, column 1: |
| 137 | `compare_one` | 整数、浮動小数点数、または実数を表す文字列を引数として受け取り、その中で最も大きい値を | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 138 | `is_equal_to_sum_even` | 与えられた数値nが、ちょうど4つの正の偶数の合計として表現できるかどうかを評価してください。 | テスト失敗(出力不一致) | テストを失敗 🔍is_equal_to_sum_even(4) ❌false ✅0 line 16, column 1: |
| 140 | `fix_spaces` | 文字列テキストが与えられた場合、その中のすべての空白をアンダースコアに置換し、 | 構文エラー | index-error ✅<28 ❌28 🔍[89, 101, 108, 108, 111, 119, 32, 89, 101, 108, 108, 111, 119, 32, 32, 68, 105, 114, 116, 121, 32, 32, 70, 101, 108, 108, 111, 119] line 9 |
| 141 | `file_name_check` | ファイル名を表す文字列を受け取り、そのファイル名が有効であれば'Yes'を返し、そうでなければ'No' | テスト失敗(出力不一致) | テストを失敗 🔍file_name_check("His12FILE94.exe") ❌"Yes" ✅"No" line 99, column 1: |
| 144 | `simplify` | あなたの仕事は、式 x * n を簡単にする関数を実装することです。 | 構文エラー | 関数が定義されていません ❌分割 line 4, column 7: |
| 145 | `order_by_points` | 各数字の桁の合計に基づいて、与えられた整数のリストを昇順に並べる | テスト失敗(出力不一致) | テストを失敗 🔍order_by_points([1, 11, -1, -11, -12]) ❌[1, -1, 11, -11, -12] ✅[-1, -11, 1, -12, 11] line 62, column 1: |
| 151 | `double_the_difference` | 数字のリストが与えられた場合、そのリスト内の奇数の数値の二乗の合計を返してください。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 154 | `cycpattern_check` | 2つの単語が与えられる。2番目の単語またはその回転させた文字列が最初の単語の部分文字列である場合、Trueを返す必要がある。 | 構文エラー | 関数が定義されていません ❌find line 34, column 9: |
| 157 | `right_angle_triangle` | 三角形の3辺の長さを与える。三角形が直角三角形ならTrueを、そうでなければFalseを返す。 | テスト失敗(出力不一致) | テストを失敗 🔍right_angle_triangle(3, 4, 5) ❌true ✅1 line 32, column 1: |
| 158 | `find_max` | 文字列のリストを受け取る関数を書きなさい。 | 構文エラー | 関数が定義されていません ❌unique_chars line 5, column 15: |
| 160 | `do_algebra` | 演算子(operator)とオペランド(operand)の2つのリストが与えられる。ひとつ目のリストは | 構文エラー | int-conversion ❌2**3*4+5 🔥could not convert string to float: '2**3*4+5' line 11, column 4: |
| 161 | `solve` | 文字列sが与えられます。 | 構文エラー | 関数が定義されていません ❌reverse line 33, column 7: |
| 162 | `string_to_md5` | 文字列 text が与えられたとき、その md5 ハッシュと等価な文字列を返す。 | 構文エラー | 関数が定義されていません ❌md5 line 7, column 4: |
| 163 | `generate_integers` | 正の整数aとbが与えられたとき、aとbの間にある偶数の数字を昇順で返してください。 | テスト失敗(出力不一致) | テストを失敗 🔍generate_integers(2, 10) ❌[4, 6, 8] ✅[2, 4, 6, 8] line 31, column 1: |
