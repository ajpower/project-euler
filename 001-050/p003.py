#!/usr/bin/env python3
"""Project Euler, Problem 3.

Uses a brute-force algorithm to compute the prime factors of n, taken from
http://stackoverflow.com/questions/23287/largest-prime-factor-of-a-number.
"""
NUMBER_TO_FACTOR = 600851475143


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
    factors = prime_factor(NUMBER_TO_FACTOR)
    print(max(factors))
