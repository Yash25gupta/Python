from Constants import *
from random import randint


class Cell(object):
    def __init__(self, i, j, w):
        self.i = i
        self.j = j
        self.x = i * w + 5
        self.y = j * w + 5
        self.w = w
        self.visited = False
        self.walls = [True, True, True, True]  # Top, Right, Bottom, Left

    def highLight(self, win):
        pygame.draw.rect(win, BLUE, (self.x+1, self.y+1, self.w-1, self.w-1))

    def draw(self, win, color=DARK_PURPLE):
        if self.visited:
            pygame.draw.rect(win, color, (self.x, self.y, self.w, self.w))
        if self.walls[0]:  # Top
            pygame.draw.line(win, WHITE, (self.x, self.y), (self.x + self.w, self.y))
        if self.walls[1]:  # Right
            pygame.draw.line(win, WHITE, (self.x + self.w, self.y), (self.x + self.w, self.y + self.w))
        if self.walls[2]:  # Bottom
            pygame.draw.line(win, WHITE, (self.x + self.w, self.y + self.w), (self.x, self.y + self.w))
        if self.walls[3]:  # Left
            pygame.draw.line(win, WHITE, (self.x, self.y + self.w), (self.x, self.y))

    def getRendomNeighbour(self, grid):
        neighbours = []
        for (x, y) in ((0, -1), (1, 0), (0, 1), (-1, 0)):  # Top, Right, Bottom, Left
            ind = index(self.i + x, self.j + y)
            if ind and not grid[ind].visited:
                neighbours.append(grid[ind])
        if len(neighbours) > 0:
            return neighbours[randint(0, len(neighbours) - 1)]
        return None


def index(i, j):
    if 0 <= i < ROWS and 0 <= j < ROWS:
        return j + i * ROWS
    return None
