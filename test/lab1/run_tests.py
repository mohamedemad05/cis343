# --- start AI code ---
"""Run scanner and CLI checks; optionally save the exact results in Markdown."""

import argparse
from pathlib import Path
import subprocess
import sys
import tempfile

from cases import CASES

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))


def output(tokens):
    return "".join(f"{kind} {lexeme!r} {literal!r} [line {line}]\n"
                   for kind, lexeme, literal, line in tokens)


def cli(arguments, source=""):
    result = subprocess.run(
        [sys.executable, str(ROOT / "src/main.py"), *arguments],
        input=source, text=True, encoding="utf-8", capture_output=True,
        cwd=ROOT, timeout=10,
    )
    return result.stdout, result.stderr, result.returncode


def readable(value):
    if isinstance(value, tuple) and len(value) == 3:
        stdout, stderr, status = value
        stdout = stdout or "(empty)\n"
        stderr = stderr or "(empty)\n"
        return f"stdout:\n{stdout}stderr:\n{stderr}exit status: {status}"
    if isinstance(value, tuple) and len(value) == 2:
        tokens, errors = value
        return "tokens:\n" + "\n".join(repr(t) for t in tokens) + "\nerrors:\n" + ("\n".join(errors) or "(none)")
    return repr(value)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", action="store_true")
    args = parser.parse_args()
    if not (ROOT / "src/scanner.py").exists():
        print("FAIL: src/scanner.py has not been implemented.")
        return 1

    from scanner import Scanner
    from tokens import TokenType

    results = []

    def check(name, purpose, source, expected, actual):
        passed = expected == actual
        results.append((name, purpose, source, expected, actual, passed))
        print(f"{'PASS' if passed else 'FAIL'} {name}")
        if not passed:
            print(f"  expected: {expected!r}\n  actual:   {actual!r}")

    for name, purpose, source, expected_tokens, errors in CASES:
        fixture = ROOT / "test/lab1/inputs" / (name + ".ember")
        # Reading bytes preserves CR and CRLF, which are themselves test inputs.
        saved_source = fixture.read_bytes().decode("utf-8")
        prefix = "// --- start AI code ---\n"
        suffix = "\n// --- end AI code ---\n"
        if not saved_source.startswith(prefix) or not saved_source.endswith(suffix):
            raise AssertionError(f"Missing AI attribution markers: {name}")
        saved_source = saved_source[len(prefix):-len(suffix)]
        if saved_source != source:
            raise AssertionError(f"Fixture differs from hand-written case: {name}")
        scanner = Scanner(saved_source)
        actual = [(t.type.name, t.lexeme, t.literal, t.line)
                  for t in scanner.scan_tokens()]
        check(name + " / scanner", purpose, repr(source),
              (expected_tokens, errors), (actual, scanner.errors))
        expected_cli = (output(expected_tokens),
                        "".join(error + "\n" for error in errors),
                        65 if errors else 0)
        # Attribution is metadata, not part of the tested source. In particular,
        # appending a comment would change unterminated-string and EOF cases.
        with tempfile.TemporaryDirectory() as directory:
            source_file = Path(directory) / fixture.name
            source_file.write_bytes(saved_source.encode("utf-8"))
            check(name + " / file", purpose, repr(source), expected_cli,
                  cli([str(source_file)]))

    expected_types = {t[0] for case in CASES for t in case[3]}
    check("token coverage", "Every declared token type has a positive test.",
          "Union of all expected token types", sorted(t.name for t in TokenType),
          sorted(expected_types))

    prompt = "ember> "
    eof_output = output([("EOF", "", None, 1)])
    say_output = output([("SAY", "say", None, 1), ("EOF", "", None, 1)])
    check("interactive recovery", "The next input works after each kind of lexical error.",
          repr('@\n"bad\n"\\q"\n/*\n' + '9' * 400 + '\nsay\n'),
          ((prompt + eof_output) * 5 + prompt + say_output + prompt + "\n",
           "[line 1] Error: Unexpected character '@'.\n"
           "[line 1] Error: Unterminated string.\n"
           "[line 1] Error: Invalid escape '\\q'.\n"
           "[line 1] Error: Unterminated block comment.\n"
           "[line 1] Error: Number is too large.\n", 0),
          cli([], '@\n"bad\n"\\q"\n/*\n' + '9' * 400 + '\nsay\n'))
    check("interactive blank", "Blank submissions produce EOF and another prompt.",
          repr("\n"), (prompt + eof_output + prompt + "\n", "", 0), cli([], "\n"))
    check("interactive EOF", "EOF immediately exits cleanly.",
          repr(""), (prompt + "\n", "", 0), cli([]))
    check("usage", "More than one file is a usage error.", "arguments: a b",
          ("", "Usage: python3 src/main.py [source.ember]\n", 64), cli(["a", "b"]))
    with tempfile.TemporaryDirectory() as directory:
        missing = Path(directory) / "missing.ember"
        read_error = ("", "Error: Cannot read source file (UTF-8 required).\n", 66)
        check("missing file", "Missing files fail without a traceback.", "nonexistent file",
              read_error, cli([str(missing)]))
        invalid = Path(directory) / "invalid.ember"
        invalid.write_bytes(b"\xff")
        check("invalid UTF-8", "Decode errors fail without a traceback.", "bytes: ff",
              read_error, cli([str(invalid)]))
        check("directory input", "A directory cannot be read as source.", "directory path",
              read_error, cli([directory]))
        spaced = Path(directory) / "source with spaces.ember"
        spaced.write_text("say", encoding="utf-8")
        check("path with spaces", "Quoted source paths work.", repr("say"),
              (say_output, "", 0), cli([str(spaced)]))

    failures = sum(not row[-1] for row in results)
    summary = f"{len(results) - failures}/{len(results)} checks passed."
    print(summary)
    if args.report:
        lines = ["# Lab 1 test results", "", summary, "",
                 "Generated by `python3 test/lab1/run_tests.py --report`.", "",
                 "Each scanner token is `(type, lexeme, literal, line)`.",
                 "CLI entries show stdout, stderr, and exit status. Python repr makes newlines,",
                 "backslashes, and CRLF visible; it does not modify source files.", ""]
        for name, purpose, source, expected, actual, passed in results:
            lines.extend([f"## {name}", "", purpose, "", "Source / input:",
                          "```text", source, "```", "", "Expected:", "```text",
                          readable(expected), "```", "", "Actual:", "```text",
                          readable(actual), "```", "", f"Result: {'PASS' if passed else 'FAIL'}", ""])
        (ROOT / "report/test-results.md").write_text("\n".join(lines), encoding="utf-8")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
# --- end AI code ---
