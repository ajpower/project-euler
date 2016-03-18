#!/usr/bin/env python3
"""Project Euler, Problem 49

First, find the set of all four digit primes. Then iterate over this set,
finding the list of all permutations of the digits of each element. For those
elements that have at least three permutations that are also prime, find the
subset of those permutations that are evenly spaced.
"""
from itertools import permutations


def prime_set(n):
    """Return a set of all primes less than or equal to 'n'.
    """
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False

    i = 2
    while i**2 <= n:
        if sieve[i]:
            for j in range(i+1, len(sieve)):
                if j % i == 0:
                    sieve[j] = False

        i += 1

    return {p for p in range(len(sieve)) if sieve[p]}

def digit_permutations(n):
    """Return a list of all permutations of the digits of 'n'.
    """
    # Get digits of n.
    digits = []
    tmp = n
    while tmp > 0:
        digits.append(tmp % 10)
        tmp = tmp // 10

    digit_permutations = []
    for digit_list in permutations(digits):
        num = 0
        exp = 0
        for d in digit_list:
            num += d * 10**exp
            exp += 1
        digit_permutations.append(num)

    return digit_permutations

def evenly_spaced(my_list):
    """Return a list of evenly spaced terms in 'my_list', provided there are at
    least three such terms. 'my_list' is assumed to be sorted.
    """
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            diff = my_list[j] - my_list[i]
            if diff != 0:
                for k in range(j+1, len(my_list)):
                    if my_list[k] - my_list[j] == diff:
                        return [my_list[i], my_list[j], my_list[k]]
    return []

def main():
    # All four digit primes.
    primes = prime_set(9999) - prime_set(999)
    
    for p in primes:
        prime_permutations = [n for n in digit_permutations(p) if n in primes]
        if len(prime_permutations) >= 3:
            prime_permutations.sort()
            spaced = evenly_spaced(prime_permutations)
            if len(spaced) == 3 and spaced[0] != 1487:
                result = ""
                for n in spaced:
                    result += str(n)
                print(result)
                return

if __name__ == "__main__":
    main()
