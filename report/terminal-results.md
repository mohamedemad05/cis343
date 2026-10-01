# Terminal checks

Run: `python3 test/lab1/terminal_test.py --report`.

These tests use a real pseudo-terminal with input echo disabled.
Ctrl-C is sent as SIGINT; Ctrl-D is sent as the terminal EOF character.

## Recovery and Ctrl-D

Input: @, Enter, say, Enter, Ctrl-D

Expected:
```text
ember> EOF '' None [line 1]
[line 1] Error: Unexpected character '@'.
ember> SAY 'say' None [line 1]
EOF '' None [line 1]
ember> 

exit status: 0
```

Actual:
```text
ember> EOF '' None [line 1]
[line 1] Error: Unexpected character '@'.
ember> SAY 'say' None [line 1]
EOF '' None [line 1]
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
