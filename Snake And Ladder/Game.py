from Constants import *
from Tile import *
from Player import *


class Game(object):
    ROLL_STATE = 0
    MOVE_STATE = 1
    SNADDER_STATE = 2
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, WIDTH))
        self.ROWS = self.COLS = WIDTH // TILE_WIDTH
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        self.state = Game.ROLL_STATE
        self.player = Player()
        self.tiles = self.createTiles()
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
                    self.playing = False
                elif event.key == pygame.K_n:
                    self.player.rollDie()
                    self.player.move()

    def update(self):
        if self.state == Game.ROLL_STATE:
            self.player.rollDie()
            self.state = Game.MOVE_STATE
        elif self.state == Game.MOVE_STATE:
            self.player.move()
            self.state = Game.SNADDER_STATE if self.player.isSnadder(self.tiles) else Game.ROLL_STATE
        elif self.state == Game.SNADDER_STATE:
            self.player.moveSnadder(self.tiles)
            self.state = Game.ROLL_STATE
            
        if self.player.spot >= len(self.tiles)-1:
            self.player.reset()

    def draw(self):
        self.screen.fill(WHITE)
        for tile in self.tiles:
            tile.draw(self.screen)
        for tile in self.tiles:
            tile.drawSnadder(self.screen, self.tiles)
        if self.state == Game.MOVE_STATE:
            self.player.drawPreview(self.screen, self.tiles)
        self.player.draw(self.screen, self.tiles)
        pygame.display.update()

    def createTiles(self):
        tiles = []
        x, y, d = 0, WIDTH-TILE_WIDTH, 1
        for i in range(self.ROWS*self.COLS):
            tiles.append(Tile(x, y, i))
            x += (TILE_WIDTH * d)
            if not 0 <= x < WIDTH:
                d *= -1
                x += TILE_WIDTH * d
                y -= TILE_WIDTH
        for _ in range(5):
            # Snake
            i = randint(self.COLS, len(tiles)-2)
            j = randint(1, i-self.COLS)
            tiles[i].snadder = -1 * abs(i-j)
            # Ladder
            i = randint(1, len(tiles) - self.COLS-1)
            j = randint(i+self.COLS, 98)
            tiles[i].snadder = abs(i-j)
        return tiles


if __name__ == '__main__':
    game = Game()
    while game.running:
        game.run()
    pygame.quit()
