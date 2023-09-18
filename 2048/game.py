from constants import *
import pygame
from random import choice


class Game(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.font = pygame.font.SysFont('Arial', 25)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        self.grid = [[0] * 4 for _ in range(4)]
        self.addNewNumber()
        self.addNewNumber()
        self.draw()
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.playing = False
                elif event.key == pygame.K_DOWN:
                    self.operate()
                    self.draw()
                elif event.key == pygame.K_LEFT:
                    self.rotate()
                    self.operate()
                    self.rotate()
                    self.rotate()
                    self.rotate()
                    self.draw()
                elif event.key == pygame.K_UP:
                    self.rotate()
                    self.rotate()
                    self.operate()
                    self.rotate()
                    self.rotate()
                    self.draw()
                elif event.key == pygame.K_RIGHT:
                    self.rotate()
                    self.rotate()
                    self.rotate()
                    self.operate()
                    self.rotate()
                    self.draw()

    def draw(self):
        self.screen.fill(LIGHT_GRAY)
        self.drawGrid()
        pygame.display.update()

    def drawGrid(self):
        w = CELL_WIDTH
        for j in range(4):
            for i in range(4):
                c = TILE_COLOR[self.grid[i][j]]
                x, y = i * w + w, j * w + w
                pygame.draw.rect(self.screen, c, (x, y, w, w), 0, 5)
                pygame.draw.rect(self.screen, BLACK, (x, y, w, w), 1, 5)
                textImg = self.font.render(f'{self.grid[i][j]}', True, BLACK)
                textRect = textImg.get_rect()
                textRect.center = (x+w/2, y+w/2)
                self.screen.blit(textImg, textRect)

    def addNewNumber(self):
        options = [(i, j) for j in range(4)
                   for i in range(4) if self.grid[i][j] == 0]
        if len(options) == 0:
            print('Game Over')
        i, j = choice(options)
        self.grid[i][j] = choice([2, 4])

    def rotate(self):
        self.grid = list(zip(*self.grid[::-1]))

    def slide(self):
        for i in range(4):
            row = [x for x in self.grid[i] if x != 0]
            row2 = [0 for _ in range(4-len(row))]
            row2.extend(row)
            self.grid[i] = row2

    def combine(self):
        for i in range(4):
            for j in range(2, -1, -1):
                if self.grid[i][j] == self.grid[i][j+1]:
                    self.grid[i][j] = 0
                    self.grid[i][j+1] *= 2

    def operate(self):
        past = [x[:] for x in self.grid]
        self.slide()
        self.combine()
        self.slide()
        if past == self.grid:
            return
        self.addNewNumber()


if __name__ == '__main__':
    game = Game()
    while game.running:
        game.run()
    pygame.quit()
