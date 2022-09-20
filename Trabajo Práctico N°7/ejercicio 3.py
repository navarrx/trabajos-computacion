from ej3test import *
import unittest
class test(unittest.TestCase):
    def test1(self):
        self.assertEqual(missing_no(nums), 5)
    def test2(self):
        self.assertEqual(missing_no(nums), 10)
