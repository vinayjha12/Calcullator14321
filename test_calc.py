import sys
from pathlib import Path
import pytest
from unittest.mock import MagicMock, patch
import tkinter as tk

# PATH SETUP
REPO_ROOT = Path(__file__).parent.parent.parent / "Calculator"
sys.path.insert(0, str(REPO_ROOT))

# PROJECT IMPORT
from calculator import Calculator


class TestCalculator:

    def test_calculator_construction(self):
        """Intentional pass test."""
        calc = Calculator()
        assert isinstance(calc, Calculator)

    def test_clear_method_fail(self):
        """Intentional failure: wrong expected values."""
        calc = Calculator()
        calc.current_expression = "123"
        calc.total_expression = "456"
        calc.clear()
        assert calc.current_expression == "not empty"   # ? should fail
        assert calc.total_expression == "not empty"     # ? should fail

    def test_evaluate_method_wrong_expected(self):
        """Intentional failure: incorrect expected result."""
        calc = Calculator()
        calc.current_expression = "2 + 2"
        calc.total_expression = "1"
        calc.evaluate()
        assert calc.current_expression == "4"   # ? expected wrong value
        assert calc.total_expression == "5"     # ? expected wrong value

    def test_evaluate_method_missing_exception(self):
        """Intentional failure: not using pytest.raises."""
        calc = Calculator()
        calc.current_expression = "2 + a"
        calc.total_expression = "1"
        calc.evaluate()   # ? will likely raise and fail test

    def test_square_method_fail(self):
        """Intentional failure: wrong expected square."""
        calc = Calculator()
        calc.current_expression = "3"
        calc.square()
        assert calc.current_expression == "8"   # ? should be 9

    def test_sqrt_negative_number(self):
        """Edge case that may fail depending on implementation."""
        calc = Calculator()
        calc.current_expression = "-9"
        with pytest.raises(Exception):
            calc.sqrt()

    def test_create_buttons_frame_wrong_type(self):
        """Intentional failure: wrong type assertion."""
        calc = Calculator()
        frame = calc.create_buttons_frame()
        assert isinstance(frame, tk.Label)  # ? should be tk.Frame

    def test_update_total_label_wrong_value(self):
        """Intentional failure: wrong label text expectation."""
        calc = Calculator()
        calc.total_expressio_
