import unittest
from src.ant import Ant
from src.grid import Grid
from src.simulation import simulate_step

class TestSimulation(unittest.TestCase):
    def test_simulate_step_ant_on_white_cell_turns_clockwise_and_turns_cell_to_dark_and_moves_forward(self):
        grid = Grid()
        ant = Ant(position=(0, 0), direction='up')
        new_ant, new_grid = simulate_step(ant, grid)
        self.assertEqual(new_ant.direction, 'right')  # turned clockwise from 'up'
        self.assertEqual(new_grid.get_cell_color((0, 0)), 'dark')  # cell set to 'dark'
        self.assertEqual(new_ant.position, (1, 0))  # moved forward to 'right'

    def test_simulate_step_ant_on_dark_cell_turns_counterclockwise_and_turns_cell_to_white_and_moves_forward(self):
        grid = Grid()
        grid.set_cell_color((0, 0), 'dark')
        ant = Ant(position=(0, 0), direction='up')
        new_ant, new_grid = simulate_step(ant, grid)
        self.assertEqual(new_ant.direction, 'left')  # turned counterclockwise from 'up'
        self.assertEqual(new_grid.get_cell_color((0, 0)), 'white')  # cell set to 'white'
        self.assertEqual(new_ant.position, (-1, 0))  # moved forward to 'left'

    def test_simulate_step_grid_state_after_step(self):
        grid = Grid()
        ant = Ant(position=(0, 0), direction='up')
        _, grid_after = simulate_step(ant, grid)
        self.assertEqual(grid_after.get_cell_color((0, 0)), 'dark')

    def test_simulate_step_ant_state_after_step(self):
        grid = Grid()
        ant = Ant(position=(0, 0), direction='up')
        new_ant, _ = simulate_step(ant, grid)
        self.assertEqual(new_ant.position, (1, 0))
        self.assertEqual(new_ant.direction, 'right')

    def test_simulate_step_with_invalid_cell_color_raises_value_error(self):
        grid = Grid()
        grid._cells[(0, 0)] = 'blue'  # Set invalid color directly for testing
        ant = Ant(position=(0, 0), direction='up')
        with self.assertRaises(ValueError):
            simulate_step(ant, grid)

if __name__ == '__main__':
    unittest.main()
