#!/usr/bin/env  python3

import re

from collections import (
        defaultdict,
        )
from pathlib import Path
from typing import (
        Iterable,
        Sequence,
        Tuple,
        )



def get_masks(mask: str) -> Tuple[int, int]:
    """
    """
    return (
            int(re.sub(r'X', '1', mask), 2),
            int(re.sub(r'X', '0', mask), 2),
            )



def parse_input(lines: Iterable) -> int:
    """
    Convert one line of the puzzle's data.
    """
    return tuple(tuple(int(v) for v in line.strip().split()) for line in lines)



def load_input(input_fn: Path = Path('input')):
    """
    Load the puzzle's data.
    """
    with input_fn.open('r') as input_f:
        yield from input_f



def solve(data: Sequence[int]) -> int:
    """
    Solve part 1 of the puzzle.
    """
    mem = dict()
    mask_and, mask_or = None, None
    for instruction in map(str.strip, data):
        if instruction.startswith('mask'):
            mask_and, mask_or = get_masks(instruction.split()[2])
        elif instruction.startswith('mem'):
            m, _, value = instruction.split()
            value = int(value)
            mem[m] = (value & mask_and) | mask_or
        else:
            raise Exception(f'Invalid instruction {instruction}')

    return sum(mem.values(), 0)





if __name__ == '__main__':
    print([bin(a) for a in get_masks('X111000X0101100001000000100011X0000X')])
    print([bin(a) for a in get_masks('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X')])

    #data = load_input(Path('test1'))
    #data = load_input(Path('test2'))
    data = load_input()

    answer = solve(data)

    print(f'Answer: {answer}')
