from Constants import *
from random import randint

class Player(object):
    def __init__(self):
        self.reset()

    def reset(self):
        self.spot = -1
        self.roll = 0

    def rollDie(self):
        self.roll = randint(1, 6)

    def move(self):
        self.spot += self.roll

    def drawPreview(self, win, tiles):
        start = self.spot if self.spot else 0
        end = min(self.spot + self.roll, len(tiles))
        for i in range(start, end):
            tiles[i].highlight(win)

    def isSnadder(self, tiles):
        tile = tiles[self.spot] if 0 <= self.spot < len(tiles) else None
        return tile and tile.snadder != 0
    
    def moveSnadder(self, tiles):
        if self.spot >= 0:
            self.spot += tiles[self.spot].snadder

    def draw(self, win, tiles):
        if self.spot >= 0:
            pos = tiles[self.spot].getCenter()
            pygame.draw.circle(win, WHITE, (pos[0], pos[1]), TILE_WIDTH // 3)