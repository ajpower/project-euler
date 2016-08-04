#!/usr/bin/env python3
"""Project Euler, Problem 29."""
A_MIN = 2
A_MAX = 100
B_MIN = 2
B_MAX = 100

if __name__ == '__main__':
    a_range = range(A_MIN, A_MAX + 1)
    b_range = range(B_MIN, B_MAX + 1)

    distinct_powers = {a ** b for a in a_range for b in b_range}
    print(len(distinct_powers))
