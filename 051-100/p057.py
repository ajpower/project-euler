#!/usr/bin/env python3
"""Project Euler, Problem 57."""
from fractions import Fraction

ITERATIONS = 1000

if __name__ == '__main__':
    count = 0
    continued_fraction = Fraction(numerator=1, denominator=2)
    for _ in range(ITERATIONS - 1):
        continued_fraction = 1 / (2 + continued_fraction)
        root_two = 1 + continued_fraction
        if len(str(root_two.numerator)) > len(str(root_two.denominator)):
            count += 1

    print(count)
