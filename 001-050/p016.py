#!/usr/bin/env python3
"""Project Euler, Problem 16."""
N = 1000

if __name__ == '__main__':
    answer = sum(int(digit) for digit in str(2 ** N))
    print(answer)
