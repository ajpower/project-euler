#!/usr/bin/env python3
"""Project Euler, Problem 23

First, produce a list of all abundant numbers less than 28124; larger abundant
numbers are not needed as the largest integer that cannot be expressed as the
sum of two abundant numbers is smaller than this threshold. Next, for every
positive integer less than 28124 determine whether it appears as a sum of two
elements in the previous list. If not, add the integer to a running sum of
integers which cannot be expressed as the sum of two abundant numbers.
"""
def sum_divisors(n):
    """Return the sum of the proper divisors of n.
    """
    # 1 is always a divisor so can be added immediately; including in the loop
    # adds complications because n cannot be included in the sum of divisors.
    d = 2
    sum_divisors = 1
    while d**2 < n:
        if n % d == 0:
            sum_divisors += d + n // d

        d += 1

    # special case if n is a perfect square
    if d**2 == n:
        sum_divisors += d

    return sum_divisors

def has_sum(n, _list):
    """Return True if sorted list '_list' has two elements that sum to 'n'.
    """
    # To search through '_list' in linear time, define two indices 'low' and
    # 'high' which are initially assigned to the first and last indices of
    # '_list'. Sum the corresponding elements. If the sum is greater than 'n',
    # decrement 'high'. If the sum is smaller than 'n', increment 'low'. If the
    # sum equals 'n', cease the search and return True. Finally, is low ever
    # exceed 'high', then 'n' cannot be expressed as the sum of two elements in
    # '_list', so cease the search and return False.
    low, high = 0, len(_list) - 1
    _sum = _list[low] + _list[high]

    while low < high and _sum != n:
        if _sum > n:
            high -= 1
        else:
            low += 1
        _sum = _list[low] + _list[high]

    return _sum == n

def main():
    """Print the sum of all positive integers that cannot be expressed as the
    sum of two abundant numbers.
    """
    # abundant numbers less than 28124
    abundant_nums = [n for n in range(1, 28124) if sum_divisors(n) > n]

    # Loop through all positive integers less than 28124. If an integer cannot
    # be expressed as the sum of two abundant numbers, add to 'result'.
    result = 0
    for n in range(1, 28124):
        if not has_sum(n, abundant_nums):
            result += n

    print(result)


if __name__ == "__main__":
    main()
