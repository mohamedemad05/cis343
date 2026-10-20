"""Scan, parse, and print one Ember expression from a file or terminal input."""

import sys

from scanner import Scanner
from parser import ParseError, Parser
from ast_printer import AstPrinter


class Ember:
    def __init__(self, tokens_only=False):
        self.tokens_only = tokens_only

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
        try:
            tree = Parser(tokens).parse()
            output = AstPrinter().print(tree)
        except ParseError as error:
            print(error, file=sys.stderr)
            return 65
        except RecursionError:
            print(f"[line {tokens[0].line}] Error: Expression tree is too deep to print.", file=sys.stderr)
            return 65
        # Build the whole string before printing, so errors never leave a partial AST.
        print(output)
        return 0

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
    if tokens_only:
        arguments.pop(0)
    if len(arguments) > 1 or any(arg.startswith("--") for arg in arguments):
        print("Usage: python3 src/main.py [--tokens] [source.ember]", file=sys.stderr)
        return 64
    interpreter = Ember(tokens_only)
    if arguments:
        return interpreter.run_file(arguments[0])
    return interpreter.run_prompt()


if __name__ == "__main__":
    raise SystemExit(main())
