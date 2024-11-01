from typing import Dict, Tuple

class Grid:
    def __init__(self) -> None:
        self._cells: Dict[Tuple[int, int], str] = {}

    def get_cell_color(self, position: Tuple[int, int]) -> str:
        return self._cells.get(position, 'white')

    def set_cell_color(self, position: Tuple[int, int], color: str) -> None:
        if color not in ['white', 'dark']:
            raise ValueError(f"Invalid color: {color}")
        self._cells[position] = color
