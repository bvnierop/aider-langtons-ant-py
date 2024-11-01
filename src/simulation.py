from typing import Tuple
from .grid import Grid
from .ant import Ant, turn_clockwise, turn_counterclockwise, move_forward

def simulate_step(ant: Ant, grid: Grid) -> Tuple[Ant, Grid]:
    current_color = grid.get_cell_color(ant.position)
    
    if current_color == 'white':
        new_direction = turn_clockwise(ant.direction)
        grid.set_cell_color(ant.position, 'dark')
    else:
        new_direction = turn_counterclockwise(ant.direction)
        grid.set_cell_color(ant.position, 'white')
    
    new_position = move_forward(ant.position, new_direction)
    new_ant = Ant(position=new_position, direction=new_direction)
    
    return new_ant, grid
