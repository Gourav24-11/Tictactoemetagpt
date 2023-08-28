import pygame
from board import Board
from player import Player
from ai import AI

class Game:
    def __init__(self):
        self.board = Board(3)
        self.player1 = Player('X')
        self.player2 = Player('O')
        self.ai = AI('O')
        self.current_player = self.player1
        self.winner = None

    def start_game(self):
        pygame.init()
        self.screen = pygame.display.set_mode((300, 400))
        pygame.display.set_caption("Tic Tac Toe")
        self.clock = pygame.time.Clock()
        self.running = True

        while self.running:
            self.handle_events()
            self.update()
            self.render()

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.current_player == self.player1:
                    self.make_move_human()
                else:
                    self.make_move_ai()

    def update(self):
        if self.board.is_winner(self.player1.get_symbol()):
            self.winner = self.player1
        elif self.board.is_winner(self.player2.get_symbol()):
            self.winner = self.player2
        elif self.board.is_full():
            self.winner = None

    def render(self):
        self.screen.fill((255, 255, 255))
        self.draw_board()
        self.draw_winner()
        pygame.display.flip()
        self.clock.tick(60)

    def draw_board(self):
        size = self.board.get_size()
        cell_size = 100
        margin = 10
        for row in range(size):
            for col in range(size):
                x = col * (cell_size + margin)
                y = row * (cell_size + margin)
                pygame.draw.rect(self.screen, (0, 0, 0), (x, y, cell_size, cell_size), 2)
                symbol = self.board.get_cell(row, col)
                if symbol:
                    font = pygame.font.Font(None, 100)
                    text = font.render(symbol, True, (0, 0, 0))
                    text_rect = text.get_rect(center=(x + cell_size // 2, y + cell_size // 2))
                    self.screen.blit(text, text_rect)

    def draw_winner(self):
        if self.winner:
            font = pygame.font.Font(None, 50)
            text = font.render(f"Winner: {self.winner.get_symbol()}", True, (0, 0, 0))
            text_rect = text.get_rect(center=(150, 350))
            self.screen.blit(text, text_rect)

    def make_move_human(self):
        mouse_pos = pygame.mouse.get_pos()
        cell_size = 100
        margin = 10
        row = mouse_pos[1] // (cell_size + margin)
        col = mouse_pos[0] // (cell_size + margin)
        if self.board.set_cell(row, col, self.current_player.get_symbol()):
            self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def make_move_ai(self):
        row, col = self.ai.get_best_move(self.board)
        self.board.set_cell(row, col, self.current_player.get_symbol())
        self.current_player = self.player1 if self.current_player == self.player2 else self.player2

    def restart_game(self):
        self.board = Board(3)
        self.current_player = self.player1
        self.winner = None

    def get_current_state(self):
        return str(self.board)

    def get_winner(self):
        if self.winner:
            return self.winner.get_symbol()
        else:
            return None

    def get_current_player(self):
        return self.current_player.get_symbol()

    def make_move(self, row: int, col: int):
        if self.board.set_cell(row, col, self.current_player.get_symbol()):
            self.current_player = self.player2 if self.current_player == self.player1 else self.player1
            return True
        return False
