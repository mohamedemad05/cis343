"""Run Ember's scanner on a UTF-8 file or one terminal line at a time."""

import sys

from scanner import Scanner


class Ember:
    def run(self, source):
        scanner = Scanner(source)
        for token in scanner.scan_tokens():
            print(token)
        for error in scanner.errors:
            print(error, file=sys.stderr)
        return 65 if scanner.errors else 0

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
    arguments = sys.argv[1:] if argv is None else argv
    if len(arguments) > 1:
        print("Usage: python3 src/main.py [source.ember]", file=sys.stderr)
        return 64
    interpreter = Ember()
    if arguments:
        return interpreter.run_file(arguments[0])
    return interpreter.run_prompt()


if __name__ == "__main__":
    raise SystemExit(main())
