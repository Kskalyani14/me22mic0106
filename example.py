"""
This module provides a simple example of a Python script
that adheres to linting rules and PEP 8 standards.
"""

def greet(name: str) -> str:
    """
    Returns a greeting message for the given name.

    Args:
        name (str): The name to greet.

    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"


def main():
    """
    Main function to demonstrate the greet function.
    """
    name = "World"
    message = greet(name)
    print(message)


if __name__ == "__main__":
    main()
