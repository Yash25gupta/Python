import pygame
from constants1 import *
from sprites1 import *
from tilemap1 import *
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "50,50"


class Game(object):

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREENSIZE)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(500, 100)
        self.font_name = pygame.font.match_font(FONT)
        self.running = True
        self.load_data()

    def load_data(self):
        self.map = TiledMap('maps\\' + MAPFILE)
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.player_img = pygame.image.load('img\\' + PLAYER_IMG).convert_alpha()
        self.enemy_img = pygame.image.load('img\\' + ENEMY_IMG).convert_alpha()
        self.bullet_img = pygame.image.load('img\\' + BULLET_IMG).convert_alpha()
        self.wall_img = pygame.image.load('img\\' + WALL_IMG).convert_alpha()
        self.wall_img = pygame.transform.scale(self.wall_img, (TILESIZE, TILESIZE))

        with open(HS_FILE, 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0

    def show_start_screen(self):
        self.screen.fill(BGCOLOR)
        self.draw_text(TITLE, 48, WHITE, HALF_WIDTH, HEIGHT / 4)
        self.draw_text('Press Arrow to Move', 22, WHITE, HALF_WIDTH, HALF_HEIGHT)
        self.draw_text('High Score: ' + str(self.highscore),
                       22, WHITE, HALF_WIDTH, HEIGHT * 3 / 4)
        pygame.display.update()
        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    waiting = False
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

    def new(self):
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.walls = pygame.sprite.Group()
        self.enemys = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        # for row, tiles in enumerate(self.map.data):
        #     for col, tile in enumerate(tiles):
        #         if tile == 'W':
        #             Wall(self, col, row)
        #         elif tile == 'E':
        #             Enemy(self, col, row)
        #         elif tile == 'P':
        #             self.player = Player(self, col, row)
        for tile_obj in self.map.tmxdata.objects:
            if tile_obj.name == 'player':
                self.player = Player(self, tile_obj.x, tile_obj.y)
            elif tile_obj.name == 'wall':
                Obstacle(self, tile_obj.x, tile_obj.y, tile_obj.width, tile_obj.height)
            elif tile_obj.name == 'zombie':
                Enemy(self, tile_obj.x, tile_obj.y)

        self.camera = Camera(self.map.width, self.map.height)
        self.debug = False
        self.score = 0
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    self.debug = not self.debug

    def update(self):
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw(self):
        pygame.display.set_caption(TITLE + ' - {:.2f} FPS'.format(self.clock.get_fps()))
        # self.screen.fill(DARKGREY)
        # self.draw_grid(LIGHTGREY)
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
            if self.debug:
                pygame.draw.rect(self.screen, CYAN,
                                 self.camera.apply_rect(sprite.hit_rect), 1)
        if self.debug:
            for wall in self.walls:
                pygame.draw.rect(self.screen, CYAN, self.camera.apply_rect(wall.rect), 1)

        self.player.draw_player_health(self.screen, 10, 10)
        pygame.display.update()

    def draw_grid(self, color):
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, color, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, color, (0, y), (WIDTH, y))

    def show_exit_screen(self):
        if not self.running:
            return
        self.screen.fill(BGCOLOR)
        self.draw_text('GAME OVER', 48, WHITE, HALF_WIDTH, HEIGHT / 4)
        self.draw_text('Score: ' + str(self.score), 22, WHITE, HALF_WIDTH, HALF_HEIGHT)
        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text('NEW HIGH SCORE', 24, WHITE, HALF_WIDTH, HALF_HEIGHT + 30)
            with open(HS_FILE, 'w') as f:
                f.write(str(self.highscore))
        else:
            self.draw_text('High Score : ' + str(self.highscore),
                           22, WHITE, HALF_WIDTH, HALF_HEIGHT + 30)
        self.draw_text('Press any key to start New Game',
                       22, WHITE, HALF_WIDTH, HEIGHT * 3 / 4)
        self.draw_text('Press Esc to Exit', 22, WHITE, HALF_WIDTH, HEIGHT * 3 / 4 + 30)

        pygame.display.update()
        self.wait_for_key()

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)


if __name__ == '__main__':
    g = Game()
    g.show_start_screen()
    while g.running:
        g.new()
        g.show_exit_screen()
    pygame.quit()
