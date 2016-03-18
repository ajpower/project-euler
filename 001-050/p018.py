#!/usr/bin/env python3
"""Project Euler, Problem 18

For each element in the second to last row, find the adjacent number in the
last row that has the greatest value and add it to the element. Then eleminate
the last row. Repeat the process until there is only one row with one element
left. The value of this final remaining element will be the largest total sum
of elements for all possible paths from the top of the triangle to its bottom.
"""
TRIANGLE_STR = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""


def str2array(triangle_str):
    """Return an array of arrays of integers representing the triangle.
    """
    triangle_array = []
    for row in triangle_str.strip().split('\n'):
        triangle_array.append([int(num) for num in row.split(' ')])
    return triangle_array

def max_total(triangle):
    """Return the maximum sum of integers for all possible paths from the top of
    'triangle' to its bottom. 'triangle' is an array or arrays of integers.
    """
    if len(triangle) == 1:
        return triangle[0][0]

    last_row = triangle[-1]
    for i in range(len(triangle[-2])):
        triangle[-2][i] += max(last_row[i], last_row[i+1])

    else:
        triangle = triangle[:-1]
        return max_total(triangle)

def main():
    """Print the maximum sum of integers for all possible paths from the top of
    'TRIANGLE_STR' to its bottom.
    """
    triangle = str2array(TRIANGLE_STR)
    print(max_total(triangle))


if __name__ == "__main__":
    main()
