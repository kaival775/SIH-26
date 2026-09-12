def fibonacci(n):
    """Generate the first n Fibonacci numbers."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
        return fib_sequence

# Generate and display Fibonacci sequence
n = 10
result = fibonacci(n)

print(f"First {n} Fibonacci numbers:")
print(result)

# Print with commas for readability
print(", ".join(map(str, result)))
