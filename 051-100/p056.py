#!/usr/bin/env python3
"""Project Euler, Problem 56."""


def digit_sum(n: int):
    """Return the sum of digits in n."""
    return sum(int(d) for d in str(n))


if __name__ == '__main__':
    print(max(digit_sum(a ** b) for a in range(101) for b in range(101)))
