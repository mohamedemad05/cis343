"""Evaluate Ember expressions and execute statements."""

from environment import EmberRuntimeError, Environment
from expr import Assign, Binary, Grouping, Literal, Unary, Variable
from stmt import BlockStmt, ExpressionStmt, PrintStmt, VarStmt
from tokens import TokenType as T

# --- start AI code ---
class Interpreter:
    def __init__(self):
        self.environment = Environment()

    def execute(self, statements):
        for statement in statements:
            if isinstance(statement, ExpressionStmt):
                self.evaluate(statement.expression)
            elif isinstance(statement, PrintStmt):
                print(self.stringify(self.evaluate(statement.expression)))
            elif isinstance(statement, VarStmt):
                self.environment.declare(statement.name)
                try:
                    value = (None if statement.initializer is None
                             else self.evaluate(statement.initializer))
                except Exception:
                    # Failed declarations must not poison a later prompt submission.
                    del self.environment.values[statement.name.lexeme]
                    raise
                self.environment.values[statement.name.lexeme] = value
            elif isinstance(statement, BlockStmt):
                previous = self.environment
                try:
                    self.environment = Environment(previous)
                    self.execute(statement.statements)
                finally:
                    self.environment = previous
            else:
                raise EmberRuntimeError("Unsupported statement.")

    def evaluate(self, expression):
        if isinstance(expression, Variable):
            return self.environment.get(expression.name)
        if isinstance(expression, Assign):
            value = self.evaluate(expression.value)
            self.environment.assign(expression.name, value)
            return value
        if isinstance(expression, Literal):
            return expression.value
        if isinstance(expression, Grouping):
            return self.evaluate(expression.expression)
        if isinstance(expression, Unary):
            value = self.evaluate(expression.right)
            if expression.operator.type is T.BANG:
                return not self.truthy(value)
            if expression.operator.type is T.MINUS:
                self.require_number(value, expression.operator)
                return -value
        if isinstance(expression, Binary):
            left = self.evaluate(expression.left)
            kind = expression.operator.type
            if kind is T.AND:
                return self.evaluate(expression.right) if self.truthy(left) else left
            if kind is T.OR:
                return left if self.truthy(left) else self.evaluate(expression.right)
            right = self.evaluate(expression.right)
            if kind is T.EQUAL_EQUAL:
                return self.equal(left, right)
            if kind is T.BANG_EQUAL:
                return not self.equal(left, right)
            if kind is T.PLUS and isinstance(left, str) and isinstance(right, str):
                return left + right
            self.require_number(left, expression.operator)
            self.require_number(right, expression.operator)
            if kind is T.PLUS:
                return left + right
            if kind is T.MINUS:
                return left - right
            if kind is T.STAR:
                return left * right
            if kind is T.SLASH:
                if right == 0:
                    raise EmberRuntimeError(f"[line {expression.operator.line}] Division by zero.")
                return left / right
            if kind is T.PERCENT:
                if right == 0:
                    raise EmberRuntimeError(f"[line {expression.operator.line}] Modulo by zero.")
                return left % right
            if kind is T.LESS:
                return left < right
            if kind is T.LESS_EQUAL:
                return left <= right
            if kind is T.GREATER:
                return left > right
            if kind is T.GREATER_EQUAL:
                return left >= right
        raise EmberRuntimeError("Unsupported expression.")

    @staticmethod
    def truthy(value):
        return value is not None and value is not False

    @staticmethod
    def equal(left, right):
        # Keep boolean and numeric semantics distinct, unless explicitly coerced.
        return type(left) is type(right) and left == right

    @staticmethod
    def require_number(value, operator):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise EmberRuntimeError(f"[line {operator.line}] Operator {operator.lexeme!r} needs numbers.")

    @staticmethod
    def stringify(value):
        if value is None:
            return "nil"
        if isinstance(value, bool):
            return "true" if value else "false"
        if isinstance(value, float):
            return str(int(value)) if value.is_integer() else str(value)
        return str(value)
# --- end AI code ---
