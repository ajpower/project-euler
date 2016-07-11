#!/usr/bin/env python3
"""Project Euler, Problem 4."""


def palindrome(n):
    """Determine whether n is a palindrome in base 10."""
    numeral = str(n)
    return numeral == numeral[::-1]


if __name__ == '__main__':
    palindromes = [n * m for n in range(100, 1000) for m in range(100, 1000) if
                   palindrome(n * m)]
    print(max(palindromes))
