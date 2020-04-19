import pygame
from constants1 import *
from random import uniform, choice
VEC = pygame.math.Vector2


def collide_with_wall(sprite, group, dir):
    if dir == 'x':
        hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centerx > sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / 2
            elif hits[0].rect.centerx < sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / 2
            sprite.vel.x = 0
            sprite.hit_rect.centerx = sprite.pos.x
    if dir == 'y':
        hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centery > sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height / 2
            elif hits[0].rect.centery < sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / 2
            sprite.vel.y = 0
            sprite.hit_rect.centery = sprite.pos.y


def collide_hit_rect(one, two):
    return one.hit_rect.colliderect(two.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = PLAYER_LAYER
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.pos = VEC(x, y)
        self.vel = VEC(0, 0)
        self.rot = 0
        self.last_shot = 0
        self.health = PLAYER_HEALTH

    def get_keys(self):
        self.rot_speed = 0
        self.vel = VEC(0, 0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rot_speed = PLAYER_ROT_SPEED
        if keys[pygame.K_RIGHT]:
            self.rot_speed = -PLAYER_ROT_SPEED
        if keys[pygame.K_UP]:
            self.vel = VEC(PLAYER_SPEED, 0).rotate(-self.rot)
        if keys[pygame.K_DOWN]:
            self.vel = VEC(-PLAYER_SPEED / 2, 0).rotate(-self.rot)
        if keys[pygame.K_SPACE]:
            now = pygame.time.get_ticks()
            if now - self.last_shot > BULLET_RATE:
                self.last_shot = now
                dir = VEC(1, 0).rotate(-self.rot)
                pos = self.pos + BARREL_OFFSET.rotate(-self.rot)
                Bullet(self.game, pos, dir)
                self.vel = VEC(-KICKBACK, 0).rotate(-self.rot)

    def update(self):
        self.get_keys()
        self.rot = (self.rot + self.rot_speed * self.game.dt) % 360
        self.image = pygame.transform.rotate(self.game.player_img, self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt
        self.hit_rect.centerx = self.pos.x
        collide_with_wall(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_wall(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center
        hits = pygame.sprite.spritecollide(self, self.game.enemys, False)
        if hits:
            self.pos += VEC(ENEMY_KNOCKBACK, 0).rotate(-hits[0].rot)
            for hit in hits:
                self.health -= ENEMY_DAMAGE
                hit.vel = VEC(0, 0)
            if self.health <= 0:
                self.game.playing = False

    def draw_player_health(self, surface, x, y):
        BAR_LENGTH = 200
        BAR_HEIGHT = 20
        fill = BAR_LENGTH * self.health // PLAYER_HEALTH
        outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
        fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
        if self.health > PLAYER_HEALTH * 0.6:
            col = GREEN
        elif self.health > PLAYER_HEALTH * 0.3:
            col = YELLOW
        else:
            col = RED
        pygame.draw.rect(surface, col, fill_rect)
        pygame.draw.rect(surface, WHITE, outline_rect, 2)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = ENEMY_LAYER
        self.groups = game.all_sprites, game.enemys
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.enemy_img
        self.rect = self.image.get_rect()
        self.hit_rect = ENEMY_HIT_RECT.copy()
        self.hit_rect.center = self.rect.center
        self.pos = VEC(x, y)
        self.vel = VEC(0, 0)
        self.acc = VEC(0, 0)
        self.rect.center = self.pos
        self.rot = 0
        self.health = ENEMY_HEALTH
        self.speed = choice(ENEMY_SPEED)

    def avoid_enemys(self):
        for enemy in self.game.enemys:
            if enemy != self:
                dist = self.pos - enemy.pos
                if 0 < dist.length() < AVOID_RADIUS:
                    self.acc += dist.normalize()

    def update(self):
        self.rot = (self.game.player.pos - self.pos).angle_to(VEC(1, 0))
        self.image = pygame.transform.rotate(self.game.enemy_img, self.rot)
        self.acc = VEC(1, 0).rotate(-self.rot)
        self.avoid_enemys()
        self.acc.scale_to_length(self.speed)
        self.acc += self.vel * -1
        self.vel += self.acc * self.game.dt
        self.pos += self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2
        self.hit_rect.centerx = self.pos.x
        collide_with_wall(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_wall(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center
        self.draw_health()
        hits = pygame.sprite.spritecollide(self, self.game.bullets, False)
        if hits:
            self.health -= BULLET_DAMAGE
            self.vel = VEC(0, 0)
            hits[0].kill()
        if self.health <= 0:
            self.kill()

    def draw_health(self):
        if self.health > ENEMY_HEALTH * 0.6:
            col = GREEN
        elif self.health > ENEMY_HEALTH * 0.3:
            col = YELLOW
        else:
            col = RED
        width = self.rect.width * self.health // ENEMY_HEALTH
        health_rect = pygame.Rect(0, 0, width, 7)
        if self.health < ENEMY_HEALTH:
            pygame.draw.rect(self.image, col, health_rect)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, game, pos, dir):
        self._layer = PLAYER_LAYER
        self.groups = game.all_sprites, game.bullets
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.bullet_img
        self.rect = self.image.get_rect()
        self.hit_rect = self.rect
        self.pos = VEC(pos)
        self.rect.center = self.pos
        spread = uniform(-GUN_SPREAD, GUN_SPREAD)
        self.vel = BULLET_SPEED * dir.rotate(spread)
        self.spawn_time = pygame.time.get_ticks()

    def update(self):
        self.pos += self.vel * self.game.dt
        self.rect.center = self.pos
        if pygame.sprite.spritecollideany(self, self.game.walls):
            self.kill()
        if pygame.time.get_ticks() - self.spawn_time > BULLET_LIFE:
            self.kill()


class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = PLAT_LAYER
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.wall_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self._layer = PLAT_LAYER
        self.groups = game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pygame.Rect(x, y, w, h)
        self.hit_rect = self.rect
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
