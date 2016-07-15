#!/usr/bin/env python3
"""Project Euler, Problem 15.

It is necessary and sufficient to make N right turns and N downward turns to
reach the bottom right of the lattice. Hence there are 2N choose N paths from
the top left to the bottom right.
"""
from functools import reduce
from operator import mul

N = 20


def binomial(n, k):
    """Return n choose k."""
    k = min(k, n - k)

    if k < 0:
        return 0
    if k == 0:
        return 1

    numerator = reduce(mul, (n + 1 - i for i in range(1, k + 1)))
    denominator = reduce(mul, range(1, k + 1))
    return numerator // denominator


if __name__ == '__main__':
    print(binomial(2 * N, N))
