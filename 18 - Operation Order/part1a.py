#!/usr/bin/env  python3

from collections import (
        defaultdict,
        )
from itertools import (
        chain,
        )
from pathlib import Path
from shunting_yard import (
        evaluate_reversed_polish_notation,
        shunting_yard_for_part1 as shunting_yard,
        )
from typing import (
        Iterable,
        Iterator,
        Mapping,
        Sequence,
        Set,
        Tuple,
        )



def parse_input(lines: Iterable[str]):
    """
    Convert one line of the puzzle's data.
    """
    no_newline = map(str.strip, lines)

    return tuple(list(''.join(l.split())) for l in no_newline)



def load_input(input_fn: Path = Path('input')):
    """
    Load the puzzle's data.
    """
    with input_fn.open('r') as input_f:
        return parse_input(input_f)



def solve(expressions: Sequence[str]) -> int:
    """
    Solve part 1 of the puzzle.
    """
    parsed    = map(shunting_yard, expressions)
    evaluated = map(evaluate_reversed_polish_notation, parsed)

    return sum(evaluated)





if __name__ == '__main__':
    #data = load_input(Path('test1'))
    #data = load_input(Path('test2'))
    data = load_input()
    #print(*data, sep='\n')

    answer = solve(data)

    # 5783053349377
    print(f'Answer: {answer}')
