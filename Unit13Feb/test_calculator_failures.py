import sys
from pathlib import Path
import pytest

# Add project root dynamically
PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from calculator import Calculator
