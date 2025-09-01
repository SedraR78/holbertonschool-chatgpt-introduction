#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # decrement to avoid infinite loop
    return result

# Check if an argument was provided
if len(sys.argv) < 2:
    print("Usage: ./factorial.py <number>")
    sys.exit(1)

try:
    num = int(sys.argv[1])
    if num < 0:
        print("Error: Factorial is not defined for negative numbers.")
        sys.exit(1)
except ValueError:
    print("Error: Please provide a valid integer.")
    sys.exit(1)

f = factorial(num)
print(f)
