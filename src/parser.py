"""Ember recursive-descent parser with recoverable statement parsing."""

from expr import Assign, Binary, Grouping, Literal, Unary, Variable
from tokens import TokenType as T
from stmt import BlockStmt, ExpressionStmt, PrintStmt, VarStmt

# --- start AI code ---
class ParseError(Exception):
    """Recoverable syntax error."""


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0
        self.errors = []

    def parse(self):
        """Read declarations until EOF; errors retain their lexical block."""
        statements = []
        while not self.is_at_end():
            statement = self.declaration()
            if statement is not None:
                statements.append(statement)
        return statements

    def parse_expression(self):
        """Legacy Lab 3 entry point: exactly one expression without a semicolon."""
        try:
            expression = self.assignment()
            if not self.is_at_end():
                raise self.error("Unexpected trailing token.")
            return expression
        except RecursionError:
            raise self.error("Expression is too deeply nested.") from None

    def declaration(self, in_block=False):
        start = self.current
        try:
            if self.match(T.LET):
                name = self.consume(T.IDENTIFIER, "Expected variable name.")
                initializer = self.assignment() if self.match(T.EQUAL) else None
                self.consume(T.SEMICOLON, "Expected ';' after variable declaration.")
                return VarStmt(name, initializer)
            return self.statement()
        except ParseError as error:
            self.errors.append(str(error))
        except RecursionError:
            self.errors.append(f"[line {self.peek().line}] Error: Expression or block is too deeply nested.")
        self.synchronize(start, in_block)
        return None

    def statement(self):
        if self.match(T.LEFT_BRACE):
            opening = self.previous()
            statements = []
            while not self.is_at_end() and self.peek().type is not T.RIGHT_BRACE:
                statement = self.declaration(in_block=True)
                if statement is not None:
                    statements.append(statement)
            self.consume(T.RIGHT_BRACE, f"Expected '}}' after block (opened on line {opening.line}).")
            return BlockStmt(statements)
        if self.peek().type is T.RIGHT_BRACE:
            raise self.error("Unmatched '}'.")
        if self.match(T.SAY):
            value = self.assignment()
            self.consume(T.SEMICOLON, "Expected ';' after print value.")
            return PrintStmt(value)
        value = self.assignment()
        self.consume(T.SEMICOLON, "Expected ';' after expression.")
        return ExpressionStmt(value)

    def assignment(self):
        expression = self.logic_or()
        if self.match(T.EQUAL):
            equals = self.previous()
            value = self.assignment()
            if not isinstance(expression, Variable):
                raise ParseError(
                    f"[line {equals.line}] Error at '=': Invalid assignment target; expected a variable identifier."
                )
            return Assign(expression.name, value)
        return expression

    def logic_or(self):
        expression = self.logic_and()
        while self.match(T.OR):
            expression = Binary(expression, self.previous(), self.logic_and())
        return expression

    def logic_and(self):
        expression = self.equality()
        while self.match(T.AND):
            expression = Binary(expression, self.previous(), self.equality())
        return expression

    def equality(self):
        expression = self.comparison()
        while self.match(T.EQUAL_EQUAL, T.BANG_EQUAL):
            expression = Binary(expression, self.previous(), self.comparison())
        return expression

    def comparison(self):
        expression = self.term()
        while self.match(T.LESS, T.LESS_EQUAL, T.GREATER, T.GREATER_EQUAL):
            expression = Binary(expression, self.previous(), self.term())
        return expression

    def term(self):
        expression = self.factor()
        while self.match(T.PLUS, T.MINUS):
            expression = Binary(expression, self.previous(), self.factor())
        return expression

    def factor(self):
        expression = self.unary()
        while self.match(T.STAR, T.SLASH, T.PERCENT):
            expression = Binary(expression, self.previous(), self.unary())
        return expression

    def unary(self):
        if self.match(T.BANG, T.MINUS):
            return Unary(self.previous(), self.unary())
        return self.primary()

    def primary(self):
        if self.match(T.IDENTIFIER):
            return Variable(self.previous())
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
            expression = self.assignment()
            self.consume(T.RIGHT_PAREN, f"Expected ')' after expression (opened on line {opening.line}).")
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

    def consume(self, kind, message):
        if self.match(kind):
            return self.previous()
        raise self.error(message)

    def is_at_end(self):
        return self.peek().type is T.EOF

    def peek(self):
        return self.tokens[self.current]

    def previous(self):
        return self.tokens[self.current - 1]

    def advance(self):
        if not self.is_at_end():
            self.current += 1
        return self.previous()

    def error(self, message):
        token = self.peek()
        location = "at end" if token.type is T.EOF else f"at {token.lexeme!r}"
        return ParseError(f"[line {token.line}] Error {location}: {message}")

    def synchronize(self, start, in_block=False):
        """Preserve closing braces so recovery cannot move declarations outward."""
        if self.is_at_end():
            return
        if in_block and self.peek().type is T.RIGHT_BRACE:
            return
        if self.current > start:
            if self.previous().type is T.SEMICOLON:
                return
            if self.peek().type in (T.SAY, T.LET, T.LEFT_BRACE):
                return
            if self.peek().line > self.previous().line:
                return
        else:
            self.advance()  # Ensure progress even for an unmatched top-level '}'.
        while not self.is_at_end():
            if self.previous().type is T.SEMICOLON:
                return
            if self.peek().type in (T.SAY, T.LET, T.LEFT_BRACE):
                return
            if self.peek().type is T.RIGHT_BRACE:
                return
            if self.peek().line > self.previous().line:
                return
            self.advance()
# --- end AI code ---
