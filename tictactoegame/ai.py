from typing import Tuple

from board import Board


class AI:
    def __init__(self, symbol: str):
        self.symbol = symbol

    def get_symbol(self) -> str:
        return self.symbol

    def get_best_move(self, board: Board) -> Tuple[int, int]:
        size = board.get_size()
        best_score = float('-inf')
        best_move = None

        for row in range(size):
            for col in range(size):
                if board.get_cell(row, col) == ' ':
                    board.set_cell(row, col, self.symbol)
                    score = self.minimax(board, 0, False)
                    board.set_cell(row, col, ' ')

                    if score > best_score:
                        best_score = score
                        best_move = (row, col)

        return best_move

    def minimax(self, board: Board, depth: int, is_maximizing: bool) -> int:
        if board.is_winner(self.symbol):
            return 1
        elif board.is_winner(self.get_opponent_symbol()):
            return -1
        elif board.is_full():
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for row in range(board.get_size()):
                for col in range(board.get_size()):
                    if board.get_cell(row, col) == ' ':
                        board.set_cell(row, col, self.symbol)
                        score = self.minimax(board, depth + 1, False)
                        board.set_cell(row, col, ' ')
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for row in range(board.get_size()):
                for col in range(board.get_size()):
                    if board.get_cell(row, col) == ' ':
                        board.set_cell(row, col, self.get_opponent_symbol())
                        score = self.minimax(board, depth + 1, True)
                        board.set_cell(row, col, ' ')
                        best_score = min(score, best_score)
            return best_score

    def get_opponent_symbol(self) -> str:
        if self.symbol == 'X':
            return 'O'
        else:
            return 'X'
