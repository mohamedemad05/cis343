"""Check the hard-coded ASTs and optionally record all results."""

import argparse
from pathlib import Path
from pprint import pformat
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", action="store_true")
    args = parser.parse_args()
    if not (ROOT / "src/ast_printer.py").exists():
        print("FAIL: AST printer has not been implemented.")
        return 1

    from ast_printer import AstPrinter
    from examples import CASES, operator
    from expr import Binary, Grouping, Literal, Unary
    from tokens import TokenType as T

    printer = AstPrinter()
    results = []

    def check(name, purpose, expression, expected, actual):
        passed = expected == actual
        results.append((name, purpose, pformat(expression, width=85), expected, actual, passed))
        print(f"{'PASS' if passed else 'FAIL'} {name}")
        if not passed:
            print(f"Expected: {expected!r}\nActual: {actual!r}")

    for name, purpose, expression, expected in CASES:
        check(name, purpose, expression, expected, printer.print(expression))

    left, right = Literal(2), Literal(3)
    op = operator(T.PLUS, "+")
    binary = Binary(left, op, right)
    unary = Unary(operator(T.MINUS, "-"), left)
    grouping = Grouping(binary)
    check("stored_fields", "Nodes retain their actual children, token, and literal value.",
          grouping, (True, True, True, True, True, 2),
          (binary.left is left, binary.right is right, binary.operator is op,
           unary.right is left, grouping.expression is binary, left.value))

    for name, expression, expected in [
        ("unknown_node", object(), "TypeError: Unsupported expression type: object"),
        ("unsupported_literal", Literal([]), "TypeError: Unsupported literal type: list"),
        ("infinity", Literal(float("inf")), "ValueError: Number literals must be finite."),
        ("nan", Literal(float("nan")), "ValueError: Number literals must be finite."),
    ]:
        try:
            actual = printer.print(expression)
        except (TypeError, ValueError) as error:
            actual = f"{type(error).__name__}: {error}"
        # Avoid a nondeterministic memory address in the report.
        source = "object()" if name == "unknown_node" else expression
        check(name, "Reject unsupported manually constructed input clearly.", source, expected, actual)

    failures = sum(not result[-1] for result in results)
    summary = f"{len(results) - failures}/{len(results)} checks passed."
    print(summary)
    if args.report:
        lines = ["# Lab 2 test results", "", summary, "",
                 "Generated with `python3 test/lab2/run_tests.py --report`.", "",
                 "ASTs below use dataclass representations, including reused Token fields.",
                 "Runnable constructions are in `test/lab2/examples.py` and `run_tests.py`.", ""]
        for name, purpose, expression, expected, actual, passed in results:
            lines.extend([f"## {name}", "", purpose, "", "Hard-coded AST / input:",
                          "```text", expression, "```", "", "Expected:", "```text",
                          str(expected), "```", "", "Actual:", "```text", str(actual),
                          "```", "", f"Result: {'PASS' if passed else 'FAIL'}", ""])
        (ROOT / "report/lab2-results.md").write_text("\n".join(lines), encoding="utf-8")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
