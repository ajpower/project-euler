#!/usr/bin/env python3
"""Project Euler, Problem 26.

To find the cycle length of the fraction 1/d, perform long division but keep
track of the remainders only. If a remainder is ever equal to zero, there is no
cycle. On the other hand, if a remainder repeats itself, then there is a cycle
starting from the first instance of that remainder.
"""
D_MAX = 1000


def cycle_length(d):
    """Return the cycle length of 1/d."""
    remainders = [1]  # 1 / d is 0 remainder 1.
    while True:
        remainder = 10 * remainders[-1] % d

        # Cycle is found.
        if remainder in remainders:
            return len(remainders) - remainders.index(remainder)
        # No cycle.
        elif remainder == 0:
            return 0
        else:
            remainders.append(remainder)


if __name__ == '__main__':
    max_cycle, d_max_cycle = max((cycle_length(d), d) for d in range(1, D_MAX))
    print(d_max_cycle)
