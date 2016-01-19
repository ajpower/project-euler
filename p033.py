#!/usr/bin/env python3
"""Project Euler, Problem 33

It can be easily seen that the only fractions two digit numerators and
denominators that allow non-trivial digit cancellation have the form

    10n + i   x
    _______ = _ 
    10i + d   d

With some simple algebra this equation can be rewritten to

    9nd + id = 10ni

with n < d. It suffices to check the above equation for all possible cominations
of i, n, and d such that 1 <= i, n, d <= 9 and n < d.
"""
from fractions import gcd


def main():
    """Print the denominator of the product of all fractions with two digit
    numerators and denominators that allow non-trivial digit cancellation.
    """
    numerator_product = 1
    denominator_product = 1
    for i in range(1, 10):
        for d in range(1, 10):
            for n in range(1, d):
                if 9*n*d + i*d == 10*n*i:
                    numerator_product *= n
                    denominator_product *= d

    final_denominator = denominator_product //
                        gcd(numerator_product, denominator_product)
    print(final_denominator)


if __name__ == "__main__":
    main()
