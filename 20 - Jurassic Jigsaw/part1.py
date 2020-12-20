#!/usr/bin/env  python3

import math
import numpy as np

from collections import (
        defaultdict,
        Counter,
        )
from dataclasses import dataclass
from functools import (
        reduce,
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


@dataclass
class Tile:
    t: int
    r: int
    b: int
    l: int



def parse_input(lines: Iterable[str]):
    """
    Convert one line of the puzzle's data.
    """
    puzzle_tiles = dict()
    tile = []
    tile_id = None
    for line in map(str.strip, lines):
        if line == '':
            continue
        if line.startswith('Tile'):
            if len(tile) > 0:
                puzzle_tiles[tile_id] = np.array(tile)
                tile = []
            tile_id = int(line[5:-1])
        else:
            tile.append(tuple(line))

    if len(tile) > 0:
        puzzle_tiles[tile_id] = np.array(tile)

    num_puzzle_tiles = len(puzzle_tiles)
    assert num_puzzle_tiles > 0
    assert int(math.sqrt(num_puzzle_tiles)) * int(math.sqrt(num_puzzle_tiles)) == num_puzzle_tiles
    assert all(len(tile) == len(puzzle_tiles[tile_id]) for tile in puzzle_tiles.values())
    assert all(tile.shape == puzzle_tiles[tile_id].shape for tile in puzzle_tiles.values())

    return puzzle_tiles



def load_input(input_fn: Path = Path('input')):
    """
    Load the puzzle's data.
    """
    with input_fn.open('r') as input_f:
        return parse_input(input_f)



def left_edge(tile):
    return tuple(tile[:,0].tolist())



def right_edge(tile):
    return tuple(tile[:,-1].tolist())



def top_edge(tile):
    return tuple(tile[0,:].tolist())



def bottom_edge(tile):
    return tuple(tile[-1,:].tolist())



def tile_to_tuple(tile) -> Tuple[Tuple]:
    return tuple(tuple(l) for l in tile)



def generate_tile_variant(tile):
    if False:
        test = set((tile_to_tuple(np.rot90(tile, i)) for i in range(4)))
        test |= set(tile_to_tuple(np.fliplr(np.rot90(tile, i))) for i in range(4))
        test |= set(tile_to_tuple(np.flipud(np.rot90(tile, i))) for i in range(4))

        yield from test
    else:
        yield from (np.rot90(tile, i) for i in range(4))
        yield from (np.fliplr(np.rot90(tile, i)) for i in range(4))



def solve(tiles: Mapping) -> int:
    """
    Solve part 1 of the puzzle.
    """
    if True:
        # How many different version of a tile are there when we rotate/flip them?
        t = tiles[3461]
        test = set((tile_to_tuple(np.rot90(t, i)) for i in range(4)))
        test |= set(tile_to_tuple(np.fliplr(np.rot90(t, i))) for i in range(4))
        test |= set(tile_to_tuple(np.flipud(np.rot90(t, i))) for i in range(4))

    if True:
        # Can we find 4 corners without rotating any tile?
        a, b, c, d= [], [], [], []
        left_edges   = set(left_edge(u) for u in data.values())
        right_edges  = set(right_edge(u) for u in data.values())
        top_edges    = set(top_edge(u) for u in data.values())
        bottom_edges = set(bottom_edge(u) for u in data.values())
        for i, t in tiles.items():
            if len(set((right_edge(t),)) & left_edges) == 1:
                if len(set((top_edge(t),)) & bottom_edges) == 1:
                    a.append(i)
                elif len(set((bottom_edge(t),)) & top_edges) == 1:
                    b.append(i)
            elif len(set((left_edge(t),)) & right_edges) == 1:
                if len(set((top_edge(t),)) & bottom_edges) == 1:
                    c.append(i)
                elif len(set((bottom_edge(t),)) & top_edges) == 1:
                    d.append(i)

    common_edge = defaultdict(set)
    for tile_id, tile in tiles.items():
        for variant in generate_tile_variant(tile):
            common_edge[left_edge(variant)].add(tile_id)
            common_edge[right_edge(variant)].add(tile_id)
            common_edge[top_edge(variant)].add(tile_id)
            common_edge[bottom_edge(variant)].add(tile_id)
    print(*common_edge.items(), sep='\n')
    print('{} tiles have at least an edge compatible with another tile'.format(len(list(filter(lambda t: len(t) > 1, common_edge.values())))))

    # Can we find our corner tiles?
    corner_tile_ids = set()
    for tile_id, tile in tiles.items():
        num_neighbor = Counter((len(c) for c in common_edge.values() if tile_id in c))
        if num_neighbor[2] == 4:
            corner_tile_ids.add(tile_id)

    return reduce(lambda a, b: a* b, corner_tile_ids)





if __name__ == '__main__':
    #data = load_input(Path('test1'))
    #data = load_input(Path('test2'))
    data = load_input()
    print(*data, sep='\n')
    print(len(data))

    answer = solve(data)

    # 13983397496713
    assert answer == 13983397496713
    print(f'Answer: {answer}')
