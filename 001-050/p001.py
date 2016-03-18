#!/usr/bin/env python3
"""Project Euler, Problem 1

The sum of all multiples of m below n equals m times the sum of all integers
less than or equal to the largest multiple of m below n; this second term can be
calculated using Gauss' trick.

To get the sum of all multiples of 3 and 5 below 1000, simply add the sum of
all multiples of 3 below 1000 with the sum of all multiples of 5 below 1000 and
then subtract the numbers that have been double counted. The numbers that will
be double counted are multiples of the least common multiple of 3 and 5, which
is 15.
"""
UPPER_BOUND = 1000
LCM = 15


def largest_multiple(m, n):
    """Return largest multiple of m below n.
    """
    remainder = n % m
    if remainder == 0:
        return n - m
    return n - remainder

def sum_integers(n):
    """Return the sum of all integers less than or equal to n.
    """
    return n * (n+1) // 2

def sum_multiples_3_5(n):
    """Return the sum of all multiples of 3 and 5 below n.
    """
    largest_multiple_3 = largest_multiple(3, n)
    largest_multiple_5 = largest_multiple(5, n)
    largest_multiple_lcm = largest_multiple(LCM, n)

    a = 3 * sum_integers(largest_multiple_3 // 3)
    b = 5 * sum_integers(largest_multiple_5 // 5)
    c = LCM * sum_integers(largest_multiple_lcm // LCM)

    return a + b - c

def main():
    """Print the sum of all multiples of 3 and 5 below UPPER_BOUND.
    """
    answer = sum_multiples_3_5(UPPER_BOUND)
    print(answer)


if __name__ == "__main__":
    main()
