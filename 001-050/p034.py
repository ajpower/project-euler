#!/usr/bin/env python3
"""Project Euler, Problem 34.

An upper bound for the largest number that equals the sum of the factorials of
its digits can be found by noting that every number larger than 9999999 cannot
have this property, as 1) 9999999 > 9!*9, and 2) the sum of the factorials of
the digits grows linearly with the number of digits, while the number itself
obviously grows exponentially with the number of digits. Hence it is only
necessary to check all numbers up to 9!*9.
"""
from math import factorial


def sum_digit_factorials(n):
    """Return the sum of the factorials of the digits of the given number."""
    # Pre-compute factorials.
    factorials = [factorial(i) for i in range(10)]

    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10

    return sum(factorials[digit] for digit in digits)


if __name__ == '__main__':
    print(sum(n for n in range(10, factorial(9) * 9) if
              n == sum_digit_factorials(n)))
