from dataclasses import dataclass
from typing import Tuple

@dataclass(frozen=True)
class Ant:
    position: Tuple[int, int]
    direction: str  # 'up', 'right', 'down', 'left'

def turn_clockwise(direction: str) -> str:
    directions = ['up', 'right', 'down', 'left']
    idx = directions.index(direction)
    return directions[(idx + 1) % 4]

def turn_counterclockwise(direction: str) -> str:
    directions = ['up', 'right', 'down', 'left']
    idx = directions.index(direction)
    return directions[(idx - 1) % 4]

def move_forward(position: Tuple[int, int], direction: str) -> Tuple[int, int]:
    x, y = position
    if direction == 'up':
        return (x, y - 1)
    elif direction == 'right':
        return (x + 1, y)
    elif direction == 'down':
        return (x, y + 1)
    elif direction == 'left':
        return (x - 1, y)
    else:
        raise ValueError(f"Invalid direction: {direction}")
