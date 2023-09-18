from Constants import *
from PathFinder import *
from Cube import *


class Game(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, WIDTH))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        self.grid = makeCubeGrid()
        self.start = self.end = None
        self.findingPath = False
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    
    def getNeighbours(self, node):
        neighbours = []
        for x, y in ((-1, 0), (0, -1), (0, 1), (1, 0)): # , (-1, -1), (-1, 1), (1, -1), (1, 1)):
            checkX, checkY = node.row + x, node.col + y
            if 0 <= checkX < ROWS and 0 <= checkY < ROWS and not self.grid[checkX][checkY].isWall():
                neighbours.append(self.grid[checkX][checkY])
        return neighbours

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN and not self.findingPath:
                if event.key == pygame.K_SPACE and self.start and self.end:
                    self.findingPath = True
                    pathFinder = PathFinder(self, self.start, self.end)
                    pathFinder.findPath()
                row, col = getRCfrom(pygame.mouse.get_pos())
                if event.key == pygame.K_s:
                    if self.start:
                        self.start.makeNone()
                    self.start = self.grid[row][col]
                    self.start.makeStart()
                if event.key == pygame.K_e:
                    if self.end:
                        self.end.makeNone()
                    self.end = self.grid[row][col]
                    self.end.makeEnd()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                self.playing = False

    def update(self):
        if not self.findingPath and pygame.mouse.get_pressed()[0]:
            row, col = getRCfrom(pygame.mouse.get_pos())
            if self.grid[row][col] not in (self.start, self.end):
                self.grid[row][col].makeWall()
        if not self.findingPath and pygame.mouse.get_pressed()[2]:
            row, col = getRCfrom(pygame.mouse.get_pos())
            self.grid[row][col].makeNone()
            if self.start == self.grid[row][col]:
                self.start = None
            if self.end == self.grid[row][col]:
                self.end = None

    def draw(self):
        self.screen.fill(WHITE)
        for row in self.grid:
            for cube in row:
                cube.draw(self.screen)
        drawGrid(self.screen)
        pygame.display.update()


def makeCubeGrid():
    grid = []
    gap = WIDTH // ROWS
    for i in range(ROWS):
        grid.append([])
        for j in range(ROWS):
            cube = Cube(i, j, gap)
            grid[i].append(cube)
    return grid


def drawGrid(win):
    gap = WIDTH // ROWS
    for i in range(0, WIDTH, gap):
        pygame.draw.line(win, GRAY, (0, i), (WIDTH, i))
        pygame.draw.line(win, GRAY, (i, 0), (i, WIDTH))


def getRCfrom(mPos):
    gap = WIDTH // ROWS
    r = mPos[0] // gap
    c = mPos[1] // gap
    return (r, c)


if __name__ == '__main__':
    game = Game()
    while game.running:
        game.run()
    pygame.quit()
