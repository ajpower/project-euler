#!/usr/bin/env python3
"""Project Euler, Problem 46

For each odd number, check if prime. If so, add to a running list of primes
(which starts with 2). If not prime, iterate over all primes so far discovered,
checking if (x - p) / 2 is a perfect square, where x and p are the number and
prime in question, respectively.
"""
from math import sqrt


def is_prime(n):
    """Return True if and only if 'n' is prime.
    """
    if n <= 1:
        return False
    d = 2
    while d**2 <= n:
        if n % d == 0:
            return False
        d += 1
    return True

def main():
    n = 3
    primes = [2]
    while True:
        if is_prime(n):
            primes.append(n)
        else:
            goldbach_conjecture = False
            for p in primes:
                if sqrt((n - p) // 2).is_integer():
                    goldbach_conjecture = True
            if not goldbach_conjecture:
                print(n)
                return

        n += 2

if __name__ == "__main__":
    main()
