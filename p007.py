#!/usr/bin/env python3
"""Project Euler, Problem 7

The nth prime is found by continuously testing odd numbers for primality and
adding them to a list of primes if they pass the test until n primes have
been produced. Numbers are tested for primality by computing the remainder of
their division with all discovered primes.
"""
N = 10001


def nth_prime(n):
    """Return the nth prime.
    """
    primes = [2]
    candidate = 3

    while len(primes) < n:
        if all(candidate % prime != 0 for prime in primes):
            primes.append(candidate)
        candidate += 2

    return primes[-1]

def main():
    """Print the Nth prime number.
    """
    print(nth_prime(N))


if __name__ == "__main__":
    main()
