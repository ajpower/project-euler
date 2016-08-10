#!/usr/bin/env python3
"""Project Euler, Problem 40."""
from functools import reduce
from operator import mul


def d(n):
    """Return the nth digit of Champernowne's constant."""
    # The largest value of n such that d_n is part of an m digit number is given
    # by 9*1 + 90*2 + 900*3 + ... + 9*10^(m-1)*(m).
    num_digits, tmp = 0, 0
    while tmp < n:
        num_digits += 1
        tmp += 9 * 10 ** (num_digits - 1) * num_digits

    num, remaining_digits = 0, n
    for i in range(1, num_digits):
        num += 9 * 10 ** (i - 1)
        remaining_digits -= 9 * 10 ** (i - 1) * i
    num += (remaining_digits - 1) // num_digits + 1

    digit_pos = num_digits - (remaining_digits - 1) % num_digits
    return num // 10 ** (digit_pos - 1) % 10


if __name__ == '__main__':
    result = reduce(mul, (d(10 ** e) for e in range(7)))
    print(result)
