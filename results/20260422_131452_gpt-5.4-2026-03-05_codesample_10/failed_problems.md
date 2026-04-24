# 失敗問題一覧 — 20260422_131452_gpt-5.4-2026-03-05_codesample_10

- モデル: gpt-5.4-2026-03-05
- 言語: ja / テンプレート: pro159/codesample_10.md
- 合計: **164問中 105問失敗** (pass@1 = 35.98%)

## 失敗原因サマリ

| 原因 | 件数 |
|------|------|
| 構文認識不可(Yui非準拠) | 56 |
| テスト失敗(出力不一致) | 38 |
| 構文エラー | 11 |

### 原因の意味

- **構文認識不可(Yui非準拠)**: Yuiパーサが文法として受理できず、そもそもコードとして実行されなかった
- **構文エラー**: パース自体は通ったが実行中に文法エラーで停止
- **テスト失敗(出力不一致)**: 実行は完了したがテストの期待値と異なる

## 失敗問題リスト

| タスクID | 関数 | 問題概要 | 失敗原因 | エラー詳細 |
|---------|------|---------|---------|-----------|
| 0 | `has_close_elements` | リストnumbersの中に、与えられたthresholdより近い２つの数値が存在するか判定する | テスト失敗(出力不一致) | テストを失敗 🔍has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) ❌true ✅1 line 27, column 1: |
| 1 | `separate_paren_groups` | この関数への入力は、入れ子になった括弧が複数含まれる文字列である。 | テスト失敗(出力不一致) | テストを失敗 🔍separate_paren_groups("(()()) ((())) () ((())()())") ❌[] ✅["(()())", "((()))", "()", "((())()())"] line 40, column 1: |
| 3 | `below_zero` | 銀行口座に対する入出金操作のリストが与えられます。あなたのタスクは、残高ゼロから | テスト失敗(出力不一致) | テストを失敗 🔍below_zero([]) ❌false ✅0 line 18, column 1: |
| 7 | `filter_by_substring` | 文字列リストstringsを、与えれた部分文字列substringを含むものだけにフィルタする | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 10 | `make_palindrome` | 与えられた文字列が回文かどうかをテストします。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 12 | `longest` | 文字列のリストのうち、最も長いものを返す。同じ長さの文字列が | テスト失敗(出力不一致) | テストを失敗 🔍longest([]) ❌null ✅"" line 25, column 1: |
| 14 | `all_prefixes` | 引数で与えられた文字列に対して、短いものから長いものへ、全ての接頭辞のリストを返す | テスト失敗(出力不一致) | テストを失敗 🔍all_prefixes("asdfgh") ❌["97", "97115", "97115100", "97115100102", "97115100102103", "97115100102103104"] ✅["a", "as", "asd", "asdf", "asdfg", "asdfgh"] |
| 17 | `parse_music` | この関数の引数は、特別なASCII形式の音符を表す文字列である。あなたの仕事は、この文字列を解析して、それぞれの音符が何拍続くかに対応する整数のリストを返すことである。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 18 | `how_many_times` | 部分文字列substringが文字列stringの中で何回見つかるか数える。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 19 | `sort_numbers` | 引数は'zero'から'nine'までの英単語の数を空白で区切った文字列である。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 20 | `find_closest_elements` | （少なくとも長さ2以上の）リストnumbersから、互いに最も近いものを2つ選び、 | 構文エラー | 関数が定義されていません ❌並べ替え line 4, column 11: |
| 22 | `filter_integers` | 任意の種類の値が含まれるリストから整数値のみ抽出する | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 25 | `factorize` | 与えられた整数の素因数のリストを小さいものから大きいものの順に返す。各因数は、 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 26 | `remove_duplicates` | 整数のリストから、複数回出現する要素をすべて取り除く。 | 構文エラー | index-error ✅<0 ❌1 🔍[] line 14, column 10: |
| 29 | `filter_by_prefix` | 文字列のリストから、指定された接頭辞prefixで始まるものだけを取り出す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 31 | `is_prime` | 与えられた数が素数であれば真を、そうでなければ偽を返す。 | テスト失敗(出力不一致) | テストを失敗 🔍is_prime(6) ❌false ✅0 line 27, column 1: |
| 32 | `find_zero` | 点xにおける係数xsを持つ多項式の値を計算する。 | 構文エラー | 関数が定義されていません ❌approx_zero line 17, column 5: |
| 33 | `sort_third` | この関数はリストlを受け取り、l'を返す。l'は、インデックスが3で割り | 構文エラー | 関数が定義されていません ❌ソート line 16, column 11: |
| 34 | `unique` | リスト内のユニークな要素をソートして返す | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 36 | `fizz_buzz` | 11または13で割り切れるn未満の整数の中に7という数字が現れる回数を返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 37 | `sort_even` | この関数はリスト l を受け取り、l' を返す。l'は、インデックスが奇数の | 構文エラー | 関数が定義されていません ❌ソート line 17, column 10: |
| 38 | `decode_cyclic` | 3文字ごとに循環させてエンコードした文字列を返す。 | テスト失敗(出力不一致) | テストを失敗 🔍decode_cyclic("axdhhixdexrvsncacbgh") ❌"xxgehludhurypnfxcedh" ✅"daxihhexdvxrcsnbacgh" line 53, column 1: |
| 39 | `prime_fib` | prime_fib はフィボナッチ数で、かつ素数であるn番目の数を返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 40 | `triples_sum_to_zero` | triples_sum_to_zero は整数のリストを引数に取り、 | テスト失敗(出力不一致) | テストを失敗 🔍triples_sum_to_zero([1, 3, 5, 0]) ❌false ✅0 line 32, column 1: |
| 42 | `incr_list` | 要素を1ずつ増やしたリストを返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 43 | `pairs_sum_to_zero` | pairs_sum_to_zero は整数のリストを引数にとる。 | テスト失敗(出力不一致) | テストを失敗 🔍pairs_sum_to_zero([1, 3, 5, 0]) ❌false ✅0 line 27, column 1: |
| 45 | `triangle_area` | 三角形の一辺の長さと高さが与えられたとき、面積を返す。 | テスト失敗(出力不一致) | テストを失敗 🔍triangle_area(5, 3) ❌7 ✅7.500000 line 8, column 1: |
| 47 | `median` | リスト l の要素の中央値を返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 48 | `is_palindrome` | 与えられた文字列が回文かどうかを判定する | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 50 | `decode_shift` | アルファベットの各文字を5ずつずらしてエンコードした文字列を返す。 | テスト失敗(出力不一致) | テストを失敗 🔍decode_shift("ifcnmmjciacwhxsgfhlm") ❌"nkhsrrohnfhbmcxlkmqr" ✅"daxihhexdvxrcsnbacgh" line 34, column 1: |
| 51 | `remove_vowels` | remove_vowelsは文字列を引数に取り、母音を除いた文字列を返す関数である。 | テスト失敗(出力不一致) | テストを失敗 🔍remove_vowels("abcdef\nghijklm") ❌"abcdef\nghijklm" ✅"bcdf\nghjklm" line 21, column 1: |
| 52 | `below_threshold` | リスト l 内の全ての数値が閾値 t 以下の場合、Trueを返す。 | テスト失敗(出力不一致) | テストを失敗 🔍below_threshold([1, 2, 4, 10], 100) ❌true ✅1 line 16, column 1: |
| 54 | `same_chars` | 2つの単語が同じ文字セットから構成されるかどうか判定する。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 56 | `correct_bracketing` | 引数bracketsは"<"と">"の文字列である。 | テスト失敗(出力不一致) | テストを失敗 🔍correct_bracketing("<>") ❌false ✅1 line 31, column 1: |
| 57 | `monotonic` | リストの要素が単調増加または単調減少する場合にTrueを返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 58 | `common` | 2つのリストについて、ユニークな共通要素をソートして返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 59 | `largest_prime_factor` | nの最大となる素因数を返す。ただし、 n > 1 を前提とし、素数ではないものとする。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 61 | `correct_bracketing` | 引数bracketsは"("と") "からなる文字列である。 | テスト失敗(出力不一致) | テストを失敗 🔍correct_bracketing("()") ❌false ✅1 line 29, column 1: |
| 62 | `derivative` | xsは多項式の係数列を表す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 64 | `vowels_count` | Add more test cases. | テスト失敗(出力不一致) | テストを失敗 🔍vowels_count("abcde") ❌0 ✅2 line 21, column 1: |
| 67 | `fruit_distribution` | この課題では、果物の入ったカゴに配られたリンゴとオレンジの数を表す文字列が | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 68 | `pluck` | 非負整数のノードを持つ木の枝を表す配列が与えられたとする。あなたの仕事は、 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 69 | `search` | 正の整数の空でないリストが与えられる。0より大きく、その整数自身の値以上の頻度を | 構文エラー | index-error ✅<0 ❌5 🔍[] line 10, column 9: |
| 71 | `triangle_area` | 三角形の3辺の長さが与えられた。3辺が有効な三角形を形成していれば、 | 構文エラー | 関数が定義されていません ❌除算 line 14, column 6: |
| 72 | `will_it_fly` | 物体qが飛べばTrueを、そうでなければFalseを返す関数を書け。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 75 | `is_multiply_prime` | 与えられた数が3つの素数の掛け算であればTrueを、そうでなければFalseを返す | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 76 | `is_simple_power` | あなたのタスクは、ある数xがnの単純なべき乗である場合にtrueを、 | テスト失敗(出力不一致) | テストを失敗 🔍is_simple_power(16, 2) ❌true ✅1 line 24, column 1: |
| 77 | `iscube` | 整数aを受け取り、この整数がある整数の3乗である場合にTrue | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 78 | `hex_key` | 16進数の数字を文字列として受け取り、その中に含まれる素数である16進数の桁数を | テスト失敗(出力不一致) | テストを失敗 🔍hex_key("AB") ❌0 ✅1 line 19, column 1: |
| 79 | `decimal_to_binary` | 10進数形式の数値が与えられ、あなたのタスクはそれを2進数形式に変換することである。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 80 | `is_happy` | あなたは文字列sが与えられる。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 82 | `prime_length` | 文字列を受け取り、文字列の長さが素数であればTrueを、そうでなければFalseを返す関数を書く。 | テスト失敗(出力不一致) | テストを失敗 🔍prime_length("Hello") ❌true ✅1 line 27, column 1: |
| 83 | `starts_one_ends` | 正の整数 n が与えられたとき、n 桁の正の整数で 1 で始まるか | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 84 | `solve` | 正の整数 N が与えられた時、その桁の総和を2進数で返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 85 | `add` | 空でない整数のリストlstが与えられたとき、奇数のインデックスにある偶数の要素を加える。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 86 | `anti_shuffle` | 文字列を引数として受け取り、その「順序付けられたバージョン」を返す関数を作成してください。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 88 | `sort_array` | 非負の整数からなる配列が与えられた場合、配列をソートしたコピーを返してください。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 90 | `next_smallest` | 整数のリストが与えられる。 | テスト失敗(出力不一致) | テストを失敗 🔍next_smallest([1, 2, 3, 4, 5]) ❌2 ✅[2] line 40, column 1: |
| 91 | `is_bored` | 単語の文字列が与えられ、あなたのタスクは退屈指数を数える | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 92 | `any_int` | 3つの数値を受け取る関数を作る。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 93 | `encode` | メッセージを受け取り、すべての文字の大文字と小文字を入れ替え、 | テスト失敗(出力不一致) | テストを失敗 🔍encode("TEST") ❌"test" ✅"tgst" line 42, column 1: |
| 94 | `skjkasdkd` | 整数のリストが与えらる。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 95 | `check_dict_case` | 辞書が与えられたとき、すべてのキーが小文字であればTrueを、 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 96 | `count_up_to` | 非負整数を受け取り、素数でnより小さい最初のn個の | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 103 | `rounded_avg` | 2つの正の整数nとmが与えられており、あなたのタスクはnからmまでの | テスト失敗(出力不一致) | テストを失敗 🔍rounded_avg(964,977) ❌"0b1111001011" ✅"0b1111001010" line 45, column 1: |
| 104 | `unique_digits` | 正の整数xのリストが与えられたとき、偶数桁の要素を持たない全ての | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 106 | `f` | iは1から始まる。iの階乗は1からiまでの数の掛け算（1 * 2 * ... * i）である。 | テスト失敗(出力不一致) | テストを失敗 🔍f(5) ❌[1, 2, 6, 24, 120] ✅[1, 2, 6, 24, 15] line 16, column 1: |
| 108 | `count_nums` | count_nums 関数は、整数の配列を引数として受け取り、その配列内の各整数の各桁の合計が | テスト失敗(出力不一致) | テストを失敗 🔍count_nums([12, 23, 34, -45, -56, 0]) ❌3 ✅5 line 55, column 1: |
| 109 | `move_one_ball` | N個の整数arr[1], arr[2], ..., arr[N]なる配列 'arr' があります。 | テスト失敗(出力不一致) | テストを失敗 🔍move_one_ball([3, 4, 5, 1, 2]) ❌true ✅1 line 32, column 1: |
| 111 | `histogram` | 空白で区切られた小文字を表す文字列が与えられる。最も出現回数が多い文字と | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 112 | `reverse_delete` | 課題 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 116 | `sort_array` | この問題では、非負整数の配列を2進数表現における"1"の個数を昇順でソートする。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 117 | `select_words` | ある文字列sと自然数nが与えらる。あなたに課せられたタスクは、文字列s | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 118 | `get_closest_vowel` | 単語が与えられる。あなたの仕事は、単語の右側から2つの子音（大文字と | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 123 | `get_odd_collatz` | 正の整数nが与えられたとき、コラッツ数列の奇数を持つソートされたリストを返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 124 | `valid_date` | 与えられた日付文字列を検証し、その日付が有効であればTrueを、そうでなければFalseを返す関数を書く必要がある。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 125 | `split_words` | 単語の文字列が与えられた場合、空白で分割された単語のリストを返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 126 | `is_sorted` | 数字のリストが与えられたとき、昇順に整列されているかどうかを返す。 | テスト失敗(出力不一致) | テストを失敗 🔍is_sorted([5]) ❌true ✅1 line 32, column 1: |
| 127 | `intersection` | 2つの区間が与えられます。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 128 | `prod_signs` | 整数の配列 arr が与えられます。この配列に含まれる各数値の絶対値の合計と、 | テスト失敗(出力不一致) | テストを失敗 🔍prod_signs([1, 2, 2, -4]) ❌-9 ✅[-9] line 36, column 1: |
| 129 | `minPath` | N行とN列 (N >= 2)) のグリッドと正の整数kが与えられた場合、各セルには値が含まれている。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 131 | `digits` | 正の整数 n が与えられた時、奇数桁数の積を返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 132 | `is_nested` | この関数は、角括弧だけを含む文字列を入力として受け取ります。括弧が有効な順序で | テスト失敗(出力不一致) | テストを失敗 🔍is_nested("[[]]") ❌false ✅1 line 35, column 1: |
| 133 | `sum_squares` | 数字のリストが与えられます。 | 構文エラー | 関数が定義されていません ❌切り上げ line 8, column 9: |
| 134 | `check_if_last_char_is_a_letter` | 与えられた文字列の最後の文字がアルファベットであり、かつ単語の一部でなければTrueを、 | テスト失敗(出力不一致) | テストを失敗 🔍check_if_last_char_is_a_letter("apple") ❌false ✅0 line 43, column 1: |
| 136 | `largest_smallest_integers` | リストから最も大きな負の整数と最も小さな正の整数を見つけ、それらをタプル（a, b） | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 137 | `compare_one` | 整数、浮動小数点数、または実数を表す文字列を引数として受け取り、その中で最も大きい値を | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 138 | `is_equal_to_sum_even` | 与えられた数値nが、ちょうど4つの正の偶数の合計として表現できるかどうかを評価してください。 | テスト失敗(出力不一致) | テストを失敗 🔍is_equal_to_sum_even(4) ❌false ✅0 line 20, column 1: |
| 140 | `fix_spaces` | 文字列テキストが与えられた場合、その中のすべての空白をアンダースコアに置換し、 | 構文エラー | index-error ✅<28 ❌28 🔍[89, 101, 108, 108, 111, 119, 32, 89, 101, 108, 108, 111, 119, 32, 32, 68, 105, 114, 116, 121, 32, 32, 70, 101, 108, 108, 111, 119] line 9 |
| 141 | `file_name_check` | ファイル名を表す文字列を受け取り、そのファイル名が有効であれば'Yes'を返し、そうでなければ'No' | テスト失敗(出力不一致) | テストを失敗 🔍file_name_check("His12FILE94.exe") ❌"Yes" ✅"No" line 92, column 1: |
| 143 | `words_in_sentence` | 文を表す文字列が与えられ、その文には空白で区切られたいくつかの単語が含まれている。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 144 | `simplify` | あなたの仕事は、式 x * n を簡単にする関数を実装することです。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 145 | `order_by_points` | 各数字の桁の合計に基づいて、与えられた整数のリストを昇順に並べる | テスト失敗(出力不一致) | テストを失敗 🔍order_by_points([1, 11, -1, -11, -12]) ❌[1, -1, 11, -11, -12] ✅[-1, -11, 1, -12, 11] line 68, column 1: |
| 146 | `specialFilter` | 数値の配列を入力とし、配列中の要素のうち、10より大きく、 | テスト失敗(出力不一致) | テストを失敗 🔍specialFilter([15, -73, 14, -15]) ❌0 ✅1 line 27, column 1: |
| 147 | `get_max_triples` | 正の整数 n が与えられるので、長さ n の整数配列 a を作成せよ。 | テスト失敗(出力不一致) | テストを失敗 🔍get_max_triples(5) ❌[1, 7, 13] ✅1 line 48, column 1: |
| 148 | `bf` | 私たちの太陽系には8つの惑星があります：太陽に最も近いのはVenus, Earth, Mars, Jupiter, Saturn, | テスト失敗(出力不一致) | テストを失敗 🔍bf("Earth", "Earth") ❌["Mars"] ✅[] line 58, column 1: |
| 149 | `sorted_list_sum` | 文字列のリストを引数として受け取る関数を作成してください。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 150 | `x_or_y` | 素数である場合はxの値を返し、それ以外の場合はyの値を返す簡単なプログラム。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 151 | `double_the_difference` | 数字のリストが与えられた場合、そのリスト内の奇数の数値の二乗の合計を返してください。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 154 | `cycpattern_check` | 2つの単語が与えられる。2番目の単語またはその回転させた文字列が最初の単語の部分文字列である場合、Trueを返す必要がある。 | テスト失敗(出力不一致) | テストを失敗 🔍cycpattern_check("xyzw","xyw") ❌false ✅0 line 48, column 1: |
| 157 | `right_angle_triangle` | 三角形の3辺の長さを与える。三角形が直角三角形ならTrueを、そうでなければFalseを返す。 | テスト失敗(出力不一致) | テストを失敗 🔍right_angle_triangle(3, 4, 5) ❌true ✅1 line 27, column 1: |
| 160 | `do_algebra` | 演算子(operator)とオペランド(operand)の2つのリストが与えられる。ひとつ目のリストは | 構文エラー | 関数が定義されていません ❌べき乗 line 15, column 34: |
| 161 | `solve` | 文字列sが与えられます。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 162 | `string_to_md5` | 文字列 text が与えられたとき、その md5 ハッシュと等価な文字列を返す。 | 構文エラー | 関数が定義されていません ❌md5 line 7, column 4: |
| 163 | `generate_integers` | 正の整数aとbが与えられたとき、aとbの間にある偶数の数字を昇順で返してください。 | テスト失敗(出力不一致) | テストを失敗 🔍generate_integers(2, 10) ❌[2, 4, 6, 8, 10] ✅[2, 4, 6, 8] line 26, column 1: |

---

## 「構文認識不可(Yui非準拠) 56件」の深掘り分析

Yuiパーサにそもそも受理されなかった 56 件を、実際にパーサにかけ直してエラー種別ごとに分類した結果。

### パーサエラー内訳

| 件数 | 文法タグ | エラートークン | 典型パターン |
|-----:|---------|---------------|-------------|
| 23 | `if-infix` | ❌`ならば` (期待: `が`) | `もし 整数判定(x) ならば` など、真偽値を直接条件にしている |
| 18 | wrong-statement | ❌`くり返す` / `を"..."で分割` / `をソートする` / `のキー列` など | 存在しない文/メソッドを使っている |
| 3 | `append-infix` | ❌`を追加する` (期待: `に`) | 配列追加の助詞順序違反 |
| 3 | `if-then` | ❌`未満ならば` | 独自の比較語尾 |
| 2 | `if-then` | ❌`と等しくないならば` | 独自の否定比較 |
| 2 | `if-suffix!=` | ❌`でない` (期待: `以外`) | `A が B でない` の形 |
| 1 ずつ | `if-then` / `if-infix` | ❌`を含むならば` / `と違うならば` / `と異なるならば` / `でないならば` / 長文複合条件 | 独自に作った比較述語 |

### 失敗原因の分類 (56件中)

| 分類 | 件数 | 比率 |
|------|-----:|-----:|
| **if文関連 (中置比較違反・独自語尾)** | **35** | **62%** |
| 存在しない文/組み込みメソッド (`くり返す`無限ループ, `分割`, `ソート` 等) | 18 | 32% |
| `append-infix` 配列追加の助詞順序 | 3 | 5% |

→ **if文関連だけで全体の約3分の2 を占める。**

### 頻出非準拠パターン

#### ① `もし` の条件に真偽値を直接置く (23件 — 最多)

```yui
もし 整数判定(x) ならば { ... }    ❌ NG
もし ok ならば { ... }              ❌ NG (ok は bool 変数)
```

Yui の `もし` は **中置比較必須** (`もし A が B ○○ならば`)。
bool をそのまま条件にできない。Python/JS の `if flag:` の感覚で書くとここで落ちる。

**正しい書き方:**
```yui
もし 整数判定(x) が 真 ならば { ... }    ✅
もし ok が 真 ならば { ... }             ✅
```

#### ② 独自に作った比較語尾 (12件)

```yui
もし n が 2 未満ならば           ❌   → もし n が 2 より小さいならば   ✅
もし a が b でない ならば         ❌   → もし a が b 以外ならば         ✅
もし a と b と等しくないならば    ❌   → もし a が b 以外ならば         ✅
もし s が "x" を含むならば        ❌   (組み込みなし)
```

Yui が許すのは `以上 / 以下 / より大きい / より小さい / 以外` のみ。
日本語として自然な「〜でない」「〜未満」「〜と違う」「〜を含む」は全て NG。

#### ③ 回数指定なしの無限 `くり返す {}` (5件)

```yui
くり返す {
    もし ... ならば { くり返しを抜ける }
}                                    ❌ NG
```

Yui には `N回くり返す` しか無く、条件なし無限ループの構文は存在しない。

#### ④ コンテキストに無い組み込みメソッド (8件)

- `文字列 を " " で分割` (4件)
- `配列 をソートする` (2件)
- `辞書 のキー列` (1件)
- `くり返し条件が i が x 以下の間` / `より小さい間くり返す` (2件)

これらは codesample_10.md に登場しないので、モデルが Python/JS 感覚で発明している。

### 本質的な傾向

この 56 件の本質は **「コンテキストに出てこない日本語表現を発明してしまう」** こと。
モデルは日本語として自然な書き方を選んでしまい、Yui の限定的な語彙（`以外` / `より小さい` / `が` 中置比較 / `N回くり返す` 固定）から外れる。

### 改善仮説

プロンプトで以下を明示すれば、35件のif関連失敗の多くと、その他の発明メソッドの一部は救える見込み:

1. **`もし` は必ず `A が B ○○ならば` の中置形式** (真偽値を直接置けない)
2. **使える比較語尾は `以上 / 以下 / より大きい / より小さい / 以外` のみ** (「未満」「でない」等は NG)
3. **ループは `N回くり返す` のみ** (条件ループ・無限ループは使えない)
4. **bool 変数は `が 真 ならば` / `が 偽 ならば` で明示的に比較する**

→ 単純計算で 56件中 30件以上が救える可能性があり、pass@1 で +18ポイント程度の改善余地がある。

