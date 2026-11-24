"""Scan, parse, and execute Ember statements (or run the legacy token mode)."""

import sys
from scanner import Scanner
from parser import ParseError, Parser
from ast_printer import AstPrinter
from interpreter import Interpreter, EmberRuntimeError

# --- start AI code ---
class Ember:
    def __init__(self, tokens_only=False, ast_only=False):
        self.tokens_only = tokens_only
        self.ast_only = ast_only
        self.interpreter = Interpreter()

    def run(self, source):
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()
        if self.tokens_only:
            for token in tokens:
                print(token)
        for error in scanner.errors:
            print(error, file=sys.stderr)
        if scanner.errors:
            return 65
        if self.tokens_only:
            return 0
        parser = Parser(tokens)
        if self.ast_only:
            try:
                print(AstPrinter().print(parser.parse_expression()))
            except ParseError as error:
                print(error, file=sys.stderr)
                return 65
            except RecursionError:
                print("Error: Expression tree is too deep to print.", file=sys.stderr)
                return 65
            return 0
        statements = parser.parse()
        for error in parser.errors:
            print(error, file=sys.stderr)
        try:
            self.interpreter.execute(statements)
        except RecursionError:
            print("Runtime error: Expression or block is too deeply nested.", file=sys.stderr)
            return 70
        except EmberRuntimeError as error:
            print(f"Runtime error: {error}", file=sys.stderr)
            return 70
        return 65 if parser.errors else 0

    def run_file(self, path):
        try:
            with open(path, encoding="utf-8", newline="") as source_file:
                source = source_file.read()
        except (OSError, UnicodeError):
            print("Error: Cannot read source file (UTF-8 required).", file=sys.stderr)
            return 66
        return self.run(source)

    def run_prompt(self):
        while True:
            try:
                source = input("ember> ")
            except (EOFError, KeyboardInterrupt):
                print()
                return 0
            self.run(source)


def main(argv=None):
    arguments = list(sys.argv[1:] if argv is None else argv)
    tokens_only = bool(arguments and arguments[0] == "--tokens")
    ast_only = bool(arguments and arguments[0] == "--ast")
    if tokens_only or ast_only:
        arguments.pop(0)
    if len(arguments) > 1 or any(arg.startswith("--") for arg in arguments):
        print("Usage: python3 src/main.py [--tokens | --ast] [source.ember]", file=sys.stderr)
        return 64
    interpreter = Ember(tokens_only, ast_only)
    if arguments:
        return interpreter.run_file(arguments[0])
    return interpreter.run_prompt()


if __name__ == "__main__":
    raise SystemExit(main())
# --- end AI code ---
