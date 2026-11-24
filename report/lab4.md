# Lab 4: Statements and Panic-Mode Error Recovery

**Project:** Ember (CIS 343)  
**Implementation language:** Python 3.10+  
**Assignment:** Lab 4 — Statements

## Summary

This lab extends the Ember parser from one expression to a program containing multiple statements. The parser supports expression statements (`4 + 2;`) and print statements (`print 1 + 2;`, also spelled `say`). All statements end with `;`. A small interpreter evaluates expressions and prints only the values of print statements. To match the provided lab examples, `print` is accepted as an alias for Ember's previous `say`, and `nil` is accepted as an alias for `null`.

Panic-mode recovery records syntax diagnostics, skips tokens until a statement boundary (semicolon, a following `print`/`say`, or a new line), and continues parsing the rest of the source. Parsing returns both successful statement nodes and accumulated diagnostics, so syntactically valid statements can execute even if others were rejected. Invalid source exits with status 65.

## Grammar

```ebnf
program        -> statement* EOF ;
statement      -> printStmt | expressionStmt ;
printStmt      -> ("print" | "say") expression ";" ;
expressionStmt -> expression ";" ;
expression     -> logic_or ;
logic_or       -> logic_and ("or" logic_and)* ;
logic_and      -> equality ("and" equality)* ;
equality       -> comparison (("==" | "!=") comparison)* ;
comparison     -> term (("<" | "<=" | ">" | ">=") term)* ;
term           -> factor (("+" | "-") factor)* ;
factor         -> unary (("*" | "/" | "%") unary)* ;
unary          -> ("!" | "-") unary | primary ;
primary        -> NUMBER | STRING | "true" | "false" | "nil" | "null" | "(" expression ")" ;
```

## Setup and run

Run these commands at the repository root; no third-party Python packages are needed.

```sh
python3 src/main.py test/lab4/errors.ember
python3 src/main.py test/lab4/statements.ember
python3 src/main.py test/lab4/recovery.ember
python3 -m unittest discover -s test/lab4 -p 'test_*.py' -v
```

The error cases intentionally exit with status code 65. The normal case exits with status code 0. Standard output and error diagnostics are separate streams, so terminal ordering can vary if they are combined.

## Test 1: Required syntax errors

**Input** (`test/lab4/errors.ember`):

```ember
"one"
true;
print 2 +
```

**Observed standard output:** *(empty)*

**Observed standard error:**

```text
[line 2] Error at 'true': Expected ';' after expression.
[line 4] Error at end: Expected an expression.
```

**Exit status:** `65`

The parser reports that the first expression needs a semicolon, recovers at the next line, accepts `true;` as an expression statement, and then reports the missing operand at end of file. The `true;` expression has no printed output by design.

## Test 2: Required valid statements

**Input** (`test/lab4/statements.ember`):

```ember
4 + 2;
print "one";
print true;
print 1 + 2;
print nil;
```

**Observed standard output:**

```text
one
true
3
nil
```

**Observed standard error:** *(empty)*  
**Exit status:** `0`

The first expression evaluates to 6 but does not print because it is not a print statement.

## Extra test: Recovery continues after invalid statement

**Input** (`test/lab4/recovery.ember`):

```ember
print 10;
print 1 + ;
print 20;
4 * 3;
print 30;
```

**Observed standard output:**

```text
10
20
30
```

**Observed standard error:**

```text
[line 2] Error at ';': Expected an expression.
```

**Exit status:** `65`

This test confirms the parser reports a malformed expression and continues to parse and execute later valid statements.

## Automated tests

Four local unit tests passed:

- Required successful output
- Required syntax error diagnostics
- Recovery and continuing execution after an error
- Compatibility with the original `say null;` syntax

## Source files

- `src/main.py`: file input, prompt, diagnostics and execution
- `src/scanner.py`: existing scanner plus keyword aliases
- `src/parser.py`: statement parser and panic-mode recovery
- `src/stmt.py`: new expression and print statement nodes
- `src/interpreter.py`: evaluate expressions and execute statements
- `src/expr.py`: existing expression AST
- `src/ast_printer.py`: existing AST printer, kept for earlier labs
- `src/tokens.py`: existing token definitions

## Limitations and AI assistance

The goal of Lab 4 is statement parsing and syntax recovery; variable declarations, functions, and control-flow statements are not implemented. The parser synchronizes at semicolons, a print-statement keyword, or a new source line. As a result, some unusual same-line malformed input may skip further tokens before the next safe boundary. A runtime error can stop execution; the panic-mode requirement concerns **syntax** errors.

AI assistance was used to implement the new statement parser, interpreter, program entry changes, keyword aliases, and Lab 4 test code. AI-generated code is clearly surrounded with `# --- start AI code ---` and `# --- end AI code ---` comments in the corresponding Python files. Existing scanner, token, expression AST, and AST-printer code is reused from previous labs.
