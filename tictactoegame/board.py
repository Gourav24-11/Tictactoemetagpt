## board.py

from typing import Optional

class Board:
    def __init__(self, size: int):
        self.size = size
        self.cells = [[' ' for _ in range(size)] for _ in range(size)]

    def get_size(self) -> int:
        return self.size

    def get_cell(self, row: int, col: int) -> Optional[str]:
        if 0 <= row < self.size and 0 <= col < self.size:
            return self.cells[row][col]
        return None

    def set_cell(self, row: int, col: int, symbol: str) -> bool:
        if 0 <= row < self.size and 0 <= col < self.size and self.cells[row][col] == ' ':
            self.cells[row][col] = symbol
            return True
        return False

    def is_full(self) -> bool:
        for row in self.cells:
            if ' ' in row:
                return False
        return True

    def is_winner(self, symbol: str) -> bool:
        # Check rows
        for row in self.cells:
            if all(cell == symbol for cell in row):
                return True

        # Check columns
        for col in range(self.size):
            if all(row[col] == symbol for row in self.cells):
                return True

        # Check diagonals
        if all(self.cells[i][i] == symbol for i in range(self.size)):
            return True
        if all(self.cells[i][self.size - 1 - i] == symbol for i in range(self.size)):
            return True

        return False
