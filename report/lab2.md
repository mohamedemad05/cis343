# Lab 2: Ember AST printer

## Scope and design

This lab adds expression trees and a printer to Ember. Trees are built directly
in Python. There is no parser or evaluator: printing `(/ 2 0)` does not perform
division or raise a divide-by-zero error. The scanner and its command-line entry
point from Lab 1 are unchanged.

Ember has four expression classes: `Literal`, `Unary`, `Binary`, and `Grouping`.
They follow the basic expression shapes in Lox. The existing `Token` and
`TokenType` definitions are reused for operators, including their line numbers.

The implementation uses Python dataclasses and a small recursive printer with
`isinstance` checks. A visitor interface or class generator is unnecessary for
four classes. This keeps the code short while preserving the tree structure.

## Expression grammar

This EBNF grammar defines Ember's expression subset. Quoted text is a terminal,
`|` means an alternative, `*` means zero or more repetitions, and parentheses
outside quotes group grammar items. `NUMBER` and `STRING` are Lab 1 token types.

```text
expression  -> logic_or ;
logic_or    -> logic_and ( "or" logic_and )* ;
logic_and   -> equality ( "and" equality )* ;
equality    -> comparison ( ( "==" | "!=" ) comparison )* ;
comparison  -> term ( ( "<" | "<=" | ">" | ">=" ) term )* ;
term        -> factor ( ( "+" | "-" ) factor )* ;
factor      -> unary ( ( "*" | "/" | "%" ) unary )* ;
unary       -> ( "!" | "-" ) unary | primary ;
primary     -> NUMBER | STRING | "true" | "false" | "null"
             | "(" expression ")" ;
```

Precedence runs from `or` (lowest), then `and`, equality, comparison, addition
and subtraction, multiplication/division/remainder, unary, and primary expressions
(highest). Repeated binary operators at the same precedence are intended to
associate left. Unary operators nest right. Parentheses explicitly group a tree.
This grammar specifies how a future parser should build trees; the current
printer simply preserves the tree supplied to it.

Unary operators are `!` and `-`. Binary operators are `+`, `-`, `*`, `/`, `%`,
`==`, `!=`, `<`, `<=`, `>`, `>=`, `and`, and `or`. Assignment `=`, declarations,
calls, variables, lists, and indexing are outside this expression subset even
though Lab 1 recognizes some corresponding tokens.

Literal categories are numbers, strings, booleans, and null. Numbers in source
follow Lab 1's decimal rules and are scanned as floats. Hand-built ASTs accept
Python integers and finite floats for convenience. Strings may contain Unicode
and the characters represented by Ember's five escape sequences. Boolean values
use `True` or `False` internally, and null uses `None`.

### Differences from Lox

- Ember spells the null literal `null`, rather than `nil`.
- Ember includes `%` at the same precedence as `*` and `/`.
- `and` and `or` are represented by `Binary` in this lab. No short-circuit
  behavior is implemented or implied by printing them.
- Strings are printed with double quotes and Ember escape sequences, which
  distinguishes a string such as `"null"` from the null literal.
- The Python implementation uses dataclasses and direct dispatch instead of
  generated Java classes and visitor methods.

## AST classes and printer

Implementation files:

| File | Responsibility |
| --- | --- |
| `src/expr.py` | `Expr` base class and the four dataclasses |
| `src/ast_printer.py` | Recursive prefix printer and literal formatting |
| `src/tokens.py` | Reused Lab 1 tokens and operator types |

Each dataclass stores exactly the information needed for its expression:

| Class | Fields |
| --- | --- |
| `Literal` | `value` |
| `Unary` | `operator: Token`, `right: Expr` |
| `Binary` | `left: Expr`, `operator: Token`, `right: Expr` |
| `Grouping` | `expression: Expr` |

The dataclasses are frozen to avoid accidentally changing the structure after
construction. This is shallow immutability, not a runtime grammar validator.

`AstPrinter.print(expression)` returns a string using these rules:

```text
Literal(value)                -> formatted value
Unary(operator, right)        -> (operator right)
Binary(left, operator, right) -> (operator left right)
Grouping(expression)          -> (group expression)
```

Children are printed recursively. Operator spelling comes from the reused
token's `lexeme`. Every nonliteral node contributes one pair of parentheses.
Explicit grouping is retained even if it seems redundant.

Numbers omit a trailing `.0`, strings keep their quotes and escape backslash,
double quote, newline, carriage return, and tab, booleans print as `true` and
`false`, and `None` prints as `null`. Booleans are checked before numeric types
because Python's `bool` is a subclass of `int`.

For example:

```python
Binary(
    Unary(Token(TokenType.MINUS, "-", None, 1), Literal(123)),
    Token(TokenType.STAR, "*", None, 1),
    Grouping(Literal(45.67)),
)
```

prints:

```text
(* (- 123) (group 45.67))
```

## Setup and running

Requires Python 3.10+ and the standard library only. No installation step is
needed. Run these commands from the repository root:

```sh
# Print all 32 hard-coded example trees.
python3 test/lab2/examples.py

# Check expected outputs, node fields, and unsupported inputs.
python3 test/lab2/run_tests.py

# Regenerate the detailed report of actual outputs.
python3 test/lab2/run_tests.py --report

# Confirm that the Lab 1 scanner still works.
python3 test/lab1/run_tests.py
python3 test/lab1/terminal_test.py
```

The last command requires macOS or Linux because it uses pseudo-terminal APIs.
The Lab 2 commands do not depend on those APIs. The scanner remains available
through `python3 src/main.py --tokens`; the AST examples are a separate test program.

## Test results

**37/37 Lab 2 checks passed.** The suite contains 32 hard-coded printing examples,
one field-preservation check, and four unsupported-input checks. All test
constructions and expected results are included under `test/lab2/`.

The [detailed test results](lab2-results.md) are part of this report. For every
case they include its purpose, the hard-coded AST (shown as a dataclass
representation), expected output, actual output, and whether they match. The
Python source files contain the runnable constructors. The result generator
records observed output without replacing the independently specified expectations.

Coverage includes:

| Requirement | Examples |
| --- | --- |
| All four expression classes | `nested_example` |
| Number, string, boolean, null | `integer`, `decimal`, `string`, `true`, `false`, `null` |
| Both unary operators | `not`, `double_unary`, `nested_example` |
| All binary operators | `addition` through `or` |
| Nested hierarchy | `left_nested`, `right_nested`, `nested_grouping`, `mixed_precedence` |
| Literal formatting edges | `whole_float`, `zero`, `empty_string`, `string_escapes`, `unicode`, `string_parentheses` |
| Stored AST fields | `stored_fields` |
| Unsupported objects and literals | `unknown_node`, `unsupported_literal`, `infinity`, `nan` |

Left and right nesting print differently: `(- (- 8 3) 1)` versus
`(- 8 (group (- 3 1)))`. The mixed-precedence case prints
`(and (< (+ 1 (* 2 3)) 10) (! false))`. These results expose the child structure
instead of flattening it into an ambiguous expression.

## Limitations and extra credit

No known failing Lab 2 tests. Parsing and execution are not implemented. The
printer does not enforce operand types, operator-token consistency, or operator
membership in the grammar; callers must construct valid trees. For example,
division by zero is printable because the expression is not evaluated.

Unknown node types and unsupported literal types raise `TypeError`; nonfinite
float literals raise `ValueError`. Dataclass type annotations alone do not
validate a manually assembled tree. Deeply nested trees are limited by Python's
recursion depth. Numeric output is a diagnostic representation, not a guaranteed
round-trippable Ember source literal; very small or large floats may use exponent
notation. No AST generator or extra-credit feature is submitted for Lab 2.

## Reference

Robert Nystrom, *Crafting Interpreters*,
[Chapter 5: Representing Code](https://craftinginterpreters.com/representing-code.html).
The four basic expression shapes and parenthesized prefix output follow the
chapter's approach, adapted to Ember and Python as described above.
