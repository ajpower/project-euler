#!/usr/bin/env python3
"""Project Euler, Problem 36

Brute force solution.
"""
UPPER_BOUND = 1000000


def is_palindrome(num, base=10):
    """Return True if num is a palindrome in given base.
    """
    # Construct the reverse of num in given base and compare to original number.
    reverse = 0
    tmp = num
    while tmp > 0:
        reverse = reverse * base + tmp % base
        tmp //= base

    return num == reverse

def main():
    """Print the sum of all numbers below UPPER_BOUND that are palindromes in
    base 2 and base 10.
    """
    _sum = 0
    for n in range(UPPER_BOUND):
        if is_palindrome(n, base=2) and is_palindrome(n, base=10):
            _sum += n

    print(_sum)


if __name__ == "__main__":
    main()
