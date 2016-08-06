#!/usr/bin/env python3
"""Project Euler, Problem 39.

From Euclid's formula it can be shown that the perimeter of a right angled
triangle must be even.

If the perimeter of a right angled triangle is p, then b must be equal to

    b = (p^2 - 2pa) / (2p - 2a)

For every possible value of p, we can generate all values of a and b by
checking if the above equation gives an integer. This will give the number of
solutions.

Note that it is not necessary to check values of p below MAX_PERIMETER / 2 as
all such p's will have a corresponding perimeter 2p with at least as many
solutions.
"""
MAX_PERIMETER = 1000


def num_solutions(p):
    """Return the number of right angle triangles with integral length sides with
    the given perimeter."""
    return sum((p * p - 2 * p * a) % (2 * p - 2 * a) == 0 for a in
               range(2, p // 2))


if __name__ == '__main__':
    p_max = max((p for p in range(MAX_PERIMETER // 2, MAX_PERIMETER + 1, 2)),
                key=num_solutions)
    print(p_max)
