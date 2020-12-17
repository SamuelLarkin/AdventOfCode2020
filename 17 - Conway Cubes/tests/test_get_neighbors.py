#!/usr/bin/env  python3

import unittest

from part1 import (
        load_input,
        get_neighbors,
        )



class TestGetNeighbors(unittest.TestCase):
    def test1(self):
        c =(2, 5, -2)
        neighbors = set(get_neighbors(c))
        self.assertFalse(c in neighbors)
        self.assertEqual(len(neighbors), 26)
