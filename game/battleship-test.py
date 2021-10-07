import unittest
from random import randint
import os
from battleship import Ship


class battleshipTest(unittest.TestCase):
    def setUp(self):
        ship1 = Ship('4', 'horizontal', '6')
        ship2 = Ship('3', 'vertical', '3')
        ship2 = Ship('2', 'horizontal', '1')
        ship2 = Ship('1', 'vertical', '5')

    def testShot(self):
        self.assertEqual(print("4"), [" ".join(str(coords) for coords in self.coordinates)])
        self.assertEqual(print("3"), [" ".join(str(coords) for coords in self.coordinates)])
        self.assertEqual(print("2"), [" ".join(str(coords) for coords in self.coordinates)])
        self.assertEqual(print("1"), [" ".join(str(coords) for coords in self.coordinates)])


if __name__ == '__main__':
    unittest.main()
