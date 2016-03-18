#!/usr/bin/env python3
"""Project Euler, Problem 12

The nth triangular number is given by the formula

    T_n = n(n+1)/2

If two numbers do not share any common factors, the the number of factors in
their product is equal to the product of the number of factors of each
individual number. n and n+1 do not have any common factors. Hence if n is
even, the number of factors in the nth triangular number is equal to the number
of factors in n/2 times the number of factors in n+1; a similar formula holds if
n is odd.
"""
MIN_NUM_FACTORS = 501


def number_of_factors(n):
    """Return the number of factors in n.
    """
    divisor = 1
    count = 0
    while divisor**2 < n:
        if n % divisor == 0:
            # every divisor less than the square root of n will have an
            # associated divisor greater than the square root of n.
            count += 2

        divisor += 1

    if divisor**2 == n:
        count += 1

    return count

def main():
    """Print the first triangular number with more than `MIN_NUM_FACTORS`
    factors.
    """
    n = 0
    num_factors = 0
    while num_factors < MIN_NUM_FACTORS:
        n += 1

        if n % 2 == 0:
            num_factors = number_of_factors(n // 2) * number_of_factors(n+1)

        else:
            num_factors = number_of_factors(n) * number_of_factors((n+1) // 2)

    triang = n*(n+1) // 2
    print(triang)


if __name__ == "__main__":
    main()
