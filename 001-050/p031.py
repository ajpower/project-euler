#!/usr/bin/env python3
"""Project Euler, Problem 31."""
AMOUNT = 200
COINS = [1, 2, 5, 10, 20, 50, 100, 200]


def combinations(amount: int, coins: list):
    """Return the number of ways the given amount can we made using the given
    coins.
    """
    remaining_coins = coins.copy()  # Prevent modification of the original list.
    largest_coin = remaining_coins.pop()

    if largest_coin == 1:
        return 1

    return sum(
            combinations(amount - quantity * largest_coin, remaining_coins) for
            quantity in range(amount // largest_coin + 1))


if __name__ == '__main__':
    print(combinations(AMOUNT, COINS))
