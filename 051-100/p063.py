#!/usr/bin/env python3
"""Project Euler, Problem 63.

It is impossible for an n-digit number to be equal to an nth power when n
exceeds N such that

    9 ^ N < 10 ^ (N - 1),

which occurs when N >= 22.
"""
from math import ceil, log


def num_digits(n):
    return ceil(log(n + 1, 10))


if __name__ == '__main__':
    count = sum(
        num_digits(b ** n) == n for n in range(1, 22) for b in range(1, 10))
    print(count)
