from Constants import *
from Bullet import *
import os

vec = pygame.math.Vector2


class Soldier(pygame.sprite.Sprite):
    def __init__(self, game, type, x, y):
        super().__init__()
        self.game = game
        self.type = type
        
        self.action = 0
        self.direction = 1
        self.frame_index = 0
        self.jumping = False

        self.pos = vec(x, y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        self.images = self.load_images()
        self.image = self.images[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.pos

        self.health = 100
        self.max_health = self.health
        self.ammo = AMMO
        self.max_ammo = self.ammo
        self.shoot_cooldown = SHOOT_COOLDOWN
        self.last_shot = pygame.time.get_ticks()
        self.alive = True        
    
    def load_images(self):
        images = []
        animation_types = ['Idle', 'Run', 'Jump', 'Death']
        for animation in animation_types:
            temp_list = []
            num_of_frames = len(os.listdir(f'img/{self.type}/{animation}'))
            for i in range(num_of_frames):
                img = pygame.image.load(f'img/{self.type}/{animation}/{i}.png')
                img = pygame.transform.scale(img, (int(img.get_width() * SCALE), int(img.get_height() * SCALE)))
                temp_list.append(img)
            images.append(temp_list)
        return images

    def update(self):
        self.action = 0
        self.acc = vec(0, PLAYER_GRAVITY)
        if self.type == 'player' and self.alive:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.action = 1
                self.direction = -1
                self.acc.x = -PLAYER_SPEED
            if keys[pygame.K_RIGHT]:
                self.action = 1
                self.direction = 1
                self.acc.x = PLAYER_SPEED
            if keys[pygame.K_UP] and not self.jumping:
                self.jump()
            if keys[pygame.K_SPACE]:
                self.shoot()
        if self.type == 'enemy' and self.alive:
            self.ai()
        
        # apply laws of physics
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # Wrap around the sides of the screen
        if self.pos.x > WIDTH + self.rect.width / 2:
            self.pos.x = 0 - self.rect.width / 2
        if self.pos.x < 0 - self.rect.width / 2:
            self.pos.x = WIDTH + self.rect.width / 2
        self.rect.midbottom = self.pos
        
        # stop from falling off screen
        if self.pos.y > HEIGHT - 50:
            self.pos.y = HEIGHT - 50
            self.vel.y = 0
            self.jumping = False

        if self.health <= 0:
            self.action = 3
            self.alive = False
        
        self.animate()

    def jump(self):
        self.vel.y = -PLAYER_JUMP_SPEED
        self.jumping = True

    def shoot(self):
        now = pygame.time.get_ticks()
        if self.ammo > 0 and now - self.last_shot > self.shoot_cooldown:
            self.ammo -= 1
            self.last_shot = now
            bullet = Bullet(self.game, self.rect.centerx + (0.75 * self.rect.size[0] * self.direction), self.rect.centery, self.direction)
            self.game.bullets.add(bullet)
    
    def ai(self):
        # advanced enemy ai
        if self.game.player.pos.x > self.pos.x and abs(self.game.player.pos.x - self.pos.x) < 150:
            self.acc.x = ENEMY_SPEED
            self.action = 1
            self.direction = 1
        elif self.game.player.pos.x < self.pos.x and abs(self.game.player.pos.x - self.pos.x) < 150:
            self.acc.x = -ENEMY_SPEED
            self.action = 1
            self.direction = -1
        else:
            self.acc.x = 0
        if abs(self.game.player.pos.x - self.pos.x) < 20 and abs(self.game.player.pos.y - self.pos.y) < 20:
            self.shoot()
        # jump if near enemy and on platform
        if self.game.player.pos.y > self.pos.y and abs(self.game.player.pos.x - self.pos.x) < 100 and abs(self.game.player.pos.x - self.pos.x) > 20:
            self.jump()
        
    def animate(self):
        self.frame_index += ANIMATION_SPEED
        if self.jumping:
            self.action = 2
        if self.frame_index >= len(self.images[self.action]):
            self.frame_index = 0
            # death animation is done playing
            if self.action == 3: 
                self.kill()
        self.image = pygame.transform.flip(self.images[self.action][int(self.frame_index)], self.direction == -1, False)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        # health bar
        pygame.draw.rect(screen, BLACK, (self.rect.x, self.rect.y - 6, self.rect.width, 6))
        pygame.draw.rect(screen, RED, (self.rect.x, self.rect.y - 6, self.rect.width * (self.health / self.max_health), 6))
        # ammo bar
        pygame.draw.rect(screen, BLACK, (self.rect.x, self.rect.y - 12, self.rect.width, 6))
        pygame.draw.rect(screen, BLUE, (self.rect.x, self.rect.y - 12, self.rect.width * (self.ammo / 30), 6))

