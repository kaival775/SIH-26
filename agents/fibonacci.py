#!/usr/bin/env python3
"""Generate a Fibonacci sequence script."""

def fibonacci(n):
    """Generate the first n Fibonacci numbers."""
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

if __name__ == "__main__":
    n = 20
    seq = fibonacci(n)
    print(f"First {n} Fibonacci numbers: {seq}")
    
    # Save to file
    with open('fibonacci_sequence.txt', 'w') as f:
        f.write(f"First {n} Fibonacci numbers:\n")
        f.write(str(seq) + "\n")
