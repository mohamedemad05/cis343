# --- start AI code ---
"""Run Lab 5 fixtures through the real CLI and record reproducible evidence."""
import argparse
import contextlib
import io
from pathlib import Path
import subprocess
import sys

from cases import CASES

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'src'))
from main import Ember
from ast_printer import AstPrinter
from parser import Parser
from scanner import Scanner


def cli(path=None, source=''):
    command = [sys.executable, str(ROOT / 'src/main.py')]
    if path is not None:
        command.append(str(path))
    result = subprocess.run(command, input=source, text=True, capture_output=True,
                            cwd=ROOT, timeout=10)
    return result.stdout, result.stderr, result.returncode


def streams(result):
    out, err, code = result
    return f'stdout:\n{out or "(empty)"}\nstderr:\n{err or "(empty)"}\nexit status: {code}'


def main():
    args = argparse.ArgumentParser(description=__doc__)
    args.add_argument('--report', action='store_true')
    options = args.parse_args()
    results = []

    def check(name, source, expected, actual):
        passed = expected == actual
        results.append((name, source, expected, actual, passed))
        print(f'{"PASS" if passed else "FAIL"} {name}')
        if not passed:
            print(f'Expected: {expected!r}\nActual: {actual!r}')

    for name, source, out, err, code in CASES:
        path = ROOT / 'test/lab5' / (name + '.ember')
        fixture = path.read_text(encoding='utf-8')
        expected_fixture = '// --- start AI code ---\n' + source
        if fixture != expected_fixture:
            raise AssertionError(f'{path} no longer matches its specified test input')
        check(name, fixture, (out, err, code), cli(path))

    textbook = ROOT / 'test/lab5/textbook.ember'
    check('textbook', textbook.read_text(),
          ('inner a\nouter b\nglobal c\nouter a\nouter b\nglobal c\nglobal a\nglobal b\nglobal c\n', '', 0),
          cli(textbook))

    session = 'var a = 1;\n{ var local = 2; print missing; }\nprint a;\nprint local;\nvar bad = bad;\nvar bad = 7; print bad;\n'
    expected_out = 'ember> ember> ember> 1\nember> ember> ember> 7\nember> \n'
    expected_err = ("Runtime error: [line 1] Undefined variable 'missing'.\n"
                    "Runtime error: [line 1] Undefined variable 'local'.\n"
                    "Runtime error: [line 1] Cannot access variable 'bad' in its own initializer.\n")
    check('prompt_persistence_and_error_recovery', session,
          (expected_out, expected_err, 0), cli(source=session))

    # Same interpreter: failed redeclaration must not evaluate its initializer.
    ember = Ember()
    source = 'var a = 1;\nvar a = (a = 99);\nprint a;'
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        codes = [ember.run(line) for line in source.splitlines()]
    check('redeclaration_preserves_value', source,
          ('1\n', "Runtime error: [line 1] Variable 'a' is already declared in this scope.\n", [0, 70, 0]),
          (out.getvalue(), err.getvalue(), codes))

    source = 'var a = 1; { print a = 2; }'
    parser = Parser(Scanner(source).scan_tokens())
    actual = '\n'.join(AstPrinter().print(node) for node in parser.parse()) + '\n'
    check('new_ast_nodes', source,
          ('(var a 1)\n(block (print (= a 2)))\n', '', 0),
          (actual, '\n'.join(parser.errors), 0))

    # Very deep inputs must fail gracefully and never hang or show tracebacks.
    for name, source in [
        ('deep_assignment', 'var a; a = ' + 'a = ' * 2000 + '1;'),
        ('deep_blocks', '{' * 2000 + 'print 1;' + '}' * 2000),
        ('deep_evaluation', 'print ' + '1 + ' * 2000 + '1;'),
    ]:
        out, err, _ = cli(source=source + '\nprint 42;\n')
        check(name, source[:90] + ' ... (2000 levels/operators)\nprint 42;',
              ('controlled error and prompt recovery', '', 0),
              ('controlled error and prompt recovery' if 'deep' in err and 'Traceback' not in err and '42\n' in out else out, '' if 'Traceback' not in err else err, 0))

    failures = sum(not result[-1] for result in results)
    summary = f'{len(results)-failures}/{len(results)} checks passed.'
    print(summary)
    if options.report:
        lines = ['# Lab 5 test results', '', summary, '',
                 'Run `python3 test/lab5/run_tests.py --report` from the repository root.', '',
                 'Expected values are specified independently in `test/lab5/cases.py` and this runner.',
                 'Each ordinary fixture runs in a separate process with a 10-second timeout.',
                 'Depth checks assert controlled diagnostics and recovery instead of implementation-specific stack limits.', '']
        for name, source, expected, actual, passed in results:
            lines.extend([f'## {name}', '', 'Input:', '```text', source.rstrip(), '```', '',
                          'Expected:', '```text', streams(expected), '```', '',
                          'Actual:', '```text', streams(actual), '```', '',
                          f'Result: {"PASS" if passed else "FAIL"}', ''])
        (ROOT / 'report/lab5-results.md').write_text('\n'.join(lines), encoding='utf-8')
    return int(bool(failures))


if __name__ == '__main__':
    raise SystemExit(main())
# --- end AI code ---
