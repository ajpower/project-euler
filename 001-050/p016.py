#!/usr/bin/env python3
"""Project Euler, Problem 16

Brute force solution.
"""
N = 1000


def main():
    """Print the sum of digits in 2^N.
    """
    power = 2**N
    digit_sum = 0
    while (power != 0):
        digit = power % 10
        digit_sum += digit
        power = power // 10

    print(digit_sum)


if __name__ == "__main__":
    main()
