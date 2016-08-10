#!/usr/bin/env python3
"""Project Euler, Problem 42.

A number is triangular if and only if 8*num + 1 is a perfect square.
"""
FILENAME = 'p042_words.txt'


def get_words(filename):
    """Return a list of words in the given file."""
    with open(filename, 'r') as f:
        text = f.read()

    # Split by ',', then remove surrounding quotation marks.
    return (field[1:-1] for field in text.split(','))


def is_perfect_square(n):
    """Return True if given number is a perfect square."""
    if n < 0:
        return False

    x = 0
    while x * x <= n:
        if x * x == n:
            return True
        x += 1

    return False


def is_triangular_word(word):
    """Return True if and only if given word is a triangular word."""
    word_value = sum(ord(c) - ord('A') + 1 for c in word)
    return is_perfect_square(8 * word_value + 1)


if __name__ == '__main__':
    words = get_words(FILENAME)
    triangular_words = sum(is_triangular_word(word) for word in words)
    print(triangular_words)
