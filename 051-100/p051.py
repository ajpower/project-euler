#!/usr/bin/env python3
"""Project Euler, Problem 51

Assume that the number of repeating digits is 3. Iterate over all primes up to
a pre-defined limit. Check if the digits 0, 1, or 2 repeat 3 times. If so,
generate all numbers that are formed by replacing the repeating digits and check
the number that are prime. If 8 are prime, then the solution has been found.
"""


def prime_list(n):
    """Return a list of primes less than or equal to 'n'.
    """
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False
    sieve[2] = True

    i = 3
    while i ** 2 <= n:
        if sieve[i]:
            for j in range(i + 2, len(sieve), 2):
                if sieve[j] and j % i == 0:
                    sieve[j] = False
        i += 2

    return [2] + [p for p in range(3, len(sieve), 2) if sieve[p]]


def is_prime(n):
    """Return True if and only if 'n' is prime.
    """
    if n <= 1:
        return False
    d = 2
    while d ** 2 <= n:
        if n % d == 0:
            return False
        d += 1

    return True


def count(n, d):
    """Return the number of times the digit 'd' appears in the number 'n'.
    """
    tmp = n
    count = 0
    while tmp > 0:
        digit = tmp % 10
        if digit == d:
            count += 1
        tmp //= 10

    return count


def eight_prime_value_family(p):
    """Return True if and only if the prime number 'p' is part of an eight
    prime value family.
    """
    # Find digits.
    digits = []
    tmp = p
    while tmp > 0:
        digit = tmp % 10
        digits.append(digit)
        tmp //= 10

    # Find the repeating digit.
    repeating_digit = 0
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
        if new_digits[-1] != 0 and is_prime(new_num):
            count += 1

    return count == 8


def main():
    # max_prime defined to be 10**6. If script does not yield solution, more
    # primes need to be considered.
    max_primes = 10 ** 6
    primes = prime_list(max_primes)
    for p in primes:
        if any([count(p, d) for d in range(3)]):
            if eight_prime_value_family(p):
                print(p)
                return
    print("Error: max_primes must be larger")


if __name__ == "__main__":
    main()
