#!/usr/bin/env  python3

import unittest

from part1 import solve



class TestSolve1(unittest.TestCase):
    def test0(self):
        answer = solve((0, 3, 6))
        self.assertEqual(answer, 436)


    def test1(self):
        answer = solve((1, 3, 2))
        self.assertEqual(answer, 1)


    def test2(self):
        answer = solve((2, 1, 3))
        self.assertEqual(answer, 10)


    def test3(self):
        answer = solve((1, 2, 3))
        self.assertEqual(answer, 27)


    def test4(self):
        answer = solve((2, 3, 1))
        self.assertEqual(answer, 78)


    def test5(self):
        answer = solve((3, 2, 1))
        self.assertEqual(answer, 438)


    def test6(self):
        answer = solve((3, 1, 2))
        self.assertEqual(answer, 1836)
