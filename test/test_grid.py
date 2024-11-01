import unittest
from src.grid import Grid

class TestGrid(unittest.TestCase):
    def setUp(self):
        self.grid = Grid()

    def test_get_cell_color_default(self):
        self.assertEqual(self.grid.get_cell_color((0, 0)), 'white')

    def test_set_and_get_cell_color(self):
        self.grid.set_cell_color((1, 1), 'dark')
        self.assertEqual(self.grid.get_cell_color((1, 1)), 'dark')

    def test_set_cell_color_overwrite(self):
        self.grid.set_cell_color((2, 2), 'dark')
        self.grid.set_cell_color((2, 2), 'white')
        self.assertEqual(self.grid.get_cell_color((2, 2)), 'white')

if __name__ == '__main__':
    unittest.main()
