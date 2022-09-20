from ej5test import *
import unittest
class test(unittest.TestCase):
    def test1(self):
        self.assertEqual(consecutive([1, 3, 5, 7], 3, 7), False)
    def test2(self):
        self.assertEqual(consecutive([1, 3, 5, 7], 3, 1), True)
    def test3(self):
        self.assertEqual(consecutive([1, 6, 9, -3, 4, -78, 0], -3, 4), True)
