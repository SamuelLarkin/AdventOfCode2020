#!/usr/bin/env  python3


from part1 import (
        load_input,
        )
from pathlib import Path
from shunting_yard import (
        evaluate_reversed_polish_notation,
        shunting_yard,
        )
from typing import (
        Iterable,
        Mapping,
        Sequence,
        Set,
        Tuple,
        )



def solve(expressions: Sequence[int]) -> int:
    """
    Solve part 2 of the puzzle.
    """
    parsed    = ( shunting_yard(e, '+') for e in expressions )
    evaluated = map(evaluate_reversed_polish_notation, parsed)

    return sum(evaluated)





if __name__ == '__main__':
    #data = load_input(Path('test1'))
    #data = load_input(Path('test2'))
    data = load_input()
    #print(data)

    answer = solve(data)

    # 74821486966872
    print(f'Answer: {answer}')
