from Constants import *
from Cell import *
from random import sample

class Game(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.ROWS = HEIGHT // CELL_WIDTH
        self.COLS = WIDTH // CELL_WIDTH
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        self.grid = [[Cell(i, j, self) for i in range(self.COLS)] for j in range(self.ROWS)]
        for i, j in sample([(i, j) for i in range(self.COLS) for j in range(self.ROWS)], BOMB_COUNT):
            self.grid[j][i].isBomb = True
        [cell.updateNeighbours() for row in self.grid for cell in row]
        [cell.updateBombCount() for row in self.grid for cell in row]
        self.markers = []
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
        pos = pygame.mouse.get_pos()
        if pos[0] < WIDTH:
            if pygame.mouse.get_pressed()[0]:
                i, j = self.getRCfrom(pos)
                cell = self.grid[i][j]
                cell.isReveled = True
                if cell.bombCount == 0:
                    cell.revelEmptyCells()
                if cell.isBomb:
                    for row in self.grid:
                        for cell in row:
                            cell.isReveled = True
            elif pygame.mouse.get_pressed()[2]:
                i, j = self.getRCfrom(pos)
                self.markers.append(self.grid[i][j])

    def draw(self):
        self.screen.fill(WHITE)
        for row in self.grid:
            for cell in row:
                cell.draw(self.screen)
        for cell in self.markers:
            pygame.draw.rect(self.screen, RED, (cell.x+10, cell.y+10, CELL_WIDTH-20, CELL_WIDTH-20))
        pygame.display.update()

    def getRCfrom(self, mPos):
        r = mPos[0] // CELL_WIDTH
        c = mPos[1] // CELL_WIDTH
        return (c, r)

if __name__ == '__main__':
    game = Game()
    while game.running:
        game.run()
    pygame.quit()
