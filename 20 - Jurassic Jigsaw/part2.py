#!/usr/bin/env  python3

import math
import numpy as np

from collections import (
        defaultdict,
        Counter,
        )
from copy import deepcopy
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


lockness = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """


lockness = np.array(
        [ [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0 ],
          [ 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1 ],
          [ 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0 ] ],
        np.int)
LOCKNESS_NUM = 15



@dataclass
class TileOrientation:
    tile_id: int
    variant_id: int
    t: int
    r: int
    b: int
    l: int
    image: np.array



@dataclass
class Tile:
    image: np.array
    variants: Tuple[TileOrientation]



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
                #puzzle_tiles[tile_id] = make_tile(np.array(tile))
                puzzle_tiles[tile_id] = np.array(tile, np.int)
                tile = []
            tile_id = int(line[5:-1])
        else:
            tile.append(tuple(map(lambda a: 0 if a == '.' else 1, line)))

    if len(tile) > 0:
        puzzle_tiles[tile_id] = np.array(tile)

    num_puzzle_tiles = len(puzzle_tiles)
    assert num_puzzle_tiles > 0
    assert int(math.sqrt(num_puzzle_tiles)) * int(math.sqrt(num_puzzle_tiles)) == num_puzzle_tiles
    assert all(len(tile) == len(puzzle_tiles[tile_id]) for tile in puzzle_tiles.values())
    assert all(tile.shape == puzzle_tiles[tile_id].shape for tile in puzzle_tiles.values())

    variants =( v for t in puzzle_tiles.values() for v in generate_tile_variant(t) )
    edges = set( e for v in variants for e in generate_edges(v) )
    edge_to_id = { e: i for i, e in enumerate(edges) }
    def make_tile(tile_id, tile):
        variants = tuple(
                TileOrientation(
                    tile_id,
                    variant_id,
                    edge_to_id[top_edge(t)],
                    edge_to_id[right_edge(t)],
                    edge_to_id[bottom_edge(t)],
                    edge_to_id[left_edge(t)],
                    t,
                    ) for variant_id, t in enumerate(generate_tile_variant(tile))
                )
        assert len(variants) == 8
        return Tile(tile, variants)

    return { tile_id: make_tile(tile_id, tile) for tile_id, tile in puzzle_tiles.items() }



def load_input(input_fn: Path = Path('input')):
    """
    Load the puzzle's data.
    """
    with input_fn.open('r') as input_f:
        return parse_input(input_f)



def left_edge(tile):
    return tuple(tile[0,:].tolist())



def right_edge(tile):
    return tuple(tile[-1,:].tolist())



def top_edge(tile):
    return tuple(tile[:,0].tolist())



def bottom_edge(tile):
    return tuple(tile[:,-1].tolist())



def tile_to_tuple(tile) -> Tuple[Tuple]:
    return tuple(tuple(l) for l in tile)



def generate_tile_variant(tile):
    yield from (np.rot90(tile, i) for i in range(4))
    yield from (np.fliplr(np.rot90(tile, i)) for i in range(4))



def generate_edges(tile):
    yield top_edge(tile)
    yield right_edge(tile)
    yield bottom_edge(tile)
    yield left_edge(tile)



def arrange_tile(grid, tiles, used_tiles: Set[int] = set(), position: int = 0):
    """
    """
    if len(used_tiles) == 144:
        # We have found a complete grid.
        return grid

    y = position // 12
    x = position % 12

    g = None
    for tile_id in set(tiles.keys()) - used_tiles:
        tile = tiles[tile_id]
        for v in tile.variants:
            #new_grid = deepcopy(grid)
            if y == 0:
                if x == 0:
                    # First tile thus there is no constraint to verify.
                    grid[y][x] = v
                    g = arrange_tile(grid, tiles, used_tiles | set((tile_id,)), position + 1)
                    if g is not None:
                        return g
                else:
                    # First row, there is only the tile to the left to satisfy.
                    if grid[y][x-1].r == v.l:
                        grid[y][x] = v
                        g = arrange_tile(grid, tiles, used_tiles | set((tile_id,)), position + 1)
                        if g is not None:
                            return g
            else:
                # Rows other than the first one.
                # The new tile must fit with the one above it.
                if grid[y-1][x].b == v.t:
                    if x == 0:
                        grid[y][x] = v
                        g = arrange_tile(grid, tiles, used_tiles | set((tile_id,)), position + 1)
                        if g is not None:
                            return g
                    else:
                        # The new cell must be compatible with the one on it left.
                        if grid[y][x-1].r == v.l:
                            grid[y][x] = v
                            g = arrange_tile(grid, tiles, used_tiles | set((tile_id,)), position + 1)
                            if g is not None:
                                return g
    return g



def arrange_tile2(grid, tiles, common_edge, used_tiles: Set[int] = set(), position: int = 0):
    """
    """
    if len(used_tiles) == 144:
        # We have found a complete grid.
        return grid

    y = position // 12
    x = position % 12

    g = None
    if y == 0:
        if x == 0:
            pass
        else:
            left = grid[y][x-1]
            for n in common_edge[left.r] - used_tiles:
                grid[y][x] = n
                g = arrange_tile2(grid, tiles, common_edge, used_tiles | set((n.tile_id,)), position + 1)
                if g != None:
                    return g
    else:
        upper = grid[y-1][x]
        if x == 0:
            for n in common_edge[upper.b] - used_tiles:
                grid[y][x] = n
                g = arrange_tile2(grid, tiles, common_edge, used_tiles | set((n.tile_id,)), position + 1)
                if g != None:
                    return g
        else:
            left = grid[y][x-1]
            for n in common_edge[upper.b] - common_edge[left.r] - used_tiles:
                grid[y][x] = n
                g = arrange_tile2(grid, tiles, common_edge, used_tiles | set((n.tile_id,)), position + 1)
                if g != None:
                    return g

    return None



def arrange_tile3(tiles: Sequence[Tile], common_edge: Mapping[str, Set]):
    """
    """
    def get_neighbors(position):
        yield (position[0], position[1]+1)
        yield (position[0], position[1]-1)
        yield (position[0]+1, position[1])
        yield (position[0]-1, position[1])

    grid: Mapping[Tuple[int,int], TileOrientation] = dict()
    grid[(0,0)] = tiles[3461].variants[0]
    bfs_next_position = [(0,0)]
    while len(bfs_next_position) > 0:
        position = bfs_next_position.pop()
        assert position in bfs_next_position
        for neighbor in get_neighbors(position):
            if neighbor not in bfs_next_position:
                bfs_next_position.append(neighbor)
                grid[neighbor] = common_edge

    assert len(set(tile.tile_id for tile in grid.values())) == 144
    # TODO: recenter the grid

    return grid



def solve(tiles: Mapping) -> int:
    """
    Solve part 1 of the puzzle.
    """
    common_edge = defaultdict(set)
    for tile_id, tile in tiles.items():
        for variant in tile.variants:
            common_edge[variant.t].add(tile_id)
            common_edge[variant.r].add(tile_id)
            common_edge[variant.t].add(tile_id)
            common_edge[variant.l].add(tile_id)
    print(*common_edge.items(), sep='\n')
    print('{} tiles have at least an edge compatible with another tile'.format(len(list(filter(lambda t: len(t) > 1, common_edge.values())))))

    if False:
        # Can we find our corner tiles?
        corner_tile_ids = set()
        for tile_id, tile in tiles.items():
            num_neighbor = Counter((len(c) for c in common_edge.values() if tile_id in c))
            if num_neighbor[2] == 4:
                corner_tile_ids.add(tile_id)

    # Find the tile layout.
    grid = [ [None] * 12 for _ in range(12) ]
    grid = arrange_tile(grid, tiles)
    print(*grid, sep='\n')

    # Assemble the image from the tiles.
    image = np.zeros((12*8, 12*8), np.int)
    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            image[x*8:(x+1)*8, y*8:(y+1)*8] = cell.image[1:-1, 1:-1]
    print(image)
    np.savetxt('delme', image, fmt='%i')

    # What is the orientation of the final image.
    for _image in generate_tile_variant(image):
        count = 0
        for x in range(_image.shape[0] - lockness.shape[0]):
            for y in range(_image.shape[1] - lockness.shape[1]):
                if sum((_image[x:x+lockness.shape[0], y:y+lockness.shape[1]] * lockness).ravel()) == LOCKNESS_NUM:
                    count += 1
        if count > 1:
            return sum(_image.ravel()) - count * LOCKNESS_NUM

    return None





if __name__ == '__main__':
    #data = load_input(Path('test1'))
    #data = load_input(Path('test2'))
    data = load_input()
    #print(*data.items(), sep='\n')
    #print(len(data))

    answer = solve(data)

    # 2424
    assert answer == 2424
    print(f'Answer: {answer}')
