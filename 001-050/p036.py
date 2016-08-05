#!/usr/bin/env python3
"""Project Euler, Problem 36."""
UPPER_BOUND = 1000000


def is_palindrome(num, base=10):
    """Return True if num is a palindrome in given base."""
    reverse = 0
    tmp = num
    while tmp > 0:
        reverse = reverse * base + tmp % base
        tmp //= base

    return num == reverse


if __name__ == '__main__':
    print(sum(n for n in range(UPPER_BOUND) if
              is_palindrome(n, base=2) and is_palindrome(n, base=10)))
