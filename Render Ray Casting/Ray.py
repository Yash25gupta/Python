from Boundary import *


class Ray(object):
    def __init__(self, pos, angle):
        self.pos = pos
        self.dir = pygame.Vector2(1, 0).rotate(angle)
        self.ePos = None

    def setAngle(self, angle):
        self.dir = pygame.Vector2(1, 0).rotate(angle)

    def draw(self, win):
        if self.ePos:
            pygame.draw.aaline(win, WHITE, self.pos, self.ePos)

    def cast(self, wall):
        x1, y1 = wall.sPos.x, wall.sPos.y
        x2, y2 = wall.ePos.x, wall.ePos.y
        x3, y3 = self.pos.x, self.pos.y
        x4, y4 = self.pos.x + self.dir.x, self.pos.y + self.dir.y

        den = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
        if den == 0:
            return
        t = ((x1-x3)*(y3-y4) - (y1-y3)*(x3-x4)) / den
        u = -((x1-x2)*(y1-y3) - (y1-y2)*(x1-x3)) / den
        if 0 < t < 1 and u > 0:
            x = x1 + t * (x2-x1)
            y = y1 + t * (y2-y1)
            return pygame.Vector2(x, y)

    # def lookAt(self, x, y):
    #     self.dir.x = x - self.pos.x
    #     self.dir.y = y - self.pos.y
    #     self.dir.normalize()