import unittest
from random import randint
import os
from battleship import Ship

class battleshipTest(unittest.TestCase):
    def setUp(self):
        ship1 = Ship(4)
        ship2 = Ship("3")
        ship2 = Ship("2")
        ship2 = Ship("1")

    def testShot(self):
        self.assertEqual(print("4"),[" ".join(str(coords) for coords in self.coordinates)])