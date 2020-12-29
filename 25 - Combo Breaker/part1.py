#!/usr/bin/env  python3

# * [Cryptography/A Basic Public Key Example](https://en.wikibooks.org/wiki/Cryptography/A_Basic_Public_Key_Example)
# * [Shor's algorithm](https://en.wikipedia.org/wiki/Shor%27s_algorithm)

from collections import (
        defaultdict,
        )
from itertools import (
        chain,
        )
from pathlib import Path
from typing import (
        Iterable,
        Mapping,
        Sequence,
        Set,
        Tuple,
        )



def parse_input(lines: Iterable[str]):
    """
    Convert one line of the puzzle's data.
    """
    return tuple(map(int, map(str.strip, lines)))



def load_input(input_fn: Path = Path('input')):
    """
    Load the puzzle's data.
    """
    with input_fn.open('r') as input_f:
        return parse_input(input_f)



def calculate(loop_size: int, subject_number: int = 7) -> int:
    value = 1
    for _ in range(loop_size):
        value = (value * subject_number) % 20201227

    return value



def solve(card: int, door: int) -> int:
    """
    Solve part 1 of the puzzle.
    """
    card_loop_size = None
    door_loop_size = None
    i = 0
    value = 1
    while card_loop_size is None or door_loop_size is None:
        i += 1
        value *= 7
        value %= 20201227
        if card_loop_size is None and card == value:
            card_loop_size = i
        if door_loop_size is None and door == value:
            door_loop_size = i

    assert calculate(card_loop_size, door) == calculate(door_loop_size, card)

    return calculate(card_loop_size, door)





if __name__ == '__main__':
    #data = load_input(Path('test1'))
    #data = load_input(Path('test2'))
    data = load_input()
    print(data)

    answer = solve(*data)

    # 3217885
    print(f'Answer: {answer}')
    assert answer == 3217885
