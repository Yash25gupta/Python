import pygame
from constants import *
from random import choice, randrange
VEC = pygame.math.Vector2


class Spritesheet(object):
    def __init__(self, filename):
        self.spritesheet = pygame.image.load(filename).convert()

    def get_image(self, x, y, w, h):
        image = pygame.Surface((w, h))
        image.blit(self.spritesheet, (0, 0), (x, y, w, h))
        image = pygame.transform.scale(image, (int(w * 0.6), int(h * 0.6)))
        image.set_colorkey(BLACK)
        return image


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        self._layer = PLAYER_LAYER
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((16, 16))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.pos = VEC(HALF_WIDTH, HALF_HEIGHT)
        self.vel = VEC(0, 0)
        self.acc = VEC(0, 0)
        self.rect.midbottom = self.pos

    def update(self):
        self.acc = VEC(0, GRAVITY)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x = -PLAYER_ACCELERATION
        if keys[pygame.K_RIGHT]:
            self.acc.x = PLAYER_ACCELERATION
        self.acc.x += self.vel.x * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        if self.pos.x < 0:
            self.pos.x = WIDTH
        if self.pos.x > WIDTH:
            self.pos.x = 0
        self.rect.midbottom = self.pos

    def jump(self):
        self.vel.y = -PLAYER_JUMP


class Platform(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = PLAT_LAYER
        self.groups = game.all_sprites, game.platforms
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.type = choice(('simple', 'one', 'kill', 'spring'))
        self.load_image()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        if randrange(100) < POWER_PCT and self.type != 'kill':
            Power(self.game, self)

    def load_image(self):
        self.simple = pygame.transform.rotate(
            self.game.spritesheet.get_image(418, 184, 70, 30), 180)
        self.one = pygame.transform.rotate(
            self.game.spritesheet.get_image(360, 472, 70, 30), 180)
        self.spike = self.game.spritesheet.get_image(347, 35, 70, 35)
        self.springs = (self.game.spritesheet.get_image(432, 308, 70, 50),
                        self.game.spritesheet.get_image(432, 236, 70, 50))

        if self.type == 'simple':
            self.image = self.simple
        elif self.type == 'one':
            self.image = self.one
        elif self.type == 'kill':
            self.image = self.spike
        elif self.type == 'spring':
            self.image = self.springs[0]


class Power(pygame.sprite.Sprite):
    def __init__(self, game, plat):
        self._layer = POWER_LAYER
        self.groups = game.all_sprites, game.powerups
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.plat = plat
        self.type = choice(('boost', 'immune'))
        self.load_image()
        self.rect = self.image.get_rect()
        self.rect.centerx = self.plat.rect.centerx
        self.rect.bottom = self.plat.rect.top - 2

    def load_image(self):
        self.image = pygame.Surface((16, 16))
        self.image.fill(WHITE)

    def update(self):
        self.rect.bottom = self.plat.rect.top - 2
        if not self.game.platforms.has(self.plat):
            self.kill()
