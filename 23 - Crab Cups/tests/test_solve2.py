#!/usr/bin/env  python3

import unittest

from part2 import solve


class TestSolve2(unittest.TestCase):
    def test1(self):
        data = tuple(map(int, '389125467')) + tuple(range(10, 1_000_000))
        answer = solve(data, 10_000_000)
        self.assertEqual(answer, 149245887792)
