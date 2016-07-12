#!/usr/bin/env python3
"""Project Euler, Problem 7.

The Nth prime is found by continuously testing odd numbers for primality and
adding them to a list of primes if they pass the test until N primes have
been produced. Numbers are tested for primality by computing the remainder of
their division with all discovered primes.
"""
N = 10001

if __name__ == '__main__':
    primes = [2]
    candidate = 3

    while len(primes) < N:
        if all(candidate % p != 0 for p in primes):
            primes.append(candidate)

        candidate += 2

    print(primes[-1])
