import unittest
from src.grid import Grid

class TestGrid(unittest.TestCase):
    def test_get_cell_color_returns_white_for_new_grid(self):
        grid = Grid()
        self.assertEqual(grid.get_cell_color((0, 0)), 'white')
        self.assertEqual(grid.get_cell_color((1, -1)), 'white')

    def test_set_cell_color_to_dark(self):
        grid = Grid()
        grid.set_cell_color((0, 0), 'dark')
        self.assertEqual(grid.get_cell_color((0, 0)), 'dark')

    def test_set_cell_color_to_white(self):
        grid = Grid()
        grid.set_cell_color((0, 0), 'dark')
        grid.set_cell_color((0, 0), 'white')
        self.assertEqual(grid.get_cell_color((0, 0)), 'white')

    def test_set_cell_color_invalid_value_raises_value_error(self):
        grid = Grid()
        with self.assertRaises(ValueError):
            grid.set_cell_color((0, 0), 'blue')

if __name__ == '__main__':
    unittest.main()
