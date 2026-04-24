# 失敗問題一覧 — 20260422_202539_claude-haiku-4-5_ebnf_ja

- モデル: claude-haiku-4-5
- 言語: ja / テンプレート: pro159/ebnf_ja.md
- 合計: **164問中 163問失敗** (pass@1 = 0.61%)

## 失敗原因サマリ

| 原因 | 件数 |
|------|------|
| 構文認識不可(Yui非準拠) | 163 |

### 原因の意味

- **構文認識不可(Yui非準拠)**: Yuiパーサが文法として受理できず、そもそもコードとして実行されなかった
- **構文エラー**: パース自体は通ったが実行中に文法エラーで停止
- **テスト失敗(出力不一致)**: 実行は完了したがテストの期待値と異なる

## 失敗問題リスト

| タスクID | 関数 | 問題概要 | 失敗原因 | エラー詳細 |
|---------|------|---------|---------|-----------|
| 0 | `has_close_elements` | リストnumbersの中に、与えられたthresholdより近い２つの数値が存在するか判定する | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 1 | `separate_paren_groups` | この関数への入力は、入れ子になった括弧が複数含まれる文字列である。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 2 | `truncate_number` | 正の浮動小数点数が与えられると、それを整数部（与えられた数より小さい最大の整数） | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 3 | `below_zero` | 銀行口座に対する入出金操作のリストが与えられます。あなたのタスクは、残高ゼロから | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 4 | `mean_absolute_deviation` | 第一引数の数値リストに対して、このデータセットの平均値を中心とした平均絶対偏差(MAD)を計算する。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 5 | `intersperse` | 数値リスト numbers 中の全ての連続する二要素の間に、'delimeterの値を挿入する | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 6 | `parse_nested_parens` | この関数の入力は、空白で区切られた複数の入れ子になった括弧のグループを表す文字列です。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 7 | `filter_by_substring` | 文字列リストstringsを、与えれた部分文字列substringを含むものだけにフィルタする | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 8 | `sum_product` | 与えられた整数リストに対して、リスト内のすべての整数の和と積からなるタプルを返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 9 | `rolling_max` | 与えられた整数リストから、各要素のそこまでの最大値（ローリング最大値）のリストを生成する。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 10 | `make_palindrome` | 与えられた文字列が回文かどうかをテストします。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 11 | `string_xor` | 引数は1と0のみからなる文字列aとbである。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 12 | `longest` | 文字列のリストのうち、最も長いものを返す。同じ長さの文字列が | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 13 | `greatest_common_divisor` | 整数 a と b の最大公約数を返す | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 14 | `all_prefixes` | 引数で与えられた文字列に対して、短いものから長いものへ、全ての接頭辞のリストを返す | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 15 | `string_sequence` | 0からnまでの数字を空白区切りで連結した文字列で返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 16 | `count_distinct_characters` | 文字列が与えられたとき、その文字列が（大文字小文字に関係なく）いくつの異なる文字が含まれているか数える | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 17 | `parse_music` | この関数の引数は、特別なASCII形式の音符を表す文字列である。あなたの仕事は、この文字列を解析して、それぞれの音符が何拍続くかに対応する整数のリストを返すことである。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 18 | `how_many_times` | 部分文字列substringが文字列stringの中で何回見つかるか数える。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 19 | `sort_numbers` | 引数は'zero'から'nine'までの英単語の数を空白で区切った文字列である。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 20 | `find_closest_elements` | （少なくとも長さ2以上の）リストnumbersから、互いに最も近いものを2つ選び、 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 21 | `rescale_to_unit` | (少なくとも 2 つ以上の要素からなる) リストnumbersに線形変換を適用し、 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 22 | `filter_integers` | 任意の種類の値が含まれるリストから整数値のみ抽出する | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 23 | `strlen` | 引数で与えられた文字列の長さを返す | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 24 | `largest_divisor` | 与えられた数nについて、nの約数のうち、nより小さい最大の数を求める | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 25 | `factorize` | 与えられた整数の素因数のリストを小さいものから大きいものの順に返す。各因数は、 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 26 | `remove_duplicates` | 整数のリストから、複数回出現する要素をすべて取り除く。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 27 | `flip_case` | 与えられた文字列に対して、英小文字を英大文字に、英大文字を英小文字に変換する。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 28 | `concatenate` | 文字列のリストを1つの文字列に連結する | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 29 | `filter_by_prefix` | 文字列のリストから、指定された接頭辞prefixで始まるものだけを取り出す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 30 | `get_positive` | リスト内の正の数だけを返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 31 | `is_prime` | 与えられた数が素数であれば真を、そうでなければ偽を返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 32 | `find_zero` | 点xにおける係数xsを持つ多項式の値を計算する。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 33 | `sort_third` | この関数はリストlを受け取り、l'を返す。l'は、インデックスが3で割り | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 34 | `unique` | リスト内のユニークな要素をソートして返す | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 35 | `max_element` | リスト内の最大要素を返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 36 | `fizz_buzz` | 11または13で割り切れるn未満の整数の中に7という数字が現れる回数を返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 37 | `sort_even` | この関数はリスト l を受け取り、l' を返す。l'は、インデックスが奇数の | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 38 | `decode_cyclic` | 3文字ごとに循環させてエンコードした文字列を返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 39 | `prime_fib` | prime_fib はフィボナッチ数で、かつ素数であるn番目の数を返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 40 | `triples_sum_to_zero` | triples_sum_to_zero は整数のリストを引数に取り、 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 41 | `car_race_collision` | 完全な直線で無限に長い道路を想像してほしい。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 42 | `incr_list` | 要素を1ずつ増やしたリストを返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 43 | `pairs_sum_to_zero` | pairs_sum_to_zero は整数のリストを引数にとる。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 44 | `change_base` | 引数xの基数をbaseに変換する。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 45 | `triangle_area` | 三角形の一辺の長さと高さが与えられたとき、面積を返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 46 | `fib4` | fib4数列はフィボナッチ数列に似た数列で、次のように定義される： | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 47 | `median` | リスト l の要素の中央値を返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 48 | `is_palindrome` | 与えられた文字列が回文かどうかを判定する | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 49 | `modp` | 2^n を p で割ったモジュロを返す。計算精度に注意。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 50 | `decode_shift` | アルファベットの各文字を5ずつずらしてエンコードした文字列を返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 51 | `remove_vowels` | remove_vowelsは文字列を引数に取り、母音を除いた文字列を返す関数である。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 52 | `below_threshold` | リスト l 内の全ての数値が閾値 t 以下の場合、Trueを返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 53 | `add` | 2つの数xとyを足す | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 54 | `same_chars` | 2つの単語が同じ文字セットから構成されるかどうか判定する。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 56 | `correct_bracketing` | 引数bracketsは"<"と">"の文字列である。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 57 | `monotonic` | リストの要素が単調増加または単調減少する場合にTrueを返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 58 | `common` | 2つのリストについて、ユニークな共通要素をソートして返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 59 | `largest_prime_factor` | nの最大となる素因数を返す。ただし、 n > 1 を前提とし、素数ではないものとする。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 60 | `sum_to_n` | sum_to_nは1からnまでの総和を求める関数である。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 61 | `correct_bracketing` | 引数bracketsは"("と") "からなる文字列である。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 62 | `derivative` | xsは多項式の係数列を表す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 63 | `fibfib` | FibFib数列はフィボナッチ数列に似た数列で、以下のように定義される： | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 64 | `vowels_count` | Add more test cases. | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 65 | `circular_shift` | 整数 x の桁を循環シフトする。shift 分だけ桁を右にシフトし、結果を文字列として返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 66 | `digitSum` | タスク | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 67 | `fruit_distribution` | この課題では、果物の入ったカゴに配られたリンゴとオレンジの数を表す文字列が | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 68 | `pluck` | 非負整数のノードを持つ木の枝を表す配列が与えられたとする。あなたの仕事は、 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 69 | `search` | 正の整数の空でないリストが与えられる。0より大きく、その整数自身の値以上の頻度を | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 70 | `strange_sort_list` | 整数のリストが与えられたとき、リストを奇妙な順序で返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 71 | `triangle_area` | 三角形の3辺の長さが与えられた。3辺が有効な三角形を形成していれば、 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 72 | `will_it_fly` | 物体qが飛べばTrueを、そうでなければFalseを返す関数を書け。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 73 | `smallest_change` | 整数の配列arrが与えられたとき、その配列を回文配列にするために | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 74 | `total_match` | ２つの文字列リストを受け取り、リストの全文字数の合計がもう一方 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 75 | `is_multiply_prime` | 与えられた数が3つの素数の掛け算であればTrueを、そうでなければFalseを返す | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 76 | `is_simple_power` | あなたのタスクは、ある数xがnの単純なべき乗である場合にtrueを、 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 77 | `iscube` | 整数aを受け取り、この整数がある整数の3乗である場合にTrue | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 78 | `hex_key` | 16進数の数字を文字列として受け取り、その中に含まれる素数である16進数の桁数を | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 79 | `decimal_to_binary` | 10進数形式の数値が与えられ、あなたのタスクはそれを2進数形式に変換することである。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 80 | `is_happy` | あなたは文字列sが与えられる。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 81 | `numerical_letter_grade` | 学期最終週、教師は生徒に成績をつけなければならない。教師は独自のアルゴリズムで採点している。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 82 | `prime_length` | 文字列を受け取り、文字列の長さが素数であればTrueを、そうでなければFalseを返す関数を書く。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 83 | `starts_one_ends` | 正の整数 n が与えられたとき、n 桁の正の整数で 1 で始まるか | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 84 | `solve` | 正の整数 N が与えられた時、その桁の総和を2進数で返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 85 | `add` | 空でない整数のリストlstが与えられたとき、奇数のインデックスにある偶数の要素を加える。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 86 | `anti_shuffle` | 文字列を引数として受け取り、その「順序付けられたバージョン」を返す関数を作成してください。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 87 | `get_row` | 2次元のデータがネストされたリストとして与えられる。これは行列に似ているが、 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 88 | `sort_array` | 非負の整数からなる配列が与えられた場合、配列をソートしたコピーを返してください。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 89 | `encrypt` | 文字列を引数にとり、アルファベットを回転させて暗号化した | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 90 | `next_smallest` | 整数のリストが与えられる。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 91 | `is_bored` | 単語の文字列が与えられ、あなたのタスクは退屈指数を数える | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 92 | `any_int` | 3つの数値を受け取る関数を作る。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 93 | `encode` | メッセージを受け取り、すべての文字の大文字と小文字を入れ替え、 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 94 | `skjkasdkd` | 整数のリストが与えらる。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 95 | `check_dict_case` | 辞書が与えられたとき、すべてのキーが小文字であればTrueを、 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 96 | `count_up_to` | 非負整数を受け取り、素数でnより小さい最初のn個の | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 97 | `multiply` | 2つの整数を受け取り、その１の位の数の積を返す関数を完成させよ。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 98 | `count_upper` | 文字列 s が与えられたとき、偶数のインデックスに含まれる大文字の母音の数を数える。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 99 | `closest_integer` | 数値を表す文字列valueを受け取り、それに最も近い整数を返す関数を作る。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 100 | `make_a_pile` | 正の整数nが与えられたとき、n段の石の山を作らなければならない。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 101 | `words_string` | カンマまたは空白で区切られた単語の文字列が与えられる。あなたのタスクは、 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 102 | `choose_num` | この関数は2つの正の数xとyを受け取り、範囲[x, y]（両端を含む）に含まれる | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 103 | `rounded_avg` | 2つの正の整数nとmが与えられており、あなたのタスクはnからmまでの | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 104 | `unique_digits` | 正の整数xのリストが与えられたとき、偶数桁の要素を持たない全ての | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 105 | `by_length` | 整数の配列が与えられたとき、1から9までの整数をソートし、 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 106 | `f` | iは1から始まる。iの階乗は1からiまでの数の掛け算（1 * 2 * ... * i）である。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 107 | `even_odd_palindrome` | 与えられた正の整数 nに対して、範囲 1 から n まで（両端を含む）に存在する | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 108 | `count_nums` | count_nums 関数は、整数の配列を引数として受け取り、その配列内の各整数の各桁の合計が | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 109 | `move_one_ball` | N個の整数arr[1], arr[2], ..., arr[N]なる配列 'arr' があります。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 110 | `exchange` | この問題では、2つの数のリストを受け取り、lst1を偶数のみのリストに | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 111 | `histogram` | 空白で区切られた小文字を表す文字列が与えられる。最も出現回数が多い文字と | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 112 | `reverse_delete` | 課題 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 113 | `odd_count` | 数字のみで構成された文字列のリストを引数として受け取り、新しいリストを返します。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 114 | `minSubArraySum` | 整数の配列 nums が与えられたとき、nums の空でない部分配列の最小和を求めよ。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 115 | `max_fill` | 長方形のグリッド状(grid)の井戸が与えられる。各行が1つの井戸を表し、 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 116 | `sort_array` | この問題では、非負整数の配列を2進数表現における"1"の個数を昇順でソートする。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 117 | `select_words` | ある文字列sと自然数nが与えらる。あなたに課せられたタスクは、文字列s | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 118 | `get_closest_vowel` | 単語が与えられる。あなたの仕事は、単語の右側から2つの子音（大文字と | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 119 | `match_parens` | 2つの文字列からなるリストが与えられます。両方の文字列は開き括弧 '(' または | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 120 | `maximum` | 整数の配列 arr と正の整数 k が与えられる。arr に含まれる大きい方から k 個の数を含む | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 121 | `solution` | 整数の空でないリストが与えられた時、偶数の位置にある奇数の要素の合計を返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 122 | `add_elements` | 整数の空でない配列 arr と整数 k が与えられたとき、 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 123 | `get_odd_collatz` | 正の整数nが与えられたとき、コラッツ数列の奇数を持つソートされたリストを返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 124 | `valid_date` | 与えられた日付文字列を検証し、その日付が有効であればTrueを、そうでなければFalseを返す関数を書く必要がある。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 125 | `split_words` | 単語の文字列が与えられた場合、空白で分割された単語のリストを返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 126 | `is_sorted` | 数字のリストが与えられたとき、昇順に整列されているかどうかを返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 127 | `intersection` | 2つの区間が与えられます。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 128 | `prod_signs` | 整数の配列 arr が与えられます。この配列に含まれる各数値の絶対値の合計と、 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 129 | `minPath` | N行とN列 (N >= 2)) のグリッドと正の整数kが与えられた場合、各セルには値が含まれている。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 130 | `tri` | フィボナッチ数列は、ここ数世紀の間に数学者によって深く研究され、誰もが知っている。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 131 | `digits` | 正の整数 n が与えられた時、奇数桁数の積を返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 132 | `is_nested` | この関数は、角括弧だけを含む文字列を入力として受け取ります。括弧が有効な順序で | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 133 | `sum_squares` | 数字のリストが与えられます。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 134 | `check_if_last_char_is_a_letter` | 与えられた文字列の最後の文字がアルファベットであり、かつ単語の一部でなければTrueを、 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 135 | `can_arrange` | 直前の要素よりも大きくない要素の中で、最も大きなインデックスを持つ要素を探して | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 136 | `largest_smallest_integers` | リストから最も大きな負の整数と最も小さな正の整数を見つけ、それらをタプル（a, b） | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 137 | `compare_one` | 整数、浮動小数点数、または実数を表す文字列を引数として受け取り、その中で最も大きい値を | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 138 | `is_equal_to_sum_even` | 与えられた数値nが、ちょうど4つの正の偶数の合計として表現できるかどうかを評価してください。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 139 | `special_factorial` | ブラジリアン階乗は次のように定義される： | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 140 | `fix_spaces` | 文字列テキストが与えられた場合、その中のすべての空白をアンダースコアに置換し、 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 141 | `file_name_check` | ファイル名を表す文字列を受け取り、そのファイル名が有効であれば'Yes'を返し、そうでなければ'No' | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 142 | `sum_squares` | " | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 143 | `words_in_sentence` | 文を表す文字列が与えられ、その文には空白で区切られたいくつかの単語が含まれている。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 144 | `simplify` | あなたの仕事は、式 x * n を簡単にする関数を実装することです。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 145 | `order_by_points` | 各数字の桁の合計に基づいて、与えられた整数のリストを昇順に並べる | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 146 | `specialFilter` | 数値の配列を入力とし、配列中の要素のうち、10より大きく、 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 147 | `get_max_triples` | 正の整数 n が与えられるので、長さ n の整数配列 a を作成せよ。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 148 | `bf` | 私たちの太陽系には8つの惑星があります：太陽に最も近いのはVenus, Earth, Mars, Jupiter, Saturn, | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 149 | `sorted_list_sum` | 文字列のリストを引数として受け取る関数を作成してください。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 150 | `x_or_y` | 素数である場合はxの値を返し、それ以外の場合はyの値を返す簡単なプログラム。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 151 | `double_the_difference` | 数字のリストが与えられた場合、そのリスト内の奇数の数値の二乗の合計を返してください。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 152 | `compare` | 待ち望んでいた出来事の結果がようやく判明したときの感覚は、誰もが覚えていると思う。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 153 | `Strongest_Extension` | クラスの名前（文字列）と拡張子のリストが与えられます。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 154 | `cycpattern_check` | 2つの単語が与えられる。2番目の単語またはその回転させた文字列が最初の単語の部分文字列である場合、Trueを返す必要がある。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 155 | `even_odd_count` | 整数が与えられた場合、偶数桁数と奇数桁数をそれぞれ持つタプルを返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 156 | `int_to_mini_roman` | 正の整数が与えられたとき、ローマ数字に相当する文字列を小文字で返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 157 | `right_angle_triangle` | 三角形の3辺の長さを与える。三角形が直角三角形ならTrueを、そうでなければFalseを返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 158 | `find_max` | 文字列のリストを受け取る関数を書きなさい。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 159 | `eat` | あなたはお腹を空かせたウサギです。すでに一定数のニンジンを食べました。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 160 | `do_algebra` | 演算子(operator)とオペランド(operand)の2つのリストが与えられる。ひとつ目のリストは | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 161 | `solve` | 文字列sが与えられます。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 162 | `string_to_md5` | 文字列 text が与えられたとき、その md5 ハッシュと等価な文字列を返す。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
| 163 | `generate_integers` | 正の整数aとbが与えられたとき、aとbの間にある偶数の数字を昇順で返してください。 | 構文認識不可(Yui非準拠) | Error: No syntax matched the given files. |
