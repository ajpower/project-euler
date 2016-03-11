#!/usr/bin/env python3
"""Project Euler, Problem 41

Brute force solution which iterates over all pandigital integers in decreasing
order. Starts with n = 7 as all pandigital integers with n = 8 or n = 9 are
multiples of 3.
"""
import itertools


def is_prime(n):
    """Return True if and only if 'n' is prime.
    """
    if n == 1:
        return False
    d = 2
    while d**2 <= n:
        if n % d == 0:
            return False
        d += 1
    return True

def digits2num(digits):
    """Return an integer produced by concatenating the digits in 'ditgits'.
    """
    num = 0
    e = len(digits) - 1
    for d in digits:
        num += d * 10**e
        e -= 1

    return num

def main():
    for n in range(7, 0, -1):
        digits = [d for d in range(n, 0, -1)]
        for permutation in itertools.permutations(digits):
            num = digits2num(permutation)
            if is_prime(num):
                print(num)
                return

    print("No pandigital prime found.")


if __name__ == "__main__":
    main()
