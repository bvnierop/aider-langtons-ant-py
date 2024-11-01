import unittest
from src.simulation import simulate_step
from src.ant import Ant
from src.grid import Grid

class TestSimulation(unittest.TestCase):
    def test_simulate_step_on_white_cell_turns_clockwise_flips_to_dark_moves_forward(self):
        grid = Grid()
        ant = Ant(position=(0, 0), direction='up')
        new_ant, new_grid = simulate_step(ant, grid)

        # Ant should turn clockwise from 'up' to 'right'
        self.assertEqual(new_ant.direction, 'right')

        # Cell should be flipped to 'dark'
        self.assertEqual(new_grid.get_cell_color((0, 0)), 'dark')

        # Ant should have moved forward to (1, 0)
        self.assertEqual(new_ant.position, (1, 0))

    def test_simulate_step_on_dark_cell_turns_counterclockwise_flips_to_white_moves_forward(self):
        grid = Grid()
        grid.set_cell_color((0, 0), 'dark')
        ant = Ant(position=(0, 0), direction='up')
        new_ant, new_grid = simulate_step(ant, grid)

        # Ant should turn counterclockwise from 'up' to 'left'
        self.assertEqual(new_ant.direction, 'left')

        # Cell should be flipped to 'white'
        self.assertEqual(new_grid.get_cell_color((0, 0)), 'white')

        # Ant should have moved forward to (-1, 0)
        self.assertEqual(new_ant.position, (-1, 0))

    def test_grid_state_after_multiple_steps(self):
        grid = Grid()
        ant = Ant(position=(0, 0), direction='up')

        # First step: white cell
        ant, grid = simulate_step(ant, grid)
        self.assertEqual(ant.direction, 'right')
        self.assertEqual(grid.get_cell_color((0, 0)), 'dark')
        self.assertEqual(ant.position, (1, 0))

        # Second step: white cell
        ant, grid = simulate_step(ant, grid)
        self.assertEqual(ant.direction, 'down')
        self.assertEqual(grid.get_cell_color((1, 0)), 'dark')
        self.assertEqual(ant.position, (1, 1))

        # Third step: white cell
        ant, grid = simulate_step(ant, grid)
        self.assertEqual(ant.direction, 'left')
        self.assertEqual(grid.get_cell_color((1, 1)), 'dark')
        self.assertEqual(ant.position, (0, 1))

        # Fourth step: dark cell
        ant, grid = simulate_step(ant, grid)
        self.assertEqual(ant.direction, 'down')
        self.assertEqual(grid.get_cell_color((0, 1)), 'white')
        self.assertEqual(ant.position, (0, 2))

    def test_ant_state_after_step_on_invalid_cell_color_raises_value_error(self):
        grid = Grid()
        ant = Ant(position=(0, 0), direction='up')
        grid.set_cell_color((0, 0), 'blue')  # Invalid color

        with self.assertRaises(ValueError):
            simulate_step(ant, grid)

if __name__ == '__main__':
    unittest.main()
