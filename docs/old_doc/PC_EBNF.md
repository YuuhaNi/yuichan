### EBNF (Extended BNF) 完全版

Yui言語の構文規則を 拡張BNF (Extended Backus-Naur Form) で定義します。

```ebnf
(* プログラム *)
program = [ stdlib_import ] , { definition | test_case } ;

stdlib_import = "標準ライブラリを使う" ;

(* 定義 *)
definition = function_def ;

function_def = identifier , "=" , "入力" , params , "に対し" , "{" , newline ,
               { statement } ,
               "}" ;

params = param_list | "なし" ;

param_list = identifier , { "," , identifier } ;

(* 文 *)
statement = assignment
          | if_statement
          | loop_statement
          | loop_control
          | return_statement
          | increment_statement
          | decrement_statement
          | array_append
          | array_update
          | expression_statement ;

assignment = identifier , "=" , expression ;

if_statement = "もし" , condition , "ならば、" , "{" , newline ,
               { statement } ,
               "}" ,
               [ "そうでなければ" , "{" , newline ,
                 { statement } ,
                 "}"
               ] ;

loop_statement = expression , "回、くり返す" , "{" , newline ,
                 { statement } ,
                 "}" ;

loop_control = "くり返しを抜ける"　;

return_statement = expression , "が答え" ;

increment_statement = identifier , "を増やす" ;

decrement_statement = identifier , "を減らす" ;

array_append = identifier , "の末尾に" , expression , "を" , "追加する" ;

array_update = identifier , "[" , expression , "]" , "=" , expression ;

expression_statement = expression ;

(* 条件 *)
condition = expression , comparison_op ;

comparison_op = "が" , expression
              | "が" , expression , "より大きい"
              | "が" , expression , "より小さい"
              | "が" , expression , "以上"
              | "が" , expression , "以下"
              | "が" , expression , "以外" ;

(* 式 *)
expression = literal
           | identifier
           | array_literal
           | array_access
           | array_length
           | function_call
           | string_literal ;

literal = integer | float ;

integer = [ "-" ] , digit , { digit } ;

float = [ "-" ] , digit , { digit } , "." , digit , { digit } ;

digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;

array_literal = "[" , [ expression_list ] , "]" ;

expression_list = expression , { "," , expression } ;

array_access = identifier , "[" , expression , "]" ;

array_length = "|" , identifier , "|" ;

function_call = identifier , "(" , [ expression_list ] , ")" ;

string_literal = '"' , { character } , '"' ;

character = ? any character except " ? ;

(* 識別子 *)
identifier = letter , { letter | digit | "_" } ;

letter = "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m" |
         "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z" |
         "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J" | "K" | "L" | "M" |
         "N" | "O" | "P" | "Q" | "R" | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z" |
         "_" ;

(* テストケース *)
test_case = ">>>" , expression , newline , value ;

value = integer | float | string_literal | array_literal ;

(* その他 *)
newline = ? line feed character ? ;

comment = "#" , { ? any character except newline ? } ;
```
