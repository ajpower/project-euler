#!/usr/bin/env python3
"""Project Euler, Problem 2

The Fibonacci sequence was generated and the sum of even elements below four
million was computed.
"""
LARGEST_FIB = 4000000


def fib_gen():
    """Generate elements of the Fibonacci sequence.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def main():
    """Print the sum of even Fibonacci numbers below LARGEST_FIB.
    """
    g = fib_gen()

    sum_even_fibs = 0
    fib = next(g)
    while fib < LARGEST_FIB:
        if fib % 2 == 0:
            sum_even_fibs += fib
        fib = next(g)

    print(sum_even_fibs)


if __name__ == "__main__":
    main()
