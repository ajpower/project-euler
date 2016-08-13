#!/usr/bin/env python3
"""Project Euler, Problem 50."""
import itertools as iter
import sys


def prime(n):
    """Return True if given number is prime."""
    if n <= 1:
        return False

    if n != 2 and n % 2 == 0:
        return False

    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2

    return True


def primes_below(n):
    """Return a list of all primes below n."""
    sieve = [True] * n
    sieve[0], sieve[1] = False, False

    i = 2
    while i * i <= n:
        if sieve[i]:
            for j in range(i * i, n, i):
                sieve[j] = False
        i += 1

    return [p for p, is_prime in enumerate(sieve) if is_prime]


if __name__ == '__main__':
    # The sum of the first 10^4 primes exceeds 10^6.
    primes = primes_below(10000)

    # The ith element of prime_sums contains the sum of the first i primes,
    # provided that the sum is below 10^6.
    prime_sums = [0]
    for consecutive_sum in iter.accumulate(primes):
        if consecutive_sum >= 1000000:
            break
        prime_sums.append(consecutive_sum)
    else:
        print('Error: insufficient number of primes computed.', file=sys.stderr)

    max_terms, max_prime = 0, 0
    for (i, sum_i), (j, sum_j) in iter.combinations(enumerate(prime_sums), r=2):
        if j - i > max_terms and prime(sum_j - sum_i):
            max_terms, max_prime = j - i, sum_j - sum_i

    print(max_prime)
