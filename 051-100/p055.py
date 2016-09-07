#!/usr/bin/env python3
"""Project Euler, Problem 55."""
MAX_ITERATIONS = 50
LIMIT = 10000


def reverse(n):
    """Return the reverse of the digits in n in base 10."""
    return int(str(n)[::-1])


def palindrome(n):
    """Return True if number is a palindrome in base 10."""
    return str(n) == str(n)[::-1]


def lychrel(n):
    """Return True if number is a Lychrel number."""
    for _ in range(MAX_ITERATIONS):
        n += reverse(n)
        if palindrome(n):
            return False

    return True


if __name__ == '__main__':
    print(sum(lychrel(n) for n in range(LIMIT)))
