#!/usr/bin/env python3
"""Project Euler, Problem 9

Squaring both sides of the equation a + b + c = 1000 and substituting
Pythagoras' formula for c gives, after some simplification, the formula

    b = (500,000 - 1000a) / (1000 - a).

a can range from 1 to 999, so we simply need to iterate a over all possible
values until the above expression yields an integer.
"""
import sys


def main():
    """Print the product of Pythagorean triplets whose sum is equal to 1000.
    """
    for a in range(1, 1000):
        if (500000 - 1000*a) % (1000 - a) == 0:
            break
    else:
        print("No solution.")
        sys.exit(1)

    b = (500000 - 1000*a) // (1000 - a)
    c = int((a**2 + b**2)**(1/2))

    print(a*b*c)


if __name__ == "__main__":
    main()
