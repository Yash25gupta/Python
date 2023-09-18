from typing import List
from settings import *
import math
from map import Map


class Player():
    def __init__(self, game, pos=(90, 90)):
        self.game = game
        self.map : Map = game.map
        self.angle = 0
        self.rect = pygame.Rect(pos[0], pos[1], 8, 8)
        self.fov = 60

    def update(self):
        dx, dy = 0, 0
        sinA, cosA = math.sin(math.radians(self.angle)), math.cos(math.radians(self.angle))
        keyCount = -1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            keyCount += 1
            dx += PLAYER_SPEED * sinA
            dy -= PLAYER_SPEED * cosA
        if keys[pygame.K_RIGHT]:
            keyCount += 1
            dx -= PLAYER_SPEED * sinA
            dy += PLAYER_SPEED * cosA
        if keys[pygame.K_UP]:
            keyCount += 1
            dx += PLAYER_SPEED * cosA
            dy += PLAYER_SPEED * sinA
        if keys[pygame.K_DOWN]:
            keyCount += 1
            dx -= PLAYER_SPEED * cosA
            dy -= PLAYER_SPEED * sinA

        if keyCount: # diagonal movement correction
            dx /= math.sqrt(2)
            dy /= math.sqrt(2)
        
        self.collide_with_walls(dx, dy)
        self.rays = self.get_rays()
    
    def collide_with_walls(self, dx, dy):
        for wall in self.map.walls:
            if wall.colliderect(self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height):
                dx = 0
            if wall.colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height):
                dy = 0
        self.rect.x += dx
        self.rect.y += dy

    def get_rays(self):
        rays = []
        for ray in range(120):
            rads = math.radians(self.angle + ray/2 - self.fov/2)
            dist, epos = self.cast_single_ray(rads)
            rays.append((dist, rads, epos))
        return rays
    
    def cast_single_ray(self, rads):
        x, y = self.rect.center
        dx, dy = math.cos(rads), math.sin(rads)
        while True:
            x += dx
            y += dy
            if self.map.map_data[int(y // TILESIZE)][int(x // TILESIZE)] == 1:
                return (math.sqrt((self.rect.centerx - x) ** 2 + (self.rect.centery - y) ** 2), (x,y))

    def draw(self, screen):
        self.draw_fov(screen)
        pygame.draw.rect(screen, GREEN, self.rect)
        self.cast_rays(screen)

    def draw_fov(self, screen):
        for ray in self.rays:
            pygame.draw.line(screen, GREEN, self.rect.center, ray[2])
    
    def cast_rays(self, screen):
        SCALE = HALF_WIDTH // len(self.rays)
        for i, ray in enumerate(self.rays):
            dist, rads, _ = ray
            c = 200 / (1 + dist * dist * 0.0001)
            # dist *= math.cos(math.radians(self.angle) - rads)
            wall_height = 21000 / (dist + 0.0001)
            pygame.draw.rect(screen, (c, c, c), (HALF_WIDTH + i * SCALE, HALF_HEIGHT - wall_height / 2, SCALE, wall_height))
            