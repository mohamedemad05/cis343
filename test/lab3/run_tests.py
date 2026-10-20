# --- start AI code ---
"""Verify parsing and real CLI behavior; optionally write the full test evidence."""

import argparse
from pathlib import Path
import subprocess
import sys
import tempfile

from cases import CASES

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))


def cli(arguments, source=""):
    result = subprocess.run([sys.executable, str(ROOT / "src/main.py"), *arguments],
                            input=source, text=True, encoding="utf-8",
                            capture_output=True, cwd=ROOT, timeout=10)
    return result.stdout, result.stderr, result.returncode


def streams(value):
    stdout, stderr, status = value
    return ("stdout:\n" + (stdout or "(empty)\n") + "stderr:\n" +
            (stderr or "(empty)\n") + f"exit status: {status}")


def main():
    arguments = argparse.ArgumentParser(description=__doc__)
    arguments.add_argument("--report", action="store_true")
    args = arguments.parse_args()
    if not (ROOT / "src/parser.py").exists():
        print("FAIL: Parser has not been implemented.")
        return 1

    from ast_printer import AstPrinter
    from expr import Binary, Grouping, Literal, Unary
    from parser import ParseError, Parser
    from scanner import Scanner
    from tokens import TokenType as T

    results = []

    def check(name, purpose, source, expected, actual):
        passed = expected == actual
        results.append((name, purpose, source, expected, actual, passed))
        print(f"{'PASS' if passed else 'FAIL'} {name}")
        if not passed:
            print(f"Expected: {expected!r}\nActual: {actual!r}")

    for name, purpose, source, stdout, stderr in CASES:
        expected = (stdout, stderr, 65 if stderr else 0)
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()
        if scanner.errors:
            actual = ("", "\n".join(scanner.errors) + "\n", 65)
        else:
            try:
                actual = (AstPrinter().print(Parser(tokens).parse()) + "\n", "", 0)
            except ParseError as error:
                actual = ("", str(error) + "\n", 65)
        check(name + " / API", purpose, repr(source), expected, actual)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "case.ember"
            path.write_bytes(source.encode("utf-8"))
            check(name + " / file", purpose, repr(source), expected, cli([str(path)]))

    # Each invalid submission is followed immediately by a valid one.
    single_line = [case for case in CASES if "\n" not in case[2] and "\r" not in case[2]]
    prompt = "ember> "
    input_lines, stdout, stderr = [], "", ""
    for _, _, source, expected_out, expected_err in single_line:
        input_lines.append(source)
        stdout += prompt + expected_out
        stderr += expected_err
        if expected_err:
            input_lines.append("2+3")
            stdout += prompt + "(+ 2 3)\n"
    interactive_source = "\n".join(input_lines) + "\n"
    check("interactive_all_cases", "All single-line cases run in one prompt session; recover after each error.",
          repr(interactive_source), (stdout + prompt + "\n", stderr, 0), cli([], interactive_source))
    check("interactive_EOF", "An immediate EOF exits the prompt cleanly.", repr(""),
          (prompt + "\n", "", 0), cli([]))

    source = "-(1 + 2) * 3"
    tree = Parser(Scanner(source).scan_tokens()).parse()
    actual_fields = (isinstance(tree, Binary), tree.operator.type is T.STAR,
                     isinstance(tree.left, Unary), tree.left.operator.type is T.MINUS,
                     isinstance(tree.left.right, Grouping),
                     tree.left.right.expression.operator.type is T.PLUS,
                     isinstance(tree.right, Literal), tree.right.value == 3.0)
    check("AST_fields", "The parser constructs the reused node classes and stores operator tokens and children.",
          repr(source), (repr((True,) * 8) + "\n", "", 0), (repr(actual_fields) + "\n", "", 0))

    # Stress only the CLI: it must catch both parsing and printing recursion failures.
    for name, source, expected_error in [
        ("deep_grouping", "(" * 2000 + "1" + ")" * 2000,
         "[line 1] Error: Expression is too deeply nested.\n"),
        ("deep_unary", "!" * 2000 + "true",
         "[line 1] Error: Expression is too deeply nested.\n"),
        ("deep_binary", "1+" * 2000 + "1",
         "[line 1] Error: Expression tree is too deep to print.\n"),
    ]:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "deep.ember"
            path.write_text(source, encoding="utf-8")
            check(name, "Excessive tree depth produces a diagnostic, never a Python traceback or partial AST.",
                  repr(source), ("", expected_error, 65), cli([str(path)]))
        check(name + " / recovery", "A valid prompt submission still works after excessive depth.",
              repr(source + "\n2+3\n"),
              (prompt + prompt + "(+ 2 3)\n" + prompt + "\n", expected_error, 0),
              cli([], source + "\n2+3\n"))

    usage = ("", "Usage: python3 src/main.py [--tokens] [source.ember]\n", 64)
    check("usage", "Only one source-file argument is accepted.", "arguments: a b", usage, cli(["a", "b"]))
    check("unknown_option", "An unknown option is rejected.", "arguments: --bad", usage, cli(["--bad"]))
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "missing.ember"
        read_error = ("", "Error: Cannot read source file (UTF-8 required).\n", 66)
        check("missing_file", "A missing file is reported without a traceback.", "nonexistent path", read_error, cli([str(path)]))
        path.write_bytes(b"\xff")
        check("invalid_UTF8", "Invalid source encoding is reported without a traceback.", "bytes: ff", read_error, cli([str(path)]))
        check("directory", "A directory cannot be read as source.", "directory path", read_error, cli([directory]))
        spaced = Path(directory) / "expression with spaces.ember"
        spaced.write_text("1+2", encoding="utf-8")
        check("path_spaces", "A source path may contain spaces.", repr("1+2"), ("(+ 1 2)\n", "", 0), cli([str(spaced)]))

    example = ROOT / "test/lab3/example.ember"
    check("example_file", "Run the committed, attributed example directly.",
          repr(example.read_text(encoding="utf-8")), ("(+ 1 (* 2 3))\n", "", 0),
          cli([str(example)]))

    failures = sum(not row[-1] for row in results)
    summary = f"{len(results) - failures}/{len(results)} checks passed."
    print(summary)
    if args.report:
        lines = ["# Lab 3 test results", "", summary, "",
                 "Run `python3 test/lab3/run_tests.py --report` to regenerate.", "",
                 "Source is shown with Python repr so physical line breaks, tabs, and escapes are unambiguous.",
                 "Expected values are specified separately from the implementation.",
                 "API entries scan/parse/print directly; file and prompt entries run the real main program.",
                 "Each case records stdout, stderr, and exit status; API cases use equivalent status values.", ""]
        for name, purpose, source, expected, actual, passed in results:
            lines.extend([f"## {name}", "", purpose, "", "Source / input:", "```text", source, "```", "",
                          "Expected:", "```text", streams(expected), "```", "",
                          "Actual:", "```text", streams(actual), "```", "",
                          f"Result: {'PASS' if passed else 'FAIL'}", ""])
        (ROOT / "report/lab3-results.md").write_text("\n".join(lines), encoding="utf-8")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
# --- end AI code ---
