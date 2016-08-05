#!/usr/bin/env python3
"""Project Euler, Problem 37.

To generate all possible left truncatable numbers, begin with a queue of all
single digit prime numbers (ie 2, 3, 5, and 7). Pop the first element and add a
digit to the right. If the resulting number is prime, then add it to the queue
and to a separate list. Continue until the queue is empty. The list then
contains all left truncatable numbers.

A list of all truncatable numbers can be generated by taking from the previous
list only those elements that are right truncatable.
"""
from queue import Queue


def is_prime(n):
    """Return True if n is prime."""
    if n < 2:
        return False

    if n != 2 and n % 2 == 0:
        return False

    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2

    return True


def num_digits(n):
    """Return the number of digits in base ten of the given number."""
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count


def is_right_truncatable(n):
    """Return True if n is a right truncatable prime, assuming that n is prime.
    """
    return all(is_prime(n % 10 ** d) for d in range(1, num_digits(n)))


if __name__ == '__main__':
    left_truncatable_primes = []
    tmp_queue = Queue()

    tmp_queue.put(2)
    tmp_queue.put(3)
    tmp_queue.put(5)
    tmp_queue.put(7)

    while not tmp_queue.empty():
        number = tmp_queue.get()
        for digit in range(1, 10):
            new_number = number * 10 + digit
            if is_prime(new_number):
                left_truncatable_primes.append(new_number)
                tmp_queue.put(new_number)

    print(sum(p for p in left_truncatable_primes if is_right_truncatable(p)))
