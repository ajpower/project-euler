#!/usr/bin/env python3
"""Project Euler, Problem 60."""
import itertools
from functools import lru_cache

MAX_PRIME = 10000


def primes_below(n):
    """Return a list of all primes below n."""
    sieve = [True] * n
    sieve[0] = sieve[1] = False

    i = 2
    while i * i <= n:
        if sieve[i]:
            for j in range(i * i, n, i):
                sieve[j] = False
        i += 1

    return [p for p, is_prime in enumerate(sieve) if is_prime]


@lru_cache(maxsize=None)
def concat_is_prime(n1: int, n2: int):
    """Return True if the concatenation of the two integers is prime."""
    n = int(str(n1) + str(n2))

    if n < 2:
        return False

    if n > 2 and n % 2 == 0:
        return False

    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2

    return True


def is_prime_pair_set(primes):
    """Return True if all pairs in primes can be concatenated in any order to
    produce another prime.
    """
    return all(concat_is_prime(p1, p2) for p1, p2 in
               itertools.permutations(primes, r=2))


def prime_pair_sets(n, primes):
    """Return all n-tuples of primes in primes that are prime pair sets."""
    if n < 2:
        return []
    elif n == 2:
        return [pair for pair in itertools.combinations(primes, r=2) if
                is_prime_pair_set(pair)]
    else:
        result = []
        for prime_pair_set in prime_pair_sets(n - 1, primes):
            for p in primes:
                if p > prime_pair_set[-1] and \
                        is_prime_pair_set(prime_pair_set + (p,)):
                    result.append(prime_pair_set + (p,))
        return result


if __name__ == '__main__':
    primes = primes_below(MAX_PRIME)

    # 2 and 5 cannot be part of any prime pair.
    primes.remove(2)
    primes.remove(5)

    print(sum(min(prime_pair_sets(n=5, primes=primes), key=sum)))
