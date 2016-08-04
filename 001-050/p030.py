#!/usr/bin/env python3
"""Project Euler, Problem 30.

Note that no number with more than 6 digits needs to be checked. This follows
from the fact that the largest possible sum of 7 digits to the power of 5 is
7*9^5, which is less than the smallest 7 digit number, 10^6.
"""


def sum_digits_to_power(n, p):
    """Return the sum of the digits of n each taken to the power of p."""
    return sum(int(digit) ** p for digit in str(n))


if __name__ == '__main__':
    answer = sum(n for n in range(2, 10 ** 6) if n == sum_digits_to_power(n, 5))
    print(answer)
