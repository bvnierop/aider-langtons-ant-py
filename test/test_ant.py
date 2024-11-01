import unittest
from src.ant import turn_clockwise, turn_counterclockwise, move_forward

class TestAntFunctions(unittest.TestCase):
    # Tests for turn_clockwise
    def test_turn_clockwise_from_up_returns_right(self):
        self.assertEqual(turn_clockwise('up'), 'right')

    def test_turn_clockwise_from_right_returns_down(self):
        self.assertEqual(turn_clockwise('right'), 'down')

    def test_turn_clockwise_from_down_returns_left(self):
        self.assertEqual(turn_clockwise('down'), 'left')

    def test_turn_clockwise_from_left_returns_up(self):
        self.assertEqual(turn_clockwise('left'), 'up')

    def test_turn_clockwise_with_invalid_direction_raises_value_error(self):
        with self.assertRaises(ValueError):
            turn_clockwise('invalid_direction')

    # Tests for turn_counterclockwise
    def test_turn_counterclockwise_from_up_returns_left(self):
        self.assertEqual(turn_counterclockwise('up'), 'left')

    def test_turn_counterclockwise_from_left_returns_down(self):
        self.assertEqual(turn_counterclockwise('left'), 'down')

    def test_turn_counterclockwise_from_down_returns_right(self):
        self.assertEqual(turn_counterclockwise('down'), 'right')

    def test_turn_counterclockwise_from_right_returns_up(self):
        self.assertEqual(turn_counterclockwise('right'), 'up')

    def test_turn_counterclockwise_with_invalid_direction_raises_value_error(self):
        with self.assertRaises(ValueError):
            turn_counterclockwise('invalid_direction')

    # Tests for move_forward
    def test_move_forward_up(self):
        self.assertEqual(move_forward((0, 0), 'up'), (0, -1))

    def test_move_forward_down(self):
        self.assertEqual(move_forward((0, 0), 'down'), (0, 1))

    def test_move_forward_left(self):
        self.assertEqual(move_forward((0, 0), 'left'), (-1, 0))

    def test_move_forward_right(self):
        self.assertEqual(move_forward((0, 0), 'right'), (1, 0))

    def test_move_forward_with_invalid_direction_raises_value_error(self):
        with self.assertRaises(ValueError):
            move_forward((0, 0), 'invalid_direction')

if __name__ == '__main__':
    unittest.main()
