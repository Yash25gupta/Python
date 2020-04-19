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
        image = pygame.transform.scale(image, (w // 2, h // 2))
        return image


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        self._layer = PLAYER_LAYER
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.walking = False
        self.jumping = False
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.image = self.stand_imgs[0]
        self.rect = self.image.get_rect()
        self.rect.midbottom = (40, HEIGHT - 100)
        self.pos = VEC(40, HEIGHT - 100)
        self.vel = VEC(0, 0)
        self.acc = VEC(0, 0)

    def load_images(self):
        self.stand_imgs = [self.game.spritesheet.get_image(614, 1063, 120, 191),
                           self.game.spritesheet.get_image(690, 406, 120, 201)]
        for frame in self.stand_imgs:
            frame.set_colorkey(BLACK)
        self.walk_r_imgs = [self.game.spritesheet.get_image(678, 860, 120, 201),
                            self.game.spritesheet.get_image(692, 1458, 120, 207)]
        self.walk_l_imgs = []
        for frame in self.walk_r_imgs:
            frame.set_colorkey(BLACK)
            self.walk_l_imgs.append(pygame.transform.flip(frame, True, False))
        self.jump_img = self.game.spritesheet.get_image(382, 763, 150, 181)
        self.jump_img.set_colorkey(BLACK)

    def update(self):
        self.animate()
        # Movement
        self.acc = VEC(0, GRAVITY)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x = -PLAYER_ACCELERATION
        if keys[pygame.K_RIGHT]:
            self.acc.x = PLAYER_ACCELERATION
        # Apply Friction and Laws of Motion
        self.acc.x += self.vel.x * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # Checking Boundary
        if self.pos.x < 0:
            self.pos.x = WIDTH
        if self.pos.x > WIDTH:
            self.pos.x = 0

        self.rect.midbottom = self.pos

    def animate(self):
        now = pygame.time.get_ticks()
        self.walking = (abs(self.vel.x) > 0.1)

        if now - self.last_update > 350:
            self.last_update = now
            self.current_frame = (self.current_frame +
                                  1) % len(self.walk_l_imgs)
            bottom = self.rect.bottom
            # General Animation
            if not self.jumping and not self.walking:
                self.image = self.stand_imgs[self.current_frame]
            # Walking Animation
            elif self.walking:
                if self.vel.x > 0:
                    self.image = self.walk_r_imgs[self.current_frame]
                else:
                    self.image = self.walk_l_imgs[self.current_frame]
            # Image position at bottom
            self.rect = self.image.get_rect()
            self.rect.bottom = bottom

    def jump(self):
        self.rect.y += 2
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 2
        if hits and not self.jumping:
            self.vel.y = -PLAYER_JUMP
            self.jumping = True

    def jump_cut(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3


class Platform(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = PLAT_LAYER
        self.groups = game.all_sprites, game.platforms
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        images = [self.game.spritesheet.get_image(0, 288, 380, 94),
                  self.game.spritesheet.get_image(213, 1662, 201, 100)]
        self.image = choice(images)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        if randrange(100) < POW_SPAWN_PCT:
            Power(self.game, self)


class Power(pygame.sprite.Sprite):
    def __init__(self, game, plat):
        self._layer = POWER_LAYER
        self.groups = game.all_sprites, game.powerups
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.plat = plat
        self.type = choice(['jet', 'wing'])
        self.load_images()
        self.rect = self.image.get_rect()
        self.rect.centerx = self.plat.rect.centerx
        self.rect.bottom = self.plat.rect.top - 5

    def load_images(self):
        self.jet = self.game.spritesheet.get_image(820, 1805, 71, 70)
        self.jet.set_colorkey(BLACK)
        self.wing = self.game.spritesheet.get_image(826, 1292, 71, 70)
        self.wing.set_colorkey(BLACK)
        self.image = self.jet if self.type == 'jet' else self.wing

    def update(self):
        self.rect.bottom = self.plat.rect.top - 5
        if not self.game.platforms.has(self.plat):
            self.kill()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, game):
        self._layer = ENEMY_LAYER
        self.groups = game.all_sprites, game.enemys
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image_up = self.game.spritesheet.get_image(566, 510, 122, 139)
        self.image_up.set_colorkey(BLACK)
        self.image_down = self.game.spritesheet.get_image(568, 1534, 122, 135)
        self.image_down.set_colorkey(BLACK)
        self.image = self.image_up
        self.rect = self.image.get_rect()
        self.rect.centerx = choice([-100, WIDTH + 100])
        self.dx = randrange(1, 4)
        if self.rect.centerx > WIDTH:
            self.dx *= -1
        self.rect.y = randrange(HEIGHT / 2)
        self.vy = 0
        self.dy = 0.5

    def update(self):
        self.rect.x += self.dx
        self.vy += self.dy
        if not -3 < self.vy < 3:
            self.dy *= -1
        center = self.rect.center
        self.image = self.image_up if self.dy < 0 else self.image_down
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.rect.y += self.vy
        if not -100 < self.rect.centerx < WIDTH + 100:
            self.kill()
