#!/usr/bin/env python3
"""Project Euler, Problem 26

To find the cycle length of the fraction 1/d, perform long division but keep
track of the remainders only. If a remainder is ever equal to zero, there is no
cycle. On the other hand, if a remainder repeats itself, then there is a cycle
starting from the first instance of that remainder.
"""
D_MAX = 1000


def cycle_length(d):
    """Return the cycle length of 1/d.
    """
    remainders = [1]
    while True:
        new_remainder = 10 * remainders[-1] % d

        # cycle is found
        if new_remainder in remainders:
            return len(remainders) - remainders.index(new_remainder)
        # no cycle
        elif new_remainder == 0:
            return 0
        else:
            remainders.append(new_remainder)

def main():
    """Print the integer below 'D_MAX' such that the inverse of the integer
    produces the largest cycle.
    """
    max_cycle_length = 0
    d_max = 0

    for d in range(1, D_MAX):
        if cycle_length(d) > max_cycle_length:
            max_cycle_length = cycle_length(d)
            d_max = d

    print(d_max)


if __name__ == "__main__":
    main()
