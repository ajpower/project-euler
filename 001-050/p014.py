#!/usr/bin/env python3
"""Project Euler, Problem 14

Brute force computation of the length of the Collatz sequence for every number
less than N.
"""
N = 1000000


def chain_length(n):
    """Return the length of the Collatz sequence starting from `n`.
    """
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + chain_length(n // 2)
    else:
        # if n is odd, then 3*n + 1 is necessarily even so we can skip a step.
        return 2 + chain_length((3*n + 1) // 2)

def main():
    """Print the starting number smaller than N which produces the largest
    Collatz sequence.
    """
    max_length = 0
    starting_number = 0
    for i in range(1, N):
        length = chain_length(i)
        if length > max_length:
            max_length = length
            starting_number = i

    print(starting_number)


if __name__ == "__main__":
    main()
