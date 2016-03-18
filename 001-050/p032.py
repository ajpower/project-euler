#!/usr/bin/env python3
"""Project Euler, Problem 32

The left hand side must contain exactly five digits in total; otherwise the
total number of digits will not be nine. By symmetry, we need only consider
cases where the first number is one or two digits long. The left hand side of
the identity can be formed by finding all permuations of 5 digits. Checking
whether the resulting multiplicant/multiplier/product identity is 1 through 9
pandigitial amounts to checking whether the resulting product is a subset of
the remaining digits.
"""
from itertools import permutations


def is_pandigital(first, second):
    """Return true if the multiplicant/multiplier/product identity formed by
        first * second = product
    is 1 through 9 pandigital. first and second are of type string.
    """
    # determine the remaining digits that must form the product of 'first' and
    # 'second'.
    remaining_digits = {str(i) for i in range(1, 10)}
    for digit in first + second:
        remaining_digits.remove(digit)

    product = str(int(first) * int(second))

    # permutations returns a tuple, so convert product into tuple and see if in
    # permuations of remaining_digits
    return tuple(product) in permutations(remaining_digits)

def main():
    """Print the sum of unique products that can be formed by a multiplicant/
    multiplier/product identity that is 1 through 9 pandigital.
    """
    digits = "123456789"
    pandigital_products = set()
    sum_pandigital_products = 0

    # first number on left hand side has a single digit.
    for left_hand_side in permutations(digits, 5):
        first = left_hand_side[4]
        second = left_hand_side[3] + left_hand_side[2] + left_hand_side[1] + left_hand_side[0]

        product = int(first) * int(second)

        # check if resulting identity is pandigital and that product is unique.
        if is_pandigital(first, second) and not product in pandigital_products:
            pandigital_products.add(product)
            sum_pandigital_products += product

    # first number on left hand side has a single digit.
    for left_hand_side in permutations(digits, 5):
        first = left_hand_side[4] + left_hand_side[3]
        second = left_hand_side[2] + left_hand_side[1] + left_hand_side[0]

        product = int(first) * int(second)

        # check if resulting identity is pandigital and that product is unique.
        if is_pandigital(first, second) and not product in pandigital_products:
            pandigital_products.add(product)
            sum_pandigital_products += product

    print(sum_pandigital_products)


if __name__ == "__main__":
    main()
