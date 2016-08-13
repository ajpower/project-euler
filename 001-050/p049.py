#!/usr/bin/env python3
"""Project Euler, Problem 49.

First, find the set of all four digit primes. Then iterate over this set,
finding the list of all permutations of the digits of each element. For those
elements that have at least three permutations that are also prime, find the
subset of those permutations that are evenly spaced.
"""
import itertools


def primes_below(n):
    """Return all primes less than n."""
    sieve = [True] * n
    sieve[0], sieve[1] = False, False

    i = 2
    while i ** 2 <= n:
        if sieve[i]:
            for j in range(i ** 2, n, i):
                sieve[j] = False
        i += 1

    return (p for p, is_prime in enumerate(sieve) if is_prime)


def digit_permutations(n):
    """Return a list of all permutations of the digits of n in sorted order."""
    digits = []
    tmp = n
    while tmp > 0:
        digits.append(tmp % 10)
        tmp //= 10

    digit_permutations = []
    for digit_list in itertools.permutations(digits):
        num, exp = 0, 0
        for d in digit_list:
            num += d * 10 ** exp
            exp += 1
        digit_permutations.append(num)

    digit_permutations.sort()

    return digit_permutations


def evenly_spaced(terms):
    """Return a list of three evenly spaces terms in the given list, assumed to
    be sorted.
    """
    for n, m, p in itertools.combinations(terms, r=3):
        if m - n == p - m != 0:
            return [n, m, p]
    return []


if __name__ == '__main__':
    primes = set(primes_below(10000)) - set(primes_below(1000))

    for p in primes:
        prime_permutations = [n for n in digit_permutations(p) if n in primes]
        spaced = evenly_spaced(prime_permutations)
        if len(spaced) == 3 and spaced[0] != 1487:
            break

    print(''.join(str(n) for n in spaced))
