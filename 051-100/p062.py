#!/usr/bin/env python3
"""Project Euler, Problem 62."""
from collections import defaultdict

N = 5


def sorted_digits(n):
    """Return the digits of n in sorted order."""
    return str(sorted(str(n)))


if __name__ == '__main__':
    counter = defaultdict(lambda: set())
    n = 0
    while True:
        n += 1
        key = sorted_digits(n ** 3)
        counter[key].add(n ** 3)

        if len(counter[key]) == N:
            break

    print(min(counter[key]))
