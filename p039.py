#!/usr/bin/env python3
"""Project Euler, Problem 39

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


def main():
    max_solutions, p_max = 0, 0
    for p in range(2*(MAX_PERIMETER // 4), MAX_PERIMETER + 1, 2):
        num_solutions = 0

        for a in range(2, p // 2 + 1):
            b = p*(p - 2*a) % (2*(p - a))
            if b == 0:
                num_solutions += 1

        if num_solutions > max_solutions:
            max_solutions = num_solutions
            p_max = p

    print(p_max)


if __name__ == "__main__":
    main()
