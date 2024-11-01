import unittest
from src.ant import Ant
from src.grid import Grid
from src.simulation import simulate_step
from typing import Tuple

class TestSimulation(unittest.TestCase):
    def setUp(self):
        self.grid = Grid()
        self.ant = Ant(position=(0, 0), direction='up')
    
    def test_simulate_step_white_cell(self):
        updated_ant, updated_grid = simulate_step(self.ant, self.grid)
        # Since initial cell is white, ant should turn clockwise to 'right'
        self.assertEqual(updated_ant.direction, 'right')
        # Cell should now be 'dark'
        self.assertEqual(updated_grid.get_cell_color((0, 0)), 'dark')
        # Ant should have moved to (1, 0)
        self.assertEqual(updated_ant.position, (1, 0))
    
    def test_simulate_step_dark_cell(self):
        # First, set the cell to 'dark'
        self.grid.set_cell_color((0, 0), 'dark')
        updated_ant, updated_grid = simulate_step(self.ant, self.grid)
        # Since initial cell is dark, ant should turn counterclockwise to 'left'
        self.assertEqual(updated_ant.direction, 'left')
        # Cell should now be 'white'
        self.assertEqual(updated_grid.get_cell_color((0, 0)), 'white')
        # Ant should have moved to (-1, 0)
        self.assertEqual(updated_ant.position, (-1, 0))
    
    def test_simulate_step_invalid_cell_color(self):
        # Manually set an invalid color
        self.grid.set_cell_color((0, 0), 'blue')
        with self.assertRaises(ValueError):
            simulate_step(self.ant, self.grid)
