#!/usr/bin/env python3
"""Project Euler, Problem 23
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

def binary_search(element, _list):
    """Return True is 'element' is located in sorted list '_list'.
    """
    if _list == []:
        return False

    midpoint = len(_list) // 2
    if _list[midpoint] == element:
        return True
    elif _list[midpoint] > element:
        return binary_search(element, _list[:midpoint])
    else:
        return binary_search(element, _list[midpoint+1:])


def main():
    """
    """
    # abundant numbers less than 28124
    abundant_nums = [n for n in range(1, 28124) if sum_divisors(n) > n]

    result = 0
    for n in range(1, 28124):
        i = 0
        sum_found = False
        while i < len(abundant_nums) and abundant_nums[i] <= n:
            if binary_search(n - abundant_nums[i], abundant_nums):
                sum_found = True
                break
            i += 1 

        if not sum_found:
            result += n

    print(result)


if __name__ == "__main__":
    main()
