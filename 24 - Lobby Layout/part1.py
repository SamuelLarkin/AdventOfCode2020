#!/usr/bin/env  python3

# Links:
# * [How do I represent a hextile/hex grid in memory?](https://stackoverflow.com/questions/1838656/how-do-i-represent-a-hextile-hex-grid-in-memory)
# * [Hexagonal Grids](https://www.redblobgames.com/grids/hexagons/)
# * [Amit’s Thoughts on Grids](http://www-cs-students.stanford.edu/~amitp/game-programming/grids/)


from collections import (
        defaultdict,
        )
from cube import (
        Cube,
        addCube,
        )
from enum import Enum
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



MOVES = {
        'e':  Cube(+1, -1, 0),
        'ne': Cube(+1, 0, -1),
        'se': Cube(0, -1, +1), 
        'w':  Cube(-1, +1, 0),
        'nw': Cube(0, +1, -1),
        'sw': Cube(-1, 0, +1),
        }


class State(Enum):
    White = False
    Black = True



def EmptyGrid():
    return defaultdict(lambda: State.White)



def parse_input(lines: Iterable[str]):
    """
    Convert one line of the puzzle's data.
    """
    def parse(line: str):
        i = 0
        while i < len(line):
            c = line[i]
            if c in ('e', 'w'):
                yield c
                i += 1
            elif c in ('n', 's'):
                if i+1 < len(line):
                    d = line[i+1]
                    if d in ('e', 'w'):
                        yield c+d
                        i += 1
                else:
                    yield c
                i += 1

    return tuple(tuple(parse(line.strip())) for line in lines)



def load_input(input_fn: Path = Path('input')):
    """
    Load the puzzle's data.
    """
    with input_fn.open('r') as input_f:
        return parse_input(input_f)



def play_game(
        instructions: Sequence[Sequence[str]],
        ) -> Mapping[Cube, State]:
    """
    """
    grid = EmptyGrid()
    for instruction in instructions:
        cell = Cube(0, 0, 0)
        for move in instruction:
            #cell = cell + MOVES[move]
            cell = addCube(cell, MOVES[move])
        grid[cell] = State(not grid[cell].value)

    return grid



def keep_black_tiles(grid: Mapping[Cube, State]) -> Mapping[Cube, State]:
    filtered_grid = EmptyGrid()
    filtered_grid.update(filter(lambda t: t[1] == State.Black, grid.items()))

    return filtered_grid



def solve(instructions: Sequence[Sequence[str]]) -> int:
    """
    Solve part 1 of the puzzle.
    """
    grid = play_game(instructions)

    return len(keep_black_tiles(grid))





if __name__ == '__main__':
    #data = load_input(Path('test1'))
    #data = load_input(Path('test2'))
    data = load_input()
    #print(*data, sep='\n')

    answer = solve(data)

    # 356
    print(f'Answer: {answer}')
    assert answer == 356
