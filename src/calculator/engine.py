"""Core Calculator engine with four arithmetic operations."""

from __future__ import annotations

from calculator.errors import DivisionByZeroError, InvalidInputError


class Calculator:
    """A simple calculator supporting add, subtract, multiply, and divide.

    Each method validates its inputs and raises descriptive errors on failure.
    The calculator is stateless — each call is independent.
    """

    @staticmethod
    def _validate_numeric(value: float | int, name: str = "value") -> None:
        """Ensure a value is a real number (int or float).

        Args:
            value: The value to validate.
            name: Parameter name used in error messages.

        Raises:
            InvalidInputError: If *value* is not an int or float.
        """
        if not isinstance(value, (int, float)):
            raise InvalidInputError(
                f"Expected a numeric value for '{name}', got {type(value).__name__}"
            )
        if isinstance(value, bool):
            # bool is a subclass of int in Python — reject it explicitly
            raise InvalidInputError(f"Expected a numeric value for '{name}', got bool")

    def add(self, a: float | int, b: float | int) -> float:
        """Return the sum of *a* and *b*.

        Args:
            a: First operand.
            b: Second operand.

        Returns:
            The sum as a float.

        Raises:
            InvalidInputError: If either operand is not numeric.
        """
        self._validate_numeric(a, "a")
        self._validate_numeric(b, "b")
        return float(a + b)

    def subtract(self, a: float | int, b: float | int) -> float:
        """Return *a* minus *b*.

        Args:
            a: Minuend.
            b: Subtrahend.

        Returns:
            The difference as a float.

        Raises:
            InvalidInputError: If either operand is not numeric.
        """
        self._validate_numeric(a, "a")
        self._validate_numeric(b, "b")
        return float(a - b)

    def multiply(self, a: float | int, b: float | int) -> float:
        """Return the product of *a* and *b*.

        Args:
            a: First factor.
            b: Second factor.

        Returns:
            The product as a float.

        Raises:
            InvalidInputError: If either operand is not numeric.
        """
        self._validate_numeric(a, "a")
        self._validate_numeric(b, "b")
        return float(a * b)

    def divide(self, a: float | int, b: float | int) -> float:
        """Return *a* divided by *b*.

        Args:
            a: Dividend.
            b: Divisor.

        Returns:
            The quotient as a float.

        Raises:
            InvalidInputError: If either operand is not numeric.
            DivisionByZeroError: If *b* is zero.
        """
        self._validate_numeric(a, "a")
        self._validate_numeric(b, "b")
        if b == 0:
            raise DivisionByZeroError("Cannot divide by zero")
        return float(a / b)
