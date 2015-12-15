#!/usr/bin/env python3
"""Project Euler
"""
N = 10000


def d(n):
    """Return the sum of proper divisors of n.
    """
    # 1 is always a divisor so can be added immediately; including in the loop
    # adds complications because n cannot be included in the sum of divisors.
    divisor = 2 
    sum_divisors = 1
    while divisor**2 < n:
        if n % divisor == 0:
            sum_divisors += divisor + n // divisor

        divisor += 1

    # special case if n is a perfect square
    if divisor**2 == n:
        sum_divisors += divisor

    return sum_divisors

def main():
    """Print the sum of all amicable numbers under N.
    """
    sum_amicable_numbers = 0
    for a in range(1,N+1):
        b = d(a)
        if d(b) == a and a != b:
            sum_amicable_numbers += a 

    print(sum_amicable_numbers)


if __name__ == "__main__":
    main()
