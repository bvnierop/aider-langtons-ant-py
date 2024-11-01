import unittest
from src.grid import Grid
from src.ant import Ant
from src.simulation import simulate_step

class TestSimulation(unittest.TestCase):
    def setUp(self):
        self.grid = Grid()
        self.ant = Ant(position=(0, 0), direction='up')

    def test_simulate_step_on_white(self):
        new_ant, new_grid = simulate_step(self.ant, self.grid)
        self.assertEqual(new_ant.direction, 'right')
        self.assertEqual(new_grid.get_cell_color((0, 0)), 'dark')
        self.assertEqual(new_ant.position, (1, 0))

    def test_simulate_step_on_dark(self):
        self.grid.set_cell_color((0, 0), 'dark')
        new_ant, new_grid = simulate_step(self.ant, self.grid)
        self.assertEqual(new_ant.direction, 'left')
        self.assertEqual(new_grid.get_cell_color((0, 0)), 'white')
        self.assertEqual(new_ant.position, (-1, 0))

    def test_simulate_multiple_steps(self):
        # First step: white -> turn right, set to dark, move to (1,0)
        ant1, grid1 = simulate_step(self.ant, self.grid)
        self.assertEqual(ant1.direction, 'right')
        self.assertEqual(grid1.get_cell_color((0, 0)), 'dark')
        self.assertEqual(ant1.position, (1, 0))

        # Second step: white -> turn right, set to dark, move to (1,1)
        ant2, grid2 = simulate_step(ant1, grid1)
        self.assertEqual(ant2.direction, 'down')
        self.assertEqual(grid2.get_cell_color((1, 0)), 'dark')
        self.assertEqual(ant2.position, (1, 1))

        # Third step: white -> turn right, set to dark, move to (0,1)
        ant3, grid3 = simulate_step(ant2, grid2)
        self.assertEqual(ant3.direction, 'left')
        self.assertEqual(grid3.get_cell_color((1, 1)), 'dark')
        self.assertEqual(ant3.position, (0, 1))

if __name__ == '__main__':
    unittest.main()
