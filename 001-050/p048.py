#!/usr/bin/env python3
"""Project Euler, Problem 48

Simply compute the sum directly, but only keep the last ten digits every
iteration.
"""
def main():
    last_10_digits = 0
    for n in range(1, 1001):
        last_10_digits += n**n
        last_10_digits = last_10_digits % 10**10

    print(last_10_digits)


if __name__ == "__main__":
    main()
