# Lab 1: Ember scanner

Compatibility note: in the Lab 3 revision, use `--tokens` to select the original
scanner-only behavior. Earlier submission commits retain their original commands.

## Language design

Ember is a small language designed for this scanning lab. The name suggests a
small starting point that can grow in later labs. This submission turns source
text into tokens. It does not parse statements or execute them.

The implementation follows the scanning approach in Robert Nystrom's
[Crafting Interpreters, Chapter 4](https://craftinginterpreters.com/scanning.html).
It walks through the source with two indices: the start of the current lexeme
and the next character to read. Lookahead distinguishes one-character operators
from two-character operators. A complete identifier is read before checking
whether it is a keyword. This prevents `letdown` from becoming `LET` + `down`.

Ember uses familiar punctuation to keep the scanner easy to follow, with a few
deliberate differences from Lox:

| Choice | Ember | Reason / difference from Lox |
| --- | --- | --- |
| Declarations | `let`, `fn` | Short replacements for Lox's `var`, `fun`. |
| Output word | `say` | A readable replacement for `print`. It is only recognized here. |
| Null word | `null` | Uses `null` instead of `nil`. |
| Remaining keywords | `if else while return true false and or` | Keeps a small vocabulary for possible future control flow. |
| Smaller scope | No `class`, `this`, `super`, or `for` keywords | Object syntax and additional loop forms are not needed for this design. |
| Extra symbols | `%`, `[`, `]` | Reserves familiar remainder and indexing/list notation for later work. |
| Strings | One physical line, with escapes | Unlike the chapter's multiline strings, a missing quote can recover at the next line. |
| Comments | `//` and nested `/* ... */` | Adds block comments beyond the chapter's line comments. |

These choices reserve token spellings; they do not implement any of their future
runtime meanings. For example, `say "hello";` prints tokens, not `hello`.
Lox words that are not Ember keywords, such as `var`, `print`, and `class`, are
ordinary identifiers.

## Lexical grammar

The following regular expressions describe **one complete token**. They use
Python regular-expression notation and can be checked with `re.fullmatch`.
They are grammar specifications; the scanner itself uses character checks.

Number:

```regex
[0-9]+(?:\.[0-9]+)?
```

Identifier:

```regex
[A-Za-z_][A-Za-z0-9_]*
```

String:

```regex
"(?:[^"\\\r\n]|\\["\\nrt])*"
```

Numbers contain one or more ASCII digits and may have a decimal point followed
by one or more digits. Leading zeros are allowed. Values use Python `float`,
so `42` has literal value `42.0`. A minus sign is a separate token. Numbers
whose float conversion would be infinite produce `Number is too large.` and
no NUMBER token. Ordinary floating-point rounding and underflow still apply.

There is no scientific, hexadecimal, or digit-separator number syntax. The
scanner still recognizes adjacent valid tokens: `1e3` becomes NUMBER `1` and
IDENTIFIER `e3`; `123abc` becomes NUMBER `123` and IDENTIFIER `abc`. Similarly,
`.5` becomes DOT and NUMBER, and `1.` becomes NUMBER and DOT. Deciding whether
such token sequences form valid expressions belongs to a future parser.

Identifiers are case-sensitive and ASCII only. `_`, `_count`, and `count2` are
valid. `let` is a keyword, while `Let` and `letdown` are identifiers. Non-ASCII
letters and digits outside strings/comments are unexpected characters.

Strings begin and end with double quotes. Their literal value excludes those
quotes and decodes these escapes:

| Source escape | Literal character |
| --- | --- |
| `\n` | Newline |
| `\r` | Carriage return |
| `\t` | Tab |
| `\"` | Double quote |
| `\\` | Backslash |

An empty string is valid. Unicode text and comment markers are ordinary string
content. Other unescaped characters are allowed except double quote, backslash,
CR, and LF; a literal tab is therefore allowed. A physical newline, including
one preceded by a backslash, cannot continue a string. Single quotes do not
delimit strings. Unsupported escapes such as `\q` are lexical errors.

### Complete token set

| Category | Spelling → token type |
| --- | --- |
| Delimiters | `(` → LEFT_PAREN, `)` → RIGHT_PAREN, `{` → LEFT_BRACE, `}` → RIGHT_BRACE, `[` → LEFT_BRACKET, `]` → RIGHT_BRACKET |
| Punctuation | `,` → COMMA, `.` → DOT, `;` → SEMICOLON |
| Arithmetic | `+` → PLUS, `-` → MINUS, `*` → STAR, `/` → SLASH, `%` → PERCENT |
| Equality | `!` → BANG, `!=` → BANG_EQUAL, `=` → EQUAL, `==` → EQUAL_EQUAL |
| Comparison | `<` → LESS, `<=` → LESS_EQUAL, `>` → GREATER, `>=` → GREATER_EQUAL |
| Keywords | `let fn say if else while return true false null and or` → their uppercase names |
| Variable text | IDENTIFIER, NUMBER, STRING |
| End of input | EOF, with an empty lexeme |

There are 38 token types. The scanner takes the longest supported operator, so
`===` becomes EQUAL_EQUAL followed by EQUAL. Spaces are not needed between
unambiguous tokens.

### Whitespace, comments, and lines

Spaces, tabs, LF, CRLF, and bare CR separate tokens and produce no tokens.
Line numbers start at 1. LF, CRLF, and bare CR each count as one line break.
The raw source is preserved, including its line-ending convention.

`//` skips everything up to the next physical line break or EOF. A block
comment starts with `/*` and ends at its matching `*/`. Nested openings increase
a depth counter; closings decrease it. Quotes and `//` inside a block comment
have no special effect. An unmatched closing `*/` outside a comment is STAR
followed by SLASH. Nested comments require a counter and are not described by
the regular expressions for the three token categories above.

## Implementation and error handling

All implementation files are in `src/`:

- `tokens.py`: `TokenType` and a `Token` dataclass containing `type`, `lexeme`,
  `literal`, and the token's starting `line`.
- `scanner.py`: the scanner, keyword table, character checks, strings, numbers,
  and nested comments. `scan_tokens()` is called once per Scanner instance.
- `main.py`: the `Ember` class and `main()` entry point, file loading, and prompt.

Each token is printed as `TYPE lexeme literal [line N]`. Python `repr` makes
quotes, empty strings, tabs, and escapes visible. Only NUMBER and STRING carry
literal values. Other tokens, including TRUE, FALSE, NULL, and EOF, have `None`
as their literal field. Their token types already distinguish them.

Tokens go to standard output; errors go to standard error. Output includes EOF
even if errors occurred. The following errors are supported:

| Error | Diagnostic location | Recovery |
| --- | --- | --- |
| Unexpected character | The character's line | Consume it and continue. |
| Unterminated string at EOF | Opening quote's line | Discard the string and emit EOF. |
| Physical newline in a string | Opening quote's line | Discard the string and continue on the next line. |
| Invalid escape | Opening quote's line | Report each invalid escape, consume to quote/newline/EOF, and discard that string. |
| Unterminated block comment | Outermost opening delimiter's line | Consume through EOF and report the error. |
| Number too large | Number's starting line | Discard the number and continue. |

An invalid escape followed by EOF can produce both an escape error and an
unterminated-string error. The scanner does not silently repair invalid input.

Each interactive submission creates a fresh Scanner. Its line numbering starts
at 1 and its error list starts empty, so one error does not affect the next
submission. Ctrl-D at an empty prompt exits on macOS/Linux; Ctrl-C while waiting
for input also exits cleanly.

## Setup and commands

Requirements: Python 3.10 or newer. No packages need to be installed. Commands
below run from the repository root, the directory containing `src/`, `test/`,
and `report/`. The recorded results were produced with Python 3.13.1 on macOS.

Run a UTF-8 source file:

```sh
python3 src/main.py --tokens test/lab1/inputs/example.ember
```

Start interactive mode:

```sh
python3 src/main.py --tokens
```

For example, typing `let count = 2;` produces:

```text
LET 'let' None [line 1]
IDENTIFIER 'count' None [line 1]
EQUAL '=' None [line 1]
NUMBER '2' 2.0 [line 1]
SEMICOLON ';' None [line 1]
EOF '' None [line 1]
```

Exit statuses are 0 for success, 65 for lexical errors in a file, 66 for an
unreadable or non-UTF-8 source file, and 64 for too many arguments. The prompt
continues after lexical errors and exits with 0 when the user finishes.

## Tests and actual results

Run all portable scanner and command-line checks:

```sh
python3 test/lab1/run_tests.py
```

Regenerate the detailed results:

```sh
python3 test/lab1/run_tests.py --report
```

Run the additional terminal checks on macOS or Linux:

```sh
python3 test/lab1/terminal_test.py --report
```

Results: **85/85 portable checks passed**, and **2/2 terminal checks passed**.
The portable suite runs 38 sources through both the Scanner API and source-file
mode (76 checks), checks coverage of all token types (1), and tests interactive
and file/argument handling (8). The terminal tests verify error recovery, EOF,
and interruption while waiting for input.

The detailed test evidence is part of this report:

- [All scanner and command-line cases](test-results.md): each case's purpose,
  exact source input, expected tokens/errors or streams, actual output, and match result.
- [Terminal cases](terminal-results.md): input actions, expected transcript,
  actual transcript, exit status, and match result.

Sources and independently written expectations are in `test/lab1/cases.py`.
Each source is also committed under `test/lab1/inputs/`, enclosed in
`// --- start AI code ---` and `// --- end AI code ---` attribution markers.
The runner verifies and removes the exact wrapper before comparing the enclosed
source with the case definition. It preserves all original bytes, including
line endings and whether the source ends with a newline. File-mode checks write
that enclosed source to a temporary `.ember` file and launch the real entry point
in a subprocess. This keeps the attribution comments from changing EOF and
unterminated-string tests. Running a marked file directly includes the wrapper
in scanning, so its line numbers and malformed-input results may differ from
the recorded tests. Special file-error inputs are made in temporary directories
by the test script and removed afterward. Expected values are never generated
from scanner output. Both test scripts exit unsuccessfully if a comparison fails.

During verification, the first terminal harness lost the final output newline
when its pseudo-terminal closed on macOS. Keeping its slave descriptor open
until output was drained fixed the harness; the scanner did not need a change.
The committed result files show the final passing runs.

## Extra-credit request

Two features are submitted for instructor consideration, subject to the lab's
overall extra-credit cap:

1. **Nested block comments.** The scanner maintains nesting depth and line
   numbers, distinguishes nested delimiters from ordinary comment text, and
   reports an unclosed outer comment. This allows temporarily commenting out a
   section that already contains block comments. See `nested_comment`,
   `block_comment`, `comment_contents`, `unterminated_comment`, and
   `unterminated_nested` in the detailed results.
2. **String escapes.** Raw lexemes are preserved while a separate decoded value
   is built. Escape validation must distinguish escaped quotes from closing
   quotes and recover from unsupported escapes. This supports quotes, backslashes,
   and control characters in one-line source strings. See `escapes`,
   `invalid_escape`, `multiple_bad_escapes`, `trailing_backslash`,
   `escaped_newline`, and `escaped_quote_eof` in the detailed results.

## Limitations and submission

There are no known failing tests. This is a scanner only; reserved words and
operators have no executed meaning. Identifiers are ASCII, numbers use floating
point, and strings use only the five listed escapes. There is no multiline
interactive buffer: block comments spanning lines must be tested in a source
file. The source and resulting token list are held in memory. The optional
pseudo-terminal script uses Unix APIs and is not intended for native Windows.
The portable suite remains available there using the appropriate Python command.

Submit a link to the exact GitHub commit containing this repository, using
`https://github.com/<owner>/<repo>/commit/<commit-hash>`. Ensure the instructor
can access the repository. A local folder or ZIP is not the Blackboard commit
link required by the assignment.

## Reference

Robert Nystrom, *Crafting Interpreters*, [Chapter 4: Scanning](https://craftinginterpreters.com/scanning.html).
Ember adapts the chapter's scanning structure to Python with the lexical rules
and extensions described above.
