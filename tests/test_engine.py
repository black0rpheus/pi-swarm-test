"""Tests for the Calculator engine class."""

from __future__ import annotations

import pytest

from pi_calc.engine import Calculator


@pytest.fixture
def calc() -> Calculator:
    """Provide a fresh Calculator instance for each test."""
    return Calculator()


# ── add ──────────────────────────────────────────────────────────────────────


class TestAdd:
    def test_two_ints(self, calc: Calculator) -> None:
        assert calc.add(2, 3) == 5.0

    def test_int_and_float(self, calc: Calculator) -> None:
        assert calc.add(2, 3.5) == 5.5

    def test_two_floats(self, calc: Calculator) -> None:
        assert calc.add(1.1, 2.2) == pytest.approx(3.3)

    def test_negative_values(self, calc: Calculator) -> None:
        assert calc.add(-5, -3) == -8.0

    def test_zero(self, calc: Calculator) -> None:
        assert calc.add(0, 0) == 0.0

    def test_returns_float(self, calc: Calculator) -> None:
        result = calc.add(1, 2)
        assert isinstance(result, float)


# ── subtract ─────────────────────────────────────────────────────────────────


class TestSubtract:
    def test_two_ints(self, calc: Calculator) -> None:
        assert calc.subtract(10, 4) == 6.0

    def test_negative_result(self, calc: Calculator) -> None:
        assert calc.subtract(3, 7) == -4.0

    def test_float_result(self, calc: Calculator) -> None:
        assert calc.subtract(5.5, 2.5) == 3.0

    def test_returns_float(self, calc: Calculator) -> None:
        assert isinstance(calc.subtract(1, 0), float)


# ── multiply ─────────────────────────────────────────────────────────────────


class TestMultiply:
    def test_two_ints(self, calc: Calculator) -> None:
        assert calc.multiply(3, 7) == 21.0

    def test_by_zero(self, calc: Calculator) -> None:
        assert calc.multiply(99, 0) == 0.0

    def test_floats(self, calc: Calculator) -> None:
        assert calc.multiply(2.5, 4.0) == 10.0

    def test_negative(self, calc: Calculator) -> None:
        assert calc.multiply(-3, 5) == -15.0

    def test_returns_float(self, calc: Calculator) -> None:
        assert isinstance(calc.multiply(1, 1), float)


# ── divide ───────────────────────────────────────────────────────────────────


class TestDivide:
    def test_even_division(self, calc: Calculator) -> None:
        assert calc.divide(10, 2) == 5.0

    def test_float_result(self, calc: Calculator) -> None:
        assert calc.divide(10, 4) == 2.5

    def test_negative_divisor(self, calc: Calculator) -> None:
        assert calc.divide(10, -2) == -5.0

    def test_returns_float(self, calc: Calculator) -> None:
        assert isinstance(calc.divide(7, 2), float)

    def test_divide_by_zero_raises(self, calc: Calculator) -> None:
        with pytest.raises(ValueError, match="Division by zero"):
            calc.divide(10, 0)

    def test_divide_by_zero_message(self, calc: Calculator) -> None:
        """Ensure the error message is clear and actionable."""
        with pytest.raises(ValueError) as exc_info:
            calc.divide(5, 0)
        assert "zero" in str(exc_info.value).lower()
