#!/usr/bin/env python3
"""Project Euler, Problem 5

Finds the prime factors for every number from 1 to 20, collects the prime
factors that have the largest power, and multiplies those together.
"""
from p003 import prime_factors

N = 20


def main():
    """Print the smallest positive number evenly divisible by all numbers from
    1 to N.
    """
    highest_power_primes = []

    for n in range(2, N+1):
        factors = prime_factors(n)
        unique_factors = set(factors)

        for prime in unique_factors:
            a = factors.count(prime)
            b = highest_power_primes.count(prime)

            if a > b:
                highest_power_primes += [prime]*(a-b)

    answer = 1
    for prime in highest_power_primes:
        answer *= prime

    print(answer)


if __name__ == "__main__":
    main()
