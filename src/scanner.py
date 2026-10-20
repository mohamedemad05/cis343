"""A character-by-character scanner, following Chapter 4's approach."""

import math

from tokens import Token, TokenType as T


KEYWORDS = {
    "let": T.LET, "fn": T.FN, "say": T.SAY, "if": T.IF, "else": T.ELSE,
    "while": T.WHILE, "return": T.RETURN, "true": T.TRUE, "false": T.FALSE,
    "null": T.NULL, "and": T.AND, "or": T.OR,
}

SINGLE_CHAR = {
    "(": T.LEFT_PAREN, ")": T.RIGHT_PAREN,
    "{": T.LEFT_BRACE, "}": T.RIGHT_BRACE,
    "[": T.LEFT_BRACKET, "]": T.RIGHT_BRACKET,
    ",": T.COMMA, ".": T.DOT, ";": T.SEMICOLON,
    "+": T.PLUS, "-": T.MINUS, "*": T.STAR, "%": T.PERCENT,
}

COMPARISONS = {
    "!": (T.BANG, T.BANG_EQUAL), "=": (T.EQUAL, T.EQUAL_EQUAL),
    "<": (T.LESS, T.LESS_EQUAL), ">": (T.GREATER, T.GREATER_EQUAL),
}

ESCAPES = {"n": "\n", "r": "\r", "t": "\t", '"': '"', "\\": "\\"}


def is_digit(char):
    return "0" <= char <= "9"


def is_alpha(char):
    return "a" <= char <= "z" or "A" <= char <= "Z" or char == "_"


class Scanner:
    def __init__(self, source):
        self.source = source
        self.tokens = []
        self.errors = []
        self.start = 0
        self.current = 0
        self.line = 1
        self.start_line = 1

    def scan_tokens(self):
        while self.current < len(self.source):
            self.start = self.current
            self.start_line = self.line
            self.scan_token()
        self.tokens.append(Token(T.EOF, "", None, self.line))
        return self.tokens

    def advance(self):
        char = self.source[self.current]
        self.current += 1
        return char

    def peek(self, offset=0):
        index = self.current + offset
        return self.source[index] if index < len(self.source) else ""

    def match(self, expected):
        if self.peek() != expected:
            return False
        self.current += 1
        return True

    def add_token(self, kind, literal=None):
        self.tokens.append(Token(kind, self.source[self.start:self.current],
                                 literal, self.start_line))

    def error(self, message):
        self.errors.append(f"[line {self.start_line}] Error: {message}")

    def newline(self, char):
        # Treat Windows CRLF as one newline, while also accepting bare CR.
        if char == "\r":
            self.match("\n")
        self.line += 1

    def scan_token(self):
        char = self.advance()
        if char in SINGLE_CHAR:
            self.add_token(SINGLE_CHAR[char])
        elif char in COMPARISONS:
            short, long = COMPARISONS[char]
            self.add_token(long if self.match("=") else short)
        elif char == "/":
            if self.match("/"):
                while self.peek() not in ("", "\n", "\r"):
                    self.advance()
            elif self.match("*"):
                self.block_comment()
            else:
                self.add_token(T.SLASH)
        elif char in (" ", "\t"):
            pass
        elif char in ("\n", "\r"):
            self.newline(char)
        elif char == '"':
            self.string()
        elif is_digit(char):
            self.number()
        elif is_alpha(char):
            self.identifier()
        else:
            self.error(f"Unexpected character {char!r}.")

    def identifier(self):
        while is_alpha(self.peek()) or is_digit(self.peek()):
            self.advance()
        word = self.source[self.start:self.current]
        self.add_token(KEYWORDS.get(word, T.IDENTIFIER))

    def number(self):
        while is_digit(self.peek()):
            self.advance()
        if self.peek() == "." and is_digit(self.peek(1)):
            self.advance()
            while is_digit(self.peek()):
                self.advance()
        value = float(self.source[self.start:self.current])
        if math.isfinite(value):
            self.add_token(T.NUMBER, value)
        else:
            self.error("Number is too large.")

    def string(self):
        value = []
        valid = True
        while self.peek() != "":
            char = self.advance()
            if char == '"':
                if valid:
                    self.add_token(T.STRING, "".join(value))
                return
            if char in ("\n", "\r"):
                self.newline(char)
                self.error("Unterminated string (newline in string).")
                return
            if char == "\\":
                if self.peek() == "":
                    break
                escaped = self.advance()
                if escaped in ("\n", "\r"):
                    self.newline(escaped)
                    self.error("Unterminated string (newline in string).")
                    return
                if escaped in ESCAPES:
                    value.append(ESCAPES[escaped])
                else:
                    self.error(f"Invalid escape '\\{escaped}'.")
                    valid = False
            else:
                value.append(char)
        self.error("Unterminated string.")

    def block_comment(self):
        depth = 1
        while self.peek() != "":
            char = self.advance()
            if char == "/" and self.match("*"):
                depth += 1
            elif char == "*" and self.match("/"):
                depth -= 1
                if depth == 0:
                    return
            elif char in ("\n", "\r"):
                self.newline(char)
        self.error("Unterminated block comment.")
