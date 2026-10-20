# Ember — Labs 1, 2, and 3

Ember is a small language project based on *Crafting Interpreters*. It now scans
and parses expressions and prints their ASTs. It does not evaluate them.

Requires Python 3.10+ and no third-party packages. Run from the repository root:

```sh
# Lab 3: parse an expression file
python3 src/main.py test/lab3/example.ember

# Lab 3: interactive expression prompt
python3 src/main.py

# Lab 1: scanner-only mode
python3 src/main.py --tokens test/lab1/inputs/example.ember

# Lab 2: print hard-coded ASTs
python3 test/lab2/examples.py
```

The Lab 3 example prints `(+ 1 (* 2 3))`. Each source file or prompt submission
must contain exactly one expression; trailing tokens, including semicolons, are
errors. Syntax and lexical errors produce diagnostics without an AST.

Run the portable test suites and regenerate their result reports:

```sh
python3 test/lab1/run_tests.py --report
python3 test/lab2/run_tests.py --report
python3 test/lab3/run_tests.py --report
```

Additional terminal checks on macOS/Linux:

```sh
python3 test/lab1/terminal_test.py --report
python3 test/lab3/terminal_test.py --report
```

Reports include grammar, setup, limitations, expected/actual results, and any
extra-credit request:

- [Lab 1: scanner](report/lab1.md)
- [Lab 2: AST printer](report/lab2.md)
- [Lab 3: parser and concrete syntax tree](report/lab3.md)

```text
src/                  Scanner, tokens, AST classes, printer, parser, entry point
test/lab1/           Scanner inputs and tests (--tokens mode)
test/lab2/           Hard-coded AST examples and tests
test/lab3/           Parser source cases, example file, and tests
report/               Reports, recorded outputs, and the Lab 3 tree image
```

AI-generated Python test code is marked using Python comments. The Ember source
fixtures use `//` comments. See each report for details. Prior submission
commits stay available in GitHub history.
