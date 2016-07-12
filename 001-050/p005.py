#!/usr/bin/env python3
"""Project Euler, Problem 5.

Find the prime factors for every number from 1 to N, collect the prime factors
that have the largest power, and multiply those together.
"""
from collections import Counter
from functools import reduce
from operator import mul

N = 20


def prime_factor(n):
    """Return the prime factors of n."""
    factors = []
    divisor = 2

    while n >= divisor * divisor:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    if n > 1:
        factors.append(n)

    return factors


if __name__ == '__main__':
    prime_count = Counter()

    for n in range(N):
        factors = prime_factor(n)
        for p in factors:
            prime_power = factors.count(p)
            prime_count[p] = max(prime_count[p], prime_power)

    answer = reduce(mul, (p ** prime_count[p] for p in prime_count))

    print(answer)
