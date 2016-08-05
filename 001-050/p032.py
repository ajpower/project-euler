#!/usr/bin/env python3
"""Project Euler, Problem 32.

The left hand side must contain exactly five digits in total; otherwise the
total number of digits will not be nine. By symmetry, we need only consider
cases where the first number is one or two digits long.
"""


def is_pandigital_product(first, second):
    """Return true if the multiplicant/multiplier/product identity formed by

        first * second = product

    is 1 through 9 pandigital.
    """
    product = first * second
    all_digits = str(first) + str(second) + str(product)
    return len(all_digits) == 9 and all(
            str(digit) in all_digits for digit in range(1, 10))


if __name__ == '__main__':
    pandigital_products = {
        left * right for left in range(1, 99) for right in range(123, 9877) if
        is_pandigital_product(left, right)}
    print(sum(product for product in pandigital_products))
