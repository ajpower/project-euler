#!/usr/bin/env python3
"""Project Euler, Problem 52."""
from collections import Counter
from itertools import count


def digits(x):
    """Return a Counter object for all digits in x."""
    digits_counter = Counter()
    tmp = x
    while tmp > 0:
        digit = tmp % 10
        digits_counter[digit] += 1
        tmp //= 10

    return digits_counter


if __name__ == '__main__':
    for x in count(start=1):
        if all(digits(n * x) == digits(x) for n in range(2, 7)):
            print(x)
            break
