#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer using recursion.

    Args:
        n (int): The number for which the factorial is to be calculated.
                 Must be a non-negative integer.

    Returns:
        int: The factorial of the input number.

    Example:
        factorial(4) -> 24
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    # Check if the user provided an argument
    if len(sys.argv) < 2:
        print("Usage: ./factorial_recursive.py <non-negative integer>")
        sys.exit(1)

    try:
        num = int(sys.argv[1])
        if num < 0:
            print("Error: Factorial is not defined for negative numbers.")
            sys.exit(1)
    except ValueError:
        print("Error: Please provide a valid integer.")
        sys.exit(1)

    # Compute and print the factorial
    f = factorial(num)
    print(f)
