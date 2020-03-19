# code.Pylet - Stage Manager: Objects & Viewport
# watch the video here - https://youtu.be/HZZ5hzF5XC8
# Any questions? Just ask!

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
W, H = 1280, 720
HW, HH = W / 2, H / 2
AREA = W * H

# initialise display
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("code.Pylet - Stage Test")
FPS = 120

# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)


class viewport:
    def __init__(self, surface=None):
        if not surface:
            surface = pygame.display.get_surface()
        self.surface = surface

        rect = surface.get_rect()
        self.w, self.h = rect.size
        self.hw, self.hh = rect.center
        self.x, self.y = (0, 0)

    def setLocation(self, x, y):
        self.x, self.y = (x, y)

    def objectVisible(self, object):
        if object.x < self.x - object.w or object.x > self.x + self.w or object.y < self.y - object.h or \
            object.y > self.y + self.h: return False
        return True

    def centerOnX(self, x):
        self.x = x - self.hw

    def centerOnY(self, y):
        self.y = y - self.hh


class manager:
    def __init__(self, width, height, layers):
        self.w, self.h = (width, height)
        self.vp = viewport()
        self.layers = layers
        self.objects = list([list([]) for z in range(layers)])
        self.focus = None

    def focusOn(self, object):
        self.focus = object

    def focusOff(self):
        self.focus = None

    def addObject(self, layer, object):
        self.objects[layer].append(object)

        object.movable = callable(getattr(object, "move", None))
        object.drawable = callable(getattr(object, "draw", None))
        object.extension = callable(getattr(object, "extension", None))

        return object

    def do(self):
        for layer in range(self.layers):
            for object in self.objects[layer]:
                x = object.x - self.vp.x
                y = object.y - self.vp.y

                if object.movable: object.move(x, y, self)

                if self.focus:
                    if self.focus == object:
                        if object.x <= self.vp.hw:
                            self.vp.x = 0
                        elif object.x >= self.w - self.vp.hw:
                            self.vp.x = self.w - self.vp.w
                        else:
                            self.vp.centerOnX(object.x)
                        if object.y <= self.vp.hh:
                            self.vp.y = 0
                        elif object.y >= self.h - self.vp.hh:
                            self.vp.y = self.h - self.vp.h
                        else:
                            self.vp.centerOnY(object.y)

                if object.drawable:
                    if self.vp.objectVisible(object):
                        object.draw(x, y, self)


class block:
    def __init__(self, x, y, size):
        self.x, self.y = x, y
        self.w, self.h = size

    def draw(self, x, y, stage):
        global WHITE
        pygame.draw.rect(stage.vp.surface, WHITE, (x, y, self.w, self.h), 1)


class fish:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.w, self.h = (25, 25)

    def move(self, x, y, stage):
        mx, my = pygame.mouse.get_pos()

        xDist = (mx - x) / 50
        yDist = (my - y) / 50

        self.x += xDist
        self.y += yDist

    def draw(self, x, y, stage):
        global WHITE
        pygame.draw.rect(stage.vp.surface, WHITE, (x, y, self.w, self.h), 0)


STAGE = manager(W * 4, H * 4, 1)

cFACTOR = 64
BLOCK_SIZE = (STAGE.w / cFACTOR, STAGE.h / cFACTOR)
for a in range(cFACTOR * cFACTOR):
    STAGE.addObject(0, block(
        (a % cFACTOR) * BLOCK_SIZE[0], (a / cFACTOR) * BLOCK_SIZE[1], BLOCK_SIZE))

f = STAGE.addObject(0, fish(STAGE.w / 2, STAGE.h / 2))
STAGE.focusOn(f)

# main loop
while True:
    events()

    STAGE.do()

    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(BLACK)
