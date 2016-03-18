#!/usr/bin/env python3
"""Project Euler, Problem 27

For n^2 + an + b to be prime when n = 0, b must be prime as well. Additionally,
a must be odd; otherwise, the above equation will be even when n = 1.

To find the longest series of primes of the form n^2 + an + b, iterate over
all prime values of b and all odd values of a and brute force compute the number
of consecutive primes.
"""
A_MAX = 1000
B_MAX = 1000


def is_prime(n):
    """Return True if 'n' is prime.
    """
    if n < 2:
        return False

    d = 2
    while d**2 <= n:
        if n % d == 0:
            return False
        d += 1

    return True

def primes_upto(n):
    """Return a list of primes up to 'n'.
    """
    # sieve of Eratosthenes
    sieve = [True] * (n + 1)   # from 0 to n
    sieve[0] = False
    sieve[1] = False

    i = 0
    while i**2 <= n:
        if sieve[i]:
            for j in range(i+1, n+1):
                if j % i == 0:
                    sieve[j] = False

        i += 1

    return [p for p in range(n+1) if sieve[p]]

def consecutive_primes(a, b):
    """Return the number of consecutive primes of the form n^2 + an + b
    starting from n = 0.
    """
    consecutive_primes = 0
    n = 0
    while is_prime(n**2 + a*n + b):
        consecutive_primes += 1
        n += 1

    return consecutive_primes

def main():
    """Print the product of a and b that produces the longest consecutive
    number of primes of the form n^2 + an + b starting from n = 0.
    """
    max_consecutive_primes = 0
    max_product_ab = 0

    # b iterates overall all primes less than 'B_MAX'
    for b in primes_upto(B_MAX - 1):
        # a iterates over all odd numbers between -A_MAX + 1 and A_MAX + 1
        if A_MAX % 2 == 0:
            a_range = range(-A_MAX + 1, A_MAX, 2)
        else:
            a_range = range(-A_MAX + 2, A_MAX, 2)

        for a in a_range:
            temp = consecutive_primes(a, b)
            
            if temp > max_consecutive_primes:
                max_consecutive_primes = temp
                max_product_ab = a*b

    print(max_product_ab)


if __name__ == "__main__":
    main()
