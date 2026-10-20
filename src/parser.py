"""Recursive-descent parser for one Ember expression followed by EOF."""

from expr import Binary, Grouping, Literal, Unary
from tokens import TokenType as T


class ParseError(Exception):
    """A syntax diagnostic that the entry point can display without a traceback."""


class Parser:
    def __init__(self, tokens):
        # Scanner output always contains a final EOF token.
        self.tokens = tokens
        self.current = 0

    def parse(self):
        try:
            expression = self.logic_or()
            if self.peek().type is not T.EOF:
                raise self.error("Unexpected trailing token.")
            return expression
        except RecursionError:
            raise ParseError(
                f"[line {self.peek().line}] Error: Expression is too deeply nested."
            ) from None

    def logic_or(self):
        expression = self.logic_and()
        while self.match(T.OR):
            operator = self.previous()
            expression = Binary(expression, operator, self.logic_and())
        return expression

    def logic_and(self):
        expression = self.equality()
        while self.match(T.AND):
            operator = self.previous()
            expression = Binary(expression, operator, self.equality())
        return expression

    def equality(self):
        expression = self.comparison()
        while self.match(T.EQUAL_EQUAL, T.BANG_EQUAL):
            operator = self.previous()
            expression = Binary(expression, operator, self.comparison())
        return expression

    def comparison(self):
        expression = self.term()
        while self.match(T.LESS, T.LESS_EQUAL, T.GREATER, T.GREATER_EQUAL):
            operator = self.previous()
            expression = Binary(expression, operator, self.term())
        return expression

    def term(self):
        expression = self.factor()
        while self.match(T.PLUS, T.MINUS):
            operator = self.previous()
            expression = Binary(expression, operator, self.factor())
        return expression

    def factor(self):
        expression = self.unary()
        while self.match(T.STAR, T.SLASH, T.PERCENT):
            operator = self.previous()
            expression = Binary(expression, operator, self.unary())
        return expression

    def unary(self):
        if self.match(T.BANG, T.MINUS):
            operator = self.previous()
            return Unary(operator, self.unary())
        return self.primary()

    def primary(self):
        if self.match(T.NUMBER, T.STRING):
            return Literal(self.previous().literal)
        if self.match(T.TRUE):
            return Literal(True)
        if self.match(T.FALSE):
            return Literal(False)
        if self.match(T.NULL):
            return Literal(None)
        if self.match(T.LEFT_PAREN):
            opening = self.previous()
            expression = self.logic_or()
            if not self.match(T.RIGHT_PAREN):
                raise self.error(f"Expected ')' after expression (opened on line {opening.line}).")
            return Grouping(expression)
        if self.peek().type in (
            T.PLUS, T.STAR, T.SLASH, T.PERCENT, T.EQUAL_EQUAL, T.BANG_EQUAL,
            T.LESS, T.LESS_EQUAL, T.GREATER, T.GREATER_EQUAL, T.AND, T.OR,
        ):
            raise self.error(f"Missing left operand for {self.peek().lexeme!r}.")
        raise self.error("Expected an expression.")

    def match(self, *types):
        if self.peek().type in types:
            self.current += 1
            return True
        return False

    def peek(self):
        return self.tokens[self.current]

    def previous(self):
        return self.tokens[self.current - 1]

    def error(self, message):
        token = self.peek()
        location = "at end" if token.type is T.EOF else f"at {token.lexeme!r}"
        return ParseError(f"[line {token.line}] Error {location}: {message}")
