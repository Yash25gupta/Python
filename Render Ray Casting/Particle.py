from Ray import *
from pygame import Vector2 as Vec2
from math import cos

class Particle(object):
    def __init__(self, x, y):
        self.pos = Vec2(x, y)
        self.fov = 60
        self.heading = 0
        self.rays = [Ray(self.pos, a) for a in range(-self.fov//2, self.fov//2)]

    def update(self, pos):
        self.pos.update(pos[0], pos[1])

    def updateFOV(self, fov):
        self.fov += fov
        self.rays = [Ray(self.pos, a+self.heading) for a in range(-self.fov//2, self.fov//2)]

    def rotate(self, angle):
        self.heading += angle
        for i, a in enumerate(range(-self.fov//2, self.fov//2)):
            self.rays[i].setAngle(a+self.heading)
    
    def move(self, amt):
        vel = Vec2(1,0).rotate(self.heading)
        vel.scale_to_length(amt)
        self.pos += vel

    def look(self, walls):
        scene = []
        for ray in self.rays:
            closest = None
            record = WIDTH*WIDTH  # float('inf')
            for wall in walls:
                pt = ray.cast(wall)
                if pt:
                    d = Vec2.distance_to(pt, self.pos)
                    # a = Vec2.angle_to(ray.dir, Vec2(0,0)) - self.heading
                    # d *= cos(a)
                    if d < record:
                        record = d
                        closest = pt
            ray.ePos = closest
            scene.append(int(record))
        return scene

    def draw(self, win):
        for ray in self.rays:
            ray.draw(win)
