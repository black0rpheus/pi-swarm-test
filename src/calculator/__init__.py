"""Calculator — a simple arithmetic library."""

from calculator.engine import Calculator
from calculator.errors import CalculatorError, DivisionByZeroError, InvalidInputError

__version__ = "0.1.0"

__all__ = [
    "Calculator",
    "CalculatorError",
    "DivisionByZeroError",
    "InvalidInputError",
]
