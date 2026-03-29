"""Tests for custom error types."""

from __future__ import annotations

import pytest

from calculator.errors import CalculatorError, DivisionByZeroError, InvalidInputError


class TestErrorHierarchy:
    """Verify the exception inheritance chain."""

    def test_calculator_error_is_exception(self) -> None:
        assert issubclass(CalculatorError, Exception)

    def test_invalid_input_is_calculator_error(self) -> None:
        assert issubclass(InvalidInputError, CalculatorError)

    def test_division_by_zero_is_calculator_error(self) -> None:
        assert issubclass(DivisionByZeroError, CalculatorError)


class TestErrorMessages:
    """Verify default and custom messages."""

    def test_calculator_error_default_message(self) -> None:
        err = CalculatorError()
        assert err.message == "Calculator error"
        assert str(err) == "Calculator error"

    def test_calculator_error_custom_message(self) -> None:
        err = CalculatorError("custom")
        assert err.message == "custom"

    def test_invalid_input_default_message(self) -> None:
        err = InvalidInputError()
        assert "Invalid input" in err.message

    def test_invalid_input_custom_message(self) -> None:
        err = InvalidInputError("bad value")
        assert err.message == "bad value"

    def test_division_by_zero_default_message(self) -> None:
        err = DivisionByZeroError()
        assert "zero" in err.message.lower()

    def test_division_by_zero_custom_message(self) -> None:
        err = DivisionByZeroError("nope")
        assert err.message == "nope"


class TestErrorCatching:
    """Verify that specific errors can be caught by their base class."""

    def test_catch_invalid_input_as_calculator_error(self) -> None:
        with pytest.raises(CalculatorError):
            raise InvalidInputError("test")

    def test_catch_division_by_zero_as_calculator_error(self) -> None:
        with pytest.raises(CalculatorError):
            raise DivisionByZeroError("test")
