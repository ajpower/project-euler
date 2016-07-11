#!/usr/bin/env python3
"""Project Euler, Problem 53

Brute force solution using the multiplication formula to calculate the binomial
coefficients.
"""


def choose(n, k):
    """Return 'n' choose 'k'."""
    numerator = 1
    denominator = 1
    for i in range(1, k + 1):
        numerator *= n + 1 - i
        denominator *= i

    return numerator // denominator


def main():
    threshold = 1000000
    results = 0
    for n in range(1, 101):
        for k in range(0, n + 1):
            if choose(n, k) > threshold:
                results += 1

    print(results)


if __name__ == "__main__":
    main()
