import unittest
from src.ant import turn_clockwise, turn_counterclockwise, move_forward, Ant

class TestAnt(unittest.TestCase):
    def test_turn_clockwise(self):
        self.assertEqual(turn_clockwise('up'), 'right')
        self.assertEqual(turn_clockwise('right'), 'down')
        self.assertEqual(turn_clockwise('down'), 'left')
        self.assertEqual(turn_clockwise('left'), 'up')

    def test_turn_counterclockwise(self):
        self.assertEqual(turn_counterclockwise('up'), 'left')
        self.assertEqual(turn_counterclockwise('left'), 'down')
        self.assertEqual(turn_counterclockwise('down'), 'right')
        self.assertEqual(turn_counterclockwise('right'), 'up')

    def test_move_forward_up(self):
        ant = Ant(position=(0, 0), direction='up')
        new_position = move_forward(ant.position, ant.direction)
        self.assertEqual(new_position, (0, -1))

    def test_move_forward_right(self):
        ant = Ant(position=(0, 0), direction='right')
        new_position = move_forward(ant.position, ant.direction)
        self.assertEqual(new_position, (1, 0))

    def test_move_forward_down(self):
        ant = Ant(position=(0, 0), direction='down')
        new_position = move_forward(ant.position, ant.direction)
        self.assertEqual(new_position, (0, 1))

    def test_move_forward_left(self):
        ant = Ant(position=(0, 0), direction='left')
        new_position = move_forward(ant.position, ant.direction)
        self.assertEqual(new_position, (-1, 0))

    def test_move_forward_invalid_direction(self):
        with self.assertRaises(ValueError):
            move_forward((0, 0), 'invalid')

if __name__ == '__main__':
    unittest.main()
