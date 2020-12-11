#!/usr/bin/env  python3

import unittest

from part1 import (
        parse_input,
        look,
        )


class TestLook(unittest.TestCase):
    def test1(self):
        data = """.......#.
        ...#.....
        .#.......
        .........
        ..#L....#
        ....#....
        .........
        #........
        ...#....."""
        data = parse_input(data.splitlines())
        print(*data, sep='\n')
        print(neighbors_count(3, 4, data))


    def disabledtest2(self):
        data = """.............
        .L.L.#.#.#.#.
        ............."""
        data = parse_input(data.splitlines())
        print(*data, sep='\n')
        print(neighbors_count(1, 1, data))


    def disabledtest3(self):
        data = """.##.##.
        #.#.#.#
        ##...##
        ...L...
        ##...##
        #.#.#.#
        .##.##."""
        data = parse_input(data.splitlines())
        print(*data, sep='\n')
        print(neighbors_count(3, 3, data))
