# Ember — Lab 1

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

```text
src/                  Token definitions, scanner, and entry point
test/lab1/            Test scripts, expectations, and source inputs
report/               Lab report and actual test results
```
