#!/usr/bin/env python3
"""Project Euler, Problem 28.

The sum of the four diagonal elements in the outer ring of an N by N number
spiral is equal to

    4N^2 - 6N + 1.

This can be seen by noting that the upper left diagonal element is equal to
N^2, and that each subsequent diagonal element moving in a counterclockwise
manner is N - 1 smaller.

Thus the sum of all diagonal elements is equal to

    1 + sum(i=2..(N-1)/2) (4(2i+1)^2 - 6(2i+1) + 6)

After some algebraic manipulation and the use of elementary summation formulas,
the above expression can be simplified to

    8(M(M+1)(2M+1))/3 + 2(M+1)(M) + 4M + 1

where M = (N-1)/2.
"""
N = 1001

if __name__ == '__main__':
    M = (N - 1) // 2
    diagonal_sum = (
        8 * (M * (M + 1) * (2 * M + 1)) // 3 + 2 * (M + 1) * M + 4 * M + 1)
    print(diagonal_sum)
