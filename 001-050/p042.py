#!/usr/bin/env python3
"""Project Euler, Problem 42

A number is triangular if and only if 8*num + 1 is a perfect square.
"""
FILENAME = "p042_words.txt"

def get_words(filename):
    """Return a list of words in 'filename'.
    """
    text = open(filename, 'r').read()
    
    # Split by ',', then remove surrounding quotation marks.
    words = [field[1:-1] for field in text.split(',')]
    return words

def is_perfect_square(n):
    """Return True if 'n' is a perfect square.
    """
    if n < 0:
        return False

    x = 0
    while x**2 <= n:
        if x**2 == n:
            return True
        x += 1

    return False

def is_triangular_word(word):
    """Return True if and only if 'word' is a triangular word.
    """
    word_value = 0
    for char in word:
        word_value += ord(char) - ord('A') + 1

    return is_perfect_square(8*word_value + 1)

def main():
    triangular_words = 0
    words = get_words(FILENAME)
    for word in words:
        if is_triangular_word(word):
            triangular_words += 1

    print(triangular_words)


if __name__ == "__main__":
    main()
