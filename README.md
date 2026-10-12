# Ember — Labs 1 and 2

A Python scanner for a small language inspired by Chapter 4 of *Crafting
Interpreters*. It prints tokens; it does not execute programs.

Requires Python 3.10+ and no external packages. From this directory:

```sh
# Scan a file
python3 src/main.py test/lab1/inputs/example.ember

# Interactive prompt
python3 src/main.py

# Reproduce the tests and detailed report
python3 test/lab1/run_tests.py --report

# Additional real terminal tests (macOS/Linux)
python3 test/lab1/terminal_test.py --report
```

The [lab report](report/lab1.md) explains the grammar, design decisions,
setup, test results, limitations, and extra-credit features.

Lab 2 adds hard-coded expression trees and a parenthesized AST printer:

```sh
python3 test/lab2/examples.py
python3 test/lab2/run_tests.py --report
```

See the [Lab 2 draft report](report/lab2.md) for its expression grammar and results.
Lab 2 is a draft with AI attribution still pending.

```text
src/                  Tokens, scanner, entry point, AST nodes, and printer
test/lab1/            Test scripts, expectations, and source inputs
test/lab2/            Hard-coded AST examples and printer tests
report/               Lab report and actual test results
```
