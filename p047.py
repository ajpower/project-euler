#!/usr/bin/env python3
"""Project Euler, Problem 47
"""
def prime_factors(n):
    """Return a set of unique prime factors of 'n'.
    """
    primes = set()
    d = 2
    tmp = n
    while d**2 <= tmp:
        if tmp % d == 0:
            primes.add(d)
            tmp //= d
        else:
            d += 1

    if tmp > 1:
        primes.add(tmp)

    return primes

def main():
    n = 1
    while True:
        if all([len(prime_factors(n+x)) == 4 for x in range(4)]):
            print(n)
            return
        n += 1


if __name__ == "__main__":
    main()
