#!/usr/bin/env python3
"""Project Euler, Problem 51.

Assume that the number of repeating digits is 3. Iterate over all primes up to
a pre-defined limit. Check if the digits 0, 1, or 2 repeat 3 times. If so,
generate all numbers that are formed by replacing the repeating digits and check
the number that are prime. If 8 are prime, then the solution has been found.
"""
import sys


def primes_below(n):
    """Return a list of primes below the given number."""
    sieve = [True] * n
    sieve[0], sieve[1] = False, False

    i = 2
    while i ** 2 <= n:
        if sieve[i]:
            for j in range(i * i, n, i):
                sieve[j] = False
        i += 1

    return [p for p, is_prime in enumerate(sieve) if is_prime]


def prime(n):
    """Return True if given number is prime."""
    if n <= 1:
        return False

    if n != 2 and n % 2 == 0:
        return False

    d = 3
    while d ** 2 <= n:
        if n % d == 0:
            return False
        d += 2

    return True


def digit_count(digit, num):
    """Return the number of times the given digit appears in the given number.
    """
    tmp = num
    count = 0
    while tmp > 0:
        d = tmp % 10
        if d == digit:
            count += 1
        tmp //= 10

    return count


def eight_prime_value_family(p):
    """Return True if the prime number is part of an eight prime value family.
    """
    digits = []
    tmp = p
    while tmp > 0:
        digit = tmp % 10
        digits.append(digit)
        tmp //= 10

    # Find the repeating digit.
    for d in digits:
        if digits.count(d) == 3:
            repeating_digit = d
            break
    else:
        return False

    # Count the number of primes that are formed by replacing the repeating
    # digits with 0, 1, ..., 9.
    count = 0
    for i in range(10):
        new_digits = [i if d == repeating_digit else d for d in digits]
        new_num = 0
        for j in range(len(new_digits)):
            new_num += new_digits[j] * 10 ** j

        # Check if new_digit is prime and hasn't lost a digit.
        if new_digits[-1] != 0 and prime(new_num):
            count += 1

    return count == 8


if __name__ == '__main__':
    # max_prime defined to be 10^6. If script does not yield solution, more
    # primes need to be considered.
    max_primes = 10 ** 6
    primes = primes_below(max_primes)
    for p in primes:
        if any([digit_count(digit=d, num=p) for d in range(3)]) and \
                eight_prime_value_family(p):
            print(p)
            break
    else:
        print('Error: max_primes must be larger', file=sys.stderr)
