#!/usr/bin/env python3.4
"""Project Euler, Problem 15

It is necessary and sufficient to make N right turns and N downward turns to
reach the bottom right of the lattice. Hence there are 2N choose N paths from
the top left to the bottom right.
"""
N = 20


def binomial(n, k):
    """Return n choose k.
    """
    product = 1
    for i in range(1, k+1):
        product *= (n + 1 - i) / i

    return int(product)

def main():
    """Print the number of routes from the top left of a NxN lattice to the
    bottom right moving only down and right.
    """
    num_routes = binomial(2*N, N)
    print(num_routes)


if __name__ == "__main__":
    main()
