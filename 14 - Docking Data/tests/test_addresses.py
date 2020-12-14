#!/usr/bin/env  python3


import unittest

from part2 import (
        addresses,
        INSTRUCTION_LEN,
        )



class TestAddresses(unittest.TestCase):
    def test1(self):
        adds = list(addresses('000000000000000000000000000000101010', '000000000000000000000000000000X1001X'))
        #print(*adds, sep='\n')
        self.assertTrue(all(len(a) == INSTRUCTION_LEN for a in adds))
        expected = (
                    '000000000000000000000000000000011010',
                    '000000000000000000000000000000011011',
                    '000000000000000000000000000000111010',
                    '000000000000000000000000000000111011',
                    )
        self.assertEqual(sorted(adds), sorted(expected))
        self.assertEqual(set(adds), set(expected))


    def test2(self):
        adds = list(addresses('000000000000000000000000000000011010', '00000000000000000000000000000000X0XX'))
        #print(*adds, sep='\n')
        self.assertTrue(all(len(a) == INSTRUCTION_LEN for a in adds))
        expected = (
                    '000000000000000000000000000000010000',
                    '000000000000000000000000000000010001',
                    '000000000000000000000000000000010010',
                    '000000000000000000000000000000010011',
                    '000000000000000000000000000000011000',
                    '000000000000000000000000000000011001',
                    '000000000000000000000000000000011010',
                    '000000000000000000000000000000011011',
                    )
        self.assertEqual(sorted(adds), sorted(expected))
        self.assertEqual(set(adds), set(expected))


    def test3(self):
        adds = list(addresses('0' * INSTRUCTION_LEN, '000011110X1X1110100011XX010X0X0X00XX'))
        self.assertEqual(len(adds), 2**9)


    def test4(self):
        adds = list(addresses('000000000000000000001001010011110110', '11001101X110000X010X01101100X1X0X001'))
