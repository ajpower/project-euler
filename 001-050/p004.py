#!/usr/bin/env python3
"""Project Euler, Problem 4

Brute force solution.
"""
def is_palindrome(n):
    """Determine whether n is a palindrome in base 10.
    """
    numeral = str(n)
    return numeral == numeral[::-1]

def palindromes():
    """Return all palindromes made from the product of two 3-digit numbers.
    """
    _palindromes = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            if is_palindrome(i*j):
                _palindromes.append(i*j)

    return _palindromes

def main():
    """Print the largest palindrome made from the product of two 3-digit
    numbers.
    """
    print(max(palindromes()))


if __name__ == "__main__":
    main()
