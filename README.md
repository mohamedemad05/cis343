# Ember — CIS 343 Labs 1–5

Ember is a small interpreter implemented in Python 3.10+ with no third-party dependencies. It supports expressions, print statements, mutable variables, assignment, and nested block scope.

Run from the repository root:

```sh
python3 src/main.pytest/lab5/variables.ember
python3 src/main.pytest/lab5/textbook.ember
python3 src/main.py
```

Statements end in semicolons. `var` declares a variable; `print` prints a value. The original aliases `let`, `say`, and `null` remain available alongside `var`, `print`, and `nil`. Declarations without initializers hold `nil`. Undeclared variables, self-referencing initializers, and redeclarations in the same scope are runtime errors. Inner blocks may shadow outer names.

The prompt retains variables between submissions. Each line must contain complete statements or a complete block; use a file for multiline programs.

```text
src/          Scanner, tokens, expression/statement ASTs, AST printer,
              parser, environment, interpreter, and entry point
test/lab5/   Lab 5 example inputs, expected results, and portable test runner
report/      Lab reports and recorded test evidence
```

Run the current test suites:

```sh
python3test/lab5/run_tests.py --report
python3 test/lab4/test_lab4.py
python3 test/lab2/run_tests.py
python3 test/lab1/run_tests.py
```

See [the Lab 5 report](report/lab5.md) for design choices, the required textbook example, error demonstrations, and reproduction instructions. [Recorded results](report/lab5-results.md) include stdout, stderr, and exit statuses.

Earlier labs and their submission commits remain in Git history. Expression-only AST printing is available with `python3 src/main.py --ast test/lab3/example.ember`; scanner-only mode is `--tokens`. Historical Lab 3 tests target its earlier expression-only parser API; the current expression entry point is `Parser.parse_expression()`, while `Parser.parse()` parses a statement program.

AI assistance was used for implementation, tests, and reports. Test files and source fixtures retain attribution comments.
