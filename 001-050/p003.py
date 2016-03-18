#!/usr/bin/env python3
"""Project Euler, Problem 3

Uses a brute-force algorithm to compute the prime factors of n, taken from
http://stackoverflow.com/questions/23287/largest-prime-factor-of-a-number.
"""
NUMBER_TO_FACTOR = 600851475143


def prime_factor(n):
    """Return the prime factors of n.
    """
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        divisor += 1
        if divisor**2 > n:
            if n > 1:
                factors.append(n)
            break

    return factors

def main():
    """Print the largest prime factor of NUMBER_TO_FACTOR.
    """
    factors = prime_factor(NUMBER_TO_FACTOR)
    largest_prime_factor = max(factors)
    print(largest_prime_factor)


if __name__ == "__main__":
    main()
