#!/usr/bin/env python3
"""Project Euler, Problem 37

To generate all possible left truncatable numbers, begin with a queue of all
single digit prime numbers (ie 2, 3, 5, and 7). Pop the first element and add a
digit to the right. If the resulting number is prime, then add it to the queue
and to a seperate list. Continue until the queue is empty. The list then
contains all left truncatable numbers.

A list of all truncatable numbers can be generated by taking from the previous
list only those elements that are right truncatable.
"""
from queue import Queue


def is_prime(n):
    """Return True if n is prime.
    """
    if n < 2: return False

    d = 2
    while d**2 <= n:
        if n % d == 0:
            return False
        d += 1

    return True

def is_right_truncatable(n):
    """Return True if n is a right truncatable prime, assuming that n is prime.
    """
    # Check if the rightmost digit is prime. If so, check if the rightmost two
    # digits are prime, etc. until either a non-prime number is encountered or
    # all of n's digits have been checked.
    num_digits = 1
    rightmost_digits = n % 10

    while rightmost_digits != n:
        if not is_prime(rightmost_digits):
            return False
        num_digits += 1
        rightmost_digits = n % 10**num_digits

    return True

def main():
    """Print the sum of all truncatable primes.
    """
    left_truncatable_primes = []
    tmp_queue = Queue()

    tmp_queue.put(2)
    tmp_queue.put(3)
    tmp_queue.put(5)
    tmp_queue.put(7)

    while not tmp_queue.empty():
        number = tmp_queue.get()
        for digit in range(1, 10):
            new_number = number*10 + digit
            if is_prime(new_number):
                left_truncatable_primes.append(new_number)
                tmp_queue.put(new_number)

    sum_truncatable_primes = 0
    for p in left_truncatable_primes:
        if is_right_truncatable(p):
            sum_truncatable_primes += p

    print(sum_truncatable_primes)


if __name__ == "__main__":
    main()
