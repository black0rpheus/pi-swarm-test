"""Core calculator engine module.

Provides the Calculator class with basic arithmetic operations.
All methods accept int or float arguments and return float results.
"""


class Calculator:
    """A simple calculator engine supporting basic arithmetic operations.

    Each method performs a single arithmetic operation and returns the
    result as a float.  The ``divide`` method raises :class:`ValueError`
    when the divisor is zero.

    Examples
    --------
    >>> calc = Calculator()
    >>> calc.add(2, 3)
    5.0
    >>> calc.subtract(10, 4)
    6.0
    >>> calc.multiply(3, 7)
    21.0
    >>> calc.divide(10, 4)
    2.5
    """

    def add(self, a: int | float, b: int | float) -> float:
        """Return the sum of *a* and *b*.

        Parameters
        ----------
        a : int | float
            The first operand.
        b : int | float
            The second operand.

        Returns
        -------
        float
            The sum of *a* and *b*.
        """
        return float(a + b)

    def subtract(self, a: int | float, b: int | float) -> float:
        """Return the difference of *a* minus *b*.

        Parameters
        ----------
        a : int | float
            The minuend.
        b : int | float
            The subtrahend.

        Returns
        -------
        float
            The result of *a* - *b*.
        """
        return float(a - b)

    def multiply(self, a: int | float, b: int | float) -> float:
        """Return the product of *a* and *b*.

        Parameters
        ----------
        a : int | float
            The first factor.
        b : int | float
            The second factor.

        Returns
        -------
        float
            The product of *a* and *b*.
        """
        return float(a * b)

    def divide(self, a: int | float, b: int | float) -> float:
        """Return the quotient of *a* divided by *b*.

        Parameters
        ----------
        a : int | float
            The dividend.
        b : int | float
            The divisor.  Must not be zero.

        Returns
        -------
        float
            The result of *a* / *b*.

        Raises
        ------
        ValueError
            If *b* is zero.
        """
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return float(a / b)
