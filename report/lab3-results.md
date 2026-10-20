# Lab 3 test results

172/172 checks passed.

Run `python3 test/lab3/run_tests.py --report` to regenerate.

Source is shown with Python repr so physical line breaks, tabs, and escapes are unambiguous.
Expected values are specified separately from the implementation.
API entries scan/parse/print directly; file and prompt entries run the real main program.
Each case records stdout, stderr, and exit status; API cases use equivalent status values.

## number / API

A scanned whole number becomes a Literal.

Source / input:
```text
'42'
```

Expected:
```text
stdout:
42
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
42
stderr:
(empty)
exit status: 0
```

Result: PASS

## number / file

A scanned whole number becomes a Literal.

Source / input:
```text
'42'
```

Expected:
```text
stdout:
42
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
42
stderr:
(empty)
exit status: 0
```

Result: PASS

## decimal / API

Fractional values retain their fraction.

Source / input:
```text
'3.14'
```

Expected:
```text
stdout:
3.14
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
3.14
stderr:
(empty)
exit status: 0
```

Result: PASS

## decimal / file

Fractional values retain their fraction.

Source / input:
```text
'3.14'
```

Expected:
```text
stdout:
3.14
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
3.14
stderr:
(empty)
exit status: 0
```

Result: PASS

## zero / API

Zero is a valid number.

Source / input:
```text
'0'
```

Expected:
```text
stdout:
0
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
0
stderr:
(empty)
exit status: 0
```

Result: PASS

## zero / file

Zero is a valid number.

Source / input:
```text
'0'
```

Expected:
```text
stdout:
0
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
0
stderr:
(empty)
exit status: 0
```

Result: PASS

## string / API

String quotes remain visible in the AST.

Source / input:
```text
'"Ember"'
```

Expected:
```text
stdout:
"Ember"
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
"Ember"
stderr:
(empty)
exit status: 0
```

Result: PASS

## string / file

String quotes remain visible in the AST.

Source / input:
```text
'"Ember"'
```

Expected:
```text
stdout:
"Ember"
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
"Ember"
stderr:
(empty)
exit status: 0
```

Result: PASS

## empty_string / API

An empty string is distinct from null.

Source / input:
```text
'""'
```

Expected:
```text
stdout:
""
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
""
stderr:
(empty)
exit status: 0
```

Result: PASS

## empty_string / file

An empty string is distinct from null.

Source / input:
```text
'""'
```

Expected:
```text
stdout:
""
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
""
stderr:
(empty)
exit status: 0
```

Result: PASS

## unicode / API

Unicode is allowed inside strings.

Source / input:
```text
'"مرحبا"'
```

Expected:
```text
stdout:
"مرحبا"
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
"مرحبا"
stderr:
(empty)
exit status: 0
```

Result: PASS

## unicode / file

Unicode is allowed inside strings.

Source / input:
```text
'"مرحبا"'
```

Expected:
```text
stdout:
"مرحبا"
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
"مرحبا"
stderr:
(empty)
exit status: 0
```

Result: PASS

## escapes / API

Decode and reprint all five string escapes.

Source / input:
```text
'"a\\n\\r\\t\\"\\\\z"'
```

Expected:
```text
stdout:
"a\n\r\t\"\\z"
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
"a\n\r\t\"\\z"
stderr:
(empty)
exit status: 0
```

Result: PASS

## escapes / file

Decode and reprint all five string escapes.

Source / input:
```text
'"a\\n\\r\\t\\"\\\\z"'
```

Expected:
```text
stdout:
"a\n\r\t\"\\z"
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
"a\n\r\t\"\\z"
stderr:
(empty)
exit status: 0
```

Result: PASS

## true / API

Convert TRUE to a boolean Literal.

Source / input:
```text
'true'
```

Expected:
```text
stdout:
true
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
true
stderr:
(empty)
exit status: 0
```

Result: PASS

## true / file

Convert TRUE to a boolean Literal.

Source / input:
```text
'true'
```

Expected:
```text
stdout:
true
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
true
stderr:
(empty)
exit status: 0
```

Result: PASS

## false / API

Convert FALSE to a boolean Literal.

Source / input:
```text
'false'
```

Expected:
```text
stdout:
false
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
false
stderr:
(empty)
exit status: 0
```

Result: PASS

## false / file

Convert FALSE to a boolean Literal.

Source / input:
```text
'false'
```

Expected:
```text
stdout:
false
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
false
stderr:
(empty)
exit status: 0
```

Result: PASS

## null / API

Convert NULL to a Literal containing None.

Source / input:
```text
'null'
```

Expected:
```text
stdout:
null
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
null
stderr:
(empty)
exit status: 0
```

Result: PASS

## null / file

Convert NULL to a Literal containing None.

Source / input:
```text
'null'
```

Expected:
```text
stdout:
null
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
null
stderr:
(empty)
exit status: 0
```

Result: PASS

## negation / API

Unary minus binds to its right operand.

Source / input:
```text
'-2'
```

Expected:
```text
stdout:
(- 2)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(- 2)
stderr:
(empty)
exit status: 0
```

Result: PASS

## negation / file

Unary minus binds to its right operand.

Source / input:
```text
'-2'
```

Expected:
```text
stdout:
(- 2)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(- 2)
stderr:
(empty)
exit status: 0
```

Result: PASS

## not / API

Unary logical negation is represented without evaluation.

Source / input:
```text
'!true'
```

Expected:
```text
stdout:
(! true)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(! true)
stderr:
(empty)
exit status: 0
```

Result: PASS

## not / file

Unary logical negation is represented without evaluation.

Source / input:
```text
'!true'
```

Expected:
```text
stdout:
(! true)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(! true)
stderr:
(empty)
exit status: 0
```

Result: PASS

## unary_chain / API

Unary operators nest from right to left.

Source / input:
```text
'!- -2'
```

Expected:
```text
stdout:
(! (- (- 2)))
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(! (- (- 2)))
stderr:
(empty)
exit status: 0
```

Result: PASS

## unary_chain / file

Unary operators nest from right to left.

Source / input:
```text
'!- -2'
```

Expected:
```text
stdout:
(! (- (- 2)))
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(! (- (- 2)))
stderr:
(empty)
exit status: 0
```

Result: PASS

## add / API

Binary addition.

Source / input:
```text
'2+3'
```

Expected:
```text
stdout:
(+ 2 3)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(+ 2 3)
stderr:
(empty)
exit status: 0
```

Result: PASS

## add / file

Binary addition.

Source / input:
```text
'2+3'
```

Expected:
```text
stdout:
(+ 2 3)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(+ 2 3)
stderr:
(empty)
exit status: 0
```

Result: PASS

## subtract / API

Binary subtraction.

Source / input:
```text
'2-3'
```

Expected:
```text
stdout:
(- 2 3)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(- 2 3)
stderr:
(empty)
exit status: 0
```

Result: PASS

## subtract / file

Binary subtraction.

Source / input:
```text
'2-3'
```

Expected:
```text
stdout:
(- 2 3)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(- 2 3)
stderr:
(empty)
exit status: 0
```

Result: PASS

## multiply / API

Binary multiplication.

Source / input:
```text
'2*3'
```

Expected:
```text
stdout:
(* 2 3)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(* 2 3)
stderr:
(empty)
exit status: 0
```

Result: PASS

## multiply / file

Binary multiplication.

Source / input:
```text
'2*3'
```

Expected:
```text
stdout:
(* 2 3)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(* 2 3)
stderr:
(empty)
exit status: 0
```

Result: PASS

## divide / API

Division is parsed, not evaluated.

Source / input:
```text
'2/0'
```

Expected:
```text
stdout:
(/ 2 0)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(/ 2 0)
stderr:
(empty)
exit status: 0
```

Result: PASS

## divide / file

Division is parsed, not evaluated.

Source / input:
```text
'2/0'
```

Expected:
```text
stdout:
(/ 2 0)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(/ 2 0)
stderr:
(empty)
exit status: 0
```

Result: PASS

## remainder / API

Retain Ember's remainder operator.

Source / input:
```text
'7%3'
```

Expected:
```text
stdout:
(% 7 3)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(% 7 3)
stderr:
(empty)
exit status: 0
```

Result: PASS

## remainder / file

Retain Ember's remainder operator.

Source / input:
```text
'7%3'
```

Expected:
```text
stdout:
(% 7 3)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(% 7 3)
stderr:
(empty)
exit status: 0
```

Result: PASS

## equal / API

Equality of null literals.

Source / input:
```text
'null==null'
```

Expected:
```text
stdout:
(== null null)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(== null null)
stderr:
(empty)
exit status: 0
```

Result: PASS

## equal / file

Equality of null literals.

Source / input:
```text
'null==null'
```

Expected:
```text
stdout:
(== null null)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(== null null)
stderr:
(empty)
exit status: 0
```

Result: PASS

## not_equal / API

Inequality.

Source / input:
```text
'2!=3'
```

Expected:
```text
stdout:
(!= 2 3)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(!= 2 3)
stderr:
(empty)
exit status: 0
```

Result: PASS

## not_equal / file

Inequality.

Source / input:
```text
'2!=3'
```

Expected:
```text
stdout:
(!= 2 3)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(!= 2 3)
stderr:
(empty)
exit status: 0
```

Result: PASS

## less / API

Less-than comparison.

Source / input:
```text
'2<3'
```

Expected:
```text
stdout:
(< 2 3)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(< 2 3)
stderr:
(empty)
exit status: 0
```

Result: PASS

## less / file

Less-than comparison.

Source / input:
```text
'2<3'
```

Expected:
```text
stdout:
(< 2 3)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(< 2 3)
stderr:
(empty)
exit status: 0
```

Result: PASS

## less_equal / API

Less-than-or-equal comparison.

Source / input:
```text
'2<=3'
```

Expected:
```text
stdout:
(<= 2 3)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(<= 2 3)
stderr:
(empty)
exit status: 0
```

Result: PASS

## less_equal / file

Less-than-or-equal comparison.

Source / input:
```text
'2<=3'
```

Expected:
```text
stdout:
(<= 2 3)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(<= 2 3)
stderr:
(empty)
exit status: 0
```

Result: PASS

## greater / API

Greater-than comparison.

Source / input:
```text
'2>3'
```

Expected:
```text
stdout:
(> 2 3)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(> 2 3)
stderr:
(empty)
exit status: 0
```

Result: PASS

## greater / file

Greater-than comparison.

Source / input:
```text
'2>3'
```

Expected:
```text
stdout:
(> 2 3)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(> 2 3)
stderr:
(empty)
exit status: 0
```

Result: PASS

## greater_equal / API

Greater-than-or-equal comparison.

Source / input:
```text
'2>=3'
```

Expected:
```text
stdout:
(>= 2 3)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(>= 2 3)
stderr:
(empty)
exit status: 0
```

Result: PASS

## greater_equal / file

Greater-than-or-equal comparison.

Source / input:
```text
'2>=3'
```

Expected:
```text
stdout:
(>= 2 3)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(>= 2 3)
stderr:
(empty)
exit status: 0
```

Result: PASS

## and / API

Logical and remains supported from Lab 2.

Source / input:
```text
'true and false'
```

Expected:
```text
stdout:
(and true false)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(and true false)
stderr:
(empty)
exit status: 0
```

Result: PASS

## and / file

Logical and remains supported from Lab 2.

Source / input:
```text
'true and false'
```

Expected:
```text
stdout:
(and true false)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(and true false)
stderr:
(empty)
exit status: 0
```

Result: PASS

## or / API

Logical or remains supported from Lab 2.

Source / input:
```text
'false or true'
```

Expected:
```text
stdout:
(or false true)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(or false true)
stderr:
(empty)
exit status: 0
```

Result: PASS

## or / file

Logical or remains supported from Lab 2.

Source / input:
```text
'false or true'
```

Expected:
```text
stdout:
(or false true)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(or false true)
stderr:
(empty)
exit status: 0
```

Result: PASS

## precedence_tree / API

Multiplication binds more tightly than addition; diagram example.

Source / input:
```text
'1 + 2 * 3'
```

Expected:
```text
stdout:
(+ 1 (* 2 3))
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(+ 1 (* 2 3))
stderr:
(empty)
exit status: 0
```

Result: PASS

## precedence_tree / file

Multiplication binds more tightly than addition; diagram example.

Source / input:
```text
'1 + 2 * 3'
```

Expected:
```text
stdout:
(+ 1 (* 2 3))
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(+ 1 (* 2 3))
stderr:
(empty)
exit status: 0
```

Result: PASS

## all_precedence / API

Exercise every precedence boundary in one expression.

Source / input:
```text
'false or true and 1 == 2 < 3 + 4 * -5'
```

Expected:
```text
stdout:
(or false (and true (== 1 (< 2 (+ 3 (* 4 (- 5)))))))
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(or false (and true (== 1 (< 2 (+ 3 (* 4 (- 5)))))))
stderr:
(empty)
exit status: 0
```

Result: PASS

## all_precedence / file

Exercise every precedence boundary in one expression.

Source / input:
```text
'false or true and 1 == 2 < 3 + 4 * -5'
```

Expected:
```text
stdout:
(or false (and true (== 1 (< 2 (+ 3 (* 4 (- 5)))))))
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(or false (and true (== 1 (< 2 (+ 3 (* 4 (- 5)))))))
stderr:
(empty)
exit status: 0
```

Result: PASS

## left_term / API

Addition and subtraction associate left.

Source / input:
```text
'8-3+1'
```

Expected:
```text
stdout:
(+ (- 8 3) 1)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(+ (- 8 3) 1)
stderr:
(empty)
exit status: 0
```

Result: PASS

## left_term / file

Addition and subtraction associate left.

Source / input:
```text
'8-3+1'
```

Expected:
```text
stdout:
(+ (- 8 3) 1)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(+ (- 8 3) 1)
stderr:
(empty)
exit status: 0
```

Result: PASS

## left_factor / API

Division, multiplication, and remainder associate left.

Source / input:
```text
'20/2*3%4'
```

Expected:
```text
stdout:
(% (* (/ 20 2) 3) 4)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(% (* (/ 20 2) 3) 4)
stderr:
(empty)
exit status: 0
```

Result: PASS

## left_factor / file

Division, multiplication, and remainder associate left.

Source / input:
```text
'20/2*3%4'
```

Expected:
```text
stdout:
(% (* (/ 20 2) 3) 4)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(% (* (/ 20 2) 3) 4)
stderr:
(empty)
exit status: 0
```

Result: PASS

## left_equality / API

Equality operators associate left, without type checking.

Source / input:
```text
'1==2!=false'
```

Expected:
```text
stdout:
(!= (== 1 2) false)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(!= (== 1 2) false)
stderr:
(empty)
exit status: 0
```

Result: PASS

## left_equality / file

Equality operators associate left, without type checking.

Source / input:
```text
'1==2!=false'
```

Expected:
```text
stdout:
(!= (== 1 2) false)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(!= (== 1 2) false)
stderr:
(empty)
exit status: 0
```

Result: PASS

## left_comparison / API

Comparison operators associate left.

Source / input:
```text
'1<2>=3'
```

Expected:
```text
stdout:
(>= (< 1 2) 3)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(>= (< 1 2) 3)
stderr:
(empty)
exit status: 0
```

Result: PASS

## left_comparison / file

Comparison operators associate left.

Source / input:
```text
'1<2>=3'
```

Expected:
```text
stdout:
(>= (< 1 2) 3)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(>= (< 1 2) 3)
stderr:
(empty)
exit status: 0
```

Result: PASS

## left_and / API

Repeated and operators associate left.

Source / input:
```text
'true and false and true'
```

Expected:
```text
stdout:
(and (and true false) true)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(and (and true false) true)
stderr:
(empty)
exit status: 0
```

Result: PASS

## left_and / file

Repeated and operators associate left.

Source / input:
```text
'true and false and true'
```

Expected:
```text
stdout:
(and (and true false) true)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(and (and true false) true)
stderr:
(empty)
exit status: 0
```

Result: PASS

## left_or / API

Repeated or operators associate left.

Source / input:
```text
'true or false or true'
```

Expected:
```text
stdout:
(or (or true false) true)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(or (or true false) true)
stderr:
(empty)
exit status: 0
```

Result: PASS

## left_or / file

Repeated or operators associate left.

Source / input:
```text
'true or false or true'
```

Expected:
```text
stdout:
(or (or true false) true)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(or (or true false) true)
stderr:
(empty)
exit status: 0
```

Result: PASS

## grouping / API

Parentheses override multiplication precedence.

Source / input:
```text
'(1+2)*3'
```

Expected:
```text
stdout:
(* (group (+ 1 2)) 3)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(* (group (+ 1 2)) 3)
stderr:
(empty)
exit status: 0
```

Result: PASS

## grouping / file

Parentheses override multiplication precedence.

Source / input:
```text
'(1+2)*3'
```

Expected:
```text
stdout:
(* (group (+ 1 2)) 3)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(* (group (+ 1 2)) 3)
stderr:
(empty)
exit status: 0
```

Result: PASS

## nested_grouping / API

Every explicit grouping node is retained.

Source / input:
```text
'((1))'
```

Expected:
```text
stdout:
(group (group 1))
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(group (group 1))
stderr:
(empty)
exit status: 0
```

Result: PASS

## nested_grouping / file

Every explicit grouping node is retained.

Source / input:
```text
'((1))'
```

Expected:
```text
stdout:
(group (group 1))
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(group (group 1))
stderr:
(empty)
exit status: 0
```

Result: PASS

## nested_unary / API

Combine unary, binary, and grouping expressions.

Source / input:
```text
'-123*(45.67)'
```

Expected:
```text
stdout:
(* (- 123) (group 45.67))
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(* (- 123) (group 45.67))
stderr:
(empty)
exit status: 0
```

Result: PASS

## nested_unary / file

Combine unary, binary, and grouping expressions.

Source / input:
```text
'-123*(45.67)'
```

Expected:
```text
stdout:
(* (- 123) (group 45.67))
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(* (- 123) (group 45.67))
stderr:
(empty)
exit status: 0
```

Result: PASS

## right_group / API

Explicit right nesting differs from left associativity.

Source / input:
```text
'8-(3-1)'
```

Expected:
```text
stdout:
(- 8 (group (- 3 1)))
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(- 8 (group (- 3 1)))
stderr:
(empty)
exit status: 0
```

Result: PASS

## right_group / file

Explicit right nesting differs from left associativity.

Source / input:
```text
'8-(3-1)'
```

Expected:
```text
stdout:
(- 8 (group (- 3 1)))
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(- 8 (group (- 3 1)))
stderr:
(empty)
exit status: 0
```

Result: PASS

## comments / API

Nested comments and a trailing line comment are ignored.

Source / input:
```text
'1/* outer /* inner */ end */+2 // end'
```

Expected:
```text
stdout:
(+ 1 2)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(+ 1 2)
stderr:
(empty)
exit status: 0
```

Result: PASS

## comments / file

Nested comments and a trailing line comment are ignored.

Source / input:
```text
'1/* outer /* inner */ end */+2 // end'
```

Expected:
```text
stdout:
(+ 1 2)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(+ 1 2)
stderr:
(empty)
exit status: 0
```

Result: PASS

## multiline / API

One expression may span physical lines in a file.

Source / input:
```text
'(1\r\n+2)\r*\n3'
```

Expected:
```text
stdout:
(* (group (+ 1 2)) 3)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(* (group (+ 1 2)) 3)
stderr:
(empty)
exit status: 0
```

Result: PASS

## multiline / file

One expression may span physical lines in a file.

Source / input:
```text
'(1\r\n+2)\r*\n3'
```

Expected:
```text
stdout:
(* (group (+ 1 2)) 3)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(* (group (+ 1 2)) 3)
stderr:
(empty)
exit status: 0
```

Result: PASS

## empty / API

EOF arrives before any expression.

Source / input:
```text
''
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at end: Expected an expression.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at end: Expected an expression.
exit status: 65
```

Result: PASS

## empty / file

EOF arrives before any expression.

Source / input:
```text
''
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at end: Expected an expression.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at end: Expected an expression.
exit status: 65
```

Result: PASS

## only_comment / API

Comments do not provide an operand.

Source / input:
```text
'// nothing'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at end: Expected an expression.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at end: Expected an expression.
exit status: 65
```

Result: PASS

## only_comment / file

Comments do not provide an operand.

Source / input:
```text
'// nothing'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at end: Expected an expression.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at end: Expected an expression.
exit status: 65
```

Result: PASS

## missing_right / API

Addition has no right operand.

Source / input:
```text
'1+'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at end: Expected an expression.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at end: Expected an expression.
exit status: 65
```

Result: PASS

## missing_right / file

Addition has no right operand.

Source / input:
```text
'1+'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at end: Expected an expression.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at end: Expected an expression.
exit status: 65
```

Result: PASS

## missing_unary / API

Unary minus has no operand.

Source / input:
```text
'-'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at end: Expected an expression.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at end: Expected an expression.
exit status: 65
```

Result: PASS

## missing_unary / file

Unary minus has no operand.

Source / input:
```text
'-'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at end: Expected an expression.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at end: Expected an expression.
exit status: 65
```

Result: PASS

## empty_group / API

Grouping must contain an expression.

Source / input:
```text
'()'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at ')': Expected an expression.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at ')': Expected an expression.
exit status: 65
```

Result: PASS

## empty_group / file

Grouping must contain an expression.

Source / input:
```text
'()'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at ')': Expected an expression.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at ')': Expected an expression.
exit status: 65
```

Result: PASS

## missing_close / API

An opening parenthesis is never closed.

Source / input:
```text
'(1+2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at end: Expected ')' after expression (opened on line 1).
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at end: Expected ')' after expression (opened on line 1).
exit status: 65
```

Result: PASS

## missing_close / file

An opening parenthesis is never closed.

Source / input:
```text
'(1+2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at end: Expected ')' after expression (opened on line 1).
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at end: Expected ')' after expression (opened on line 1).
exit status: 65
```

Result: PASS

## missing_outer_close / API

Closing an inner group does not close its parent.

Source / input:
```text
'((1)'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at end: Expected ')' after expression (opened on line 1).
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at end: Expected ')' after expression (opened on line 1).
exit status: 65
```

Result: PASS

## missing_outer_close / file

Closing an inner group does not close its parent.

Source / input:
```text
'((1)'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at end: Expected ')' after expression (opened on line 1).
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at end: Expected ')' after expression (opened on line 1).
exit status: 65
```

Result: PASS

## multiline_close / API

Identify both the EOF line and the opening line.

Source / input:
```text
'\n(1+\n2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 3] Error at end: Expected ')' after expression (opened on line 2).
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 3] Error at end: Expected ')' after expression (opened on line 2).
exit status: 65
```

Result: PASS

## multiline_close / file

Identify both the EOF line and the opening line.

Source / input:
```text
'\n(1+\n2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 3] Error at end: Expected ')' after expression (opened on line 2).
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 3] Error at end: Expected ')' after expression (opened on line 2).
exit status: 65
```

Result: PASS

## unexpected_close / API

A closing parenthesis cannot begin an expression.

Source / input:
```text
')'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at ')': Expected an expression.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at ')': Expected an expression.
exit status: 65
```

Result: PASS

## unexpected_close / file

A closing parenthesis cannot begin an expression.

Source / input:
```text
')'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at ')': Expected an expression.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at ')': Expected an expression.
exit status: 65
```

Result: PASS

## extra_close / API

An extra closing parenthesis is an unexpected trailing token.

Source / input:
```text
'1)'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at ')': Unexpected trailing token.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at ')': Unexpected trailing token.
exit status: 65
```

Result: PASS

## extra_close / file

An extra closing parenthesis is an unexpected trailing token.

Source / input:
```text
'1)'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at ')': Unexpected trailing token.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at ')': Unexpected trailing token.
exit status: 65
```

Result: PASS

## missing_inside / API

The plus operator needs an operand before the group closes.

Source / input:
```text
'(1+)'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at ')': Expected an expression.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at ')': Expected an expression.
exit status: 65
```

Result: PASS

## missing_inside / file

The plus operator needs an operand before the group closes.

Source / input:
```text
'(1+)'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at ')': Expected an expression.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at ')': Expected an expression.
exit status: 65
```

Result: PASS

## identifier / API

Variables are outside Ember's expression subset.

Source / input:
```text
'count'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at 'count': Expected an expression.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at 'count': Expected an expression.
exit status: 65
```

Result: PASS

## identifier / file

Variables are outside Ember's expression subset.

Source / input:
```text
'count'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at 'count': Expected an expression.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at 'count': Expected an expression.
exit status: 65
```

Result: PASS

## keyword / API

A declaration keyword is not an expression.

Source / input:
```text
'let'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at 'let': Expected an expression.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at 'let': Expected an expression.
exit status: 65
```

Result: PASS

## keyword / file

A declaration keyword is not an expression.

Source / input:
```text
'let'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at 'let': Expected an expression.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at 'let': Expected an expression.
exit status: 65
```

Result: PASS

## two_literals / API

Exactly one expression is accepted.

Source / input:
```text
'1 2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at '2': Unexpected trailing token.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at '2': Unexpected trailing token.
exit status: 65
```

Result: PASS

## two_literals / file

Exactly one expression is accepted.

Source / input:
```text
'1 2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at '2': Unexpected trailing token.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at '2': Unexpected trailing token.
exit status: 65
```

Result: PASS

## semicolon / API

This expression grammar has no statement terminator.

Source / input:
```text
'1;'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at ';': Unexpected trailing token.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at ';': Unexpected trailing token.
exit status: 65
```

Result: PASS

## semicolon / file

This expression grammar has no statement terminator.

Source / input:
```text
'1;'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at ';': Unexpected trailing token.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at ';': Unexpected trailing token.
exit status: 65
```

Result: PASS

## assignment / API

Assignment is not an expression operator in this grammar.

Source / input:
```text
'1=2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at '=': Unexpected trailing token.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at '=': Unexpected trailing token.
exit status: 65
```

Result: PASS

## assignment / file

Assignment is not an expression operator in this grammar.

Source / input:
```text
'1=2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at '=': Unexpected trailing token.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at '=': Unexpected trailing token.
exit status: 65
```

Result: PASS

## group_tokens / API

A second operand inside parentheses cannot replace the closing delimiter.

Source / input:
```text
'(1 2)'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at '2': Expected ')' after expression (opened on line 1).
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at '2': Expected ')' after expression (opened on line 1).
exit status: 65
```

Result: PASS

## group_tokens / file

A second operand inside parentheses cannot replace the closing delimiter.

Source / input:
```text
'(1 2)'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at '2': Expected ')' after expression (opened on line 1).
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at '2': Expected ')' after expression (opened on line 1).
exit status: 65
```

Result: PASS

## trailing_multiline / API

Trailing tokens are located on the correct line.

Source / input:
```text
'1\n2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 2] Error at '2': Unexpected trailing token.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 2] Error at '2': Unexpected trailing token.
exit status: 65
```

Result: PASS

## trailing_multiline / file

Trailing tokens are located on the correct line.

Source / input:
```text
'1\n2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 2] Error at '2': Unexpected trailing token.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 2] Error at '2': Unexpected trailing token.
exit status: 65
```

Result: PASS

## decimal_dot / API

Lab 1 scans 1. as NUMBER then DOT; the DOT is rejected.

Source / input:
```text
'1.'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at '.': Unexpected trailing token.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at '.': Unexpected trailing token.
exit status: 65
```

Result: PASS

## decimal_dot / file

Lab 1 scans 1. as NUMBER then DOT; the DOT is rejected.

Source / input:
```text
'1.'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at '.': Unexpected trailing token.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at '.': Unexpected trailing token.
exit status: 65
```

Result: PASS

## number_identifier / API

Adjacent number and identifier tokens are not one expression.

Source / input:
```text
'123abc'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at 'abc': Unexpected trailing token.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at 'abc': Unexpected trailing token.
exit status: 65
```

Result: PASS

## number_identifier / file

Adjacent number and identifier tokens are not one expression.

Source / input:
```text
'123abc'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at 'abc': Unexpected trailing token.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at 'abc': Unexpected trailing token.
exit status: 65
```

Result: PASS

## lexical_character / API

A lexical error prevents printing an otherwise valid AST.

Source / input:
```text
'1 @ + 2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error: Unexpected character '@'.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error: Unexpected character '@'.
exit status: 65
```

Result: PASS

## lexical_character / file

A lexical error prevents printing an otherwise valid AST.

Source / input:
```text
'1 @ + 2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error: Unexpected character '@'.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error: Unexpected character '@'.
exit status: 65
```

Result: PASS

## lexical_string / API

An unterminated trailing string suppresses the entire AST.

Source / input:
```text
'1 "oops'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error: Unterminated string.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error: Unterminated string.
exit status: 65
```

Result: PASS

## lexical_string / file

An unterminated trailing string suppresses the entire AST.

Source / input:
```text
'1 "oops'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error: Unterminated string.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error: Unterminated string.
exit status: 65
```

Result: PASS

## lexical_escape / API

An invalid escape prevents parsing.

Source / input:
```text
'"bad\\q"'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error: Invalid escape '\q'.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error: Invalid escape '\q'.
exit status: 65
```

Result: PASS

## lexical_escape / file

An invalid escape prevents parsing.

Source / input:
```text
'"bad\\q"'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error: Invalid escape '\q'.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error: Invalid escape '\q'.
exit status: 65
```

Result: PASS

## lexical_comment / API

An unterminated comment suppresses a preceding valid number.

Source / input:
```text
'1 /*'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error: Unterminated block comment.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error: Unterminated block comment.
exit status: 65
```

Result: PASS

## lexical_comment / file

An unterminated comment suppresses a preceding valid number.

Source / input:
```text
'1 /*'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error: Unterminated block comment.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error: Unterminated block comment.
exit status: 65
```

Result: PASS

## lexical_overflow / API

An overflowing number produces a lexical error, not a host exception.

Source / input:
```text
'9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error: Number is too large.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error: Number is too large.
exit status: 65
```

Result: PASS

## lexical_overflow / file

An overflowing number produces a lexical error, not a host exception.

Source / input:
```text
'9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error: Number is too large.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error: Number is too large.
exit status: 65
```

Result: PASS

## missing_left_+ / API

A binary-only operator has no left operand.

Source / input:
```text
'+ 2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at '+': Missing left operand for '+'.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at '+': Missing left operand for '+'.
exit status: 65
```

Result: PASS

## missing_left_+ / file

A binary-only operator has no left operand.

Source / input:
```text
'+ 2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at '+': Missing left operand for '+'.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at '+': Missing left operand for '+'.
exit status: 65
```

Result: PASS

## missing_left_* / API

A binary-only operator has no left operand.

Source / input:
```text
'* 2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at '*': Missing left operand for '*'.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at '*': Missing left operand for '*'.
exit status: 65
```

Result: PASS

## missing_left_* / file

A binary-only operator has no left operand.

Source / input:
```text
'* 2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at '*': Missing left operand for '*'.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at '*': Missing left operand for '*'.
exit status: 65
```

Result: PASS

## missing_left_/ / API

A binary-only operator has no left operand.

Source / input:
```text
'/ 2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at '/': Missing left operand for '/'.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at '/': Missing left operand for '/'.
exit status: 65
```

Result: PASS

## missing_left_/ / file

A binary-only operator has no left operand.

Source / input:
```text
'/ 2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at '/': Missing left operand for '/'.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at '/': Missing left operand for '/'.
exit status: 65
```

Result: PASS

## missing_left_% / API

A binary-only operator has no left operand.

Source / input:
```text
'% 2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at '%': Missing left operand for '%'.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at '%': Missing left operand for '%'.
exit status: 65
```

Result: PASS

## missing_left_% / file

A binary-only operator has no left operand.

Source / input:
```text
'% 2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at '%': Missing left operand for '%'.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at '%': Missing left operand for '%'.
exit status: 65
```

Result: PASS

## missing_left_== / API

A binary-only operator has no left operand.

Source / input:
```text
'== 2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at '==': Missing left operand for '=='.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at '==': Missing left operand for '=='.
exit status: 65
```

Result: PASS

## missing_left_== / file

A binary-only operator has no left operand.

Source / input:
```text
'== 2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at '==': Missing left operand for '=='.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at '==': Missing left operand for '=='.
exit status: 65
```

Result: PASS

## missing_left_!= / API

A binary-only operator has no left operand.

Source / input:
```text
'!= 2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at '!=': Missing left operand for '!='.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at '!=': Missing left operand for '!='.
exit status: 65
```

Result: PASS

## missing_left_!= / file

A binary-only operator has no left operand.

Source / input:
```text
'!= 2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at '!=': Missing left operand for '!='.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at '!=': Missing left operand for '!='.
exit status: 65
```

Result: PASS

## missing_left_< / API

A binary-only operator has no left operand.

Source / input:
```text
'< 2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at '<': Missing left operand for '<'.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at '<': Missing left operand for '<'.
exit status: 65
```

Result: PASS

## missing_left_< / file

A binary-only operator has no left operand.

Source / input:
```text
'< 2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at '<': Missing left operand for '<'.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at '<': Missing left operand for '<'.
exit status: 65
```

Result: PASS

## missing_left_<= / API

A binary-only operator has no left operand.

Source / input:
```text
'<= 2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at '<=': Missing left operand for '<='.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at '<=': Missing left operand for '<='.
exit status: 65
```

Result: PASS

## missing_left_<= / file

A binary-only operator has no left operand.

Source / input:
```text
'<= 2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at '<=': Missing left operand for '<='.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at '<=': Missing left operand for '<='.
exit status: 65
```

Result: PASS

## missing_left_> / API

A binary-only operator has no left operand.

Source / input:
```text
'> 2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at '>': Missing left operand for '>'.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at '>': Missing left operand for '>'.
exit status: 65
```

Result: PASS

## missing_left_> / file

A binary-only operator has no left operand.

Source / input:
```text
'> 2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at '>': Missing left operand for '>'.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at '>': Missing left operand for '>'.
exit status: 65
```

Result: PASS

## missing_left_>= / API

A binary-only operator has no left operand.

Source / input:
```text
'>= 2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at '>=': Missing left operand for '>='.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at '>=': Missing left operand for '>='.
exit status: 65
```

Result: PASS

## missing_left_>= / file

A binary-only operator has no left operand.

Source / input:
```text
'>= 2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at '>=': Missing left operand for '>='.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at '>=': Missing left operand for '>='.
exit status: 65
```

Result: PASS

## missing_left_and / API

A binary-only operator has no left operand.

Source / input:
```text
'and 2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at 'and': Missing left operand for 'and'.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at 'and': Missing left operand for 'and'.
exit status: 65
```

Result: PASS

## missing_left_and / file

A binary-only operator has no left operand.

Source / input:
```text
'and 2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at 'and': Missing left operand for 'and'.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at 'and': Missing left operand for 'and'.
exit status: 65
```

Result: PASS

## missing_left_or / API

A binary-only operator has no left operand.

Source / input:
```text
'or 2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at 'or': Missing left operand for 'or'.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at 'or': Missing left operand for 'or'.
exit status: 65
```

Result: PASS

## missing_left_or / file

A binary-only operator has no left operand.

Source / input:
```text
'or 2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at 'or': Missing left operand for 'or'.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at 'or': Missing left operand for 'or'.
exit status: 65
```

Result: PASS

## consecutive_binary / API

The second binary-only operator lacks a left operand.

Source / input:
```text
'1 + * 2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at '*': Missing left operand for '*'.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at '*': Missing left operand for '*'.
exit status: 65
```

Result: PASS

## consecutive_binary / file

The second binary-only operator lacks a left operand.

Source / input:
```text
'1 + * 2'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error at '*': Missing left operand for '*'.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error at '*': Missing left operand for '*'.
exit status: 65
```

Result: PASS

## interactive_all_cases

All single-line cases run in one prompt session; recover after each error.

Source / input:
```text
'42\n3.14\n0\n"Ember"\n""\n"مرحبا"\n"a\\n\\r\\t\\"\\\\z"\ntrue\nfalse\nnull\n-2\n!true\n!- -2\n2+3\n2-3\n2*3\n2/0\n7%3\nnull==null\n2!=3\n2<3\n2<=3\n2>3\n2>=3\ntrue and false\nfalse or true\n1 + 2 * 3\nfalse or true and 1 == 2 < 3 + 4 * -5\n8-3+1\n20/2*3%4\n1==2!=false\n1<2>=3\ntrue and false and true\ntrue or false or true\n(1+2)*3\n((1))\n-123*(45.67)\n8-(3-1)\n1/* outer /* inner */ end */+2 // end\n\n2+3\n// nothing\n2+3\n1+\n2+3\n-\n2+3\n()\n2+3\n(1+2\n2+3\n((1)\n2+3\n)\n2+3\n1)\n2+3\n(1+)\n2+3\ncount\n2+3\nlet\n2+3\n1 2\n2+3\n1;\n2+3\n1=2\n2+3\n(1 2)\n2+3\n1.\n2+3\n123abc\n2+3\n1 @ + 2\n2+3\n1 "oops\n2+3\n"bad\\q"\n2+3\n1 /*\n2+3\n9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999\n2+3\n+ 2\n2+3\n* 2\n2+3\n/ 2\n2+3\n% 2\n2+3\n== 2\n2+3\n!= 2\n2+3\n< 2\n2+3\n<= 2\n2+3\n> 2\n2+3\n>= 2\n2+3\nand 2\n2+3\nor 2\n2+3\n1 + * 2\n2+3\n'
```

Expected:
```text
stdout:
ember> 42
ember> 3.14
ember> 0
ember> "Ember"
ember> ""
ember> "مرحبا"
ember> "a\n\r\t\"\\z"
ember> true
ember> false
ember> null
ember> (- 2)
ember> (! true)
ember> (! (- (- 2)))
ember> (+ 2 3)
ember> (- 2 3)
ember> (* 2 3)
ember> (/ 2 0)
ember> (% 7 3)
ember> (== null null)
ember> (!= 2 3)
ember> (< 2 3)
ember> (<= 2 3)
ember> (> 2 3)
ember> (>= 2 3)
ember> (and true false)
ember> (or false true)
ember> (+ 1 (* 2 3))
ember> (or false (and true (== 1 (< 2 (+ 3 (* 4 (- 5)))))))
ember> (+ (- 8 3) 1)
ember> (% (* (/ 20 2) 3) 4)
ember> (!= (== 1 2) false)
ember> (>= (< 1 2) 3)
ember> (and (and true false) true)
ember> (or (or true false) true)
ember> (* (group (+ 1 2)) 3)
ember> (group (group 1))
ember> (* (- 123) (group 45.67))
ember> (- 8 (group (- 3 1)))
ember> (+ 1 2)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> 
stderr:
[line 1] Error at end: Expected an expression.
[line 1] Error at end: Expected an expression.
[line 1] Error at end: Expected an expression.
[line 1] Error at end: Expected an expression.
[line 1] Error at ')': Expected an expression.
[line 1] Error at end: Expected ')' after expression (opened on line 1).
[line 1] Error at end: Expected ')' after expression (opened on line 1).
[line 1] Error at ')': Expected an expression.
[line 1] Error at ')': Unexpected trailing token.
[line 1] Error at ')': Expected an expression.
[line 1] Error at 'count': Expected an expression.
[line 1] Error at 'let': Expected an expression.
[line 1] Error at '2': Unexpected trailing token.
[line 1] Error at ';': Unexpected trailing token.
[line 1] Error at '=': Unexpected trailing token.
[line 1] Error at '2': Expected ')' after expression (opened on line 1).
[line 1] Error at '.': Unexpected trailing token.
[line 1] Error at 'abc': Unexpected trailing token.
[line 1] Error: Unexpected character '@'.
[line 1] Error: Unterminated string.
[line 1] Error: Invalid escape '\q'.
[line 1] Error: Unterminated block comment.
[line 1] Error: Number is too large.
[line 1] Error at '+': Missing left operand for '+'.
[line 1] Error at '*': Missing left operand for '*'.
[line 1] Error at '/': Missing left operand for '/'.
[line 1] Error at '%': Missing left operand for '%'.
[line 1] Error at '==': Missing left operand for '=='.
[line 1] Error at '!=': Missing left operand for '!='.
[line 1] Error at '<': Missing left operand for '<'.
[line 1] Error at '<=': Missing left operand for '<='.
[line 1] Error at '>': Missing left operand for '>'.
[line 1] Error at '>=': Missing left operand for '>='.
[line 1] Error at 'and': Missing left operand for 'and'.
[line 1] Error at 'or': Missing left operand for 'or'.
[line 1] Error at '*': Missing left operand for '*'.
exit status: 0
```

Actual:
```text
stdout:
ember> 42
ember> 3.14
ember> 0
ember> "Ember"
ember> ""
ember> "مرحبا"
ember> "a\n\r\t\"\\z"
ember> true
ember> false
ember> null
ember> (- 2)
ember> (! true)
ember> (! (- (- 2)))
ember> (+ 2 3)
ember> (- 2 3)
ember> (* 2 3)
ember> (/ 2 0)
ember> (% 7 3)
ember> (== null null)
ember> (!= 2 3)
ember> (< 2 3)
ember> (<= 2 3)
ember> (> 2 3)
ember> (>= 2 3)
ember> (and true false)
ember> (or false true)
ember> (+ 1 (* 2 3))
ember> (or false (and true (== 1 (< 2 (+ 3 (* 4 (- 5)))))))
ember> (+ (- 8 3) 1)
ember> (% (* (/ 20 2) 3) 4)
ember> (!= (== 1 2) false)
ember> (>= (< 1 2) 3)
ember> (and (and true false) true)
ember> (or (or true false) true)
ember> (* (group (+ 1 2)) 3)
ember> (group (group 1))
ember> (* (- 123) (group 45.67))
ember> (- 8 (group (- 3 1)))
ember> (+ 1 2)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> ember> (+ 2 3)
ember> 
stderr:
[line 1] Error at end: Expected an expression.
[line 1] Error at end: Expected an expression.
[line 1] Error at end: Expected an expression.
[line 1] Error at end: Expected an expression.
[line 1] Error at ')': Expected an expression.
[line 1] Error at end: Expected ')' after expression (opened on line 1).
[line 1] Error at end: Expected ')' after expression (opened on line 1).
[line 1] Error at ')': Expected an expression.
[line 1] Error at ')': Unexpected trailing token.
[line 1] Error at ')': Expected an expression.
[line 1] Error at 'count': Expected an expression.
[line 1] Error at 'let': Expected an expression.
[line 1] Error at '2': Unexpected trailing token.
[line 1] Error at ';': Unexpected trailing token.
[line 1] Error at '=': Unexpected trailing token.
[line 1] Error at '2': Expected ')' after expression (opened on line 1).
[line 1] Error at '.': Unexpected trailing token.
[line 1] Error at 'abc': Unexpected trailing token.
[line 1] Error: Unexpected character '@'.
[line 1] Error: Unterminated string.
[line 1] Error: Invalid escape '\q'.
[line 1] Error: Unterminated block comment.
[line 1] Error: Number is too large.
[line 1] Error at '+': Missing left operand for '+'.
[line 1] Error at '*': Missing left operand for '*'.
[line 1] Error at '/': Missing left operand for '/'.
[line 1] Error at '%': Missing left operand for '%'.
[line 1] Error at '==': Missing left operand for '=='.
[line 1] Error at '!=': Missing left operand for '!='.
[line 1] Error at '<': Missing left operand for '<'.
[line 1] Error at '<=': Missing left operand for '<='.
[line 1] Error at '>': Missing left operand for '>'.
[line 1] Error at '>=': Missing left operand for '>='.
[line 1] Error at 'and': Missing left operand for 'and'.
[line 1] Error at 'or': Missing left operand for 'or'.
[line 1] Error at '*': Missing left operand for '*'.
exit status: 0
```

Result: PASS

## interactive_EOF

An immediate EOF exits the prompt cleanly.

Source / input:
```text
''
```

Expected:
```text
stdout:
ember> 
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
ember> 
stderr:
(empty)
exit status: 0
```

Result: PASS

## AST_fields

The parser constructs the reused node classes and stores operator tokens and children.

Source / input:
```text
'-(1 + 2) * 3'
```

Expected:
```text
stdout:
(True, True, True, True, True, True, True, True)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(True, True, True, True, True, True, True, True)
stderr:
(empty)
exit status: 0
```

Result: PASS

## deep_grouping

Excessive tree depth produces a diagnostic, never a Python traceback or partial AST.

Source / input:
```text
'((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((1))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error: Expression is too deeply nested.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error: Expression is too deeply nested.
exit status: 65
```

Result: PASS

## deep_grouping / recovery

A valid prompt submission still works after excessive depth.

Source / input:
```text
'((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((1))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))\n2+3\n'
```

Expected:
```text
stdout:
ember> ember> (+ 2 3)
ember> 
stderr:
[line 1] Error: Expression is too deeply nested.
exit status: 0
```

Actual:
```text
stdout:
ember> ember> (+ 2 3)
ember> 
stderr:
[line 1] Error: Expression is too deeply nested.
exit status: 0
```

Result: PASS

## deep_unary

Excessive tree depth produces a diagnostic, never a Python traceback or partial AST.

Source / input:
```text
'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!true'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error: Expression is too deeply nested.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error: Expression is too deeply nested.
exit status: 65
```

Result: PASS

## deep_unary / recovery

A valid prompt submission still works after excessive depth.

Source / input:
```text
'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!true\n2+3\n'
```

Expected:
```text
stdout:
ember> ember> (+ 2 3)
ember> 
stderr:
[line 1] Error: Expression is too deeply nested.
exit status: 0
```

Actual:
```text
stdout:
ember> ember> (+ 2 3)
ember> 
stderr:
[line 1] Error: Expression is too deeply nested.
exit status: 0
```

Result: PASS

## deep_binary

Excessive tree depth produces a diagnostic, never a Python traceback or partial AST.

Source / input:
```text
'1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1'
```

Expected:
```text
stdout:
(empty)
stderr:
[line 1] Error: Expression tree is too deep to print.
exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 1] Error: Expression tree is too deep to print.
exit status: 65
```

Result: PASS

## deep_binary / recovery

A valid prompt submission still works after excessive depth.

Source / input:
```text
'1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1\n2+3\n'
```

Expected:
```text
stdout:
ember> ember> (+ 2 3)
ember> 
stderr:
[line 1] Error: Expression tree is too deep to print.
exit status: 0
```

Actual:
```text
stdout:
ember> ember> (+ 2 3)
ember> 
stderr:
[line 1] Error: Expression tree is too deep to print.
exit status: 0
```

Result: PASS

## usage

Only one source-file argument is accepted.

Source / input:
```text
arguments: a b
```

Expected:
```text
stdout:
(empty)
stderr:
Usage: python3 src/main.py [--tokens] [source.ember]
exit status: 64
```

Actual:
```text
stdout:
(empty)
stderr:
Usage: python3 src/main.py [--tokens] [source.ember]
exit status: 64
```

Result: PASS

## unknown_option

An unknown option is rejected.

Source / input:
```text
arguments: --bad
```

Expected:
```text
stdout:
(empty)
stderr:
Usage: python3 src/main.py [--tokens] [source.ember]
exit status: 64
```

Actual:
```text
stdout:
(empty)
stderr:
Usage: python3 src/main.py [--tokens] [source.ember]
exit status: 64
```

Result: PASS

## missing_file

A missing file is reported without a traceback.

Source / input:
```text
nonexistent path
```

Expected:
```text
stdout:
(empty)
stderr:
Error: Cannot read source file (UTF-8 required).
exit status: 66
```

Actual:
```text
stdout:
(empty)
stderr:
Error: Cannot read source file (UTF-8 required).
exit status: 66
```

Result: PASS

## invalid_UTF8

Invalid source encoding is reported without a traceback.

Source / input:
```text
bytes: ff
```

Expected:
```text
stdout:
(empty)
stderr:
Error: Cannot read source file (UTF-8 required).
exit status: 66
```

Actual:
```text
stdout:
(empty)
stderr:
Error: Cannot read source file (UTF-8 required).
exit status: 66
```

Result: PASS

## directory

A directory cannot be read as source.

Source / input:
```text
directory path
```

Expected:
```text
stdout:
(empty)
stderr:
Error: Cannot read source file (UTF-8 required).
exit status: 66
```

Actual:
```text
stdout:
(empty)
stderr:
Error: Cannot read source file (UTF-8 required).
exit status: 66
```

Result: PASS

## path_spaces

A source path may contain spaces.

Source / input:
```text
'1+2'
```

Expected:
```text
stdout:
(+ 1 2)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(+ 1 2)
stderr:
(empty)
exit status: 0
```

Result: PASS

## example_file

Run the committed, attributed example directly.

Source / input:
```text
'// --- start AI code ---\n1 + 2 * 3\n// --- end AI code ---\n'
```

Expected:
```text
stdout:
(+ 1 (* 2 3))
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(+ 1 (* 2 3))
stderr:
(empty)
exit status: 0
```

Result: PASS
