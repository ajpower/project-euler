#!/usr/bin/env python3
"""Project Euler, Problem 34

An upper bound for the largest number that equals the sum of the factorials of
its digits can be found by noting that every number larger than 9999999 cannot
have this property, as 1) 9999999 > 9!*9, and 2) the sum of the factorials of
the digits grows linearly with the number of digits, while the number itself
obviously grows exponentially with the number of digits. Hence it is only
necessary to check all numbers up to 9!*9.
"""
from math import factorial


def sum_digit_factorials(n):
    """Return the sum of the factorials of the digits of 'n'.
    """
    # pre-compute factorials
    factorials = [factorial(i) for i in range(10)]

    _sum = 0
    tmp = n # as the factorial of each digit is computed, tmp will be divided
            # by ten. When tmp equals 0, there are no more digits to evaluate.
    while tmp != 0:
        _sum += factorials[(tmp % 10)]
        tmp //= 10

    return _sum

def main():
    """Print the sum of all numbers that are equal to the sum of the factorials
    of their digits.
    """
    # iterate over all positive integers up to 9!*7, ignoring 1 and 2 because
    # they are the only two integers that equal their factorials, and by the
    # definition of the problem they are excluded.
    _sum = 0
    for n in range(3, factorial(9)*7):
        if n == sum_digit_factorials(n):
            _sum += n

    print(_sum)


if __name__ == "__main__":
    main()
