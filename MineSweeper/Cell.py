from Constants import *

class Cell(object):
    def __init__(self, i, j, game):
        self.i = i
        self.j = j
        self.game = game
        self.x = i * CELL_WIDTH
        self.y = j * CELL_WIDTH
        self.isReveled = False
        self.isBomb = False
        self.bombCount = 0
        self.neighbours = []

    def revelEmptyCells(self):
        for neighbour in self.neighbours:
            if not neighbour.isReveled and self.bombCount == 0:
                neighbour.isReveled = True
                neighbour.revelEmptyCells()

    def updateNeighbours(self):
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                checkI = self.i + i
                checkJ = self.j + j
                if 0 <= checkI < self.game.COLS and 0 <= checkJ < self.game.ROWS:
                    self.neighbours.append(self.game.grid[checkJ][checkI])
    
    def updateBombCount(self):
        for neighbour in self.neighbours:
            if neighbour.isBomb:
                self.bombCount += 1
    
    def draw(self, win):
        w = CELL_WIDTH
        if self.isReveled:
            pygame.draw.rect(win, GRAY, (self.x, self.y, w, w))
            if self.isBomb:
                pygame.draw.circle(win, DARK_PURPLE, (self.x + w // 2, self.y + w // 2), w // 3)
            elif self.bombCount > 0:
                draw_text(win, f'{self.bombCount}', 16, BLACK, self.x + w // 2, self.y + w // 2)
        pygame.draw.rect(win, BLACK, (self.x, self.y, w, w), 1)

def draw_text(win, text, size, color, x, y):
    font = pygame.font.SysFont('arial', size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    win.blit(text_surface, text_rect)