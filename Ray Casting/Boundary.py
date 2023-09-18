from Constants import *


class Boundary(object):
    def __init__(self, x1, y1, x2, y2):
        self.sPos = pygame.Vector2(x1, y1)
        self.ePos = pygame.Vector2(x2, y2)

    def draw(self, win):
        pygame.draw.line(win, WHITE, self.sPos, self.ePos, 4)
