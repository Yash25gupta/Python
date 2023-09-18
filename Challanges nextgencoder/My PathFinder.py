import pygame
from math import sqrt, pow

WIDTH = 600
TITLE = 'My PathFinder'
ROWS = 10  # multiple of 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
FONT = pygame.font.match_font('arial')


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

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN and not self.findingPath:
                if event.key == pygame.K_SPACE and self.start and self.end:
                    self.findingPath = True
                    pathFinder = PathFinder(self)
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
                self.running = False

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


class PathFinder(object):
    def __init__(self, game):
        self.game = game
        self.run = True

    def findPath(self):
        while self.run:
            self.game.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.game.playing = False
                self.game.running = False
                self.run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                self.run = False
                self.game.playing = False

    def update(self):
        if pygame.mouse.get_pressed()[0]:
            row, col = getRCfrom(pygame.mouse.get_pos())
            current = self.game.grid[row][col]
            current.updateNeighbor(self.game.grid)
            current.makeClosed()
            # current.g = distance(self.game.start, current)
            # current.h = distance(current, self.game.end)
            # current.f = current.g + current.h
            for neighbor in current.neighbors:
                if not neighbor.isClosed():
                    neighbor.makeVisited()
                    neighbor.g = distance(current, neighbor)
                    neighbor.h = distance(neighbor, self.game.end)
                    neighbor.f = neighbor.g + neighbor.h

    def draw(self):
        self.game.screen.fill(WHITE)
        for row in self.game.grid:
            for cube in row:
                cube.draw(self.game.screen)
        drawGrid(self.game.screen)
        pygame.display.update()


def distance(c1, c2):
    return abs(c1.x - c2.x) + abs(c1.y - c2.y)


"""class PathFinder(object):
    def __init__(self, game):
        self.game = game

    def findPath(self):
        for row in game.grid:
            for cube in row:
                cube.updateNeighbor(game.grid)
        game.start.visited = True
        game.start.g = 0
        game.start.f = self.h(game.start, game.end)
        st = [game.start]
        while (not len(st) == 0):
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    game.playing = False
                    game.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                    game.playing = False
            current = st[-1]
            if current == game.end:
                # reconstructPath()
                return True
            for neighbor in current.neighbors:
                neighbor.parent = current

    def h(self, c1, c2):
        return abs(c1.x - c2.x) + abs(c1.y - c2.y)"""


class Cube(object):
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.width = width
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.parent = None
        self.g = self.h = self.f = 0

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
        if self.isVisited() or self.isClosed():
            self.drawText(win, f'{self.g}', 10, BLACK, self.x + 2, self.y, 1)
            self.drawText(win, f'{self.h}', 10, BLACK, self.x + self.width, self.y, 3)
            self.drawText(win, f'{self.f}', 10, BLACK, self.x+self.width//2, self.y+self.width, 8)

    def makeWall(self):
        self.color = BLACK

    def makeStart(self):
        self.color = CYAN

    def makeEnd(self):
        self.color = PURPLE

    def makeNone(self):
        self.color = WHITE

    def makeVisited(self):
        self.color = GREEN

    def makeClosed(self):
        self.color = RED

    def isWall(self):
        return self.color == BLACK

    def isVisited(self):
        return self.color == GREEN

    def isClosed(self):
        return self.color == RED

    def updateNeighbor(self, grid):
        self.neighbors = []
        # UP-LEFT
        if self.row > 0 and self.col > 0 and not grid[self.row - 1][self.col - 1].isWall():
            self.neighbors.append(grid[self.row - 1][self.col - 1])
        # UP
        if self.row > 0 and not grid[self.row - 1][self.col].isWall():
            self.neighbors.append(grid[self.row - 1][self.col])
        # UP-RIGHT
        if self.row > 0 and self.col < ROWS - 1 and not grid[self.row - 1][self.col + 1].isWall():
            self.neighbors.append(grid[self.row - 1][self.col + 1])
        # RIGHT
        if self.col < ROWS - 1 and not grid[self.row][self.col + 1].isWall():
            self.neighbors.append(grid[self.row][self.col + 1])
        # LEFT
        if self.col > 0 and not grid[self.row][self.col - 1].isWall():
            self.neighbors.append(grid[self.row][self.col - 1])
        # DOWN-LEFT
        if self.row < ROWS - 1 and self.col > 0 and not grid[self.row + 1][self.col].isWall():
            self.neighbors.append(grid[self.row + 1][self.col - 1])
        # DOWN
        if self.row < ROWS - 1 and not grid[self.row + 1][self.col].isWall():
            self.neighbors.append(grid[self.row + 1][self.col])
        # DOWN-RIGHT
        if self.row < ROWS - 1 and self.col < ROWS - 1 and not grid[self.row + 1][self.col].isWall():
            self.neighbors.append(grid[self.row + 1][self.col + 1])

    def drawText(self, win, text, size, color, x, y, loc):
        font = pygame.font.Font(FONT, size)
        txtSurface = font.render(text, True, color)
        txtRect = txtSurface.get_rect()
        if loc == 1:
            txtRect.topleft = (x, y)
        elif loc == 2:
            txtRect.midtop = (x, y)
        elif loc == 3:
            txtRect.topright = (x, y)
        elif loc == 4:
            txtRect.midleft = (x, y)
        elif loc == 5:
            txtRect.center = (x, y)
        elif loc == 6:
            txtRect.midright = (x, y)
        elif loc == 7:
            txtRect.bottomleft = (x, y)
        elif loc == 8:
            txtRect.midbottom = (x, y)
        elif loc == 9:
            txtRect.bottomright = (x, y)
        win.blit(txtSurface, txtRect)


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


game = Game()
while game.running:
    game.run()
pygame.quit()
