from ej4test import *
import unittest
class test(unittest.TestCase):
    def test1(self):
        self.assertEqual(bingo(1,2,3,4,5,6,7,8,9,10), "LOSE")
    def test2(self):
        self.assertEqual(bingo(20,12,23,14,6,22,12,17,2,26), "LOSE")
    def test3(self):
        self.assertEqual(bingo(1,2,3,7,5,14,7,16,9,10), "WIN")
    def test4(self):
        self.assertEqual(bingo(5,2,13,7,5,14,17,16,9,10), "WIN")