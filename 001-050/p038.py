#!/usr/bin/env python3
"""Project Euler, Problem 38

Inefficient brute force solution. Generate all 1 to 9 pandigital numbers in
decreasing order and check each one to see if it is the concatenated product of
an integer and (1, 2, ..., n) for some n > 1.
"""
from itertools import permutations


def factorize(n):
    """Return a list of factors of n.
    """
    factors = []
    d = 1
    while d**2 < n:
        if n % d == 0:
            factors.append(d)
            factors.append(n // d)
        d += 1

    # Special case if n is perfect square to avoid adding the square root twice.
    if d**2 == n:
        factors.append(d)

    return factors

def is_cat_product(n):
    """Return true if and only if n is the concatenated product of an integer
    with (1, 2, ..., m).
    """
    for factor in factorize(n):
        divisor = n // factor
        m = divisor % 10

        # m must be greater than 1.
        if m <= 1:
            continue

        # Form concatenated product of factor and (1, 2, ..., m) and compare to
        # n.
        cat_product = m * factor
        for i in range(m-1, 0, -1):
            cat_product += i * factor * 10**len(str(cat_product))

        if cat_product == n:
            return True

    return False

def pandigitals():
    """Yield all 1 to 9 pandigital numbers in decreasing order.
    """
    for pandigital_tuple in permutations('987654321', 9):
        pandigital = int(''.join(pandigital_tuple))
        yield pandigital

def main():
    """Print the largest 1 to 9 panditigal number that is the concatenated
    product of an integer and (1, 2, ..., n) for some n > 1.
    """
    largest_pandigital = 0
    for pandigital in pandigitals():
        if is_cat_product(pandigital):
            largest_pandigital = pandigital
            break

    print(largest_pandigital)


if __name__ == "__main__":
    main()
