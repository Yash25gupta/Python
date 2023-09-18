from Constants import *
from math import sqrt, pow


def heuristic(s1, s2):
    # d = abs(s1.x - s2.x) + abs(s1.y - s2.y)
    d = sqrt(pow(s1.x-s2.x, 2) + pow(s1.y-s2.y, 2))
    return d


class PathFinder(object):
    def __init__(self, game, startNode, endNode):
        self.game = game
        self.startNode = startNode
        self.endNode = endNode

    def findPath(self):
        self.openSet = [(0, self.startNode)]
        self.closedSet = []
        self.path = []
        self.found = False
        self.nextFrame = False
        while (not self.found):
            self.game.clock.tick(FPS)
            self.events()
            if not self.game.UPDATE_ONLY_ON_CLICK:
                self.update()
                self.draw()
        return self.path

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.game.playing = False
                self.game.running = False
                self.found = True
            if self.nextFrame:
                self.update()
                self.draw()
                self.nextFrame = False
            for btn in self.game.allBtns:
                btn.handleEvent(event)

    def update(self):
        if len(self.openSet) > 0:
            self.current = self.openSet[0][1]
            if self.current == self.endNode:
                self.found = True
                self.game.status = 'Path Founded'
                return
            self.openSet.pop(0)
            self.closedSet.append(self.current)
            for neighbour in self.game.getNeighbours(self.current):
                if neighbour not in self.closedSet and not neighbour.isWall:
                    tempG = self.current.gCost + heuristic(neighbour, self.current)
                    for (_, spot) in self.openSet:
                        if neighbour == spot:  # neighbour in openSet
                            if tempG < neighbour.gCost:  # new Path is shorter
                                neighbour.gCost = tempG
                                neighbour.hCost = heuristic(neighbour, self.endNode)
                                neighbour.parent = self.current
                            break
                    else:  # neighbour not in openSet
                        neighbour.gCost = tempG
                        neighbour.hCost = heuristic(neighbour, self.endNode)
                        neighbour.parent = self.current
                        self.addToOpenSet((neighbour.fCost(), neighbour))
        else:
            self.game.status = 'No Solution'
            self.found = True

    def draw(self):
        win = self.game.screen
        win.fill(COL_BACKGROUND)
        for row in self.game.grid:
            for spot in row:
                spot.draw(win)
        if self.game.SHOW_OPEN_CLOSED_SET:
            for (_, spot) in self.openSet:
                spot.draw(win, COL_OPENSET)
            for spot in self.closedSet:
                spot.draw(win, COL_CLOSEDSET)
        spot = self.current
        self.path = [spot]
        while spot.parent:
            self.path.append(spot.parent)
            spot = spot.parent
        self.drawPath(win, self.path, self.game.SHOW_PATH_AS_LINE)
        self.startNode.draw(win, COL_START)
        self.endNode.draw(win, COL_END)
        if self.game.SHOW_GRID:
            self.game.drawGrid(win)
        pygame.draw.lines(win, COL_WALL, True, ((0, 0), (WIDTH, 0), (WIDTH, WIDTH), (0, WIDTH)))
        for btn in self.game.allBtns:
            btn.draw(win)
        pygame.display.update()

    def drawPath(self, win, path, asLine):
        for spot in path:
            spot.draw(win, COL_PATH)
        if asLine:
            w = self.game.SPOT_WIDTH // 2
            vertexs = [(spot.x + w, spot.y + w) for spot in path]
            if len(vertexs) > 1:
                pygame.draw.lines(win, COL_PATH, False, vertexs, width=self.game.SPOT_WIDTH)
                pygame.draw.lines(win, COL_BACKGROUND, False, vertexs)

    def addToOpenSet(self, tup):
        ''' Add (f, spot) to OpenSet in increasing order of f values '''
        for i, t in enumerate(self.openSet):
            if tup[0] < t[0]:
                self.openSet.insert(i, tup)
                return
        self.openSet.append(tup)

    def addToOpenSet2(self, tup):
        l, r = 0, len(self.openSet)
        while (l+1) != r:
            m = (l+r)//2
            f = self.openSet[m][0]
            if tup[0] == f:
                l = m
                break
            elif tup[0] < f:
                r = m-1
            else:
                l = m+1
        self.openSet.insert(l, tup)
        