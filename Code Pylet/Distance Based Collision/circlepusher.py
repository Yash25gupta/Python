# code.Pylet - Distance Based Collision
# watch the video here - https://youtu.be/gAkUlyj6irw
# Any questions? Just ask!

import math
import random
import sys
import pygame
from pygame.locals import *

# exit the program


def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()


# define display surface
W, H = 960, 540
HW, HH = W / 2, H / 2
AREA = W * H

# initialise display
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("code.Pylet - Circle Pusher")
FPS = 120

# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)


class circle:
    def __init__(self, xy, radius, id):
        self.xy = xy
        self.radius = radius
        self.id = id
        self.color = (random.randint(128, 255), random.randint(
            128, 255), random.randint(128, 255), 255)

    def hasOverlapped(self, xy, radius):
        minDistance = 0.0 + radius + self.radius
        distance = math.hypot(xy[0] - self.xy[0], xy[1] - self.xy[1])
        if distance >= minDistance: return False

        radians = math.atan2(xy[1] - self.xy[1], xy[0] - self.xy[0])
        overlap = 1 + (minDistance - distance)
        return (math.cos(radians) * overlap, math.sin(radians) * overlap, overlap)

    def setXY(self, xy):
        self.xy = xy

    def draw(self):
        d = pygame.display.get_surface()
        pygame.draw.circle(
            d, self.color, (int(self.xy[0]), int(self.xy[1])), self.radius, 0)


class circles:
    def __init__(self):
        self.container = list([])
        self.overlap = list([])

    def add(self):
        global W, H
        while True:
            radius = random.randint(15, 50)
            xy = [random.randint(radius, W - radius),
                  random.randint(radius, H - radius)]
            noOverlap = True
            for c in self.container:
                if c.hasOverlapped(xy, radius):
                    noOverlap = False
                    break
            if noOverlap: break
        self.container.append(circle(xy, radius, len(self.container)))

    def collision(self):
        self.overlap.append(self.container[0])
        while self.overlap:
            source = self.overlap[0]
            self.overlap.pop(0)

            for index in range(1, len(self.container)):
                target = self.container[index]
                if target.id == source.id: continue

                result = source.hasOverlapped(target.xy, target.radius)
                if result:
                    target.xy[0] += result[0]
                    target.xy[1] += result[1]
                    self.overlap.append(target)

    def drawAll(self):
        for source in self.container:
            source.draw()

    def do(self):
        self.collision()
        self.drawAll()


circs = circles()
for i in range(0, 200): circs.add()

# main loop
while True:
    events()

    mx, my = pygame.mouse.get_pos()
    circs.container[0].setXY([mx, my])
    circs.do()

    pygame.display.update()
    # CLOCK.tick(FPS)
    DS.fill(BLACK)
