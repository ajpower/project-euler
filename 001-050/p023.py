#!/usr/bin/env python3
"""Project Euler, Problem 23.

Find all abundant numbers less than 28124. Store the sum of every pair of
abundant numbers in a set and sum all numbers less than 28124 that are not in
this set.
"""
from itertools import combinations_with_replacement

LIMIT = 28124


def sum_divisors(n):
    """Return the sum of the proper divisors of n."""
    divisor_sum = 1  # Include 1 from the start.
    d = 2
    while d * d < n:
        if n % d == 0:
            divisor_sum += d
            divisor_sum += n // d
        d += 1

    # Explicit check if n is a perfect square.
    if d * d == n:
        divisor_sum += d

    return divisor_sum


if __name__ == '__main__':
    abundant_nums = [n for n in range(1, LIMIT) if sum_divisors(n) > n]
    sum_abundant_pairs = {n + m for n, m in
                          combinations_with_replacement(abundant_nums, 2)}
    answer = sum(n for n in range(1, LIMIT) if n not in sum_abundant_pairs)
    print(answer)
