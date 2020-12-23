#!/usr/bin/env  python3

import sys

from game_with_array_of_next_cup import (
        play_game,
        )
from part1 import (
        load_input,
        )
from pathlib import Path
from sllist import make_circular_list
from tqdm import trange
from typing import (
        Iterable,
        Mapping,
        Sequence,
        Set,
        Tuple,
        )


def solve(data: Sequence[int], num_rounds: int = 10_000_000) -> int:
    """
    Solve part 2 of the puzzle.
    """
    next_cups = play_game(data, num_rounds)

    next1 = next_cups[1]
    next2 = next_cups[next1]

    return next1 * next2





if __name__ == '__main__':
    #data = load_input(Path('test1'))
    #data = load_input(Path('test2'))
    data = load_input()

    M = 1_000_000
    data = data + tuple(range(10, M+1))
    assert len(data) == M
    answer = solve(data, num_rounds=10_000_000)

    # 689500518476
    print(f'Answer: {answer}')
    assert answer == 689500518476
