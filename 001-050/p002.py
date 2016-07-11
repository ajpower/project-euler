#!/usr/bin/env python3
"""Project Euler, Problem 2."""
import math

LARGEST_FIB = 4000000


def fib_gen(max_fib=math.inf):
    """Generate elements of the Fibonacci sequence."""
    a, b = 0, 1
    while a <= max_fib:
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    sum_even_fibs = 0
    for n in fib_gen(LARGEST_FIB):
        if n % 2 == 0:
            sum_even_fibs += n

    print(sum_even_fibs)
