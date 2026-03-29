"""Tests for pi_calc.pi module."""

from pi_calc.pi import compute_pi, pi_digits


def test_compute_pi_default():
    """Default iterations should approximate pi to within 0.001."""
    result = compute_pi()
    assert abs(result - 3.14159) < 0.001


def test_compute_pi_few_iterations():
    """Even a few iterations should produce a result in the right ballpark."""
    result = compute_pi(iterations=10)
    assert 2.5 < result < 4.0


def test_pi_digits_count():
    """pi_digits should return exactly n digits."""
    digits = pi_digits(5)
    assert len(digits) == 5


def test_pi_digits_values():
    """First 9 digits of pi after the decimal should match known values."""
    digits = pi_digits(9)
    assert digits == [1, 4, 1, 5, 9, 2, 6, 5, 3]
