#!/usr/bin/env python3
"""Project Euler, Problem 45.

All odd-indexed triangle numbers -- and only odd-indexed triangle numbers -- are
hexagonal numbers as well. Hence it is necessary and sufficient to check every
odd-indexed triangular number to see if they are pentagonal numbers as well.
A number x will be pentagonal if

    sqrt(24x + 1) + 1
    -----------------
           6
is an integer.
"""
from math import sqrt


def triangle(n):
    """Return the triangle number with given index."""
    return n * (n + 1) // 2


def is_pentagonal(x):
    """Return True if and only if given number is pentagonal."""
    return sqrt(24 * x + 1).is_integer() and (sqrt(24 * x + 1) + 1) % 6 == 0


if __name__ == '__main__':
    # Start at n = 287, as that is the first odd index greater than the known
    # solution of 285.
    n = 287
    while True:
        if is_pentagonal(triangle(n)):
            print(triangle(n))
            break
        n += 2
