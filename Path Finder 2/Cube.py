from Constants import *

class Cube(object):
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.width = width
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.parent = None
        self.gCost = self.hCost = 0

    def fCost(self):
        return self.gCost + self.hCost

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
        if self.isVisited() or self.isClosed():
            # self.drawText(win, f'{self.gCost}', 10, BLACK, self.x + 2, self.y, 1)
            # self.drawText(win, f'{self.hCost}', 10, BLACK, self.x + self.width, self.y, 3)
            self.drawText(win, f'{self.fCost()}', 10, BLACK, self.x+self.width//2, self.y+self.width//2, 5)

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

    def makePath(self):
        self.color = YELLOW

    def isWall(self):
        return self.color == BLACK

    def isVisited(self):
        return self.color == GREEN

    def isClosed(self):
        return self.color == RED

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
