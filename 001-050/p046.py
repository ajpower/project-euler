#!/usr/bin/env python3
"""Project Euler, Problem 46.

For each odd number, check if prime. If so, add to a running list of primes
(which starts with 2). If not prime, iterate over all primes so far discovered,
checking if (x - p) / 2 is a perfect square, where x and p are the number and
prime in question, respectively.
"""
from itertools import count
from math import sqrt


def is_prime(n):
    """Return True if and only if given number is prime."""
    if n < 2:
        return False

    if n != 2 and n % 2 == 0:
        return False

    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


if __name__ == '__main__':
    primes_below = [2]
    for n in count(start=3, step=2):
        if is_prime(n):
            primes_below.append(n)
        else:
            if not any(sqrt((n - p) // 2).is_integer() for p in primes_below):
                print(n)
                break
