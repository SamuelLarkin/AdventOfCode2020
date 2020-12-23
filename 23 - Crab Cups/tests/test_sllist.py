#!/usr/bin/env  python3

import unittest

from sllist import (
        Node,
        make_circular_list,
        )


class TestNode(unittest.TestCase):
    def test1(self):
        a = Node()
        self.assertEqual(a.data, None)
        self.assertEqual(a.next, a)


    def test2(self):
        a = Node(5)
        self.assertEqual(a.data, 5)
        self.assertEqual(a.next, a)



class TestMakeCircularList(unittest.TestCase):
    def test1(self):
        l = make_circular_list((1,))
        self.assertEqual(l.data, 1)
        self.assertEqual(l.next, l)


    def test2(self):
        l = make_circular_list((1,2))
        self.assertEqual(l.data, 1)
        self.assertEqual(l.next.data, 2)
        self.assertEqual(l.next.next, l)


    def test3(self):
        l = make_circular_list((1,2,3))
        self.assertEqual(l.data, 1)
        self.assertEqual(l.next.data, 2)
        self.assertEqual(l.next.next.data, 3)
        self.assertEqual(l.next.next.next, l)


    def test4(self):
        l = make_circular_list((1,2,3,4))
        self.assertEqual(l.data, 1)
        self.assertEqual(l.next.data, 2)
        self.assertEqual(l.next.next.data, 3)
        self.assertEqual(l.next.next.next.data, 4)
        self.assertEqual(l.next.next.next.next, l)
