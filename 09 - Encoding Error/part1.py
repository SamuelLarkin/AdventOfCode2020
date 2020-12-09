#!/usr/bin/env  python3

from itertools import permutations
from pathlib import Path
from typing import (
        Sequence,
        Tuple,
        )


def load_input(input_fn = Path('input')):
    """
    Parse the puzzle input file.
    """
    with input_fn.open('r') as f:
        return [ int(x) for x in f ]


def puzzle(data: Sequence[int]) -> Tuple[int, Sequence[int]]:
    """
    Generator of puzzle data which are 25 contiguous number and the following
    number.
    """
    for s in range(len(data) - 25 - 1):
        yield data[s:s+25], data[s+25]


def is_valid(data: Sequence[int], answer: int) -> bool:
    """
    Can the answer be computed from any two numbers in data?
    """
    return answer in set(map(sum, permutations(data, 2)))


def solve(data: Sequence[int]) -> int:
    """
    Returns the first number that cannot be computed from the preceding 25
    numbers.
    """
    for d, n in puzzle(data):
        assert len(d) == 25
        #print(d, n, is_valid(d, n))
        if not is_valid(d, n):
            return n





if __name__ == '__main__':
    data = load_input()
    #print(data)
    answer = solve(data)

    # 217430975
    print(f'Answer: {answer}')
