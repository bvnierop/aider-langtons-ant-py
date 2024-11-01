import unittest
from src.grid import Grid

class TestGrid(unittest.TestCase):
    def test_get_cell_color_default_white(self):
        grid = Grid()
        positions = [(0, 0), (1, 1), (-1, -1), (100, 100)]
        for pos in positions:
            self.assertEqual(grid.get_cell_color(pos), 'white')

    def test_set_and_get_cell_color_dark(self):
        grid = Grid()
        position = (2, 3)
        grid.set_cell_color(position, 'dark')
        self.assertEqual(grid.get_cell_color(position), 'dark')

    def test_set_and_get_cell_color_white(self):
        grid = Grid()
        position = (-2, -3)
        grid.set_cell_color(position, 'white')
        self.assertEqual(grid.get_cell_color(position), 'white')

    def test_set_cell_color_invalid_value_raises_value_error(self):
        grid = Grid()
        position = (0, 0)
        with self.assertRaises(ValueError):
            grid.set_cell_color(position, 'blue')

if __name__ == '__main__':
    unittest.main()
