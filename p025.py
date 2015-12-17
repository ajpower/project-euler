#!/usr/bin/env python3
"""Project Euler, Problem 25

Brute force solution: use a generator to yield Fibonacci numbers until one has
more than NUM_DIGITS digits.
"""
NUM_DIGITS = 1000


def fib():
    """Yields the next Fibonacci number.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def main():
    """Print the index of the first Fibonacci with 'NUM_DIGITS' digits or more.
    """
    index = 0
    for num in fib():
        if len(str(num)) >= NUM_DIGITS:
            print(index)
            break
        else:
            index += 1


if __name__ == "__main__":
    main()
