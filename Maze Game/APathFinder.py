from Constants import *
from Cell import index
from math import sqrt, pow


def heuristic(s1, s2):
    # d = abs(s1.x - s2.x) + abs(s1.y - s2.y)
    d = sqrt(pow(s1.x-s2.x, 2) + pow(s1.y-s2.y, 2))
    return d


class APathFinder(object):
    def __init__(self, game, startCell, endCell):
        self.game = game
        self.startCell = startCell
        self.endCell = endCell

    def findPath(self):
        self.openSet = [(0, self.startCell)]
        self.closedSet = []
        self.path = []
        self.found = False
        while (not self.found):
            self.game.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        return self.path

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.game.playing = False
                self.game.running = False
                self.found = True

    def update(self):
        if len(self.openSet) > 0:
            self.current = self.openSet[0][1]
            if self.current == self.endCell:
                self.found = True
                print('Path Founded')
                return
            self.openSet.pop(0)
            self.closedSet.append(self.current)
            for neighbour in self.getNeighbours(self.current):
                if neighbour not in self.closedSet:
                    tempG = self.current.gCost + heuristic(neighbour, self.current)
                    for (_, cell) in self.openSet:
                        if neighbour == cell:  # neighbour in openSet
                            if tempG < neighbour.gCost:  # new Path is shorter
                                neighbour.gCost = tempG
                                neighbour.hCost = heuristic(neighbour, self.endCell)
                                neighbour.parent = self.current
                            break
                    else:  # neighbour not in openSet
                        neighbour.gCost = tempG
                        neighbour.hCost = heuristic(neighbour, self.endCell)
                        neighbour.parent = self.current
                        self.addToOpenSet((neighbour.fCost(), neighbour))
        else:
            print('No Solution')
            self.found = True

    def getNeighbours(self, cell):
        neighbours = []
        for x, y, dir in ((0, -1, 0), (1, 0, 1), (0, 1, 2), (-1, 0, 3)):
            checkX, checkY = cell.i + x, cell.j + y
            if not cell.walls[dir]:
                neighbours.append(self.game.grid[index(checkX, checkY)])
        return neighbours

    def draw(self):
        win = self.game.screen
        win.fill(COL_BACKGROUND)
        for cell in self.game.grid:
            cell.draw(win)
        for (_, cell) in self.openSet:
            cell.draw(win, GREEN)
        for cell in self.closedSet:
            cell.draw(win, RED)
        cell = self.current
        cell.highLight(win)
        self.path = [cell]
        while cell.parent:
            self.path.append(cell.parent)
            cell = cell.parent
        # for cell in self.path:
        #     cell.draw(win, PINK)
        # self.startCell.draw(win, CYAN)
        # self.endCell.draw(win, YELLOW)
        pygame.display.update()

    def addToOpenSet(self, tup):
        ''' Add (f, cell) to OpenSet in increasing order of f values '''
        for i, t in enumerate(self.openSet):
            if tup[0] < t[0]:
                self.openSet.insert(i, tup)
                return
        self.openSet.append(tup)
