from Constants import *

vec = pygame.math.Vector2
box = {'ammo': 'ammo_box.png',
    'health': 'health_box.png'}

class Itembox(pygame.sprite.Sprite):
    def __init__(self, game, type, x, y):
        super().__init__()
        self.game = game
        self.type = type
        self.pos = vec(x, y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        img = pygame.image.load('img/icons/' + box[self.type])
        self.image = pygame.transform.scale(img, (int(img.get_width() * SCALE * 0.6), int(img.get_height() * SCALE * 0.6)))
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
    
    def update(self):
        if pygame.sprite.collide_rect(self, self.game.player):
            if self.type == 'ammo':
                self.game.player.ammo += 10
                if self.game.player.ammo > self.game.player.max_ammo:
                    self.game.player.ammo = self.game.player.max_ammo
            elif self.type == 'health':
                self.game.player.health += 20
                if self.game.player.health > self.game.player.max_health:
                    self.game.player.health = self.game.player.max_health
            self.kill()
        # apply laws of physics
        self.acc = vec(0, ENEMY_GRAVITY)
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # stop from falling off screen
        if self.pos.y > HEIGHT - 50:
            self.pos.y = HEIGHT - 50
            self.vel.y = 0
        
        self.rect.midbottom = self.pos

    def draw(self, screen):
        screen.blit(self.image, self.rect)