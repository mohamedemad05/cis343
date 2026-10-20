# Lab 3 terminal checks

Run: `python3 test/lab3/terminal_test.py --report`.

These tests use a real pseudo-terminal with input echo disabled.
Ctrl-C is sent as SIGINT; Ctrl-D is sent as the terminal EOF character.

## Recovery and Ctrl-D

Input: @, Enter, 1+, Enter, 2+3, Enter, Ctrl-D

Expected:
```text
ember> [line 1] Error: Unexpected character '@'.
ember> [line 1] Error at end: Expected an expression.
ember> (+ 2 3)
ember> 

exit status: 0
```

Actual:
```text
ember> [line 1] Error: Unexpected character '@'.
ember> [line 1] Error at end: Expected an expression.
ember> (+ 2 3)
ember> 

exit status: 0
```

Result: PASS

## Ctrl-C

Input: SIGINT while waiting at the first prompt

Expected:
```text
ember> 

exit status: 0
```

Actual:
```text
ember> 

exit status: 0
```

Result: PASS
