#!/usr/bin/env  python3

import unittest

from part1 import (
        calculate,
        solve,
        )



class TestCalculate(unittest.TestCase):
    def test_card(self):
        answer = calculate(8)
        self.assertEqual(answer, 5764801)


    def test_door(self):
        answer = calculate(11)
        self.assertEqual(answer, 17807724)


    def test_encryption_key_from_card(self):
        answer = calculate(8, 17807724)
        self.assertEqual(answer, 14897079)


    def test_encryption_key_from_door(self):
        answer = calculate(11, 5764801)
        self.assertEqual(answer, 14897079)



class TestSolve(unittest.TestCase):
    def test1(self):
        answer = solve(5764801, 17807724)
        self.assertEqual(answer, 14897079)
