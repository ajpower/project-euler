#!/usr/bin/env python3
"""Project Euler, Problem 22."""
FILE_NAME = "p022_names.txt"


def alphabetical_value(name):
    """Return the alphabetical value (ie the sum of the alphabetical positions
    of each character) of 'name', assuming the 'name' is in capital letters.
    """
    value = 0
    for char in name:
        value += ord(char) - 64

    return value


def total_score():
    """Return the sum of scores for all names in 'FILE_NAME'.
    """
    name_file = open(FILE_NAME, 'r')
    name_file_text = name_file.read()
    name_file.close()

    # put 'name_file_text' into an array
    names = [name[1:-1] for name in name_file_text.split(',')]

    # sort 'names' alphabetically
    names.sort()

    # compute total score
    total_score = 0
    for i in range(len(names)):
        score = alphabetical_value(names[i]) * (i + 1)
        total_score += score

    return total_score


def main():
    """Print the sum of scores for all names in 'FILE_NAME'.
    """
    print(total_score())


if __name__ == "__main__":
    main()
