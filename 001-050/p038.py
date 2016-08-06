#!/usr/bin/env python3
"""Project Euler, Problem 38"""


def num_digits(n):
    """Return the number of digits in base ten of the given number."""
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count


def is_pandigital(n):
    """Return True if n is a 1 to 9 pandigital number."""
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    n_str = str(n)
    return len(n_str) == 9 and all(digit in n_str for digit in digits)


if __name__ == '__main__':
    max_pandigital = 0

    # The base integer cannot be larger than 9999, or else it will not produce
    # a 9-digit number when concatenated with the products itself with 1, 2, ...
    for base in range(1, 10000):
        n, cat_product = 2, base
        while num_digits(cat_product) < 9:
            cat_product = str(cat_product) + str(base * n)
            cat_product = int(cat_product)
            n += 1
        if cat_product > max_pandigital and is_pandigital(cat_product):
            max_pandigital = cat_product

    print(max_pandigital)
