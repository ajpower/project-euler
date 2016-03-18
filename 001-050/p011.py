#!/usr/bin/env python3
"""Project Euler, Problem 11

Brute-force solution.
"""
SEQUENCE_LENGTH = 4
NUMBERS = """
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
""".strip()


def convert_to_grid():
    """Convert `NUMBERS` to a 2D array of NUMBERS, assuming that `NUMBERS` is
    a string of NUMBERS where each row is seperated by a newline and eash column
    is seperated by a space.
    """
    grid = NUMBERS.split('\n')
    for i in range(len(grid)):
        temp = grid[i].split(' ') #list of strings, need ints
        grid[i] = [int(num) for num in temp]

    return grid

def max_product(number_sequence):
    """Return the maximum product of adjacent numbers of length
    `SEQUENCE_LENGTH` in `number_sequence`, assuming that `number_sequence` is a
    list of numbers.
    """
    #Rather than calculate the product of every sequence of length
    #`SEQUENCE_LENGTH` seperately, this algorithm records the result of the
    #previous product and uses it to speed up the calculation. Special
    #provisions have to be made if a sequence will contain a 0. Specifically,
    #`previous_product` is set to zero and the iteration skips ahead to the
    #number immediately after the offending 0.
    _max_product = 0
    previous_product = 0
    i = 0
    while i < len(number_sequence) - (SEQUENCE_LENGTH-1):
        if previous_product == 0:
            previous_product = 1
            for j in range(SEQUENCE_LENGTH):
                previous_product *= number_sequence[i+j]

            i += 1

        elif number_sequence[i+SEQUENCE_LENGTH-1] == 0:
            previous_product = 0
            i += SEQUENCE_LENGTH

        else:
            final_digit = number_sequence[i + SEQUENCE_LENGTH - 1]
            previous_final_digit = number_sequence[i - 1]
            previous_product = (previous_product * final_digit) // previous_final_digit

            i += 1

        if previous_product > _max_product:
            _max_product = previous_product

    return _max_product

def max_horizontal_product(grid):
    """Return the maximum product of horizontally adjacent NUMBERS in `grid` of
    length `SEQUENCE_LENGTH`.
    """
    return max(max_product(row) for row in grid)

def max_vertical_product(grid):
    """Return the maximum product of veritcally adjacent NUMBERS in `grid` of
    length `sequence length`.
    """
    n_rows = len(grid)
    n_cols = len(grid[0])

    vertical_products = []
    for j in range(n_cols):
        column = [grid[i][j] for i in range(n_rows)]
        product = max_product(column)
        vertical_products.append(product)

    return max(vertical_products)

def max_diagonal_product(grid):
    """Return the maximum product of diagonally adjacent NUMBERS in `grid` of
    length `sequence length`.
    """
    n_rows = len(grid)

    downward_diagonal_products = []
    for i in range(n_rows - (SEQUENCE_LENGTH-1)):
        downward_diagonal = [grid[i+j][j] for j in range(n_rows-i)]
        product = max_product(downward_diagonal)
        downward_diagonal_products.append(product)

    upward_diagonal_products = []
    for i in range(4, n_rows):
        upward_diagonal = [grid[i-j][j] for j in range(i+1)]
        product = max_product(upward_diagonal)
        upward_diagonal_products.append(product)

    diagonal_products = downward_diagonal_products + upward_diagonal_products
    return max(diagonal_products)

def main():
    """Find the largest product of consecutive horizontal, vertical, and
    diagonal digits in NUMBERS of length SEQUENCE_LENGTH, then print the
    largest of the three.
    """
    grid = convert_to_grid()
    largest_product = max(max_horizontal_product(grid),
                          max_vertical_product(grid),
                          max_diagonal_product(grid))

    print(largest_product)


if __name__ == "__main__":
    main()
