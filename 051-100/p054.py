#!/usr/bin/env python3
"""Project Euler, Problem 54.

Poker hands are represented by the pair (s, r), where s is the strength of the
hand (higher is better) while r is a list of distinct ranks in the hand, ordered
by frequency and then rank. This representation allows two hands to be compared
with simple inequality operators.
"""
from collections import Counter
from enum import IntEnum

FILE = 'p054_poker.txt'
RANKS = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
         'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


class Strength(IntEnum):
    """The strength of a poker hand. Higher values beat lower values."""
    straight_flush = 9
    four = 8
    full_house = 7
    flush = 6
    straight = 5
    three = 4
    two_pairs = 3
    pair = 2
    high_card = 1


def hand_rep(hand):
    """Return the representation (ie the (s, r) pair) for the given hand."""
    ranks = sorted(RANKS[rank] for rank, _ in hand)
    # Make explicit check for ace-low straight.
    if ranks == [2, 3, 4, 5, 14]:
        ranks = [1, 2, 3, 4, 5]
    suits = [suit for _, suit in hand]

    count = Counter(ranks)
    counts = sorted(count.values())
    distinct_ranks = sorted(count, reverse=True, key=lambda c: (count[c], c))

    flush = all(suit == suits[0] for suit in suits)
    straight = len(distinct_ranks) == 5 and ranks[-1] - ranks[0] == 4

    if straight and flush:
        s = Strength.straight_flush
    elif counts == [1, 4]:
        s = Strength.four
    elif counts == [2, 3]:
        s = Strength.full_house
    elif flush:
        s = Strength.flush
    elif straight:
        s = Strength.straight
    elif counts == [1, 1, 3]:
        s = Strength.three
    elif counts == [1, 2, 2]:
        s = Strength.two_pairs
    elif counts == [1, 1, 1, 2]:
        s = Strength.pair
    else:
        s = Strength.high_card

    return s, distinct_ranks


if __name__ == '__main__':
    with open(FILE, 'r') as f:
        p1_hands = []
        p2_hands = []
        for line in f:
            cards = line.split()
            p1_hands.append(hand_rep(cards[:5]))
            p2_hands.append(hand_rep(cards[5:]))

    p1_wins = sum(
            p1_hand > p2_hand for p1_hand, p2_hand in zip(p1_hands, p2_hands))
    print(p1_wins)
