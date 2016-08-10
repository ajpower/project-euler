#!/usr/bin/env python3
"""Project Euler, Problem 41."""
from itertools import permutations
from sys import stderr


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


def digits2num(digits):
    """Return an integer produced by concatenating the given digits."""
    num = 0
    e = len(digits) - 1
    for d in digits:
        num += d * 10 ** e
        e -= 1

    return num


if __name__ == '__main__':
    # There are no 8-digit or 9-digit pandigital numbers, because such numbers
    # would be divisible by 3. Therefore we search for 7-digit pandigital
    # primes.

    digits = [d for d in range(7, 0, -1)]
    for permutation in permutations(digits):
        num = digits2num(permutation)
        if is_prime(num):
            print(num)
            break

    else:
        print("No 7-digit pandigital prime found.", file=stderr)
