#!/usr/bin/env python3
"""Project Euler, Problem 1.

The sum of all multiples of m below n equals m times the sum of all integers
less than or equal to (n - 1) / m; this second term can be calculated using
Gauss' trick.

To get the sum of all multiples of 3 and 5 below 1000, simply add the sum of
all multiples of 3 below 1000 with the sum of all multiples of 5 below 1000 and
then subtract the numbers that have been double counted. The numbers that will
be double counted are multiples of the least common multiple of 3 and 5, which
is 15.
"""
UPPER_BOUND = 1000


def sum_integers(n):
    """Return the sum of all positive integers less than or equal to n."""
    return n * (n + 1) // 2


if __name__ == '__main__':
    sum_multiples_3 = 3 * sum_integers((UPPER_BOUND - 1) // 3)
    sum_multiples_5 = 5 * sum_integers((UPPER_BOUND - 1) // 5)
    sum_multiples_15 = 15 * sum_integers((UPPER_BOUND - 1) // 15)

    sum_multiples = sum_multiples_3 + sum_multiples_5 - sum_multiples_15
    print(sum_multiples)
