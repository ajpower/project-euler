#!/usr/bin/env python3
"""Project Euler, Problem 43

First, find all three digit numbers that are divisible by 17 and store in a
list. For each element in this list add a digit at the front and check if its
first three digits from the front are divisible by the next smallest prime. If
so, include in the list. Continue until all primes are exhausted.

This will produce a list of ten digit integers with the substring divisibility
property described in the problem statement. Iterate over this list and find
the elements that are pandigital as well, and add those numbers to a running
total.
"""
def is_pandigital(n):
    """Return True if and only if 'n' is 0 to 9 pandigital.
    """
    digits = []
    for _ in range(10) :
        d = n % 10
        if d in digits:
            return False
        digits.append(d)
        n = n // 10

    return True

def main():
    substring_divisibles = [n for n in range(1, 1000) if n % 17 == 0]
    num_digits = 3
    primes = [13, 11, 7, 5, 3, 2, 1] # Includes 1 to take into account the last
                                     # three digits.
    for p in primes:
        tmp = []
        for s in substring_divisibles:
            for d in range(10):
                new_s = d * 10**num_digits + s
                if (new_s // 10**(num_digits - 2)) % p == 0:
                    tmp.append(new_s)

        substring_divisibles = tmp
        num_digits += 1

    _sum = 0
    for n in substring_divisibles:
        if is_pandigital(n):
            _sum += n

    print(_sum)


if __name__ == "__main__":
    main()
