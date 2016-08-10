#!/usr/bin/env python3
"""Project Euler, Problem 44.

Iterate over pentagonal numbers in increasing order. Add each such pentagonal
number P_p to a set and then iterate over this set. For each element P_n in
the set, check 1) that P_m = P_p - P_n is in the set, and 2) P_m - P_n is in
the set. If both conditions hold, then P_m and P_n are pentagonal numbers whose
sum and difference are both pentagonal numbers as well, with the difference
being minimized.
"""
import sys


def pentagonals():
    """Yield pentagonal numbers in increasing order."""
    n = 1
    while True:
        yield n * (3 * n - 1) // 2
        n += 1


if __name__ == '__main__':
    pentagonal_set = set()
    for P_p in pentagonals():
        pentagonal_set.add(P_p)
        for P_n in pentagonal_set:
            P_m = P_p - P_n
            D = P_m - P_n
            if P_m in pentagonal_set and D in pentagonal_set:
                print(D)
                sys.exit(0)
