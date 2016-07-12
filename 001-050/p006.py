#!/usr/bin/env python3
"""Project Euler, Problem 6.

The square of the sum of integers from 1 to N is equal to (N(N+1)/2)^2, while
the sum of the squares of integers from 1 to N is equal to N(N+1)(2N+1)/6. With
some simple algebra, it can be shown that the difference between these two
quantities is N(N-1)(N+1)(3N+2)/12.
"""
N = 100

if __name__ == '__main__':
    answer = N * (N - 1) * (N + 1) * (3 * N + 2) // 12
    print(answer)
