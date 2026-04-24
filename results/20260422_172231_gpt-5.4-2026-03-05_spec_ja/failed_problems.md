# 失敗問題一覧 — 20260422_172231_gpt-5.4-2026-03-05_spec_ja

- モデル: gpt-5.4-2026-03-05
- 言語: ja / テンプレート: pro159/spec_ja.md
- 合計: **164問中 95問失敗** (pass@1 = 42.07%)

## 失敗原因サマリ

| 原因 | 件数 |
|------|------|
| テスト失敗(出力不一致) | 60 |
| 構文認識不可(Yui非準拠) | 27 |
| 構文エラー | 8 |

### 原因の意味

- **構文認識不可(Yui非準拠)**: Yuiパーサが文法として受理できず、そもそもコードとして実行されなかった
- **構文エラー**: パース自体は通ったが実行中に文法エラーで停止
- **テスト失敗(出力不一致)**: 実行は完了したがテストの期待値と異なる

## 失敗問題リスト

| タスクID | 関数 | 問題概要 | 失敗原因 | エラー詳細 |
|---------|------|---------|---------|-----------|
| 0 | `has_close_elements` | リストnumbersの中に、与えられたthresholdより近い２つの数値が存在するか判定する | テスト失敗(出力不一致) | テストを失敗 🔍has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) ❌true ✅1 line 22, column 1: |
| 1 | `separate_paren_groups` | この関数への入力は、入れ子になった括弧が複数含まれる文字列である。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 3 | `below_zero` | 銀行口座に対する入出金操作のリストが与えられます。あなたのタスクは、残高ゼロから | テスト失敗(出力不一致) | テストを失敗 🔍below_zero([]) ❌false ✅0 line 17, column 1: |
| 10 | `make_palindrome` | 与えられた文字列が回文かどうかをテストします。 | テスト失敗(出力不一致) | テストを失敗 🔍make_palindrome("") ❌true ✅"" line 19, column 1: |
| 11 | `string_xor` | 引数は1と0のみからなる文字列aとbである。 | テスト失敗(出力不一致) | テストを失敗 🔍string_xor("111000", "101010") ❌"[48, 49, 48, 48, 49, 48]" ✅"010010" line 19, column 1: |
| 12 | `longest` | 文字列のリストのうち、最も長いものを返す。同じ長さの文字列が | テスト失敗(出力不一致) | テストを失敗 🔍longest([]) ❌null ✅"" line 22, column 1: |
| 17 | `parse_music` | この関数の引数は、特別なASCII形式の音符を表す文字列である。あなたの仕事は、この文字列を解析して、それぞれの音符が何拍続くかに対応する整数のリストを返すことである。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 20 | `find_closest_elements` | （少なくとも長さ2以上の）リストnumbersから、互いに最も近いものを2つ選び、 | テスト失敗(出力不一致) | テストを失敗 🔍find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) ❌[1.000000, 2.000000] ✅[5.000000, 5.900000] line 29, column 1: |
| 26 | `remove_duplicates` | 整数のリストから、複数回出現する要素をすべて取り除く。 | 構文エラー | index-error ✅<0 ❌1 🔍[] line 8, column 8: |
| 27 | `flip_case` | 与えられた文字列に対して、英小文字を英大文字に、英大文字を英小文字に変換する。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 31 | `is_prime` | 与えられた数が素数であれば真を、そうでなければ偽を返す。 | テスト失敗(出力不一致) | テストを失敗 🔍is_prime(6) ❌false ✅0 line 30, column 1: |
| 32 | `find_zero` | 点xにおける係数xsを持つ多項式の値を計算する。 | 構文エラー | 関数が定義されていません ❌approx_zero line 16, column 5: |
| 34 | `unique` | リスト内のユニークな要素をソートして返す | 構文エラー | index-error ✅<6 ❌6 🔍[5, 3, 2, 9, 0, 123] line 33, column 19: |
| 36 | `fizz_buzz` | 11または13で割り切れるn未満の整数の中に7という数字が現れる回数を返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 38 | `decode_cyclic` | 3文字ごとに循環させてエンコードした文字列を返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 40 | `triples_sum_to_zero` | triples_sum_to_zero は整数のリストを引数に取り、 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 42 | `incr_list` | 要素を1ずつ増やしたリストを返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 43 | `pairs_sum_to_zero` | pairs_sum_to_zero は整数のリストを引数にとる。 | テスト失敗(出力不一致) | テストを失敗 🔍pairs_sum_to_zero([1, 3, 5, 0]) ❌false ✅0 line 22, column 1: |
| 45 | `triangle_area` | 三角形の一辺の長さと高さが与えられたとき、面積を返す。 | テスト失敗(出力不一致) | テストを失敗 🔍triangle_area(5, 3) ❌7 ✅7.500000 line 8, column 1: |
| 47 | `median` | リスト l の要素の中央値を返す。 | テスト失敗(出力不一致) | テストを失敗 🔍median([3, 1, 2, 4, 5]) ❌2 ✅3 line 30, column 1: |
| 48 | `is_palindrome` | 与えられた文字列が回文かどうかを判定する | テスト失敗(出力不一致) | テストを失敗 🔍is_palindrome("") ❌true ✅1 line 19, column 1: |
| 50 | `decode_shift` | アルファベットの各文字を5ずつずらしてエンコードした文字列を返す。 | テスト失敗(出力不一致) | テストを失敗 🔍decode_shift("ifcnmmjciacwhxsgfhlm") ❌"[110, 107, 104, 115, 114, 114, 111, 104, 110, 102, 104, 98, 109, 99, 120, 108, 107, 109, 113, 114]" ✅"daxihhexdvx |
| 52 | `below_threshold` | リスト l 内の全ての数値が閾値 t 以下の場合、Trueを返す。 | テスト失敗(出力不一致) | テストを失敗 🔍below_threshold([1, 2, 4, 10], 100) ❌true ✅1 line 15, column 1: |
| 54 | `same_chars` | 2つの単語が同じ文字セットから構成されるかどうか判定する。 | テスト失敗(出力不一致) | テストを失敗 🔍same_chars("eabcdzzzz", "dddzzzzzzzddeddabc") ❌true ✅1 line 41, column 1: |
| 55 | `fib` | n番目のフィボナッチ数を返す。 | テスト失敗(出力不一致) | テストを失敗 🔍fib(10) ❌89 ✅55 line 26, column 1: |
| 56 | `correct_bracketing` | 引数bracketsは"<"と">"の文字列である。 | テスト失敗(出力不一致) | テストを失敗 🔍correct_bracketing("<>") ❌false ✅1 line 27, column 1: |
| 57 | `monotonic` | リストの要素が単調増加または単調減少する場合にTrueを返す。 | テスト失敗(出力不一致) | テストを失敗 🔍monotonic([1, 2, 4, 10]) ❌true ✅1 line 31, column 1: |
| 59 | `largest_prime_factor` | nの最大となる素因数を返す。ただし、 n > 1 を前提とし、素数ではないものとする。 | テスト失敗(出力不一致) | テストを失敗 🔍largest_prime_factor(15) ❌15 ✅5 line 30, column 1: |
| 61 | `correct_bracketing` | 引数bracketsは"("と") "からなる文字列である。 | テスト失敗(出力不一致) | テストを失敗 🔍correct_bracketing("()") ❌false ✅1 line 27, column 1: |
| 62 | `derivative` | xsは多項式の係数列を表す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 64 | `vowels_count` | Add more test cases. | テスト失敗(出力不一致) | テストを失敗 🔍vowels_count("abcde") ❌0 ✅2 line 37, column 1: |
| 65 | `circular_shift` | 整数 x の桁を循環シフトする。shift 分だけ桁を右にシフトし、結果を文字列として返す。 | テスト失敗(出力不一致) | テストを失敗 🔍circular_shift(100, 2) ❌"[48, 48, 49]" ✅"001" line 34, column 1: |
| 67 | `fruit_distribution` | この課題では、果物の入ったカゴに配られたリンゴとオレンジの数を表す文字列が | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 69 | `search` | 正の整数の空でないリストが与えられる。0より大きく、その整数自身の値以上の頻度を | 構文エラー | index-error ✅<0 ❌5 🔍[] line 12, column 10: |
| 71 | `triangle_area` | 三角形の3辺の長さが与えられた。3辺が有効な三角形を形成していれば、 | テスト失敗(出力不一致) | テストを失敗 🔍triangle_area(4, 8, 5) ❌0 ✅8.180000 line 30, column 1: |
| 72 | `will_it_fly` | 物体qが飛べばTrueを、そうでなければFalseを返す関数を書け。 | テスト失敗(出力不一致) | テストを失敗 🔍will_it_fly([3, 2, 3], 9) ❌true ✅1 line 32, column 1: |
| 74 | `total_match` | ２つの文字列リストを受け取り、リストの全文字数の合計がもう一方 | テスト失敗(出力不一致) | テストを失敗 🔍total_match(["hi", "admin"], ["hi", "hi"]) ❌["hi", "admin"] ✅["hi", "hi"] line 34, column 1: |
| 75 | `is_multiply_prime` | 与えられた数が3つの素数の掛け算であればTrueを、そうでなければFalseを返す | テスト失敗(出力不一致) | テストを失敗 🔍is_multiply_prime(5) ❌false ✅0 line 67, column 1: |
| 76 | `is_simple_power` | あなたのタスクは、ある数xがnの単純なべき乗である場合にtrueを、 | テスト失敗(出力不一致) | テストを失敗 🔍is_simple_power(16, 2) ❌true ✅1 line 20, column 1: |
| 77 | `iscube` | 整数aを受け取り、この整数がある整数の3乗である場合にTrue | テスト失敗(出力不一致) | テストを失敗 🔍iscube(1) ❌true ✅1 line 26, column 1: |
| 78 | `hex_key` | 16進数の数字を文字列として受け取り、その中に含まれる素数である16進数の桁数を | テスト失敗(出力不一致) | テストを失敗 🔍hex_key("AB") ❌0 ✅1 line 42, column 1: |
| 79 | `decimal_to_binary` | 10進数形式の数値が与えられ、あなたのタスクはそれを2進数形式に変換することである。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 80 | `is_happy` | あなたは文字列sが与えられる。 | テスト失敗(出力不一致) | テストを失敗 🔍is_happy("a") ❌false ✅0 line 28, column 1: |
| 82 | `prime_length` | 文字列を受け取り、文字列の長さが素数であればTrueを、そうでなければFalseを返す関数を書く。 | テスト失敗(出力不一致) | テストを失敗 🔍prime_length("Hello") ❌true ✅1 line 24, column 1: |
| 83 | `starts_one_ends` | 正の整数 n が与えられたとき、n 桁の正の整数で 1 で始まるか | テスト失敗(出力不一致) | テストを失敗 🔍starts_one_ends(2) ❌1 ✅18 line 14, column 1: |
| 84 | `solve` | 正の整数 N が与えられた時、その桁の総和を2進数で返す。 | テスト失敗(出力不一致) | テストを失敗 🔍solve(1000) ❌"[\"1\"]" ✅"1" line 53, column 1: |
| 86 | `anti_shuffle` | 文字列を引数として受け取り、その「順序付けられたバージョン」を返す関数を作成してください。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 89 | `encrypt` | 文字列を引数にとり、アルファベットを回転させて暗号化した | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 90 | `next_smallest` | 整数のリストが与えられる。 | テスト失敗(出力不一致) | テストを失敗 🔍next_smallest([1, 2, 3, 4, 5]) ❌null ✅[2] line 43, column 1: |
| 91 | `is_bored` | 単語の文字列が与えられ、あなたのタスクは退屈指数を数える | 構文エラー | index-error ✅>=0 ❌-1 line 12, column 18: |
| 92 | `any_int` | 3つの数値を受け取る関数を作る。 | テスト失敗(出力不一致) | テストを失敗 🔍any_int(2, 3, 1) ❌true ✅1 line 38, column 1: |
| 93 | `encode` | メッセージを受け取り、すべての文字の大文字と小文字を入れ替え、 | テスト失敗(出力不一致) | テストを失敗 🔍encode("Mudasir") ❌[109, 83, 68, 67, 83, 75, 82] ✅"mWDCSKR" line 64, column 1: |
| 95 | `check_dict_case` | 辞書が与えられたとき、すべてのキーが小文字であればTrueを、 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 96 | `count_up_to` | 非負整数を受け取り、素数でnより小さい最初のn個の | テスト失敗(出力不一致) | テストを失敗 🔍count_up_to(5) ❌[2, 3, 5] ✅[2, 3] line 35, column 1: |
| 100 | `make_a_pile` | 正の整数nが与えられたとき、n段の石の山を作らなければならない。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 101 | `words_string` | カンマまたは空白で区切られた単語の文字列が与えられる。あなたのタスクは、 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 103 | `rounded_avg` | 2つの正の整数nとmが与えられており、あなたのタスクはnからmまでの | テスト失敗(出力不一致) | テストを失敗 🔍rounded_avg(1, 5) ❌"0b3" ✅"0b11" line 20, column 1: |
| 104 | `unique_digits` | 正の整数xのリストが与えられたとき、偶数桁の要素を持たない全ての | テスト失敗(出力不一致) | テストを失敗 🔍unique_digits([15, 33, 1422, 1]) ❌[1, 15] ✅[1, 15, 33] line 50, column 1: |
| 105 | `by_length` | 整数の配列が与えられたとき、1から9までの整数をソートし、 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 106 | `f` | iは1から始まる。iの階乗は1からiまでの数の掛け算（1 * 2 * ... * i）である。 | テスト失敗(出力不一致) | テストを失敗 🔍f(5) ❌[1, 2, 6, 24, 120] ✅[1, 2, 6, 24, 15] line 16, column 1: |
| 107 | `even_odd_palindrome` | 与えられた正の整数 nに対して、範囲 1 から n まで（両端を含む）に存在する | テスト失敗(出力不一致) | テストを失敗 🔍even_odd_palindrome(123) ❌[32, 34] ✅[8, 13] line 44, column 1: |
| 108 | `count_nums` | count_nums 関数は、整数の配列を引数として受け取り、その配列内の各整数の各桁の合計が | テスト失敗(出力不一致) | テストを失敗 🔍count_nums([1, 1, 2, -2, 3, 4, 5]) ❌3 ✅6 line 50, column 1: |
| 109 | `move_one_ball` | N個の整数arr[1], arr[2], ..., arr[N]なる配列 'arr' があります。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 111 | `histogram` | 空白で区切られた小文字を表す文字列が与えられる。最も出現回数が多い文字と | テスト失敗(出力不一致) | テストを失敗 🔍histogram([97, 32, 98, 32, 98, 32, 97]) ❌{"a": 1, "b": 1} ✅[[[97], 2], [[98], 2]] line 66, column 1: |
| 117 | `select_words` | ある文字列sと自然数nが与えらる。あなたに課せられたタスクは、文字列s | テスト失敗(出力不一致) | テストを失敗 🔍select_words("Mary had a little lamb", 4) ❌[] ✅["little"] line 84, column 1: |
| 118 | `get_closest_vowel` | 単語が与えられる。あなたの仕事は、単語の右側から2つの子音（大文字と | テスト失敗(出力不一致) | テストを失敗 🔍get_closest_vowel("yogurt") ❌"" ✅"u" line 34, column 1: |
| 120 | `maximum` | 整数の配列 arr と正の整数 k が与えられる。arr に含まれる大きい方から k 個の数を含む | 構文エラー | index-error ✅<3 ❌3 🔍[-3, -4, 5] line 12, column 10: |
| 124 | `valid_date` | 与えられた日付文字列を検証し、その日付が有効であればTrueを、そうでなければFalseを返す関数を書く必要がある。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 125 | `split_words` | 単語の文字列が与えられた場合、空白で分割された単語のリストを返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 126 | `is_sorted` | 数字のリストが与えられたとき、昇順に整列されているかどうかを返す。 | テスト失敗(出力不一致) | テストを失敗 🔍is_sorted([5]) ❌true ✅1 line 33, column 1: |
| 128 | `prod_signs` | 整数の配列 arr が与えられます。この配列に含まれる各数値の絶対値の合計と、 | テスト失敗(出力不一致) | テストを失敗 🔍prod_signs([1, 2, 2, -4]) ❌-9 ✅[-9] line 32, column 1: |
| 129 | `minPath` | N行とN列 (N >= 2)) のグリッドと正の整数kが与えられた場合、各セルには値が含まれている。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 130 | `tri` | フィボナッチ数列は、ここ数世紀の間に数学者によって深く研究され、誰もが知っている。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 132 | `is_nested` | この関数は、角括弧だけを含む文字列を入力として受け取ります。括弧が有効な順序で | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 134 | `check_if_last_char_is_a_letter` | 与えられた文字列の最後の文字がアルファベットであり、かつ単語の一部でなければTrueを、 | テスト失敗(出力不一致) | テストを失敗 🔍check_if_last_char_is_a_letter("apple") ❌false ✅0 line 50, column 1: |
| 135 | `can_arrange` | 直前の要素よりも大きくない要素の中で、最も大きなインデックスを持つ要素を探して | 構文エラー | index-error ✅<5 ❌5 🔍[1, 2, 4, 3, 5] line 8, column 12: |
| 136 | `largest_smallest_integers` | リストから最も大きな負の整数と最も小さな正の整数を見つけ、それらをタプル（a, b） | テスト失敗(出力不一致) | テストを失敗 🔍largest_smallest_integers([2, 4, 1, 3, 5, 7]) ❌[null, 1] ✅[[], 1] line 41, column 1: |
| 137 | `compare_one` | 整数、浮動小数点数、または実数を表す文字列を引数として受け取り、その中で最も大きい値を | 構文エラー | 小数への変換エラーです ❌2,3 🔥could not convert string to float: '2,3' line 8, column 9: |
| 138 | `is_equal_to_sum_even` | 与えられた数値nが、ちょうど4つの正の偶数の合計として表現できるかどうかを評価してください。 | テスト失敗(出力不一致) | テストを失敗 🔍is_equal_to_sum_even(4) ❌false ✅0 line 18, column 1: |
| 139 | `special_factorial` | ブラジリアン階乗は次のように定義される： | テスト失敗(出力不一致) | テストを失敗 🔍special_factorial(4) ❌1 ✅288 line 14, column 1: |
| 140 | `fix_spaces` | 文字列テキストが与えられた場合、その中のすべての空白をアンダースコアに置換し、 | テスト失敗(出力不一致) | テストを失敗 🔍fix_spaces("Yellow Yellow Dirty Fellow") ❌[89, 101, 108, 108, 111, 119, 95, 89, 101, 108, 108, 111, 119, 45, 68, 105, 114, 116, 121, 45, 70, 101, 108, 1 |
| 141 | `file_name_check` | ファイル名を表す文字列を受け取り、そのファイル名が有効であれば'Yes'を返し、そうでなければ'No' | テスト失敗(出力不一致) | テストを失敗 🔍file_name_check("His12FILE94.exe") ❌"Yes" ✅"No" line 116, column 1: |
| 143 | `words_in_sentence` | 文を表す文字列が与えられ、その文には空白で区切られたいくつかの単語が含まれている。 | テスト失敗(出力不一致) | テストを失敗 🔍words_in_sentence("This is a test") ❌"" ✅"is" line 66, column 1: |
| 144 | `simplify` | あなたの仕事は、式 x * n を簡単にする関数を実装することです。 | テスト失敗(出力不一致) | テストを失敗 🔍simplify("1/5", "5/1") ❌true ✅1 line 83, column 1: |
| 145 | `order_by_points` | 各数字の桁の合計に基づいて、与えられた整数のリストを昇順に並べる | テスト失敗(出力不一致) | テストを失敗 🔍order_by_points([1, 11, -1, -11, -12]) ❌[1, -1, -12, 11, -11] ✅[-1, -11, 1, -12, 11] line 64, column 1: |
| 146 | `specialFilter` | 数値の配列を入力とし、配列中の要素のうち、10より大きく、 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 147 | `get_max_triples` | 正の整数 n が与えられるので、長さ n の整数配列 a を作成せよ。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 148 | `bf` | 私たちの太陽系には8つの惑星があります：太陽に最も近いのはVenus, Earth, Mars, Jupiter, Saturn, | テスト失敗(出力不一致) | テストを失敗 🔍bf("Earth", "Earth") ❌["Mars"] ✅[] line 51, column 1: |
| 152 | `compare` | 待ち望んでいた出来事の結果がようやく判明したときの感覚は、誰もが覚えていると思う。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 154 | `cycpattern_check` | 2つの単語が与えられる。2番目の単語またはその回転させた文字列が最初の単語の部分文字列である場合、Trueを返す必要がある。 | テスト失敗(出力不一致) | テストを失敗 🔍cycpattern_check("xyzw","xyw") ❌false ✅0 line 52, column 1: |
| 157 | `right_angle_triangle` | 三角形の3辺の長さを与える。三角形が直角三角形ならTrueを、そうでなければFalseを返す。 | テスト失敗(出力不一致) | テストを失敗 🔍right_angle_triangle(3, 4, 5) ❌true ✅1 line 27, column 1: |
| 158 | `find_max` | 文字列のリストを受け取る関数を書きなさい。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 161 | `solve` | 文字列sが与えられます。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 162 | `string_to_md5` | 文字列 text が与えられたとき、その md5 ハッシュと等価な文字列を返す。 | テスト失敗(出力不一致) | テストを失敗 🔍string_to_md5("A B C") ❌"3e25960a79dbc69b674cd4ec67a72c62" ✅"0ef78513b0cb8cef12743f5aeb35f888" line 15, column 1: |
| 163 | `generate_integers` | 正の整数aとbが与えられたとき、aとbの間にある偶数の数字を昇順で返してください。 | テスト失敗(出力不一致) | テストを失敗 🔍generate_integers(2, 10) ❌[2, 4, 6, 8, 10] ✅[2, 4, 6, 8] line 28, column 1: |
