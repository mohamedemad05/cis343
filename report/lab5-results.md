# Lab 5 test results

45/45 checks passed.

Run `python3 test/lab5/run_tests.py --report` from the repository root.

Expected values are specified independently in `test/lab5/cases.py` and this runner.
Each ordinary fixture runs in a separate process with a 10-second timeout.
Depth checks assert controlled diagnostics and recovery instead of implementation-specific stack limits.

## variables

Input:
```text
// --- start AI code ---
var score = 10; print score; score = score + 5; print score;
```

Expected:
```text
stdout:
10
15

stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
10
15

stderr:
(empty)
exit status: 0
```

Result: PASS

## missing_initializer

Input:
```text
// --- start AI code ---
var value; print value; value = 42; print value;
```

Expected:
```text
stdout:
nil
42

stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
nil
42

stderr:
(empty)
exit status: 0
```

Result: PASS

## chained_assignment

Input:
```text
// --- start AI code ---
var a; var b; print a = b = 3; print a; print b;
```

Expected:
```text
stdout:
3
3
3

stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
3
3
3

stderr:
(empty)
exit status: 0
```

Result: PASS

## outer_assignment

Input:
```text
// --- start AI code ---
var a = 1; { { a = 9; } print a; } print a;
```

Expected:
```text
stdout:
9
9

stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
9
9

stderr:
(empty)
exit status: 0
```

Result: PASS

## shadow_assignment

Input:
```text
// --- start AI code ---
var a = 1; { var a = 2; a = 3; print a; } print a;
```

Expected:
```text
stdout:
3
1

stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
3
1

stderr:
(empty)
exit status: 0
```

Result: PASS

## sibling_scopes

Input:
```text
// --- start AI code ---
{ var a = 1; print a; } { var a = 2; print a; }
```

Expected:
```text
stdout:
1
2

stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
1
2

stderr:
(empty)
exit status: 0
```

Result: PASS

## empty_blocks

Input:
```text
// --- start AI code ---
{} { {} }
```

Expected:
```text
stdout:
(empty)
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(empty)
stderr:
(empty)
exit status: 0
```

Result: PASS

## dynamic_type

Input:
```text
// --- start AI code ---
var a = 1; a = "changed"; print a; a = false; print a;
```

Expected:
```text
stdout:
changed
false

stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
changed
false

stderr:
(empty)
exit status: 0
```

Result: PASS

## aliases

Input:
```text
// --- start AI code ---
let a; say a; a = null; print a; var b = nil; say b;
```

Expected:
```text
stdout:
nil
nil
nil

stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
nil
nil
nil

stderr:
(empty)
exit status: 0
```

Result: PASS

## assignment_precedence

Input:
```text
// --- start AI code ---
var a; print a = 1 + 2 * 3; print (a = 4) + 1; print a;
```

Expected:
```text
stdout:
7
5
4

stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
7
5
4

stderr:
(empty)
exit status: 0
```

Result: PASS

## short_circuit

Input:
```text
// --- start AI code ---
var a = 0; false and (a = 1); true or (a = 2); print a;
```

Expected:
```text
stdout:
0

stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
0

stderr:
(empty)
exit status: 0
```

Result: PASS

## nil_truthiness

Input:
```text
// --- start AI code ---
var a; print !a; print a == nil; print 0 == false;
```

Expected:
```text
stdout:
true
true
false

stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
true
true
false

stderr:
(empty)
exit status: 0
```

Result: PASS

## declaration_order

Input:
```text
// --- start AI code ---
var a = "outer"; { print a; var a = "inner"; print a; } print a;
```

Expected:
```text
stdout:
outer
inner
outer

stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
outer
inner
outer

stderr:
(empty)
exit status: 0
```

Result: PASS

## read_before_declaration

Input:
```text
// --- start AI code ---
print a; var a = 1;
```

Expected:
```text
stdout:
(empty)
stderr:
Runtime error: [line 2] Undefined variable 'a'.

exit status: 70
```

Actual:
```text
stdout:
(empty)
stderr:
Runtime error: [line 2] Undefined variable 'a'.

exit status: 70
```

Result: PASS

## assign_before_declaration

Input:
```text
// --- start AI code ---
a = 1;
```

Expected:
```text
stdout:
(empty)
stderr:
Runtime error: [line 2] Undefined variable 'a'.

exit status: 70
```

Actual:
```text
stdout:
(empty)
stderr:
Runtime error: [line 2] Undefined variable 'a'.

exit status: 70
```

Result: PASS

## scope_escape

Input:
```text
// --- start AI code ---
{ var local = 1; } print local;
```

Expected:
```text
stdout:
(empty)
stderr:
Runtime error: [line 2] Undefined variable 'local'.

exit status: 70
```

Actual:
```text
stdout:
(empty)
stderr:
Runtime error: [line 2] Undefined variable 'local'.

exit status: 70
```

Result: PASS

## redeclaration

Input:
```text
// --- start AI code ---
var a = 1; var a = 2;
```

Expected:
```text
stdout:
(empty)
stderr:
Runtime error: [line 2] Variable 'a' is already declared in this scope.

exit status: 70
```

Actual:
```text
stdout:
(empty)
stderr:
Runtime error: [line 2] Variable 'a' is already declared in this scope.

exit status: 70
```

Result: PASS

## block_redeclaration

Input:
```text
// --- start AI code ---
{ var a; var a; }
```

Expected:
```text
stdout:
(empty)
stderr:
Runtime error: [line 2] Variable 'a' is already declared in this scope.

exit status: 70
```

Actual:
```text
stdout:
(empty)
stderr:
Runtime error: [line 2] Variable 'a' is already declared in this scope.

exit status: 70
```

Result: PASS

## self_initializer

Input:
```text
// --- start AI code ---
var a = a;
```

Expected:
```text
stdout:
(empty)
stderr:
Runtime error: [line 2] Cannot access variable 'a' in its own initializer.

exit status: 70
```

Actual:
```text
stdout:
(empty)
stderr:
Runtime error: [line 2] Cannot access variable 'a' in its own initializer.

exit status: 70
```

Result: PASS

## shadow_self_initializer

Input:
```text
// --- start AI code ---
var a = 1; { var a = a; }
```

Expected:
```text
stdout:
(empty)
stderr:
Runtime error: [line 2] Cannot access variable 'a' in its own initializer.

exit status: 70
```

Actual:
```text
stdout:
(empty)
stderr:
Runtime error: [line 2] Cannot access variable 'a' in its own initializer.

exit status: 70
```

Result: PASS

## self_assignment_initializer

Input:
```text
// --- start AI code ---
var a = (a = 1);
```

Expected:
```text
stdout:
(empty)
stderr:
Runtime error: [line 2] Cannot access variable 'a' in its own initializer.

exit status: 70
```

Actual:
```text
stdout:
(empty)
stderr:
Runtime error: [line 2] Cannot access variable 'a' in its own initializer.

exit status: 70
```

Result: PASS

## undefined_initializer

Input:
```text
// --- start AI code ---
var a = missing;
```

Expected:
```text
stdout:
(empty)
stderr:
Runtime error: [line 2] Undefined variable 'missing'.

exit status: 70
```

Actual:
```text
stdout:
(empty)
stderr:
Runtime error: [line 2] Undefined variable 'missing'.

exit status: 70
```

Result: PASS

## invalid_literal_target

Input:
```text
// --- start AI code ---
1 = 2; print "recovered";
```

Expected:
```text
stdout:
recovered

stderr:
[line 2] Error at '=': Invalid assignment target; expected a variable identifier.

exit status: 65
```

Actual:
```text
stdout:
recovered

stderr:
[line 2] Error at '=': Invalid assignment target; expected a variable identifier.

exit status: 65
```

Result: PASS

## invalid_binary_target

Input:
```text
// --- start AI code ---
var a = 1; a + 1 = 2; print a;
```

Expected:
```text
stdout:
1

stderr:
[line 2] Error at '=': Invalid assignment target; expected a variable identifier.

exit status: 65
```

Actual:
```text
stdout:
1

stderr:
[line 2] Error at '=': Invalid assignment target; expected a variable identifier.

exit status: 65
```

Result: PASS

## invalid_group_target

Input:
```text
// --- start AI code ---
var a = 1; (a) = 2; print a;
```

Expected:
```text
stdout:
1

stderr:
[line 2] Error at '=': Invalid assignment target; expected a variable identifier.

exit status: 65
```

Actual:
```text
stdout:
1

stderr:
[line 2] Error at '=': Invalid assignment target; expected a variable identifier.

exit status: 65
```

Result: PASS

## unclosed_block

Input:
```text
// --- start AI code ---
{ var a = 1;
```

Expected:
```text
stdout:
(empty)
stderr:
[line 2] Error at end: Expected '}' after block (opened on line 2).

exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 2] Error at end: Expected '}' after block (opened on line 2).

exit status: 65
```

Result: PASS

## extra_brace

Input:
```text
// --- start AI code ---
} print 1;
```

Expected:
```text
stdout:
1

stderr:
[line 2] Error at '}': Unmatched '}'.

exit status: 65
```

Actual:
```text
stdout:
1

stderr:
[line 2] Error at '}': Unmatched '}'.

exit status: 65
```

Result: PASS

## missing_name

Input:
```text
// --- start AI code ---
var = 1; print 2;
```

Expected:
```text
stdout:
2

stderr:
[line 2] Error at '=': Expected variable name.

exit status: 65
```

Actual:
```text
stdout:
2

stderr:
[line 2] Error at '=': Expected variable name.

exit status: 65
```

Result: PASS

## reserved_name

Input:
```text
// --- start AI code ---
var print = 1;
```

Expected:
```text
stdout:
(empty)
stderr:
[line 2] Error at 'print': Expected variable name.
[line 2] Error at '=': Expected an expression.

exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 2] Error at 'print': Expected variable name.
[line 2] Error at '=': Expected an expression.

exit status: 65
```

Result: PASS

## missing_declaration_semicolon

Input:
```text
// --- start AI code ---
var a = 1 print 2;
```

Expected:
```text
stdout:
2

stderr:
[line 2] Error at 'print': Expected ';' after variable declaration.

exit status: 65
```

Actual:
```text
stdout:
2

stderr:
[line 2] Error at 'print': Expected ';' after variable declaration.

exit status: 65
```

Result: PASS

## missing_initializer_expression

Input:
```text
// --- start AI code ---
var a = ; print 2;
```

Expected:
```text
stdout:
2

stderr:
[line 2] Error at ';': Expected an expression.

exit status: 65
```

Actual:
```text
stdout:
2

stderr:
[line 2] Error at ';': Expected an expression.

exit status: 65
```

Result: PASS

## missing_assignment_value

Input:
```text
// --- start AI code ---
var a = 1; a = ; print a;
```

Expected:
```text
stdout:
1

stderr:
[line 2] Error at ';': Expected an expression.

exit status: 65
```

Actual:
```text
stdout:
1

stderr:
[line 2] Error at ';': Expected an expression.

exit status: 65
```

Result: PASS

## brace_recovery

Input:
```text
// --- start AI code ---
var a = "global"; { var a = ; } print a;
```

Expected:
```text
stdout:
global

stderr:
[line 2] Error at ';': Expected an expression.

exit status: 65
```

Actual:
```text
stdout:
global

stderr:
[line 2] Error at ';': Expected an expression.

exit status: 65
```

Result: PASS

## block_missing_semicolon

Input:
```text
// --- start AI code ---
{ print 1 } print 2;
```

Expected:
```text
stdout:
2

stderr:
[line 2] Error at '}': Expected ';' after print value.

exit status: 65
```

Actual:
```text
stdout:
2

stderr:
[line 2] Error at '}': Expected ';' after print value.

exit status: 65
```

Result: PASS

## variable_type_error

Input:
```text
// --- start AI code ---
var a; print a + 1;
```

Expected:
```text
stdout:
(empty)
stderr:
Runtime error: [line 2] Operator '+' needs numbers.

exit status: 70
```

Actual:
```text
stdout:
(empty)
stderr:
Runtime error: [line 2] Operator '+' needs numbers.

exit status: 70
```

Result: PASS

## variable_division_zero

Input:
```text
// --- start AI code ---
var a = 0; print 1 / a;
```

Expected:
```text
stdout:
(empty)
stderr:
Runtime error: [line 2] Division by zero.

exit status: 70
```

Actual:
```text
stdout:
(empty)
stderr:
Runtime error: [line 2] Division by zero.

exit status: 70
```

Result: PASS

## lexical_error

Input:
```text
// --- start AI code ---
var a = @;
```

Expected:
```text
stdout:
(empty)
stderr:
[line 2] Error: Unexpected character '@'.

exit status: 65
```

Actual:
```text
stdout:
(empty)
stderr:
[line 2] Error: Unexpected character '@'.

exit status: 65
```

Result: PASS

## multiline_location

Input:
```text
// --- start AI code ---
var a = 1;
{
 print missing;
}
```

Expected:
```text
stdout:
(empty)
stderr:
Runtime error: [line 4] Undefined variable 'missing'.

exit status: 70
```

Actual:
```text
stdout:
(empty)
stderr:
Runtime error: [line 4] Undefined variable 'missing'.

exit status: 70
```

Result: PASS

## textbook

Input:
```text
// --- start AI code ---
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
// --- end AI code ---
```

Expected:
```text
stdout:
inner a
outer b
global c
outer a
outer b
global c
global a
global b
global c

stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
inner a
outer b
global c
outer a
outer b
global c
global a
global b
global c

stderr:
(empty)
exit status: 0
```

Result: PASS

## prompt_persistence_and_error_recovery

Input:
```text
var a = 1;
{ var local = 2; print missing; }
print a;
print local;
var bad = bad;
var bad = 7; print bad;
```

Expected:
```text
stdout:
ember> ember> ember> 1
ember> ember> ember> 7
ember> 

stderr:
Runtime error: [line 1] Undefined variable 'missing'.
Runtime error: [line 1] Undefined variable 'local'.
Runtime error: [line 1] Cannot access variable 'bad' in its own initializer.

exit status: 0
```

Actual:
```text
stdout:
ember> ember> ember> 1
ember> ember> ember> 7
ember> 

stderr:
Runtime error: [line 1] Undefined variable 'missing'.
Runtime error: [line 1] Undefined variable 'local'.
Runtime error: [line 1] Cannot access variable 'bad' in its own initializer.

exit status: 0
```

Result: PASS

## redeclaration_preserves_value

Input:
```text
var a = 1;
var a = (a = 99);
print a;
```

Expected:
```text
stdout:
1

stderr:
Runtime error: [line 1] Variable 'a' is already declared in this scope.

exit status: [0, 70, 0]
```

Actual:
```text
stdout:
1

stderr:
Runtime error: [line 1] Variable 'a' is already declared in this scope.

exit status: [0, 70, 0]
```

Result: PASS

## new_ast_nodes

Input:
```text
var a = 1; { print a = 2; }
```

Expected:
```text
stdout:
(var a 1)
(block (print (= a 2)))

stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
(var a 1)
(block (print (= a 2)))

stderr:
(empty)
exit status: 0
```

Result: PASS

## deep_assignment

Input:
```text
var a; a = a = a = a = a = a = a = a = a = a = a = a = a = a = a = a = a = a = a = a = a = ... (2000 levels/operators)
print 42;
```

Expected:
```text
stdout:
controlled error and prompt recovery
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
controlled error and prompt recovery
stderr:
(empty)
exit status: 0
```

Result: PASS

## deep_blocks

Input:
```text
{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{ ... (2000 levels/operators)
print 42;
```

Expected:
```text
stdout:
controlled error and prompt recovery
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
controlled error and prompt recovery
stderr:
(empty)
exit status: 0
```

Result: PASS

## deep_evaluation

Input:
```text
print 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 +  ... (2000 levels/operators)
print 42;
```

Expected:
```text
stdout:
controlled error and prompt recovery
stderr:
(empty)
exit status: 0
```

Actual:
```text
stdout:
controlled error and prompt recovery
stderr:
(empty)
exit status: 0
```

Result: PASS
