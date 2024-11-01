import time
from src.grid import Grid
from src.ant import Ant
from src.simulation import simulate_step
from src.terminal_ui import render_grid

def main() -> None:
    grid = Grid()
    ant = Ant(position=(0, 0), direction='up')
    viewport_size = (80, 24)  # width, height

    while True:
        render_grid(grid, ant, viewport_size)
        ant, grid = simulate_step(ant, grid)
        x, y = ant.position
        half_width, half_height = viewport_size[0] // 2, viewport_size[1] // 2
        if not (-half_width <= x <= half_width and -half_height <= y <= half_height):
            print("Ant has moved out of the viewport. Exiting.")
            break
        time.sleep(0.1)

if __name__ == '__main__':
    main()
