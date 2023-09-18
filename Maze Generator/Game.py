from Constants import *
from Cell import *

class Game(object):
    '''Maze Generator Visualizer using Python'''
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH+10, WIDTH+10))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        self.grid = [Cell(i, j, CELL_WIDTH) for i in range(ROWS) for j in range(ROWS)]
        self.current = self.grid[0]
        self.current.visited = True
        self.stack = [self.current]
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.playing = False

    def update(self):
        nextCell = self.current.getRendomNeighbour(self.grid)
        if nextCell:
            nextCell.visited = True
            self.stack.append(nextCell)
            self.removeWalls(self.current, nextCell)
            self.current = nextCell
        elif len(self.stack) > 0:
            self.current = self.stack.pop()

    def draw(self):
        self.screen.fill(COL_BACKGROUND)
        for cell in self.grid:
            cell.draw(self.screen)
        for cell in self.stack:
            cell.draw(self.screen, PURPLE)
        self.current.highLight(self.screen)
        pygame.display.update()

    def removeWalls(self, a, b):
        dx = a.i - b.i
        if dx == 1:
            a.walls[3] = False
            b.walls[1] = False
        elif dx == -1:
            a.walls[1] = False
            b.walls[3] = False
        dy = a.j - b.j
        if dy == 1:
            a.walls[0] = False
            b.walls[2] = False
        elif dy == -1:
            a.walls[2] = False
            b.walls[0] = False


if __name__ == '__main__':
    game = Game()
    while game.running:
        game.run()
    pygame.quit()
