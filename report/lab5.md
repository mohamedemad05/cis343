# Lab 5: Variables and block scope

## Setup and reproduction

Ember uses Python 3.10 or newer and requires no third-party packages. From the repository root:

```sh
python3 src/main.py test/lab5/variables.ember
python3 src/main.py test/lab5/textbook.ember
python3 test/lab5/run_tests.py --report
python3 test/lab4/test_lab4.py
python3 test/lab2/run_tests.py
```

The Lab 5 suite reports **45/45 checks passed**. The reused Lab 4 suite passes all 4 tests, the Lab 2 AST suite passes all 37 checks, and the scanner suite passes all 85 checks. Its keyword-alias expectations and CLI usage expectation were updated for the current language. Exact inputs, expected results, actual stdout/stderr, and exit statuses are recorded in [lab5-results.md](lab5-results.md). All Lab 5 source fixtures and the portable test runner are under `test/lab5/`.

Start the interactive prompt with `python3 src/main.py`. Variables persist between prompt submissions. Each submission must contain complete statements; enter an entire block on one line or put a multiline program in a file. EOF or Ctrl-C at the prompt exits. Run legacy expression printing with `python3 src/main.py --ast test/lab3/example.ember`; scanner-only mode remains `--tokens`.

The repository on which this lab builds contained Labs 1–3. This commit integrates the saved Lab 4 statement evaluator and recovery support before adding Lab 5. Historical Lab 3 tests describe the former expression-only API; use `Parser.parse_expression()` or `--ast` for that mode now. `Parser.parse()` returns a list of statements.

## Design choices

| Question | Decision and observable behavior |
| --- | --- |
| Access before declaration | No hoisting or implicit declaration. Lookup searches the current environment, then enclosing environments. If no binding exists, reading or assigning raises `Undefined variable`. Execution stops at that runtime error. |
| Missing initializer | `var a;` creates a declared variable holding `nil`. Reading it prints `nil`; later assignment can replace it. |
| Redeclaration | Declaring a name twice in the same environment is a runtime error. The existing value remains unchanged, and the rejected initializer is not evaluated. |
| Scope | Each `{ ... }` creates a new environment linked to the surrounding one. Inner declarations may shadow outer names. Lookup and assignment use the nearest existing binding. Leaving the block discards its local bindings. |
| Initializer self-reference | A declaration reserves its local name before evaluating the initializer. Reading or assigning that binding from its own initializer is an error, even if an outer variable has the same name. Failed declarations are removed so the prompt can recover. |
| Types | Variables are dynamically typed and mutable. A variable can hold a number, string, Boolean, or `nil`, and assignments may change its type. Arithmetic still checks operand types. |
| Assignment | `=` has lower precedence than logical operators and associates right to left. Assignment returns its assigned value, so `a = b = 3;` and `print a = 3;` are valid. Only a bare variable identifier is a valid target; `(a) = 3;` is rejected. |

The original spellings `let`, `say`, and `null` remain available. `var`, `print`, and `nil` are aliases, allowing the assignment's textbook program to run exactly as written. Keywords cannot be variable names. There are no functions, closures, or control-flow statements in this lab.

Declaration order matters: before an inner declaration executes, an outer binding remains visible. Thus `var a = "outer"; { print a; var a = "inner"; print a; }` prints `outer`, then `inner`. Once the inner declaration begins, its initializer cannot read that new binding.

## Implementation and grammar

The scanner and token definitions are reused in `src/`, with the keyword aliases added to the scanner. `Variable` and `Assign` extend the expression AST. `VarStmt` and `BlockStmt` extend the statement AST. The AST printer handles all new nodes as well as the earlier expression nodes.

`src/environment.py` stores each scope's bindings in a dictionary and links it to its enclosing scope. Lookup walks these links; assignment updates the environment that owns the nearest matching binding. `src/interpreter.py` saves the current environment before executing a block and restores it in a `finally` clause, including after a runtime error. A separate uninitialized sentinel distinguishes an initializer in progress from the ordinary `nil` value.

`src/parser.py` uses these additions to the previous recursive-descent grammar:

```text
program        -> declaration* EOF ;
declaration    -> varDecl | statement ;
varDecl        -> ("var" | "let") IDENTIFIER ("=" expression)? ";" ;
statement      -> printStmt | expressionStmt | block ;
block          -> "{" declaration* "}" ;
printStmt      -> ("print" | "say") expression ";" ;
expressionStmt -> expression ";" ;
expression     -> assignment ;
assignment     -> logic_or ("=" assignment)? ;
primary        -> NUMBER | STRING | "true" | "false" | "nil" | "null"
                | IDENTIFIER | "(" expression ")" ;
```

The assignment rule additionally requires its left expression to be a `Variable` node. The existing precedence levels between `logic_or` and `primary` are retained: `or`, `and`, equality, comparison, addition/subtraction, multiplication/division/remainder, and unary operators. Logical operators short-circuit, including when their skipped operands contain assignments.

## Declaration, access, and assignment demonstration

Input (`test/lab5/variables.ember`, excluding its attribution comment):

```text
var score = 10;
print score;
score = score + 5;
print score;
```

Actual stdout:

```text
10
15
```

A declaration creates the binding, the first print reads it, and assignment replaces its value. Expression statements do not print a value automatically. This program exits with status 0 and no stderr.

A missing initializer (`test/lab5/missing_initializer.ember`) is handled as follows:

```text
var value;
print value;
value = 42;
print value;
```

Actual stdout:

```text
nil
42
```

The chained-assignment fixture declares `a` and `b`, executes `print a = b = 3;`, and prints both variables. Its output is `3` on three lines. The outer-assignment fixture changes an outer `a` from a nested block and prints `9` both inside and outside the block. The shadow-assignment fixture updates an inner `a` to `3` and then prints the unchanged outer value `1` after the block.

## Required textbook scope program

The complete required program is committed as `test/lab5/textbook.ember`:

```text
var a = "global a";
var b = "global b";
var c = "global c";
{
  var a = "outer a";
  var b = "outer b";
  {
    var a = "inner a";
    print a;
    print b;
    print c;
  }
  print a;
  print b;
  print c;
}
print a;
print b;
print c;
```

Actual stdout (status 0, no stderr):

```text
inner a
outer b
global c
outer a
outer b
global c
global a
global b
global c
```

In the innermost block, `a` is local, `b` is found one environment outward, and `c` is found in the global environment. After the inner block ends, its `a` is discarded, exposing `outer a`. After the outer block ends, its `a` and `b` are discarded, exposing all three global values. Shadowing creates separate bindings and does not overwrite outer variables.

## Error demonstrations

Each fixture starts with an attribution comment, so its code begins on line 2. The table shows actual stderr without its trailing newline. Unless stated otherwise, these examples produce no stdout. Syntax errors return 65; runtime errors return 70. Each row's complete recorded execution appears in [lab5-results.md](lab5-results.md).

| Fixture and example input | Actual diagnostic |
| --- | --- |
| `read_before_declaration.ember`: `print a; var a = 1;` | `Runtime error: [line 2] Undefined variable 'a'.` |
| `assign_before_declaration.ember`: `a = 1;` | `Runtime error: [line 2] Undefined variable 'a'.` |
| `scope_escape.ember`: `{ var local = 1; } print local;` | `Runtime error: [line 2] Undefined variable 'local'.` |
| `redeclaration.ember`: `var a = 1; var a = 2;` | `Runtime error: [line 2] Variable 'a' is already declared in this scope.` |
| `block_redeclaration.ember`: `{ var a; var a; }` | `Runtime error: [line 2] Variable 'a' is already declared in this scope.` |
| `self_initializer.ember`: `var a = a;` | `Runtime error: [line 2] Cannot access variable 'a' in its own initializer.` |
| `shadow_self_initializer.ember`: `var a = 1; { var a = a; }` | `Runtime error: [line 2] Cannot access variable 'a' in its own initializer.` |
| `self_assignment_initializer.ember`: `var a = (a = 1);` | `Runtime error: [line 2] Cannot access variable 'a' in its own initializer.` |
| `undefined_initializer.ember`: `var a = missing;` | `Runtime error: [line 2] Undefined variable 'missing'.` |
| `invalid_literal_target.ember`: `1 = 2; print "recovered";` | `[line 2] Error at '=': Invalid assignment target; expected a variable identifier.` |
| `invalid_binary_target.ember`: `var a = 1; a + 1 = 2; print a;` | `[line 2] Error at '=': Invalid assignment target; expected a variable identifier.` |
| `invalid_group_target.ember`: `var a = 1; (a) = 2; print a;` | `[line 2] Error at '=': Invalid assignment target; expected a variable identifier.` |
| `unclosed_block.ember`: `{ var a = 1;` | `[line 2] Error at end: Expected '}' after block (opened on line 2).` |
| `extra_brace.ember`: `} print 1;` | `[line 2] Error at '}': Unmatched '}'.` |
| `missing_name.ember`: `var = 1; print 2;` | `[line 2] Error at '=': Expected variable name.` |
| `missing_declaration_semicolon.ember`: `var a = 1 print 2;` | `[line 2] Error at 'print': Expected ';' after variable declaration.` |
| `missing_initializer_expression.ember`: `var a = ; print 2;` | `[line 2] Error at ';': Expected an expression.` |
| `missing_assignment_value.ember`: `var a = 1; a = ; print a;` | `[line 2] Error at ';': Expected an expression.` |
| `block_missing_semicolon.ember`: `{ print 1 } print 2;` | `[line 2] Error at '}': Expected ';' after print value.` |
| `variable_type_error.ember`: `var a; print a + 1;` | `Runtime error: [line 2] Operator '+' needs numbers.` |
| `variable_division_zero.ember`: `var a = 0; print 1 / a;` | `Runtime error: [line 2] Division by zero.` |
| `lexical_error.ember`: `var a = @;` | `[line 2] Error: Unexpected character '@'.` |

For `reserved_name.ember`, `var print = 1;` reports both of these syntax diagnostics during recovery:

```text
[line 2] Error at 'print': Expected variable name.
[line 2] Error at '=': Expected an expression.
```

The invalid literal target fixture still prints `recovered`; the invalid binary and grouped target fixtures print the original value `1`. The extra-brace fixture prints `1`. The missing-name, missing-initializer, missing-declaration-semicolon, and block-missing-semicolon fixtures print `2`. The missing-assignment-value fixture prints `1`. These results demonstrate panic-mode recovery after the rejected statement. A runtime error stops the remaining statements in that submission; the interactive prompt can accept the next submission.

Recovery leaves a block's closing brace for the block parser to consume. For example, `var a = "global"; { var a = ; } print a;` reports the malformed initializer and then prints `global`. An unterminated block is discarded rather than executed in the surrounding scope. Depth errors during parsing or execution are caught and reported without Python tracebacks; the test runner also verifies that the prompt handles a subsequent `print 42;`.

## Validation and limitations

The suite checks the required textbook output, valid variables, missing initializers, declaration order, chained assignment, precedence, shadowing, sibling scopes, outer assignment, scope exit, empty blocks, type changes, aliases, short-circuiting, syntax errors, variable-related runtime errors, and source line numbers. Additional checks verify the AST printer, prompt persistence, restoration of the global environment after a block runtime error, removal of failed declarations, rejection of a redeclaration before initializer side effects, and controlled depth failures.

The prompt accepts one complete submission per line; multiline blocks are supported in files. Runtime errors stop the current submission instead of continuing with potentially invalid state. Parser recovery can produce more than one diagnostic for one malformed declaration. Diagnostics include line numbers and token text, but no columns. Recursion depth depends on Python's limit; no fixed maximum depth is promised.

AI assistance was used for implementation, tests, and this report. New Python test files use `# --- start AI code ---` / `# --- end AI code ---`; source fixtures include an AI attribution comment. The implementation follows the environment-chain and assignment approach used in *Crafting Interpreters*, adapted to Ember's existing Python scanner and AST.

Submit the exact GitHub commit URL, in the form `https://github.com/mohamedemad05/cis343/commit/<commit-hash>`, on Blackboard. This commit must contain `src/`, `test/lab5/`, and `report/lab5.md`; the repository is public so the instructor can clone it and run the commands above.
