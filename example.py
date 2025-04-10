"""
This module provides utility functions for basic arithmetic operations.
"""

def add_numbers(a: float, b: float) -> float:
    """
    Add two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of the two numbers.
    """
    return a + b


def subtract_numbers(a: float, b: float) -> float:
    """
    Subtract one number from another.

    Args:
        a (float): The number to subtract from.
        b (float): The number to subtract.

    Returns:
        float: The result of the subtraction.
    """
    return a - b


def multiply_numbers(a: float, b: float) -> float:
    """
    Multiply two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The product of the two numbers.
    """
    return a * b


def divide_numbers(a: float, b: float) -> float:
    """
    Divide one number by another.

    Args:
        a (float): The dividend.
        b (float): The divisor.

    Returns:
        float: The result of the division.

    Raises:
        ValueError: If the divisor is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


if __name__ == "__main__":
    # Example usage
    print("Addition:", add_numbers(10, 5))
    print("Subtraction:", subtract_numbers(10, 5))
    print("Multiplication:", multiply_numbers(10, 5))
    print("Division:", divide_numbers(10, 5))
