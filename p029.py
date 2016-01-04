#!/usr/bin/env python3
"""Project Euler, Problem 29

Brute force solution using Python's set. Because sets are implemented
in Python with a hash table, the solution below will have the same time
complexity as a solution that finds all integers that are perfect powers and
removes their duplicate entries.
"""
A_MIN = 2
A_MAX = 100
B_MIN = 2
B_MAX = 100


def main():
    """Print the number of distinct powers formed by taking all integer
    combinations of a^b for A_MIN <= a <= A_MAX and B_MIN <= b <= B_MAX.
    """
    a_range = range(A_MIN, A_MAX+1)
    b_range = range(B_MIN, B_MAX+1)

    distinct_powers = {a**b for a in a_range for b in b_range}
    print(len(distinct_powers))


if __name__ == "__main__":
    main()
