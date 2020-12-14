#!/usr/bin/env  python3

import unittest

from part2 import (
        parse_mem,
        )


class TestParseMem(unittest.TestCase):
    def test1(self):
        address, value = parse_mem('mem[42] = 100')
        self.assertEqual(address, '000000000000000000000000000000101010')
        self.assertEqual(value, 100)


    def test2(self):
        address, value = parse_mem('mem[26] = 1')
        self.assertEqual(address, '000000000000000000000000000000011010')
        self.assertEqual(value, 1)
