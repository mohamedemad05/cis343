"""Statement AST nodes for the Ember language."""

from dataclasses import dataclass
from expr import Expr
from tokens import Token

# --- start AI code ---
class Stmt:
    pass


@dataclass(frozen=True)
class ExpressionStmt(Stmt):
    expression: Expr


@dataclass(frozen=True)
class PrintStmt(Stmt):
    expression: Expr
# --- end AI code ---


# --- start AI code ---
@dataclass(frozen=True)
class VarStmt(Stmt):
    name: Token
    initializer: Expr | None


@dataclass(frozen=True)
class BlockStmt(Stmt):
    statements: list[Stmt]
# --- end AI code ---
