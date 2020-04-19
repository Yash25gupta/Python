import pygame
from random import randint, choice
from constants import *
from sprites import *
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "750,100"


class Game(object):

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREENSIZE)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.font_name = pygame.font.match_font(FONT)
        self.load_data()

    def load_data(self):
        self.spritesheet = Spritesheet(SPRITESHEET)
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
        self.platforms = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()
        self.player = Player(self)
        for plat in PLAT_LIST:
            Platform(self, *plat)
        self.score = 0
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()

    def update(self):
        self.all_sprites.update()

        # Player stand on platform if falling
        if self.player.vel.y > 0:
            plat_hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
            if plat_hits:
                plat = plat_hits[0]
                for hit in plat_hits:
                    if hit.rect.bottom > plat.rect.bottom:
                        plat = hit
                if self.player.pos.y < plat.rect.bottom:
                    self.player.jump()
                    if plat.type == 'one':
                        plat.kill()
                    elif plat.type == 'kill':
                        self.playing = False
                    elif plat.type == 'spring':
                        plat.image = plat.springs[1]
                        self.player.vel.y = PLAYER_JUMP * -2

        # Move screen and add new platform
        if self.player.rect.top < HEIGHT / 4:
            self.player.pos.y += max(abs(self.player.vel.y), 5)
            for plat in self.platforms:
                plat.rect.y += max(abs(self.player.vel.y), 5)
                if plat.rect.top > HEIGHT + 10:
                    plat.kill()
                    self.score += 10
        while len(self.platforms) < PLAT_COUNT:
            Platform(self, randint(10, WIDTH), randint(-75, -20))

        # Power ups
        power_hits = pygame.sprite.spritecollide(self.player, self.powerups, True)
        if power_hits:
            if power_hits[0].type == 'boost':
                self.player.vel.y = PLAYER_JUMP * -4
            elif power_hits[0].type == 'immune':
                pass

        # Die
        if self.player.rect.top > HEIGHT:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y, 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()
            if len(self.platforms) == 0:
                self.playing = False

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        self.draw_text('Score: ' + str(self.score), 22, WHITE, HALF_WIDTH, 20)
        pygame.display.update()

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
