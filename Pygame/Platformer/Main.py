from Constants import *
from Soldier import *
from Itembox import *
import random


class Game(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.playing = True

    def run(self):
        self.load_data()
        self.running = True
        self.menuMain()
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def load_data(self):
        self.level = 1
        
        self.enemys = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.itemboxes = pygame.sprite.Group()
        self.player = Soldier(self, 'player', 200, 300)
        for _ in range(3):
            self.enemys.add(Soldier(self, 'enemy', random.randint(0, WIDTH), random.randint(0, HEIGHT-60)))
    
    def menuMain(self):
        onMainMenu = True
        while onMainMenu:
            # event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    onMainMenu = False
                    self.playing = False
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        onMainMenu = False
                        self.playing = False
                        self.running = False
                    if event.key == pygame.K_SPACE:
                        onMainMenu = False
            # update
            # draw
            self.screen.fill(COL_BG)
            self.draw_text(TITLE, 44, RED, WIDTH//2, HEIGHT//4)
            self.draw_text('Press Space to start', 22, RED, WIDTH//2, HEIGHT//2)
            pygame.display.update()

    def menuPause(self):
        onPauseMenu = True
        # create menu options
        options = ['Resume', 'Restart', 'Quit']
        selected = 0
        while onPauseMenu:
            # event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    onPauseMenu = False
                    self.playing = False
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        onPauseMenu = False
                    if event.key == pygame.K_UP:
                        selected = (selected - 1) % len(options)
                    if event.key == pygame.K_DOWN:
                        selected = (selected + 1) % len(options)
            # update
            if selected == 0:
                if pygame.key.get_pressed()[pygame.K_RETURN]:
                    onPauseMenu = False
            elif selected == 1:
                if pygame.key.get_pressed()[pygame.K_RETURN]:
                    self.load_data()
                    onPauseMenu = False
            elif selected == 2:
                if pygame.key.get_pressed()[pygame.K_RETURN]:
                    onPauseMenu = False
                    self.playing = False
                    self.running = False
            # draw
            self.screen.fill(COL_BG)
            self.draw_text('PAUSED', 44, RED, WIDTH//2, HEIGHT//4)
            # draw menu options
            for i in range(len(options)):
                if i == selected:
                    self.draw_text(options[i], 24, BLUE, WIDTH//2, HEIGHT//2 + i*30)
                else:
                    self.draw_text(options[i], 22, RED, WIDTH//2, HEIGHT//2 + i*30)
            pygame.display.update()

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.SysFont(FONT_NAME, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.menuPause()
                if event.key == pygame.K_r:
                    self.running = False
    
    def update(self):
        if random.randint(1, 500) == 1 and len(self.itemboxes) < 3:
            self.itemboxes.add(Itembox(self, 'ammo', random.randint(0, WIDTH), random.randint(0, HEIGHT-60)))
        if random.randint(1, 700) == 1 and len(self.itemboxes) < 3:
            self.itemboxes.add(Itembox(self, 'health', random.randint(0, WIDTH), random.randint(0, HEIGHT-60)))
        
        self.player.update()
        for enemy in self.enemys:
            enemy.update()
        self.bullets.update()
        self.itemboxes.update()

    def draw(self):
        self.screen.fill(COL_BG)
        pygame.draw.line(self.screen, BLACK, (0, HEIGHT - 50), (WIDTH, HEIGHT - 50))
        for enemy in self.enemys:
            enemy.draw(self.screen)
        self.player.draw(self.screen)
        self.bullets.draw(self.screen)
        self.itemboxes.draw(self.screen)
        pygame.display.update()


if __name__ == "__main__":
    game = Game()
    while game.playing:
        game.run()
    pygame.quit()
    