from Constants import *
from PathFinder import *
from Spot import *


class Game(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH + E_WIDTH, WIDTH))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.ROWS = ROWS

    def run(self):
        # Constants
        self.INCLUDE_DIAGONAL = False
        self.SHOW_GRID = False
        self.SHOW_F_VALUE = False
        self.SHOW_PATH_AS_LINE = False
        self.SHOW_OPEN_CLOSED_SET = False
        self.UPDATE_ONLY_ON_CLICK = False
        self.SPOT_WIDTH = WIDTH // self.ROWS
        # Game Variables
        self.grid = [[Spot(i, j, self) for j in range(self.ROWS)] for i in range(self.ROWS)]
        self.start, self.end = self.grid[0][0], self.grid[-1][-1]
        self.start.isWall, self.end.isWall = False, False
        self.playing, self.findPath = True, False
        self.pathFinder = None
        self.path = []
        self.status = None
        btnDiag = Button(WIDTH + E_H_WIDTH,  50, 250, 50, 'Include Diagonal Neighbours', 'Exclude Diagonal Neighbours', self._tglDiag)
        btnGrid = Button(WIDTH + E_H_WIDTH, 110, 250, 50, 'Show Grid', 'Hide Grid', self._tglGrid)
        btnFVal = Button(WIDTH + E_H_WIDTH, 170, 250, 50, 'Show F Values', 'Hide F Values', self._tglFVal)
        btnPath = Button(WIDTH + E_H_WIDTH, 230, 250, 50, 'Show Path as Line', 'Show path as Circle', self._tglLine)
        btnSet = Button(WIDTH + E_H_WIDTH, 290, 250, 50, 'View Current status of all Spots', 'Hide Current status of all Spots', self._tglSet)
        btnUpdate = Button(WIDTH + E_H_WIDTH, 350, 250, 50, 'Manual Update', 'Automatic Update', self._tglUpdate)
        btnStart = Button(WIDTH + E_H_WIDTH, 410, 250, 50, 'Start Finding', 'Start Finding', self._startBtn)
        btnReset = Button(WIDTH + E_H_WIDTH, 470, 250, 50, 'Reset', 'Reset', self._resetBtn)
        self.btnNext = Button(WIDTH + E_H_WIDTH, 530, 250, 50, 'Next', 'Next', self._nxtBtn)
        self.allBtns = (btnDiag, btnGrid, btnFVal, btnPath, btnSet, btnUpdate, btnStart, btnReset, self.btnNext)
        self.textBox = TextBox(game, WIDTH + E_WIDTH - 80, WIDTH - 52, 40, 26)
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
                if event.key == pygame.K_s:
                    row, col = self.getRCfrom(pygame.mouse.get_pos())
                    self.start = self.grid[row][col]
                    self.start.isWall = False
                elif event.key == pygame.K_e:
                    row, col = self.getRCfrom(pygame.mouse.get_pos())
                    self.end = self.grid[row][col]
                    self.end.isWall = False
            for btn in self.allBtns:
                btn.handleEvent(event)
            self.textBox.handleEvent(event)

    def update(self):
        if self.findPath and self.start and self.end:
            self.pathFinder = PathFinder(self, self.start, self.end)
            self.path = self.pathFinder.findPath()
            self.findPath = False
        pos = pygame.mouse.get_pos()
        if pos[0] < WIDTH:
            if pygame.mouse.get_pressed()[0]:
                row, col = self.getRCfrom(pos)
                spot = self.grid[row][col]
                if spot not in (self.start, self.end):
                    spot.isWall = True
            if pygame.mouse.get_pressed()[2]:
                row, col = self.getRCfrom(pos)
                spot = self.grid[row][col]
                spot.isWall = False
                if spot == self.start:
                    self.start = None
                if spot == self.end:
                    self.end = None

    def draw(self):
        self.screen.fill(COL_BACKGROUND)
        self.textBox.draw(self.screen)
        for row in self.grid:
            for spot in row:
                spot.draw(self.screen)
        if self.pathFinder:
            self.pathFinder.drawPath(self.screen, self.path, self.SHOW_PATH_AS_LINE)
        if self.start:
            self.start.draw(self.screen, COL_START)
        if self.end:
            self.end.draw(self.screen, COL_END)
        if self.SHOW_GRID:
            self.drawGrid(self.screen)
        pygame.draw.lines(self.screen, COL_WALL, True, ((0, 0), (WIDTH, 0), (WIDTH, WIDTH), (0, WIDTH)))
        for btn in self.allBtns:
            btn.draw(self.screen)
        if self.status:
            draw_text(self.screen, self.status, 32, BLACK, WIDTH + E_H_WIDTH, 600)
        pygame.display.update()

    def getNeighbours(self, node):
        neighbours = []
        nsew, diag = [(-1, 0), (0, -1), (0, 1), (1, 0)], ((-1, -1), (-1, 1), (1, -1), (1, 1))
        if self.INCLUDE_DIAGONAL:
            nsew.extend(diag)
        for x, y in nsew:
            checkX, checkY = node.row + x, node.col + y
            if 0 <= checkX < self.ROWS and 0 <= checkY < self.ROWS and not self.grid[checkX][checkY].isWall:
                neighbours.append(self.grid[checkX][checkY])
        return neighbours

    def _tglDiag(self):
        self.INCLUDE_DIAGONAL = not self.INCLUDE_DIAGONAL

    def _tglGrid(self):
        self.SHOW_GRID = not self.SHOW_GRID

    def _tglFVal(self):
        self.SHOW_F_VALUE = not self.SHOW_F_VALUE

    def _tglLine(self):
        self.SHOW_PATH_AS_LINE = not self.SHOW_PATH_AS_LINE

    def _tglSet(self):
        self.SHOW_OPEN_CLOSED_SET = not self.SHOW_OPEN_CLOSED_SET

    def _tglUpdate(self):
        self.UPDATE_ONLY_ON_CLICK = not self.UPDATE_ONLY_ON_CLICK

    def _startBtn(self):
        self.findPath = True

    def _nxtBtn(self):
        if self.pathFinder and self.UPDATE_ONLY_ON_CLICK:
            self.pathFinder.nextFrame = True
            self.btnNext.state = True

    def _resetBtn(self):
        self.playing = False
        if self.pathFinder:
            self.pathFinder.found = True

    def drawGrid(self, win):
        for i in range(0, WIDTH, self.SPOT_WIDTH):
            pygame.draw.line(win, GRAY, (0, i), (WIDTH, i))
            pygame.draw.line(win, GRAY, (i, 0), (i, WIDTH))

    def getRCfrom(self, mPos):
        r = mPos[0] // self.SPOT_WIDTH
        c = mPos[1] // self.SPOT_WIDTH
        return (r, c)


if __name__ == '__main__':
    game = Game()
    while game.running:
        game.run()
    pygame.quit()
