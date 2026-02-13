import sys
from pathlib import Path
import pytest

# Search upwards for calculator.py
current = Path(__file__).resolve()
for parent in current.parents:
    if (parent / "calculator.py").exists():
        sys.path.insert(0, str(parent))
        break

from calculator import Calculator


class TestCalculatorFailures:

    def test_always_fail(self):
        """Guaranteed failure."""
        assert 1 == 2

    def test_clear_wrong_expectation(self):
        calc = Calculator()
        calc.current_expression = "123"
        calc.total_expression = "456"
        calc.clear()

        # Intentionally wrong expectations
        assert calc.current_expression == "123"
        assert calc.total_expression == "456"

    def test_evaluate_wrong_result(self):
        calc = Calculator()
        calc.current_expression = "2+2"
        calc.total_expression = "0"
        calc.evaluate()

        assert calc.current_expression == "10"

    def test_square_wrong_result(self):
        calc = Calculator()
        calc.current_expression = "5"
        calc.square()

        assert calc.current_expression == "100"

    def test_sqrt_wrong_result(self):
        calc = Calculator()
        calc.current_expression = "16"
        calc.sqrt()

        assert calc.current_expression == "10"

    def test_force_exception(self):
        calc = Calculator()

        with pytest.raises(ZeroDivisionError):
            calc.current_expression = "10/0"
            calc.evaluate()
