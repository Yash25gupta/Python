from Constants import *

def getDistance(node1, node2):
    disX, disY = abs(node1.x - node2.x), abs(node1.y - node2.y)
    if disX > disY:
        return 1.5 * disY + (disX - disY)
    return 1.5 * disX + (disY - disX)

class PathFinder(object):
    def __init__(self, game, startNode, endNode):
        self.game = game
        self.startNode = startNode
        self.endNode = endNode

    def findPath(self):
        self.openSet = []
        closedSet = []
        self.openSet.append(self.startNode)
        while (len(self.openSet) > 0):
            # set node with lowset FCost to currentNode
            currentNode = self.openSet[0]
            for i in range(1, len(self.openSet)):
                hasLowFCost = self.openSet[i].fCost() < currentNode.fCost()
                hasLowHCost = self.openSet[i].fCost() == currentNode.fCost() and self.openSet[i].hCost < currentNode.hCost
                if hasLowFCost or hasLowHCost:
                    currentNode = self.openSet[i]

            self.openSet.remove(currentNode)
            closedSet.append(currentNode)
            currentNode.makeClosed()
            if currentNode == self.endNode:
                self.retracePath()
                return
            for neighbour in self.game.getNeighbours(currentNode):
                if (neighbour.isClosed() or (neighbour in closedSet)):
                    continue
                newMovementCostToNeighbour = currentNode.gCost + getDistance(currentNode, neighbour)
                if (newMovementCostToNeighbour < neighbour.gCost or neighbour not in self.openSet):
                    neighbour.gCost = newMovementCostToNeighbour
                    neighbour.hCost = getDistance(neighbour, self.endNode)
                    neighbour.parent = currentNode
                    if neighbour not in self.openSet:
                        self.openSet.append(neighbour)
                        neighbour.makeVisited()
            self.game.clock.tick(FPS)
            self.events()
            self.game.draw()
    
    def retracePath(self):
        currentNode = self.endNode
        while (currentNode is not self.startNode):
            currentNode.makePath()
            currentNode.draw(self.game.screen)
            pygame.display.update()
            currentNode = currentNode.parent

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.game.playing = False
                self.game.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                self.game.playing = False
