#!/usr/bin/env python3
"""Project Euler, Problem 14."""
from functools import lru_cache

N = 1000000


@lru_cache(maxsize=None)
def chain_length(n):
    """Return the length of the Collatz sequence starting from n."""
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + chain_length(n // 2)
    else:
        # If n is odd, then 3n + 1 is necessarily even so we can skip a step.
        return 2 + chain_length((3 * n + 1) // 2)


if __name__ == '__main__':
    max_length, starting_number = max((chain_length(n), n) for n in range(1, N))
    print(starting_number)
