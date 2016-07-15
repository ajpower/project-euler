#!/usr/bin/env python3
"""Project Euler, Problem 20."""
from math import factorial

N = 100

if __name__ == '__main__':
    sum_digits = sum(int(digit) for digit in str(factorial(N)))
    print(sum_digits)
