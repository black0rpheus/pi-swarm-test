"""Core pi calculation functions."""

import math


def compute_pi(iterations: int = 1_000_000) -> float:
    """Approximate pi using the Leibniz formula.

    Args:
        iterations: Number of iterations for the approximation.
            Higher values yield better accuracy.

    Returns:
        Approximated value of pi.
    """
    approximation = 0.0
    for i in range(iterations):
        term = (-1) ** i / (2 * i + 1)
        approximation += term
    return 4 * approximation


def pi_digits(n: int) -> list[int]:
    """Return the first *n* decimal digits of pi.

    Args:
        n: Number of decimal digits to return.

    Returns:
        List of integer digits (does not include the leading 3).
    """
    pi_str = f"{math.pi:.{n + 10}f}"  # extra precision for safety
    # Skip "3." prefix
    return [int(d) for d in pi_str[2 : 2 + n]]
