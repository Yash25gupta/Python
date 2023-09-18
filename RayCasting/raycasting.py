from settings import *
import math

DISTANCE_TO_PROJ_PLANE = HALF_WIDTH / math.tan(math.radians(60 / 2))


class RayCasting():
    def __init__(self, game):
        self.game = game
        self.player = self.game.player
        self.map = self.game.map

    def ray_casting(self, screen):
        self.draw_background(screen)
        self.draw_stake(screen)
        self.draw_player_fov(screen)
    
    def draw_background(self, screen):
        pygame.draw.rect(screen, SKYBLUE, (0, 0, WIDTH, HALF_HEIGHT))
        pygame.draw.rect(screen, DARKGREY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))
    
    def draw_stake(self, screen):
        for ray in range(self.player.fov):
            pygame.draw.line(screen, DARKGREY, self.player.rect.center, self.player.rays[ray][0], 2)
    
    def draw_player_fov(self, screen):
        rads = math.radians(self.player.angle)
        for ray in self.player.rays:
            if ray[1] == rads:
                dist = ray[0] * math.cos(math.radians(self.player.angle - self.player.fov // 2))
                rectHeight = (TILESIZE / dist) * DISTANCE_TO_PROJ_PLANE
                rectWidth = WIDTH / self.player.fov
                rectX = ray[1] * rectWidth / TILESIZE
                rectY = HALF_HEIGHT - rectHeight / 2
                pygame.draw.rect(screen, RED, (rectX, rectY, rectWidth, rectHeight))
                break
