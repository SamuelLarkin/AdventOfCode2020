#!/usr/bin/env  python3

import unittest

from pathlib import Path
from part1 import (
        load_input,
        )
from part2 import (
        solve,
        )


class TestSolve2(unittest.TestCase):
    def test1(self):
        deck1, deck2 = load_input(Path('test1'))
        answer = solve(deck1, deck2)
        self.assertEqual(answer, 291)
