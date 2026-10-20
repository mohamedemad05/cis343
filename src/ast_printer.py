# --- start AI code ---
"""Print expression trees in parenthesized prefix notation."""

import math

from expr import Binary, Grouping, Literal, Unary


class AstPrinter:
    def print(self, expression):
        if isinstance(expression, Literal):
            return self.literal(expression.value)
        if isinstance(expression, Unary):
            return f"({expression.operator.lexeme} {self.print(expression.right)})"
        if isinstance(expression, Binary):
            left = self.print(expression.left)
            right = self.print(expression.right)
            return f"({expression.operator.lexeme} {left} {right})"
        if isinstance(expression, Grouping):
            return f"(group {self.print(expression.expression)})"
        raise TypeError(f"Unsupported expression type: {type(expression).__name__}")

    def literal(self, value):
        if value is None:
            return "null"
        # bool is a subclass of int in Python, so handle it before numbers.
        if isinstance(value, bool):
            return "true" if value else "false"
        if isinstance(value, str):
            escaped = (value.replace("\\", "\\\\").replace('"', '\\"')
                       .replace("\n", "\\n").replace("\r", "\\r").replace("\t", "\\t"))
            return '"' + escaped + '"'
        if isinstance(value, (int, float)):
            if isinstance(value, float) and not math.isfinite(value):
                raise ValueError("Number literals must be finite.")
            text = str(value)
            return text[:-2] if text.endswith(".0") else text
        raise TypeError(f"Unsupported literal type: {type(value).__name__}")
# --- end AI code ---
