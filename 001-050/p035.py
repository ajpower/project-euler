#!/usr/bin/env python3
"""Project Euler, Problem 35.

Any potential circular prime (with more than a single digit) can be composed
only of the digits 1, 3, 7, and 9; otherwise, at least one of the rotations
of the number would produce an even integer or a multiple of 5.

Begin by generating all two digit numbers formed from the above 4 digits. Find
the rotations of each one and check their primality to verify if the number is
a circular prime. Then move to three digits, then four, etc. until all 6 digit
numbers have been checked.
"""
from itertools import product


def is_prime(n):
    """Return True if the given number is prime."""
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


def rotations(n, d):
    """Return a list of all rotations of n with number of digits d in base 10.
    """
    rotations = []
    for _ in range(d):
        n = (n % 10 ** (d - 1)) * 10 + (n // 10 ** (d - 1))
        rotations.append(n)

    return rotations


def is_circular_prime(n, d):
    """Return True if n with number of digits d in base 10 is a circular prime.
    """
    return all(is_prime(r) for r in rotations(n, d))


if __name__ == '__main__':
    circular_primes = [2, 3, 5, 7]
    allowed_digits = ['1', '3', '7', '9']

    for num_digits in range(2, 7):
        for num_tuple in product(allowed_digits, repeat=num_digits):
            num = int(''.join(num_tuple))
            if is_circular_prime(num, num_digits):
                circular_primes.append(num)

    print(len(circular_primes))
