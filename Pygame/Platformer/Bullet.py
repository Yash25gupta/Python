from Constants import *

vec = pygame.math.Vector2


class Bullet(pygame.sprite.Sprite):
    def __init__(self, game, x, y, direction):
        super().__init__()
        self.game = game
        self.pos = vec(x, y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        img = pygame.image.load('img/icons/bullet.png')
        self.image = pygame.transform.scale(img, (int(img.get_width() * SCALE), int(img.get_height() * SCALE)))
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.direction = direction
        self.speed = BULLET_SPEED
    
    def update(self):
        self.acc.x = self.speed * self.direction
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.center = self.pos

        if self.rect.left > WIDTH or self.rect.right < 0:
            self.kill()
        if pygame.sprite.collide_rect(self, self.game.player):
            self.kill()
            self.game.player.health -= 12
        for enemy in self.game.enemys:
            if pygame.sprite.collide_rect(self, enemy) and enemy.alive:
                enemy.health -= 20
                self.kill()
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
