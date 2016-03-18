#!/usr/bin/env python3
"""Project Euler, Problem 20

Brute force solution.
"""
from math import factorial

N = 100


def main():
    """Print the sum of digits in N!.
    """
    N_fact = factorial(N)
    num_digits = len(str(N_fact))

    sum_digits = 0
    for i in range(num_digits - 1, -1, -1):
        sum_digits += N_fact // 10**i
        N_fact = N_fact % 10**i

    print(sum_digits)


if __name__ == "__main__":
    main()
