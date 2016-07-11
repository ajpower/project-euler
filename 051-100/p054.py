#!/usr/bin/env python3
"""Project Euler, Problem 54
"""
from collections import Counter


class Card:
    def __init__(self, card):
        """'card' is a string of the form <number><suit>."""
        if card[0] == 'A':
            self.number = 14
        elif card[0] == 'K':
            self.number = 13
        elif card[0] == 'Q':
            self.number = 12
        elif card[0] == 'J':
            self.number = 11
        elif card[0] == 'T':
            self.number = 10
        else:
            self.number = int(card[0])
        self.suit = card[1]

    def __lt__(self, other):
        return self.number < other.number

    def __le__(self, other):
        return self.number <= other.number

    def __eq__(self, other):
        return self.number == other.number

    def __ne__(self, other):
        return self.number != other.number

    def __gt__(self, other):
        return self.number > other.number

    def __ge__(self, other):
        return self.number >= other.number

    def __str__(self):
        to_print = ""
        if self.number == 14:
            to_print += 'A'
        elif self.number == 13:
            to_print += 'K'
        elif self.number == 12:
            to_print += 'Q'
        elif self.number == 11:
            to_print += 'J'
        elif self.number == 10:
            to_print += 'T'
        else:
            to_print += str(self.number)

        to_print += self.suit

        return to_print

    def __sub__(self, other):
        return self.number - other.number


class PokerHand:
    def __init__(self, hand):
        """'hand' is a space seperated string of the player's cards."""
        self.hand = sorted([Card(card) for card in hand.split()])
        self._card_counter = Counter()
        for card in self.hand:
            self._card_counter[card.number] += 1

    def __str__(self):
        to_print = ""
        for card in self.hand:
            to_print += str(card) + " "

        return to_print.strip()

    def quads(self):
        return self._card_counter.most_common(1)[0][1] == 4

    def triple(self):
        return self._card_counter.most_common()[0][1] == 3 and \
               not self._card_counter.most_common()[1][1] == 3

    def two_pair(self):
        return self._card_counter.most_common()[0][1] == 2 and \
               self._card_counter.most_common()[1][1] == 2

    def pair(self):
        return self._card_counter.most_common()[0][1] == 2 and \
               not self._card_counter.most_common()[1][1] == 2

    def fullhouse(self):
        return (self.hand[0] == self.hand[1] == self.hand[2] and self.hand[3] ==
                self.hand[4]) or \
               (self.hand[0] == self.hand[1] and self.hand[2] == self.hand[3] ==
                self.hand[4])

    def flush(self):
        return all([card.suit == self.hand[0].suit for card in self.hand])

    def straight(self):
        return all(
                [self.hand[i] - self.hand[0] == i for i in
                 range(len(self.hand))])

    def rank(self):
        if self.straight() and self.flush():
            return 1
        elif self.quads():
            return 2
        elif self.fullhouse():
            return 3
        elif self.flush():
            return 4
        elif self.straight():
            return 5
        elif self.flush():
            return 6
        elif self.triple():
            return 7
        elif self.two_pair():
            return 8
        elif self.pair():
            return 9
        else:
            return 10


def player_1_wins(hand_1, hand_2):
    if hand_1.rank() < hand_2.rank():
        return True
    if hand_1.rank() > hand_2.rank():
        return False


def main():
    file = open("p054_poker.txt", 'r')
    count = 0
    for line in file:
        cards = line.split()
        hand_1 = PokerHand(" ".join(cards[:5]))
        hand_2 = PokerHand(" ".join(cards[5:]))

        if player_1_wins(hand_1, hand_2):
            count += 1

    print(count)


if __name__ == "__main__":
    main()
