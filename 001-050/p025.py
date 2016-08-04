#!/usr/bin/env python3
"""Project Euler, Problem 25."""
NUM_DIGITS = 1000


def fib():
    """Yield the next Fibonacci number."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    index = next(i for i, n in enumerate(fib()) if len(str(n)) >= NUM_DIGITS)
    print(index)
