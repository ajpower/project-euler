#!/usr/bin/env python3
"""Project Euler, Problem 31

Brute force solution using recursion.
"""
AMOUNT = 200
DENOMINATIONS = [1, 2, 5, 10, 20, 50, 100, 200]

def combinations(amount, max_denomination):
    """Return the number of different ways that the coins in DENOMINATIONS up
    to 'max_denomination' can be combined to make 'amount'.
    """
    # no recursive call if only one denomination left.
    if max_denomination == 1:
        return 1

    # find the next highest denomination
    next_highest_denomination_index = DENOMINATIONS.index(max_denomination) - 1
    next_highest_denomination = DENOMINATIONS[next_highest_denomination_index]

    # loop through all possible quantities of max_denomination, calculation the
    # number of different ways for each and summing.
    combos = 0
    for quantity_of_max_denomination in range(amount // max_denomination + 1):
        new_amount = amount - quantity_of_max_denomination * max_denomination
        combos += combinations(new_amount, next_highest_denomination)

    return combos

def main():
    """Print the number of different ways that the coins in DENOMINATIONS can
    be combined to make AMOUNT.
    """
    print(combinations(AMOUNT, DENOMINATIONS[-1]))


if __name__ == "__main__":
    main()
