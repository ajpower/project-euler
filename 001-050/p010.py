#!/usr/bin/env python3
"""Project Euler, Problem 10

Uses a sieve of Eratosthenes to find all prime numbers below N, which can then
be easily summed.
"""
from math import sqrt

N = 2000000


def sieve(n):
    """Return a list of all primes less than or equal to n.
    """
    _sieve = [False] + [False] + (n-1)*[True]

    divisor = 2
    while divisor <= sqrt(n):
        if _sieve[divisor]:
            for k in range(divisor**2, n+1):
                if k % divisor == 0:
                    _sieve[k] = False

        divisor += 1

    primes = [i for i in range(len(_sieve)) if _sieve[i]]
    return primes

def main():
    """Find sum of all prime numbers below N.
    """
    primes = sieve(N)
    sum_primes = sum(primes)
    print(sum_primes)


if __name__ == "__main__":
    main()
