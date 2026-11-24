"""Lexically nested variable bindings and their runtime diagnostics."""

# --- start AI code ---
from tokens import Token


class EmberRuntimeError(Exception):
    """A source-level error, displayed without a Python traceback."""


UNINITIALIZED = object()


class Environment:
    def __init__(self, enclosing=None):
        self.enclosing = enclosing
        self.values = {}

    def declare(self, name: Token):
        if name.lexeme in self.values:
            raise EmberRuntimeError(
                f"[line {name.line}] Variable {name.lexeme!r} is already declared in this scope."
            )
        self.values[name.lexeme] = UNINITIALIZED

    def resolve(self, name: Token):
        environment = self
        while environment is not None:
            if name.lexeme in environment.values:
                if environment.values[name.lexeme] is UNINITIALIZED:
                    raise EmberRuntimeError(
                        f"[line {name.line}] Cannot access variable {name.lexeme!r} in its own initializer."
                    )
                return environment
            environment = environment.enclosing
        raise EmberRuntimeError(f"[line {name.line}] Undefined variable {name.lexeme!r}.")

    def get(self, name: Token):
        return self.resolve(name).values[name.lexeme]

    def assign(self, name: Token, value):
        self.resolve(name).values[name.lexeme] = value
# --- end AI code ---
