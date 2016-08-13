#!/usr/bin/env python3
"""Project Euler, Problem 53."""
THRESHOLD = 1000000


def choose(n, k):
    """Return n choose k."""
    numerator, denominator = 1, 1
    for i in range(1, k + 1):
        numerator *= n + 1 - i
        denominator *= i

    return numerator // denominator


if __name__ == '__main__':
    results = sum(
            choose(n, k) > THRESHOLD for n in range(101) for k in range(n))
    print(results)
