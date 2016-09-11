#!/usr/bin/env python3
"""Project Euler, Problem 58."""


def is_prime(n):
    """Return True if prime."""
    if n < 2:
        return False

    if n > 2 and n % 2 == 0:
        return False

    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2

    return True


if __name__ == '__main__':
    side_length = 3
    n_primes = 3
    n_diagonals = 5
    last_diagonal = 9

    while n_primes / n_diagonals >= 0.1:
        side_length += 2
        n_diagonals += 4
        next_diagonals = [last_diagonal + (side_length - 1) * n for n in
                          range(1, 5)]

        n_primes += sum(is_prime(diagonal) for diagonal in next_diagonals)
        last_diagonal = next_diagonals[-1]

    print(side_length)
