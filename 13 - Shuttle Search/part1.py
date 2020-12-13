#!/usr/bin/env  python3

from dataclasses import (
        dataclass,
        )
from itertools import (
        zip_longest,
        )
from pathlib import Path
from typing import (
        Iterable,
        Sequence,
        Tuple,
        )


@dataclass
class Schedule:
    time: int
    bus: Tuple[int]


def parse_input(lines: Iterable) -> int:
    """
    Convert one line of the puzzle's data.
    """
    lines = list(lines)
    assert len(lines) == 2
    time = int(lines[0])
    buses = tuple(map(int, filter(lambda x: x!='x', lines[1].split(','))))
    return Schedule(time, buses)


def load_input(input_fn: Path = Path('input')):
    """
    Load the puzzle's data.
    """
    with input_fn.open('r') as input_f:
        return parse_input(input_f)


def solve(schedule: Schedule) -> int:
    """
    Solve part 1 of the puzzle.
    """
    next_departure = tuple(x - (schedule.time % x) for x in schedule.bus)
    m = min(zip(next_departure, schedule.bus))

    return m[0] * m[1]





if __name__ == '__main__':
    #data = load_input(Path('test'))
    #data = load_input(Path('test2'))
    data = load_input()
    print(data)

    answer = solve(data)

    # 2406
    print(f'Answer: {answer}')
