#!/usr/bin/env  python3

import unittest

from part1 import (
        solve_with_array_of_next_cup,
        solve_with_circular_linked_list,
        )



class TestSolve1WithCircularLinkedList(unittest.TestCase):
    def test10(self):
        data = tuple(map(int, '389125467'))
        answer = solve_with_circular_linked_list(data, 10)
        self.assertEqual(answer, '92658374')


    def test100(self):
        data = tuple(map(int, '389125467'))
        answer = solve_with_circular_linked_list(data, 100)
        self.assertEqual(answer, '67384529')



class TestSolve1WithArrayOfNextCup(unittest.TestCase):
    def test10(self):
        data = tuple(map(int, '389125467'))
        answer = solve_with_array_of_next_cup(data, 10)
        self.assertEqual(answer, '92658374')


    def test100(self):
        data = tuple(map(int, '389125467'))
        answer = solve_with_array_of_next_cup(data, 100)
        self.assertEqual(answer, '67384529')
