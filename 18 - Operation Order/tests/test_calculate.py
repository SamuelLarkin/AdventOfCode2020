#!/usr/bin/env  python3

import unittest

from part1 import calculate


class TestCalculate(unittest.TestCase):
    def test1(self):
        answer = calculate(list('1+2*3+4*5+6'))
        self.assertEqual(answer, 71)


    def test2(self):
        answer = calculate(list('1+(2*3)+(4*(5+6))'))
        self.assertEqual(answer, 51)


    def test3(self):
        answer = calculate(list('2*3+(4*5)'))
        self.assertEqual(answer, 26)


    def test4(self):
        answer = calculate(list('5+(8*3+9+3*4*3)'))
        self.assertEqual(answer, 437)


    def test5(self):
        answer = calculate(list('5*9*(7*3*3+9*3+(8+6*4))'))
        self.assertEqual(answer, 12240)


    def test6(self):
        answer = calculate(list('((2+4*9)*(6+9*8+6)+6)+2+4*2'))
        self.assertEqual(answer, 13632)
