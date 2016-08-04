#!/usr/bin/env python3
"""Project Euler, Problem 27."""
from itertools import count

A_LIMIT = 1000
B_LIMIT = 1001


def prime(n):
    """Return True if n is prime."""
    if n < 2:
        return False

    if n > 2 and n % 2 == 0:
        return False

    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2

    return True


def primes_below(n):
    """Return all primes less than n."""
    sieve = [True] * n
    sieve[0] = sieve[1] = False

    i = 2
    while i * i <= n:
        if sieve[i]:
            for j in range(i * i, n, i):
                sieve[j] = False
        i += 1

    return [p for p, is_prime in enumerate(sieve) if is_prime]


def consecutive_primes(a, b):
    """Return the number of consecutive primes of the form n^2 + an + b
    starting from n = 0.
    """
    return next(n for n in count() if not prime(n * n + a * n + b))


if __name__ == '__main__':
    max_consecutive_primes, product = max(
        (consecutive_primes(a, b), a * b) for a in range(-A_LIMIT + 1, A_LIMIT)
        for b in primes_below(B_LIMIT))
    print(product)
