# code.Pylet - Player Class
# watch the video here - https://youtu.be/7W0VKHzhCRQ
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
W, H = 576, 720
HW, HH = W / 2, H / 2
AREA = W * H

# initialise display
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("code.Pylet - Player Class")
FPS = 120

# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)


class player:
    def __init__(self, velocity, maxJumpRange):
        self.velocity = velocity
        self.maxJumpRange = maxJumpRange

    def setLocation(self, x, y):
        self.x = x
        self.y = y
        self.xVelocity = 0
        self.jumping = False
        self.jumpCounter = 0
        self.falling = True

    def keys(self):
        k = pygame.key.get_pressed()

        if k[K_LEFT]: self.xVelocity = -self.velocity
        elif k[K_RIGHT]: self.xVelocity = self.velocity
        else: self.xVelocity = 0

        if k[K_UP] and not self.jumping and not self.falling:
            self.jumping = True
            self.jumpCounter = 0

    def move(self):
        self.x += self.xVelocity
        # check x boundries

        if self.jumping:
            self.y -= self.velocity
            self.jumpCounter += 1
            if self.jumpCounter == self.maxJumpRange:
                self.jumping = False
                self.falling = True
        elif self.falling:
            if self.y <= H - 10 and self.y + self.velocity >= H - 10:
                self.y = H - 10
                self.falling = False
            else:
                self.y += self.velocity

    def draw(self):
        display = pygame.display.get_surface()
        pygame.draw.circle(
            display, WHITE, (int(self.x), int(self.y - 25)), 25, 0)

    def do(self):
        self.keys()
        self.move()
        self.draw()


P = player(3, 50)
P.setLocation(HW, 0)

# main loop
while True:
    events()

    P.do()

    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(BLACK)
