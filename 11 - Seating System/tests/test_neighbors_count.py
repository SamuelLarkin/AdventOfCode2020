#!/usr/bin/env  python3

import unittest

from collections import (
        Counter,
        )
from part1 import (
        parse_input,
        load_input,
        )
from part2 import (
        neighbors_count
        )
from pathlib import Path



class TestNeighborsCount(unittest.TestCase):
    def test1(self):
        test_fn = Path(__file__).parent / 'test2a'
        data = load_input(test_fn)
        #print(*data, sep='\n')

        answer = neighbors_count(3, 4, data)
        #print(answer)
        self.assertEqual(len(list(answer.elements())), 8)
        self.assertEqual(answer, Counter('########'))


    def test2(self):
        test_fn = Path(__file__).parent / 'test2b'
        data = load_input(test_fn)
        #print(*data, sep='\n')

        answer = neighbors_count(1, 1, data)
        #print(answer)
        self.assertEqual(len(list(answer.elements())), 8)
        self.assertEqual(answer, Counter('L.......'))


    def test3(self):
        test_fn = Path(__file__).parent / 'test2c'
        data = load_input(test_fn)
        #print(*data, sep='\n')

        answer = neighbors_count(3, 3, data)
        #print(answer)
        self.assertEqual(len(list(answer.elements())), 8)
        self.assertEqual(answer, Counter('........'))





if __name__ == '__main__':
    unittest.main()
