#!/usr/bin/env python3
"""Project Euler, Problem 24.

Find the nth lexicographic permutation of a set of m digits as follows:
First note that there are (m - 1)! permutations with a given starting digit.
The first digit will be the digit for which the total number of permutations
with a starting digit less than or equal to that digit is as large as possible
without exceeding n. The index of this digit is given by the formula

    (n - 1) div (m - 1)!

To find the remaining digits, remove this digit from the set of digits and apply
the above procedure to the remaining digits, with n -> n - digit * (m - 1)!
"""
from math import factorial

N = 1000000
DIGITS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

if __name__ == '__main__':
    permutation_digits = []
    remaining_digits = DIGITS.copy()
    remaining_permutations = N - 1

    while remaining_digits:
        n_digits = len(remaining_digits)
        digit_index = remaining_permutations // factorial(n_digits - 1)
        digit = remaining_digits[digit_index]

        permutation_digits.append(digit)
        remaining_digits.remove(digit)
        remaining_permutations -= digit_index * factorial(n_digits - 1)

    permutation = "".join(str(digit) for digit in permutation_digits)
    print(permutation)
