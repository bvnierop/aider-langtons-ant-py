import os
from typing import Tuple
from .grid import Grid
from .ant import Ant

def clear_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def render_grid(grid: Grid, ant: Ant, viewport_size: Tuple[int, int]) -> None:
    clear_screen()
    width, height = viewport_size
    center_x, center_y = 0, 0  # Assuming the ant starts at (0,0)
    half_width, half_height = width // 2, height // 2

    for y in range(center_y - half_height, center_y + half_height):
        line = ""
        for x in range(center_x - half_width, center_x + half_width):
            if (x, y) == ant.position:
                if ant.direction == 'up':
                    line += '↑'
                elif ant.direction == 'right':
                    line += '→'
                elif ant.direction == 'down':
                    line += '↓'
                elif ant.direction == 'left':
                    line += '←'
                else:
                    line += 'A'
            else:
                color = grid.get_cell_color((x, y))
                if color == 'white':
                    line += '⬜'
                else:
                    line += '⬛'
        print(line)
