"""Basic arithmetic helpers used by the sample test repo."""


def add(left: int | float, right: int | float) -> int | float:
    """Return the sum of two numbers."""
    return left + right


def subtract(left: int | float, right: int | float) -> int | float:
    """Return the difference of two numbers."""
    return left - right


def multiply(left: int | float, right: int | float) -> int | float:
    """Return the product of two numbers."""
    return left * right


def divide(left: int | float, right: int | float) -> float:
    """Return the quotient of two numbers.

    Raises:
        ZeroDivisionError: If `right` is 0.
    """
    if right == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return left / right
