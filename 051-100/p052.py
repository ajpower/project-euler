#!/usr/bin/env python3
"""Project Euler, Problem 52

Brute force solution based on the Counter collection. Micro-optimizations are possible, such as not iterating over all numbers for a given number of digits, but the current solution is fast enough.
"""
from collections import Counter


def digits(x):
    """Return a Counter object for all digits in x.
    """
    digits_counter = Counter()
    tmp = x
    while tmp > 0:
        digit = tmp % 10
        digits_counter[digit] += 1
        tmp //= 10

    return digits_counter


def main():
    x = 10
    while True:
        if all(digits(n*x) == digits(x) for n in range(2, 7)):
            print(x)
            return

        x += 1


if __name__ == "__main__":
    main()
