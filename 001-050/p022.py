#!/usr/bin/env python3
"""Project Euler, Problem 22."""
FILE_NAME = "p022_names.txt"


def alphabetical_value(name):
    """Return the alphabetical value (ie the sum of the alphabetical positions
    of each character) of the given name, assuming it is in uppercase letters.
    """
    return sum(ord(char) - ord('A') + 1 for char in name)


if __name__ == '__main__':
    with open(FILE_NAME, 'r') as f:
        file_text = f.read()

    names = [name[1:-1] for name in file_text.split(',')]
    names.sort()

    total_score = sum(
        alphabetical_value(name) * (i + 1) for i, name in enumerate(names))
    print(total_score)
