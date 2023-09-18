from Constants import *
from Cell import *
from APathFinder import *


class Game2(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH+10, WIDTH+10))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        self.grid = self.createMaze()
        self.current = self.grid[0]
        self.end = self.grid[-1]
        self.path = None
        self.mPath = []
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.playing = False
                elif event.key == pygame.K_SPACE:
                    pathFinder = APathFinder(self, self.grid[0], self.grid[-1])
                    self.path = pathFinder.findPath()

    def update(self):
        if self.current == self.end:
            print('game over\nYou won!!!')
            self.playing = False
        if PLAY_MANUAL:
            i, j, pos = self.current.i, self.current.j, None
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                isWall = self.current.walls[0]
                pos = index(i, j - 1)
            elif keys[pygame.K_RIGHT]:
                isWall = self.current.walls[1]
                pos = index(i + 1, j)
            elif keys[pygame.K_DOWN]:
                isWall = self.current.walls[2]
                pos = index(i, j + 1)
            elif keys[pygame.K_LEFT]:
                isWall = self.current.walls[3]
                pos = index(i - 1, j)
            if pos and not isWall:
                nextCell = self.grid[pos]
                if nextCell in self.mPath:
                    self.mPath.remove(nextCell)
                else:
                    self.mPath.append(self.current)
                self.current = nextCell
        

    def draw(self):
        self.screen.fill(COL_BACKGROUND)
        for cell in self.grid:
            cell.draw(self.screen)
        if self.path:
            for cell in self.path:
                cell.draw(self.screen, PINK)
        # for cell in self.mPath:
        #     cell.draw(self.screen, PINK)
        self.end.draw(self.screen, RED)
        self.current.highLight(self.screen)
        pygame.display.update()

    def createMaze(self):
        grid = [Cell(i, j, CELL_WIDTH) for i in range(ROWS) for j in range(ROWS)]
        current = grid[0]
        current.visited = True
        stack = [current]
        while True:
            nextCell = current.getRendomNeighbour(grid)
            if nextCell:
                nextCell.visited = True
                stack.append(nextCell)
                self.removeWalls(current, nextCell)
                current = nextCell
            elif len(stack) > 0:
                current = stack.pop()
            else:
                break
        return grid

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
    game = Game2()
    while game.running:
        game.run()
    pygame.quit()
