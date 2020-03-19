import pygame
from random import randint
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

players = ('Yellow', 'Red')


class App():
    # --- (global) variables ---
    board = [[0 for col in range(7)] for row in range(6)]

    # --- init ---
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Connect 4')
        self.is_running = False
        self.turn = 0
        self.posx = None

    def quit(self):
        pygame.quit()

    # --- functions ---
    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.posx = event.pos[0]
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.turn % 2 == 0:   # Human Turn
                c = event.pos[0] // 100
                self.update(c, 1)
        elif self.turn % 2 == 1:   # Computer
            c = self.comp_move()
            self.update(c, 2)

    def draw(self, surface):
        self.draw_board(surface, self.board)
        if self.is_wining_move():
            self.show_msg('Player {} wins!!!'.format(
                players[self.turn % 2]), 200)
            self.is_running = False
        if self.is_game_over():
            self.show_msg('GAME OVER. Nobody wins...', 100)
            self.is_running = False

    def update(self, c, p):
        if self.board[5][c] != 0: return
        for r in range(6):
            if self.board[r][c] == 0:
                self.board[r][c] = p
                break
        self.turn += 1

    def is_wining_move(self):
        b = self.board
        for r in range(6):
            for c in range(7):
                # Horizontal
                if c < 4 and (b[r][c] == b[r][c + 1] == b[r][c + 2] == b[r][c + 3] != 0): return True
                # Vertical
                if r < 3 and (b[r][c] == b[r + 1][c] == b[r + 2][c] == b[r + 3][c] != 0): return True
                # Diagonal
                if r < 3 and c < 4 and (b[r][c] == b[r + 1][c + 1] == b[r + 2][c + 2] == b[r + 3][c + 3] != 0): return True
                # -ve Diagonal
                if r > 2 and c < 4 and (b[r][c] == b[r - 1][c + 1] == b[r - 2][c + 2] == b[r - 3][c + 3] != 0): return True
        return False

    def comp_move(self):
        for r in range(6):
            for c in range(7):
                condition = self.board[r - 1][c] != 0
                if r == 0: condition = True
                if self.board[r][c] == 0 and condition:
                    self.board[r][c] = 1
                    if self.is_wining_move():
                        self.board[r][c] = 0
                        return c
                    self.board[r][c] = 2
                    if self.is_wining_move():
                        self.board[r][c] = 0
                        return c
                    self.board[r][c] = 0
        return randint(0, 6)

    def is_game_over(self):
        for r in range(6):
            for c in range(7):
                if 0 == self.board[5 - r][c]: return False
        return True

    def show_msg(self, text, x):
        font = pygame.font.Font('freesansbold.ttf', 36)
        msg = font.render(text, True, WHITE)
        self.screen.blit(msg, (x, 20))

    def draw_board(self, win, b):
        pygame.draw.rect(win, BLUE, (0, 100, 700, 700))
        for r in range(6):
            for c in range(7):
                COLOR = BLACK
                if b[5 - r][c] == 1:
                    COLOR = RED
                if b[5 - r][c] == 2:
                    COLOR = YELLOW
                pygame.draw.circle(
                    win, COLOR, (50 + (c * 100), 150 + (r * 100)), 45)
        pygame.draw.circle(win, RED, (self.posx, 50), 45)

    # --- mainloop --- (don't change it)
    def mainloop(self):
        self.is_running = True
        while self.is_running:
            # --- events ---
            for event in pygame.event.get():
                # --- global events ---
                if event.type == pygame.QUIT:
                    self.is_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.is_running = False
                # --- objects events ---
                self.handle_event(event)

            # --- draws ---
            self.screen.fill(BLACK)
            self.draw(self.screen)
            pygame.display.update()

            # --- FPS ---
            self.clock.tick(25)

        # --- the end ---
        pygame.time.delay(2000)
        self.quit()
# ----------------------------------------------------------------------


if __name__ == '__main__':
    App().mainloop()
