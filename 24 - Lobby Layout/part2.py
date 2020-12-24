#!/usr/bin/env  python3


from collections import (
        Counter,
        )
from cube import (
        Cube,
        addCube,
        )
from part1 import (
        EmptyGrid,
        MOVES,
        State,
        keep_black_tiles,
        load_input,
        play_game,
        )
from pathlib import Path
from tqdm import trange
from typing import (
        Iterable,
        Mapping,
        Sequence,
        Set,
        Tuple,
        )


def get_neighbors(cell: Cube) -> Cube:
    """
    Generate a cell's 6 neighbors.
    """
    for move in MOVES.values():
        yield addCube(cell, move)



def visit(grid: Mapping[Cube, State]) -> Tuple[Cube, State]:
    """
    Generates the neighbors of the black cells and the black cell themselves.
    """
    visited_cell = set()
    for cell in grid.keys():
        if cell not in visited_cell:
            visited_cell.add(cell)
            yield cell, grid.get(cell, State.White)
        for neighbor in get_neighbors(cell):
            if neighbor not in visited_cell:
                visited_cell.add(cell)
                # Don't use [] since it might change grid if the cell is not present.
                yield neighbor, grid.get(neighbor, State.White)



def conway_game_of_life(grid: Mapping[Cube, State]) -> Mapping[Cube, State]:
    """
    """
    new_grid = EmptyGrid()
    for cell, state in visit(grid):
        # NOTE: cell might not be in the grid and we CAN'T change the grid thus we use get().
        neighbor_states = Counter(map(lambda n: grid.get(n, State.White), get_neighbors(cell)))
        # Any black tile with zero or more than 2 black tiles immediately
        # adjacent to it is flipped to white.
        if state == State.Black and (0 < neighbor_states[State.Black] <= 2):
            new_grid[cell] = State.Black
        # Any white tile with exactly 2 black tiles immediately adjacent to it
        # is flipped to black.
        if state == State.White and neighbor_states[State.Black] == 2:
            new_grid[cell] = State.Black

    return new_grid



def solve(instructions: Sequence[Sequence[str]], num_days: int = 100) -> int:
    """
    Solve part 2 of the puzzle.
    """
    # Initialize the floor's grid.
    grid = play_game(instructions)
    for _ in trange(num_days):
        grid = keep_black_tiles(conway_game_of_life(grid))

    return len(grid)





if __name__ == '__main__':
    #data = load_input(Path('test1'))
    #data = load_input(Path('test2'))
    data = load_input()

    answer = solve(data)

    # 3887
    print(f'Answer: {answer}')
    assert answer == 3887
