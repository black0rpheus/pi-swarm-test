"""Custom error types for the Calculator library.

Hierarchy::

    CalculatorError
    ├── InvalidInputError
    └── DivisionByZeroError
"""

from __future__ import annotations


class CalculatorError(Exception):
    """Base exception for all calculator-related errors."""

    def __init__(self, message: str = "Calculator error") -> None:
        self.message = message
        super().__init__(self.message)


class InvalidInputError(CalculatorError):
    """Raised when an input value is not a valid numeric type."""

    def __init__(self, message: str = "Invalid input: expected a numeric value") -> None:
        super().__init__(message)


class DivisionByZeroError(CalculatorError):
    """Raised when a division by zero is attempted."""

    def __init__(self, message: str = "Division by zero is not allowed") -> None:
        super().__init__(message)
