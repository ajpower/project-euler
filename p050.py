#!/usr/bin/env python3
"""Project Euler, Problem 50
"""
def is_prime(n):
    """Return True if and only if 'n' is prime.
    """
    if n <= 1:
        return False
    d = 2
    while d**2 <= n:
        if n % d == 0:
            return False

        d += 1

    return True

def prime_list(n):
    """Return a list of all primes less than or equal to 'n'.
    """
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False
    sieve[2] = True

    i = 3
    while i**2 <= n:
        if sieve[i]:
            for j in range(i+2, len(sieve), 2):
                if sieve[j] and j % i == 0:
                    sieve[j] = False

        i += 2

    primes = [2] + [p for p in range(3, len(sieve), 2) if sieve[p]]
    return primes

def prime_sum(max_sum, primes):
    """Return a list where the ith element contains the sum of the first i
    primes. If the sum exceeds 'max_sum', it is not included.
    """
    prime_sum = [0]
    for p in primes:
        if prime_sum[-1] + p > max_sum:
            break
        prime_sum.append(prime_sum[-1] + p)

    return prime_sum

def main():
    primes = prime_list(10**4)
    prime_sum_table = prime_sum(10**6, primes)

    max_terms = 1
    max_prime = 0
    for i in range(len(prime_sum_table)):
        for j in range(len(prime_sum_table) - 1, i + max_terms, -1):
            n = prime_sum_table[j] - prime_sum_table[i]
            if j - i > max_terms and is_prime(n):
                max_terms = j - 1
                max_prime = n
                break
    print(max_prime)

if __name__ == "__main__":
    main()
