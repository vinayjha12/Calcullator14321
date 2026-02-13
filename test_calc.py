import sys
from pathlib import Path
import pytest
from unittest.mock import MagicMock, patch
import tkinter as tk

# PATH SETUP
REPO_ROOT = Path(__file__).parent.parent.parent / "Calculator"
sys.path.insert(0, str(REPO_ROOT))

# NOW ADD PROJECT-SPECIFIC IMPORTS
from calculator import Calculator  # Assuming the file is named calculator.py


class TestCalculator:
    def test_calculator_construction(self):
        """Test successful construction of the Calculator class."""
        calc = Calculator()
        assert isinstance(calc, Calculator)

    def test_clear_method(self):
        """Test the clear method."""
        calc = Calculator()
        calc.clear()
        assert calc.current_expression == ""
        assert calc.total_expression == ""

      @pytest.mark.xfail
def test_intentional_failure():
    calc = Calculator()
    assert 1 == 2

    def test_evaluate_method_valid_expression(self):
        """Test the evaluate method with a valid expression."""
        calc = Calculator()
        calc.current_expression = "2 + 2"
        calc.total_expression = "1"
        calc.evaluate()
        assert calc.current_expression == "5"
        assert calc.total_expression == "6"

    def test_evaluate_method_invalid_expression(self):
        """Test the evaluate method with an invalid expression."""
        calc = Calculator()
        calc.current_expression = "2 + a"
        calc.total_expression = "1"
        with pytest.raises(Exception):
            calc.evaluate()
        assert calc.current_expression == "Error"
        assert calc.total_expression == "1"

    def test_square_method(self):
        """Test the square method."""
        calc = Calculator()
        calc.current_expression = "3"
        calc.square()
        assert calc.current_expression == "9"

    def test_sqrt_method(self):
        """Test the sqrt method."""
        calc = Calculator()
        calc.current_expression = "9"
        calc.sqrt()
        assert calc.current_expression == "3.0"

    def test_create_buttons_frame_method(self):
        """Test the create_buttons_frame method."""
        calc = Calculator()
        frame = calc.create_buttons_frame()
        assert isinstance(frame, tk.Frame)

    def test_update_total_label_method(self):
        """Test the update_total_label method."""
        calc = Calculator()
        calc.total_expression = "1 + 2 * 3"
        calc.update_total_label()
        assert calc.total_label.cget("text") == "1 + 2 * 3"

    def test_update_label_method(self):
        """Test the update_label method."""
        calc = Calculator()
        calc.current_expression = "123456789012"
        calc.update_label()
        assert calc.label.cget("text") == "12345678901"