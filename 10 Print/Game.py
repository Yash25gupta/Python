import pygame
from random import randint
WIDTH = 800
HEIGHT = 600
SPACING = 20
TITLE = '10 Print - Yash Gupta'
COL_BG = (120, 40, 120)
WHITE = (255, 255, 255)


class Game(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.ROWS = HEIGHT // SPACING
        self.COLS = WIDTH // SPACING
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        self.FPS = 60
        self.x, self.y = 0, 0
        self.screen.fill(COL_BG)
        self.playing = True
        while self.playing:
            self.clock.tick(self.FPS)
            self.events()
            self.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.playing = False

    def update(self):
        if randint(0, 1) < 0.5:
            pygame.draw.line(self.screen, WHITE, (self.x, self.y), (self.x + SPACING, self.y + SPACING), 5)
        else:
            pygame.draw.line(self.screen, WHITE, (self.x, self.y + SPACING), (self.x + SPACING, self.y), 5)
        self.x += SPACING
        if self.x > WIDTH:
            self.x = 0
            self.y += SPACING
        if self.y > HEIGHT:
            self.FPS = 1
        pygame.display.update()


if __name__ == '__main__':
    game = Game()
    while game.running:
        game.run()
    pygame.quit()
