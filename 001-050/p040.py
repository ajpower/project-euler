#!/usr/bin/env python3
"""Project Euler, Problem 40

To determine d_n, begin by calculating the number of digits of the number that
was used to make the nth digit. For example, a 2 digit number (13) was used to
create the 16th and 17th digits. Next, determine the actual number that was used
to create the nth digit. Finally, find the appropriate digit.
"""
def d(n):
    """Return the nth digit of Champernowe's constant.
    """
    # Determine the number of digits of the number that was used to create the
    # nth digit.
    num_digits, tmp = 0, n
    while tmp > 0:
        num_digits += 1
        tmp -= 9 * (10**(num_digits-1)) * num_digits

    # Determine the number that went into constructing the nth digit.
    # `digits` tracks the number of actual digits that have been passed in the
    # for loop.
    num, digits = 0, 0 
    for i in range(1, num_digits):
        num += 9 * (10**(i-1))
        digits += 9 * (10**(i-1)) * i
    num += (n - digits - 1) // num_digits + 1

    # Return the appropriate digit of `num`.
    digit_pos = num_digits - (n - digits - 1) % num_digits
    return (num // 10**(digit_pos-1)) % 10

def main():
    # Iterate over all powers of 10 up to 10^6.
    result = 1
    for e in range(7):
        result *= d(10**e)

    print(result)


if __name__ == "__main__":
    main()
