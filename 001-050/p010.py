#!/usr/bin/env python3
"""Project Euler, Problem 10.

Uses a sieve of Eratosthenes to find all prime numbers below N, which can then
be easily summed.
"""
N = 2000000


def primes(limit):
    """Return a list of all primes below limit."""
    sieve = limit * [True]
    sieve[0] = sieve[1] = False

    i = 0
    while i * i <= limit:
        if sieve[i]:
            for j in range(i * i, limit, i):
                sieve[j] = False

        i += 1

    return [p for (p, is_prime) in enumerate(sieve) if is_prime]


if __name__ == '__main__':
    answer = sum(primes(N))
    print(answer)
