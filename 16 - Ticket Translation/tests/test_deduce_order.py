#!/usr/bin/env  python3

import unittest

from pathlib import Path
from part1 import load_input
from part2 import deduce_order



class TestDeduceOrder(unittest.TestCase):
    def test1(self):
        """
        class is 12, row is 11, and seat is 13.
        """
        constraints, my_ticket, tickets = load_input(Path('test2'))
        order = deduce_order(tickets + (my_ticket,), constraints)
        self.assertEqual(my_ticket[order['class']], 12)
        self.assertEqual(my_ticket[order['row']],   11)
        self.assertEqual(my_ticket[order['seat']],  13)
