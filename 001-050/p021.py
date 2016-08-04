#!/usr/bin/env python3
"""Project Euler, Problem 21."""
N = 10000


def d(n):
    """Return the sum of the proper divisors of n."""
    sum_divisors = 1  # Include 1 from the start.
    div = 2
    while div * div < n:
        if n % div == 0:
            sum_divisors += div
            sum_divisors += n // div
        div += 1

    # Explicit check if n is a perfect square.
    if div * div == n:
        sum_divisors += div

    return sum_divisors


if __name__ == '__main__':
    amicable_nums = [n for n in range(1, N) if n == d(d(n)) and n != d(n)]
    print(sum(amicable_nums))
