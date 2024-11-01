import os
from typing import Tuple
from src.grid import Grid
from src.ant import Ant

def clear_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def render_grid(grid: Grid, ant: Ant, viewport_size: Tuple[int, int]) -> None:
    clear_screen()
    width, height = viewport_size
    half_width, half_height = width // 2, height // 2

    for y in range(-half_height, half_height + 1):
        line = ''
        for x in range(-half_width, half_width + 1):
            pos = (x, y)
            if pos == ant.position:
                line += 'A'
            else:
                color = grid.get_cell_color(pos)
                if color == 'dark':
                    line += '█'
                else:
                    line += ' '
        print(line)
