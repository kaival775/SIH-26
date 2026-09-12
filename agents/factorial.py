#!/usr/bin/env python3
"""Calculate factorial values."""

def factorial(n):
    """Calculate factorial of n."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    print("Factorial calculations:")
    for i in range(1, 11):
        print(f"{i}! = {factorial(i)}")
    
    # Save to file
    with open('factorial_values.txt', 'w') as f:
        f.write("Factorial values:\n")
        for i in range(1, 11):
            f.write(f"{i}! = {factorial(i)}\n")
