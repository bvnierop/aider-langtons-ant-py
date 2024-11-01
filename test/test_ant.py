import unittest
from src.ant import turn_clockwise, turn_counterclockwise, move_forward, Ant
from typing import Tuple

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
    
    def test_move_forward(self):
        position = (0, 0)
        self.assertEqual(move_forward(position, 'up'), (0, -1))
        self.assertEqual(move_forward(position, 'down'), (0, 1))
        self.assertEqual(move_forward(position, 'left'), (-1, 0))
        self.assertEqual(move_forward(position, 'right'), (1, 0))
    
    def test_invalid_direction_move_forward(self):
        with self.assertRaises(ValueError):
            move_forward((0, 0), 'invalid')
