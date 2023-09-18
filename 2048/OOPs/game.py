from tile import *
from random import choice, randint


class Game(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.font = pygame.font.SysFont('Arial', 25)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        self.grid = [[Tile(i, j) for j in range(4)] for i in range(4)]
        self.randomTile = None
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
                    self.rotate(1)
                    self.operate()
                    self.rotate(3)
                    self.draw()
                elif event.key == pygame.K_UP:
                    self.rotate(2)
                    self.operate()
                    self.rotate(2)
                    self.draw()
                elif event.key == pygame.K_RIGHT:
                    self.rotate(3)
                    self.operate()
                    self.rotate(1)
                    self.draw()

    def draw(self):
        self.screen.fill(LIGHT_GRAY)
        for row in self.grid:
            for tile in row:
                tile.draw(self.screen)
        pygame.display.update()

    def addNewNumber(self):
        options = [tile for row in self.grid for tile in row if tile.value == 0]
        if len(options) == 0:
            print('Game Over')
        if self.randomTile:
            self.randomTile.highlight = False
        self.randomTile = choice(options)
        self.randomTile.value = 2 if (randint(0, 100) > 20) else 4
        self.randomTile.highlight = True

    def slide(self):
        for i in range(4):
            row = [tile for tile in self.grid[i] if tile.value != 0]
            row2 = [Tile(0, 0) for _ in range(4-len(row))]
            row2.extend(row)
            j = 0
            for tile in row2:
                tile.i = i
                tile.j = j
                j += 1
            self.grid[i] = row2

    def combine(self):
        for i in range(4):
            for j in range(2, -1, -1):
                if self.grid[i][j].value == self.grid[i][j+1].value:
                    self.grid[i][j].value = 0
                    self.grid[i][j+1].value *= 2
    
    def rotate(self, times=1):
        for _ in range(times):
            self.grid = list(zip(*self.grid[::-1]))
        for a in range(4):
            for b in range(4):
                self.grid[a][b].i = a
                self.grid[a][b].j = b

    def operate(self):
        self.past = [x[:] for x in self.grid]
        self.slide()
        self.combine()
        self.slide()
        if self.past == self.grid:
            return
        self.addNewNumber()


if __name__ == '__main__':
    game = Game()
    while game.running:
        game.run()
    pygame.quit()
