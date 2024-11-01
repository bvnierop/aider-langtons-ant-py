from typing import Tuple, Dict

class Grid:
    def __init__(self) -> None:
        self.cells: Dict[Tuple[int, int], str] = {}

    def get_cell_color(self, position: Tuple[int, int]) -> str:
        return self.cells.get(position, 'white')

    def set_cell_color(self, position: Tuple[int, int], color: str) -> None:
        self.cells[position] = color
