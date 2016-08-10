#!/usr/bin/env python3
"""Project Euler, Problem 47."""
from itertools import count


def prime_factors(n):
    """Return the unique prime factors of n."""
    primes = set()
    if n % 2 == 0:
        primes.add(2)

    d = 3
    tmp = n
    while d * d <= tmp:
        if tmp % d == 0:
            primes.add(d)
            tmp //= d
        else:
            d += 2

    if tmp > 1:
        primes.add(tmp)

    return primes


if __name__ == '__main__':
    for n in count(start=1):
        if all([len(prime_factors(n + x)) == 4 for x in range(4)]):
            print(n)
            break
