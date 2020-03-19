# code.Pylet - More Platforms
# watch the video here - https://youtu.be/XsKX_czrEPc
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
pygame.display.set_caption("code.Pylet - More Platforms")
FPS = 120

# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)


class platform:
    def __init__(self, x, y, width):
        self.x1 = x
        self.y = y
        self.x2 = x + width

    def test(self, player):
        if player.x < self.x1 or player.x > self.x2: return None
        if player.y <= self.y and player.y + player.velocity >= self.y: return self
        return None


class platforms:
    def __init__(self):
        self.container = list([])

    def add(self, p):
        self.container.append(p)

    def testCollision(self, player):
        if not player.falling: return False
        for p in self.container:
            result = p.test(player)
            if result:
                player.currentPlatform = result
                player.y = result.y
                player.falling = False
                return True
        return False

    def draw(self):
        global WHITE
        display = pygame.display.get_surface()
        for p in self.container:
            pygame.draw.line(display, WHITE, (p.x1, p.y), (p.x2, p.y), 1)

    def do(self, player):
        self.testCollision(player)
        self.draw()


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
        self.currentPlatform = None

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
        if self.currentPlatform:
            if not self.currentPlatform.test(self):
                self.falling = True
                self.currentPlatform = None

        if self.jumping:
            self.y -= self.velocity
            self.jumpCounter += 1
            if self.jumpCounter == self.maxJumpRange:
                self.jumping = False
                self.falling = True
        elif self.falling:  # and not self.currentPlatform:
            self.y += self.velocity

    def draw(self):
        display = pygame.display.get_surface()
        pygame.draw.circle(
            display, WHITE, (int(self.x), int(self.y - 25)), 25, 0)

    def do(self):
        self.keys()
        self.move()
        self.draw()


PLAYER = player(3, 50)
PLAYER.setLocation(HW, 0)

PLATFORMS = platforms()
PLATFORMS.add(platform(0, H - 10, W))
for i in range(0, 50):
    PLATFORMS.add(platform(random.randint(0, W - 50),
                           random.randint(50, H - 60), 50))

# main loop
while True:
    events()

    PLATFORMS.do(PLAYER)
    PLAYER.do()

    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(BLACK)
