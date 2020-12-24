#!/usr/bin/env  python3

import unittest

from pathlib import Path
from part1 import (
        load_input,
        parse_input,
        play_game,
        solve,
        )



class TestPlayGame(unittest.TestCase):
    def test1(self):
        instructions = parse_input(('esew',))
        grid = play_game(instructions)
        print(grid)


    def test_back_to_start(self):
        instructions = parse_input(('nwwswee',))
        grid = play_game(instructions)
        print(grid)



class TestSolve(unittest.TestCase):
    def test1(self):
        instructions = load_input(Path('test1'))
        answer = solve(instructions)
        self.assertEqual(answer, 10)


