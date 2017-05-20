#!/usr/bin/env python3
"""Project Euler, Problem 61."""
from itertools import count, dropwhile, permutations, takewhile
from typing import Iterable, Iterator, List, Sequence


def triangular(n: int) -> int:
    return n * (n + 1) // 2


def square(n: int) -> int:
    return n * n


def pentagonal(n: int) -> int:
    return n * (3 * n - 1) // 2


def hexagonal(n: int) -> int:
    return n * (2 * n - 1)


def heptagonal(n: int) -> int:
    return n * (5 * n - 3) // 2


def octagonal(n: int) -> int:
    return n * (3 * n - 2)


def four_digit_nums(seq: Iterable[int]) -> Iterator[int]:
    """Return a iterator of four digit numbers from input iterable assuming that
    it is sorted."""
    return takewhile(lambda n: n < 10000, dropwhile(lambda n: n < 1000, seq))


def gen_nonlooping_chains(sequences: Sequence[Sequence[int]]) -> Iterator[
    List[int]]:
    """Yield a chain of four digit integers from the sequence of sequences that
    does not loop."""
    if len(sequences) == 1:
        for n in sequences[0]:
            yield [n]
        return

    for chain in gen_nonlooping_chains(sequences[:-1]):
        starting_digits = chain[-1] % 100
        for n in filter(lambda n: n // 100 == starting_digits, sequences[-1]):
            chain.append(n)
            yield chain
            chain.pop()


def gen_chains(sequences: Sequence[Sequence[int]]) -> Iterator[List[int]]:
    """Yield a chain of four digit integers from the sequence of sequences that
    does loop."""
    return filter(lambda chain: chain[0] // 100 == chain[-1] % 100,
                  gen_nonlooping_chains(sequences))


if __name__ == '__main__':
    TRIANGULARS = list(four_digit_nums(map(triangular, count(1))))
    SQUARES = list(four_digit_nums(map(square, count(1))))
    PENTAGONALS = list(four_digit_nums(map(pentagonal, count(1))))
    HEXAGONALS = list(four_digit_nums(map(hexagonal, count(1))))
    HEPTAGONALS = list(four_digit_nums(map(heptagonal, count(1))))
    OCTAGONALS = list(four_digit_nums(map(octagonal, count(1))))

    # Starting sequence doesn't matter because cyclic, so set to triangular.
    for sequences in permutations(
            [SQUARES, PENTAGONALS, HEXAGONALS, HEPTAGONALS, OCTAGONALS]):
        sequences = (TRIANGULARS,) + sequences
        for chain in gen_chains(sequences):
            print(sum(chain))
