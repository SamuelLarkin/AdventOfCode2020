#!/usr/bin/env  python3


from part1 import (
        load_input,
        solve,
        )
from pathlib import Path
from typing import (
        Iterable,
        Mapping,
        Sequence,
        Set,
        Tuple,
        )



if __name__ == '__main__':
    #data = load_input(Path('test1'))
    #data = load_input(Path('test2'))
    rules, data = load_input(Path('input2'))

    answer = solve(rules, data)

    # 439
    print('The solution was to manually augment the grammar to add a couple of recursive rules.')
    print(f'Answer: {answer}')
