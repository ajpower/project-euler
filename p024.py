#!/usr/bin/env python3
"""Project Euler, Problem 24

For the first digit, find the maximum digit such that the required number of
permutations to reach a number starting with that digit is less that N. For
example, if N = 1000000 and the digits to permute are 0, 1, 2, ..., 8, 9, then
it takes 725761 permutations to reach the number 2013456789 but 1088541
permutations to reach the number 3012456789; hence the required digit is 2. In
general, this maximum digit is given by

    N div (n - 1)!

where n is the number of digits.

After this number has been reached, there are N - (n - 1)! permutations left;
repeat the above process, but with N reduced to N - (n - 1)! and the previously
discovered digit removed from the list of digits.
"""
from math import factorial
from sys import exit, stderr

N = 1000000
DIGITS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def main():
    """Print the 'N'th lexicographic permutation of 'DIGITS'.
    """
    used_digits = []
    remaining_digits = DIGITS
    remaining_permutations = N - 1

    # find the largest digit that requires less permutations than N to reach,
    # then remove from 'remaining digits', add to 'used_digits', and reduce
    # 'remaining_permutations' accordingly.
    while remaining_digits != []:
        fact = factorial(len(remaining_digits) - 1) # (n - 1)!, used to
                                                    # calculate 'digit_to_add';
                                                    # see module docstring.
        digit_index = remaining_permutations // fact
        digit_to_add = remaining_digits[digit_index]

        used_digits.append(digit_to_add)
        remaining_digits.remove(digit_to_add)

        remaining_permutations -= digit_index * fact 

    # join the elements of 'used_digits' into a single string
    nth_permutation = ""
    for digit in used_digits:
        nth_permutation += str(digit)

    print(nth_permutation)


if __name__ == "__main__":
    main()
