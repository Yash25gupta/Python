from Ray import *


class Particle(object):
    def __init__(self):
        self.pos = pygame.Vector2()
        self.rays = [Ray(self.pos, a) for a in range(360)]

    def update(self, pos):
        self.pos.update(pos[0], pos[1])

    def look(self, walls):
        for ray in self.rays:
            closest = None
            record = float('inf')
            for wall in walls:
                pt = ray.cast(wall)
                if pt:
                    d = pygame.Vector2.distance_to(pt, self.pos)
                    if d < record:
                        record = d
                        closest = pt
            ray.ePos = closest

    def draw(self, win):
        for ray in self.rays:
            ray.draw(win)
