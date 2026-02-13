import sys
from pathlib import Path
import pytest
import tkinter as tk

# PATH SETUP
REPO_ROOT = Path(__file__).parent.parent.parent / "Calculator"
sys.path.insert(0, str(REPO_ROOT))

from calculator import Calculator


class TestCalculatorFailures:

    def test_always_fail(self):
        """Guaranteed failure test."""
        assert 100 == 200   # ? This will ALWAYS fail

    def test_clear_wrong_behavior(self):
        """Expect wrong values after clear()."""
        calc = Calculator()
        calc.current_expression = "999"
        calc.total_expression = "888"
        calc.clear()

        # These expectations are intentionally wrong
        assert calc.current_expression == "999"
        assert calc.total_expression == "888"

    def test_evaluate_incorrect_math(self):
        """Force incorrect math expectation."""
        calc = Calculator()
        calc.current_expression = "5 + 5"
        calc.total_expression = "0"
        calc.evaluate()

        # Wrong expected value
        assert calc.current_expression == "15"

    def test_square_wrong_result(self):
        """Wrong square result."""
        calc = Calculator()
        calc.current_expression = "4"
        calc.square()

        assert calc.current_expression == "12"

    def test_sqrt_wrong_result(self):
        """Wrong sqrt result."""
        calc = Calculator()
        calc.current_expression = "16"
        calc.sqrt()

        assert calc.current_expression == "5"

    def test_button_frame_wrong_type(self):
        """Check for wrong return type."""
        calc = Calculator()
        frame = calc.create_buttons_frame()

        assert isinstance(frame, tk.Button)  # ? Should not be Button

    def test_label_text_wrong_value(self):
        """Wrong label update expectation."""
        calc = Calculator()
        calc.current_expression = "12345"
        calc.update_label()

        assert calc.label.cget("text") == "WRONG_TEXT"

    def test_total_label_wrong_value(self):
        """Wrong total label expectation."""
        calc = Calculator()
        calc.total_expression = "7*7"
        calc.update_total_label()

        assert calc.total_label.cget("text") == "100"

    def test_force_exception(self):
        """Force an unexpected exception."""
        calc = Calculator()

        with pytest.raises(ZeroDivisionError):
            calc.current_expression = "10/0"
            calc.evaluate()
