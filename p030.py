#!/usr/bin/env python3
"""Project Euler, Problem 30

Brute force solution. Note that no number with more than 6 digits needs to be
checked. This follows from the fact that the largest possible sum of 7 digits to
the power 5 is 7*9^5, which is less than the smallest 7 digit number, 10^6.
"""
def sum_digits_to_power(n, p):
    """Return the sum of the digits of n each taken to the power of p.
    """
    numeral = str(n)
    _sum = 0
    for digit in numeral:
        _sum += int(digit)**p

    return _sum

def main():
    """Print the sum of all numbers, excluding 1, which are equal to the sum of
    their digits to the power 5.
    """
    _sum = 0
    for n in range(2, 10**6):
        if (n == sum_digits_to_power(n, 5)):
            _sum += n

    print(_sum)


if __name__ == "__main__":
    main()
