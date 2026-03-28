"""Tests for the Calculator engine."""

from __future__ import annotations

import pytest

from calculator.engine import Calculator
from calculator.errors import DivisionByZeroError, InvalidInputError

# ── Fixtures ──────────────────────────────────────────────────────────────────


@pytest.fixture
def calc() -> Calculator:
    """Provide a fresh Calculator instance."""
    return Calculator()


# ── Addition ──────────────────────────────────────────────────────────────────


class TestAdd:
    """Tests for Calculator.add()."""

    def test_positive_integers(self, calc: Calculator) -> None:
        assert calc.add(2, 3) == 5.0

    def test_negative_integers(self, calc: Calculator) -> None:
        assert calc.add(-5, -3) == -8.0

    def test_mixed_signs(self, calc: Calculator) -> None:
        assert calc.add(10, -4) == 6.0

    def test_floats(self, calc: Calculator) -> None:
        assert calc.add(1.5, 2.5) == 4.0

    def test_int_and_float(self, calc: Calculator) -> None:
        assert calc.add(3, 0.14) == pytest.approx(3.14)

    def test_zero(self, calc: Calculator) -> None:
        assert calc.add(0, 0) == 0.0

    def test_large_numbers(self, calc: Calculator) -> None:
        assert calc.add(1_000_000, 2_000_000) == 3_000_000.0


# ── Subtraction ───────────────────────────────────────────────────────────────


class TestSubtract:
    """Tests for Calculator.subtract()."""

    def test_positive_result(self, calc: Calculator) -> None:
        assert calc.subtract(10, 4) == 6.0

    def test_negative_result(self, calc: Calculator) -> None:
        assert calc.subtract(3, 7) == -4.0

    def test_zero_result(self, calc: Calculator) -> None:
        assert calc.subtract(5, 5) == 0.0

    def test_floats(self, calc: Calculator) -> None:
        assert calc.subtract(5.5, 1.5) == 4.0

    def test_negative_operands(self, calc: Calculator) -> None:
        assert calc.subtract(-3, -7) == 4.0


# ── Multiplication ────────────────────────────────────────────────────────────


class TestMultiply:
    """Tests for Calculator.multiply()."""

    def test_positive_integers(self, calc: Calculator) -> None:
        assert calc.multiply(3, 7) == 21.0

    def test_by_zero(self, calc: Calculator) -> None:
        assert calc.multiply(5, 0) == 0.0

    def test_negative(self, calc: Calculator) -> None:
        assert calc.multiply(-2, 6) == -12.0

    def test_two_negatives(self, calc: Calculator) -> None:
        assert calc.multiply(-3, -4) == 12.0

    def test_floats(self, calc: Calculator) -> None:
        assert calc.multiply(2.5, 4.0) == 10.0

    def test_identity(self, calc: Calculator) -> None:
        assert calc.multiply(7, 1) == 7.0


# ── Division ──────────────────────────────────────────────────────────────────


class TestDivide:
    """Tests for Calculator.divide()."""

    def test_even_division(self, calc: Calculator) -> None:
        assert calc.divide(10, 2) == 5.0

    def test_float_result(self, calc: Calculator) -> None:
        assert calc.divide(7, 2) == 3.5

    def test_negative_dividend(self, calc: Calculator) -> None:
        assert calc.divide(-10, 2) == -5.0

    def test_negative_divisor(self, calc: Calculator) -> None:
        assert calc.divide(10, -2) == -5.0

    def test_both_negative(self, calc: Calculator) -> None:
        assert calc.divide(-10, -2) == 5.0

    def test_division_by_zero_raises(self, calc: Calculator) -> None:
        with pytest.raises(DivisionByZeroError, match="Cannot divide by zero"):
            calc.divide(10, 0)

    def test_zero_dividend(self, calc: Calculator) -> None:
        assert calc.divide(0, 5) == 0.0


# ── Input Validation ──────────────────────────────────────────────────────────


class TestInputValidation:
    """Tests for input validation across all operations."""

    @pytest.mark.parametrize("operation", ["add", "subtract", "multiply", "divide"])
    def test_string_first_operand(self, calc: Calculator, operation: str) -> None:
        method = getattr(calc, operation)
        with pytest.raises(InvalidInputError, match="Expected a numeric value"):
            method("hello", 2)  # type: ignore[arg-type]

    @pytest.mark.parametrize("operation", ["add", "subtract", "multiply", "divide"])
    def test_string_second_operand(self, calc: Calculator, operation: str) -> None:
        method = getattr(calc, operation)
        with pytest.raises(InvalidInputError, match="Expected a numeric value"):
            method(2, "world")  # type: ignore[arg-type]

    @pytest.mark.parametrize("operation", ["add", "subtract", "multiply", "divide"])
    def test_none_operand(self, calc: Calculator, operation: str) -> None:
        method = getattr(calc, operation)
        with pytest.raises(InvalidInputError):
            method(None, 2)  # type: ignore[arg-type]

    @pytest.mark.parametrize("operation", ["add", "subtract", "multiply", "divide"])
    def test_boolean_operand_rejected(self, calc: Calculator, operation: str) -> None:
        """bool is a subclass of int in Python — we explicitly reject it."""
        method = getattr(calc, operation)
        with pytest.raises(InvalidInputError, match="bool"):
            method(True, 2)  # type: ignore[arg-type]

    @pytest.mark.parametrize("operation", ["add", "subtract", "multiply", "divide"])
    def test_list_operand_rejected(self, calc: Calculator, operation: str) -> None:
        method = getattr(calc, operation)
        with pytest.raises(InvalidInputError):
            method([1, 2], 3)  # type: ignore[arg-type]
