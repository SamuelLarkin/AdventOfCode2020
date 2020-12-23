#!/usr/bin/env  python3

from collections import (
        defaultdict,
        )
from game_with_array_of_next_cup import (
        play_game as play_game_with_array_of_next_cup,
        )
from game_with_circular_linked_list import (
        play_game as play_game_with_circular_linked_list,
        )
from itertools import (
        chain,
        )
from pathlib import Path
from sllist import (
        Node,
        make_circular_list,
        )
from tqdm import trange
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
    return tuple(int(v) for v in lines.readline().strip())



def load_input(input_fn: Path = Path('input')):
    """
    Load the puzzle's data.
    """
    with input_fn.open('r') as input_f:
        return parse_input(input_f)



def solve_with_circular_linked_list(data: Tuple[int], num_rounds: int = 100) -> int:
    """
    Solve part 1 of the puzzle.
    """
    current_cup = play_game_with_circular_linked_list(data, num_rounds)

    one = current_cup.find(1)
    answer = []
    node = one.next
    for _ in range(8):
        answer.append(node.data)
        node = node.next

    return ''.join(map(str, answer))



def solve_with_array_of_next_cup(data: Tuple[int], num_rounds: int = 100) -> int:
    """
    Solve part 1 of the puzzle.
    Even circular list is too slow.
    Using an array where arr[cup] = next_cup
    """
    next_cups = play_game_with_array_of_next_cup(data, num_rounds)

    answer = []
    n = 1
    for i in range(len(data)-1):
        answer.append(next_cups[n])
        n = next_cups[n]

    return ''.join(map(str, answer))





if __name__ == '__main__':
    #data = load_input(Path('test1'))
    #data = load_input(Path('test2'))
    #data = tuple(map(int, '389125467'))
    data = load_input()
    print(data)

    answer = solve_with_array_of_next_cup(data)

    # 98645732 
    print(f'Answer: {answer}')
    assert answer == '98645732'
