#!/usr/bin/env  python3


from part1 import (
        load_input,
        map_ingredient_to_allergen,
        Dish,
        )
from pathlib import Path
from typing import (
        Iterable,
        Mapping,
        Sequence,
        Set,
        Tuple,
        )


def solve(dishes: Sequence[Dish]) -> str:
    """
    Solve part 2 of the puzzle.
    """
    ingredient_to_allergen = map_ingredient_to_allergen(dishes)

    alphabetical_order = sorted(ingredient_to_allergen.items())
    allergens = map(lambda t: t[1], alphabetical_order)

    return ','.join(allergens)





if __name__ == '__main__':
    #data = load_input(Path('test1'))
    #data = load_input(Path('test2'))
    data = load_input()

    answer = solve(data)

    # rhvbn,mmcpg,kjf,fvk,lbmt,jgtb,hcbdb,zrb
    assert answer == 'rhvbn,mmcpg,kjf,fvk,lbmt,jgtb,hcbdb,zrb'
    print(f'Answer: {answer}')
