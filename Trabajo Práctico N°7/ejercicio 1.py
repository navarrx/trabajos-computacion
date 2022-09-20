from ej1test import *
import unittest
class test(unittest.TestCase):
    def test1(self):
        self.assertEqual(sum_of_differences(1, 2, 10), 9)
    def test2(self):
        self.assertEqual(sum_of_differences(-3, -2, -1), 2)
    def test3(self):
        self.assertEqual(sum_of_differences(-17, 17, 0), 34)
