#!/usr/bin/env  python3

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



def parse_input(lines: Iterable[str]) -> Tuple[Sequence[int], Sequence[int]]:
    """
    Convert one line of the puzzle's data.
    """
    decks = [[], []]
    for line in map(str.strip, lines):
        if line.startswith('Player'):
            _, player_id = line.split()
            player_id = int(player_id[:-1]) - 1
        elif line == '':
            pass
        else:
            decks[player_id].append(int(line))

    assert len(decks[0]) == len(decks[1])

    return decks



def load_input(input_fn: Path = Path('input')):
    """
    Load the puzzle's data.
    """
    with input_fn.open('r') as input_f:
        return parse_input(input_f)



def solve(decks: Tuple[Sequence[int], Sequence[int]]) -> int:
    """
    Solve part 1 of the puzzle.
    """
    deck1, deck2 = decks
    while len(deck1) > 0 and len(deck2) > 0:
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)
        if card1 > card2:
            deck1.extend((card1, card2))
        elif card2 > card1:
            deck2.extend((card2, card1))
        else:
            assert card1 != card2

    if len(deck1) > 0:
        deck = deck1
    else:
        deck = deck2

    return sum((a*(b+1) for a, b in zip(reversed(deck), range(len(deck)))))





if __name__ == '__main__':
    #data = load_input(Path('test1'))
    #data = load_input(Path('test2'))
    data = load_input()
    print(data)

    answer = solve(data)

    # 32598
    print(f'Answer: {answer}')
    assert answer == 32598
