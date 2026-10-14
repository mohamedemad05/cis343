# --- start AI code ---
"""Hard-coded Ember expression trees and their expected printed forms."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from expr import Binary, Grouping, Literal, Unary
from tokens import Token, TokenType as T


def operator(kind, lexeme):
    return Token(kind, lexeme, None, 1)


CASES = [
    ("nested_example", "Unary, binary, and grouping nodes in one tree.",
     Binary(Unary(operator(T.MINUS, "-"), Literal(123)),
            operator(T.STAR, "*"), Grouping(Literal(45.67))),
     "(* (- 123) (group 45.67))"),
    ("integer", "Print an integer literal.", Literal(42), "42"),
    ("decimal", "Preserve a fractional number.", Literal(3.14), "3.14"),
    ("whole_float", "Whole floats use the same display as integers.", Literal(42.0), "42"),
    ("zero", "Print zero without an unnecessary decimal point.", Literal(0.0), "0"),
    ("string", "Keep quotes around string values.", Literal("Ember"), '"Ember"'),
    ("empty_string", "An empty string is distinct from null.", Literal(""), '""'),
    ("string_escapes", "Escape quotes, backslashes, LF, CR, and tab.",
     Literal('a"b\\c\n\r\t'), r'"a\"b\\c\n\r\t"'),
    ("unicode", "Preserve Unicode text inside strings.", Literal("مرحبا"), '"مرحبا"'),
    ("true", "Use Ember spelling for true.", Literal(True), "true"),
    ("false", "Use Ember spelling for false.", Literal(False), "false"),
    ("null", "Use Ember null instead of Python None or Lox nil.", Literal(None), "null"),
    ("not", "Print unary logical negation.", Unary(operator(T.BANG, "!"), Literal(True)), "(! true)"),
    ("double_unary", "Preserve nested unary operators.",
     Unary(operator(T.MINUS, "-"), Unary(operator(T.MINUS, "-"), Literal(2))), "(- (- 2))"),
    ("addition", "Print addition.", Binary(Literal(2), operator(T.PLUS, "+"), Literal(3)), "(+ 2 3)"),
    ("subtraction", "Print binary subtraction.", Binary(Literal(2), operator(T.MINUS, "-"), Literal(3)), "(- 2 3)"),
    ("multiplication", "Print multiplication.", Binary(Literal(2), operator(T.STAR, "*"), Literal(3)), "(* 2 3)"),
    ("division", "Print division without evaluating it.", Binary(Literal(2), operator(T.SLASH, "/"), Literal(0)), "(/ 2 0)"),
    ("remainder", "Print Ember's remainder operator.", Binary(Literal(7), operator(T.PERCENT, "%"), Literal(3)), "(% 7 3)"),
    ("equal", "Print equality.", Binary(Literal(None), operator(T.EQUAL_EQUAL, "=="), Literal(None)), "(== null null)"),
    ("not_equal", "Print inequality.", Binary(Literal(2), operator(T.BANG_EQUAL, "!="), Literal(3)), "(!= 2 3)"),
    ("less", "Print less-than.", Binary(Literal(2), operator(T.LESS, "<"), Literal(3)), "(< 2 3)"),
    ("less_equal", "Print less-than-or-equal.", Binary(Literal(2), operator(T.LESS_EQUAL, "<="), Literal(3)), "(<= 2 3)"),
    ("greater", "Print greater-than.", Binary(Literal(2), operator(T.GREATER, ">"), Literal(3)), "(> 2 3)"),
    ("greater_equal", "Print greater-than-or-equal.", Binary(Literal(2), operator(T.GREATER_EQUAL, ">="), Literal(3)), "(>= 2 3)"),
    ("and", "Represent logical and without evaluating it.", Binary(Literal(True), operator(T.AND, "and"), Literal(False)), "(and true false)"),
    ("or", "Represent logical or without evaluating it.", Binary(Literal(False), operator(T.OR, "or"), Literal(True)), "(or false true)"),
    ("left_nested", "Preserve left nesting for subtraction.",
     Binary(Binary(Literal(8), operator(T.MINUS, "-"), Literal(3)),
            operator(T.MINUS, "-"), Literal(1)), "(- (- 8 3) 1)"),
    ("right_nested", "A different tree must produce different parentheses.",
     Binary(Literal(8), operator(T.MINUS, "-"),
            Grouping(Binary(Literal(3), operator(T.MINUS, "-"), Literal(1)))),
     "(- 8 (group (- 3 1)))"),
    ("nested_grouping", "Retain even redundant grouping nodes.",
     Grouping(Grouping(Literal(1))), "(group (group 1))"),
    ("mixed_precedence", "Show arithmetic nested inside comparison and logic.",
     Binary(Binary(Binary(Literal(1), operator(T.PLUS, "+"),
                          Binary(Literal(2), operator(T.STAR, "*"), Literal(3))),
                   operator(T.LESS, "<"), Literal(10)),
            operator(T.AND, "and"), Unary(operator(T.BANG, "!"), Literal(False))),
     "(and (< (+ 1 (* 2 3)) 10) (! false))"),
    ("string_parentheses", "Quoted string punctuation cannot be mistaken for tree structure.",
     Literal("(group x)"), '"(group x)"'),
]


if __name__ == "__main__":
    from ast_printer import AstPrinter

    printer = AstPrinter()
    for name, _, expression, _ in CASES:
        print(f"{name}: {printer.print(expression)}")
# --- end AI code ---
