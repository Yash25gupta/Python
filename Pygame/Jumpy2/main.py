import pygame
from random import randint, choice
from constants import *
from sprites import *


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
        self.draw_text('Arrow to Move, Space to Jump',
                       22, WHITE, HALF_WIDTH, HALF_HEIGHT)
        self.draw_text('High Score : ' + str(self.highscore),
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
        # Start new Game
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.platforms = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()
        self.enemys = pygame.sprite.Group()
        self.player = Player(self)
        for plat in PLATFORM_LIST:
            Platform(self, *plat)
        self.score = 0
        self.enemy_timer = 0
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
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.player.jump_cut()

    def update(self):
        self.all_sprites.update()

        # new Enemy
        now = pygame.time.get_ticks()
        if now - self.enemy_timer > 5000 + choice([-1000, -500, 0, 500, 1000]):
            self.enemy_timer = now
            Enemy(self)

        # if player hit Enemy
        enemy_hits = pygame.sprite.spritecollide(
            self.player, self.enemys, False, pygame.sprite.collide_mask)
        if enemy_hits:
            self.playing = False

        # Player stand on platform
        if self.player.vel.y >= 0:
            hits = pygame.sprite.spritecollide(
                self.player, self.platforms, False)
            if hits:
                lowest = hits[0]
                for hit in hits:
                    if hit.rect.bottom > lowest.rect.bottom:
                        lowest = hit
                if lowest.rect.left - 10 < self.player.pos.x < lowest.rect.right + 10:
                    if self.player.pos.y < lowest.rect.centery:
                        self.player.pos.y = lowest.rect.top
                        self.player.vel.y = 0
                        self.player.jumping = False

        # Move Screen and kill Platform
        if self.player.rect.top < HEIGHT / 4:
            self.player.pos.y += max(abs(self.player.vel.y), 5)
            for enemy in self.enemys:
                enemy.rect.y += max(abs(self.player.vel.y), 5)
            for plat in self.platforms:
                plat.rect.y += max(abs(self.player.vel.y), 5)
                if plat.rect.y > HEIGHT:
                    plat.kill()
                    self.score += 10

        # if player hits powerup
        pow_hits = pygame.sprite.spritecollide(
            self.player, self.powerups, True)
        for power in pow_hits:
            if power.type == 'jet':
                self.player.vel.y = -JET_POWER
                self.player.jumping = False
            if power.type == 'wing':
                self.player.vel.y = -WING_POWER
                self.player.jumping = False

        # Create new Platform
        while len(self.platforms) < PLAT_NUMBERS:
            Platform(self, randint(0, WIDTH - 50), randint(-70, -30))

        # Die
        if self.player.rect.bottom > HEIGHT:
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
        self.draw_text('Score : ' + str(self.score),
                       22, WHITE, HALF_WIDTH, HALF_HEIGHT)
        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text('NEW HIGH SCORE', 24, WHITE,
                           HALF_WIDTH, HALF_HEIGHT + 30)
            with open(HS_FILE, 'w') as f:
                f.write(str(self.highscore))
        else:
            self.draw_text('High Score : ' + str(self.highscore),
                           22, WHITE, HALF_WIDTH, HALF_HEIGHT + 30)

        self.draw_text('Press any key to start New Game',
                       22, WHITE, HALF_WIDTH, HEIGHT * 3 / 4)
        self.draw_text('Press Esc to Exit', 22, WHITE,
                       HALF_WIDTH, HEIGHT * 3 / 4 + 30)

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
