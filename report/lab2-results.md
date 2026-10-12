# Lab 2 test results

37/37 checks passed.

Generated with `python3 test/lab2/run_tests.py --report`.

ASTs below use dataclass representations, including reused Token fields.
Runnable constructions are in `test/lab2/examples.py` and `run_tests.py`.

## nested_example

Unary, binary, and grouping nodes in one tree.

Hard-coded AST / input:
```text
Binary(left=Unary(operator=Token(type=<TokenType.MINUS: 11>,
                                 lexeme='-',
                                 literal=None,
                                 line=1),
                  right=Literal(value=123)),
       operator=Token(type=<TokenType.STAR: 12>, lexeme='*', literal=None, line=1),
       right=Grouping(expression=Literal(value=45.67)))
```

Expected:
```text
(* (- 123) (group 45.67))
```

Actual:
```text
(* (- 123) (group 45.67))
```

Result: PASS

## integer

Print an integer literal.

Hard-coded AST / input:
```text
Literal(value=42)
```

Expected:
```text
42
```

Actual:
```text
42
```

Result: PASS

## decimal

Preserve a fractional number.

Hard-coded AST / input:
```text
Literal(value=3.14)
```

Expected:
```text
3.14
```

Actual:
```text
3.14
```

Result: PASS

## whole_float

Whole floats use the same display as integers.

Hard-coded AST / input:
```text
Literal(value=42.0)
```

Expected:
```text
42
```

Actual:
```text
42
```

Result: PASS

## zero

Print zero without an unnecessary decimal point.

Hard-coded AST / input:
```text
Literal(value=0.0)
```

Expected:
```text
0
```

Actual:
```text
0
```

Result: PASS

## string

Keep quotes around string values.

Hard-coded AST / input:
```text
Literal(value='Ember')
```

Expected:
```text
"Ember"
```

Actual:
```text
"Ember"
```

Result: PASS

## empty_string

An empty string is distinct from null.

Hard-coded AST / input:
```text
Literal(value='')
```

Expected:
```text
""
```

Actual:
```text
""
```

Result: PASS

## string_escapes

Escape quotes, backslashes, LF, CR, and tab.

Hard-coded AST / input:
```text
Literal(value='a"b\\c\n\r\t')
```

Expected:
```text
"a\"b\\c\n\r\t"
```

Actual:
```text
"a\"b\\c\n\r\t"
```

Result: PASS

## unicode

Preserve Unicode text inside strings.

Hard-coded AST / input:
```text
Literal(value='مرحبا')
```

Expected:
```text
"مرحبا"
```

Actual:
```text
"مرحبا"
```

Result: PASS

## true

Use Ember spelling for true.

Hard-coded AST / input:
```text
Literal(value=True)
```

Expected:
```text
true
```

Actual:
```text
true
```

Result: PASS

## false

Use Ember spelling for false.

Hard-coded AST / input:
```text
Literal(value=False)
```

Expected:
```text
false
```

Actual:
```text
false
```

Result: PASS

## null

Use Ember null instead of Python None or Lox nil.

Hard-coded AST / input:
```text
Literal(value=None)
```

Expected:
```text
null
```

Actual:
```text
null
```

Result: PASS

## not

Print unary logical negation.

Hard-coded AST / input:
```text
Unary(operator=Token(type=<TokenType.BANG: 15>, lexeme='!', literal=None, line=1),
      right=Literal(value=True))
```

Expected:
```text
(! true)
```

Actual:
```text
(! true)
```

Result: PASS

## double_unary

Preserve nested unary operators.

Hard-coded AST / input:
```text
Unary(operator=Token(type=<TokenType.MINUS: 11>, lexeme='-', literal=None, line=1),
      right=Unary(operator=Token(type=<TokenType.MINUS: 11>,
                                 lexeme='-',
                                 literal=None,
                                 line=1),
                  right=Literal(value=2)))
```

Expected:
```text
(- (- 2))
```

Actual:
```text
(- (- 2))
```

Result: PASS

## addition

Print addition.

Hard-coded AST / input:
```text
Binary(left=Literal(value=2),
       operator=Token(type=<TokenType.PLUS: 10>, lexeme='+', literal=None, line=1),
       right=Literal(value=3))
```

Expected:
```text
(+ 2 3)
```

Actual:
```text
(+ 2 3)
```

Result: PASS

## subtraction

Print binary subtraction.

Hard-coded AST / input:
```text
Binary(left=Literal(value=2),
       operator=Token(type=<TokenType.MINUS: 11>, lexeme='-', literal=None, line=1),
       right=Literal(value=3))
```

Expected:
```text
(- 2 3)
```

Actual:
```text
(- 2 3)
```

Result: PASS

## multiplication

Print multiplication.

Hard-coded AST / input:
```text
Binary(left=Literal(value=2),
       operator=Token(type=<TokenType.STAR: 12>, lexeme='*', literal=None, line=1),
       right=Literal(value=3))
```

Expected:
```text
(* 2 3)
```

Actual:
```text
(* 2 3)
```

Result: PASS

## division

Print division without evaluating it.

Hard-coded AST / input:
```text
Binary(left=Literal(value=2),
       operator=Token(type=<TokenType.SLASH: 13>, lexeme='/', literal=None, line=1),
       right=Literal(value=0))
```

Expected:
```text
(/ 2 0)
```

Actual:
```text
(/ 2 0)
```

Result: PASS

## remainder

Print Ember's remainder operator.

Hard-coded AST / input:
```text
Binary(left=Literal(value=7),
       operator=Token(type=<TokenType.PERCENT: 14>,
                      lexeme='%',
                      literal=None,
                      line=1),
       right=Literal(value=3))
```

Expected:
```text
(% 7 3)
```

Actual:
```text
(% 7 3)
```

Result: PASS

## equal

Print equality.

Hard-coded AST / input:
```text
Binary(left=Literal(value=None),
       operator=Token(type=<TokenType.EQUAL_EQUAL: 18>,
                      lexeme='==',
                      literal=None,
                      line=1),
       right=Literal(value=None))
```

Expected:
```text
(== null null)
```

Actual:
```text
(== null null)
```

Result: PASS

## not_equal

Print inequality.

Hard-coded AST / input:
```text
Binary(left=Literal(value=2),
       operator=Token(type=<TokenType.BANG_EQUAL: 16>,
                      lexeme='!=',
                      literal=None,
                      line=1),
       right=Literal(value=3))
```

Expected:
```text
(!= 2 3)
```

Actual:
```text
(!= 2 3)
```

Result: PASS

## less

Print less-than.

Hard-coded AST / input:
```text
Binary(left=Literal(value=2),
       operator=Token(type=<TokenType.LESS: 19>, lexeme='<', literal=None, line=1),
       right=Literal(value=3))
```

Expected:
```text
(< 2 3)
```

Actual:
```text
(< 2 3)
```

Result: PASS

## less_equal

Print less-than-or-equal.

Hard-coded AST / input:
```text
Binary(left=Literal(value=2),
       operator=Token(type=<TokenType.LESS_EQUAL: 20>,
                      lexeme='<=',
                      literal=None,
                      line=1),
       right=Literal(value=3))
```

Expected:
```text
(<= 2 3)
```

Actual:
```text
(<= 2 3)
```

Result: PASS

## greater

Print greater-than.

Hard-coded AST / input:
```text
Binary(left=Literal(value=2),
       operator=Token(type=<TokenType.GREATER: 21>,
                      lexeme='>',
                      literal=None,
                      line=1),
       right=Literal(value=3))
```

Expected:
```text
(> 2 3)
```

Actual:
```text
(> 2 3)
```

Result: PASS

## greater_equal

Print greater-than-or-equal.

Hard-coded AST / input:
```text
Binary(left=Literal(value=2),
       operator=Token(type=<TokenType.GREATER_EQUAL: 22>,
                      lexeme='>=',
                      literal=None,
                      line=1),
       right=Literal(value=3))
```

Expected:
```text
(>= 2 3)
```

Actual:
```text
(>= 2 3)
```

Result: PASS

## and

Represent logical and without evaluating it.

Hard-coded AST / input:
```text
Binary(left=Literal(value=True),
       operator=Token(type=<TokenType.AND: 36>, lexeme='and', literal=None, line=1),
       right=Literal(value=False))
```

Expected:
```text
(and true false)
```

Actual:
```text
(and true false)
```

Result: PASS

## or

Represent logical or without evaluating it.

Hard-coded AST / input:
```text
Binary(left=Literal(value=False),
       operator=Token(type=<TokenType.OR: 37>, lexeme='or', literal=None, line=1),
       right=Literal(value=True))
```

Expected:
```text
(or false true)
```

Actual:
```text
(or false true)
```

Result: PASS

## left_nested

Preserve left nesting for subtraction.

Hard-coded AST / input:
```text
Binary(left=Binary(left=Literal(value=8),
                   operator=Token(type=<TokenType.MINUS: 11>,
                                  lexeme='-',
                                  literal=None,
                                  line=1),
                   right=Literal(value=3)),
       operator=Token(type=<TokenType.MINUS: 11>, lexeme='-', literal=None, line=1),
       right=Literal(value=1))
```

Expected:
```text
(- (- 8 3) 1)
```

Actual:
```text
(- (- 8 3) 1)
```

Result: PASS

## right_nested

A different tree must produce different parentheses.

Hard-coded AST / input:
```text
Binary(left=Literal(value=8),
       operator=Token(type=<TokenType.MINUS: 11>, lexeme='-', literal=None, line=1),
       right=Grouping(expression=Binary(left=Literal(value=3),
                                        operator=Token(type=<TokenType.MINUS: 11>,
                                                       lexeme='-',
                                                       literal=None,
                                                       line=1),
                                        right=Literal(value=1))))
```

Expected:
```text
(- 8 (group (- 3 1)))
```

Actual:
```text
(- 8 (group (- 3 1)))
```

Result: PASS

## nested_grouping

Retain even redundant grouping nodes.

Hard-coded AST / input:
```text
Grouping(expression=Grouping(expression=Literal(value=1)))
```

Expected:
```text
(group (group 1))
```

Actual:
```text
(group (group 1))
```

Result: PASS

## mixed_precedence

Show arithmetic nested inside comparison and logic.

Hard-coded AST / input:
```text
Binary(left=Binary(left=Binary(left=Literal(value=1),
                               operator=Token(type=<TokenType.PLUS: 10>,
                                              lexeme='+',
                                              literal=None,
                                              line=1),
                               right=Binary(left=Literal(value=2),
                                            operator=Token(type=<TokenType.STAR: 12>,
                                                           lexeme='*',
                                                           literal=None,
                                                           line=1),
                                            right=Literal(value=3))),
                   operator=Token(type=<TokenType.LESS: 19>,
                                  lexeme='<',
                                  literal=None,
                                  line=1),
                   right=Literal(value=10)),
       operator=Token(type=<TokenType.AND: 36>, lexeme='and', literal=None, line=1),
       right=Unary(operator=Token(type=<TokenType.BANG: 15>,
                                  lexeme='!',
                                  literal=None,
                                  line=1),
                   right=Literal(value=False)))
```

Expected:
```text
(and (< (+ 1 (* 2 3)) 10) (! false))
```

Actual:
```text
(and (< (+ 1 (* 2 3)) 10) (! false))
```

Result: PASS

## string_parentheses

Quoted string punctuation cannot be mistaken for tree structure.

Hard-coded AST / input:
```text
Literal(value='(group x)')
```

Expected:
```text
"(group x)"
```

Actual:
```text
"(group x)"
```

Result: PASS

## stored_fields

Nodes retain their actual children, token, and literal value.

Hard-coded AST / input:
```text
Grouping(expression=Binary(left=Literal(value=2),
                           operator=Token(type=<TokenType.PLUS: 10>,
                                          lexeme='+',
                                          literal=None,
                                          line=1),
                           right=Literal(value=3)))
```

Expected:
```text
(True, True, True, True, True, 2)
```

Actual:
```text
(True, True, True, True, True, 2)
```

Result: PASS

## unknown_node

Reject unsupported manually constructed input clearly.

Hard-coded AST / input:
```text
'object()'
```

Expected:
```text
TypeError: Unsupported expression type: object
```

Actual:
```text
TypeError: Unsupported expression type: object
```

Result: PASS

## unsupported_literal

Reject unsupported manually constructed input clearly.

Hard-coded AST / input:
```text
Literal(value=[])
```

Expected:
```text
TypeError: Unsupported literal type: list
```

Actual:
```text
TypeError: Unsupported literal type: list
```

Result: PASS

## infinity

Reject unsupported manually constructed input clearly.

Hard-coded AST / input:
```text
Literal(value=inf)
```

Expected:
```text
ValueError: Number literals must be finite.
```

Actual:
```text
ValueError: Number literals must be finite.
```

Result: PASS

## nan

Reject unsupported manually constructed input clearly.

Hard-coded AST / input:
```text
Literal(value=nan)
```

Expected:
```text
ValueError: Number literals must be finite.
```

Actual:
```text
ValueError: Number literals must be finite.
```

Result: PASS
