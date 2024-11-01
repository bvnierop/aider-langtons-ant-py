import unittest
from src.grid import Grid
from typing import Tuple

class TestGrid(unittest.TestCase):
    def setUp(self):
        self.grid = Grid()

    def test_get_cell_color_default_white(self):
        pos: Tuple[int, int] = (5, 5)
        self.assertEqual(self.grid.get_cell_color(pos), 'white')

    def test_set_and_get_cell_color(self):
        pos: Tuple[int, int] = (1, 2)
        self.grid.set_cell_color(pos, 'dark')
        self.assertEqual(self.grid.get_cell_color(pos), 'dark')
        self.grid.set_cell_color(pos, 'white')
        self.assertEqual(self.grid.get_cell_color(pos), 'white')

    def test_set_invalid_color(self):
        pos: Tuple[int, int] = (0, 0)
        with self.assertRaises(ValueError):
            self.grid.set_cell_color(pos, 'blue')
