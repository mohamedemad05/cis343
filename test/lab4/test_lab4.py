"""Regression tests for Lab 4."""
# --- start AI code ---
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MAIN = ROOT / "src" / "main.py"
TESTS = ROOT / "test" / "lab4"


def run(filename):
    return subprocess.run([sys.executable, str(MAIN), str(TESTS / filename)],
                          cwd=ROOT, text=True, capture_output=True, check=False)


class Lab4Tests(unittest.TestCase):
    def test_required_success(self):
        result = run("statements.ember")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "one\ntrue\n3\nnil\n")
        self.assertEqual(result.stderr, "")

    def test_required_errors(self):
        result = run("errors.ember")
        self.assertEqual(result.returncode, 65)
        self.assertIn("Expected ';' after expression.", result.stderr)
        self.assertIn("Expected an expression.", result.stderr)

    def test_panic_mode_continues(self):
        result = run("recovery.ember")
        self.assertEqual(result.returncode, 65)
        self.assertEqual(result.stdout, "10\n20\n30\n")
        self.assertIn("Expected an expression.", result.stderr)

    def test_original_syntax(self):
        result = subprocess.run([sys.executable, str(MAIN)], input="say null;\n",
                                cwd=ROOT, text=True, capture_output=True)
        self.assertIn("null", result.stdout.replace("nil", "null"))


if __name__ == "__main__":
    unittest.main()
# --- end AI code ---
