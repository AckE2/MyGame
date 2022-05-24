import pygame
from laser import Laser

class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.image.load('player.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(midbottom = pos)
        self.speed = 5
        self.over = False
        self.ready = True
        self.laser_time = 0
        self.laser_cooldown = 100

        self.lasers = pygame.sprite.Group()

    
    def get_input(self):
        if self.over:
            return
            
        keys = pygame.key.get_pressed()
    

        if keys[pygame.K_RIGHT] and self.rect.x < 600 - 50:
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT] and self.rect.x > 10:
            self.rect.x -= self.speed
        elif keys[pygame.K_DOWN] and self.rect.y < 600 - 50:
            self.rect.y += self.speed
        elif keys[pygame.K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed

        if keys[pygame.K_SPACE] and self.ready:
            self.shoot_laser()
            self.ready = False
            self.laser_time = pygame.time.get_ticks()

    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_cooldown:
                self.ready = True

    def shoot_laser(self):
        self.lasers.add(Laser(self.rect.center))

    def update(self):
        self.get_input()
        self.recharge()
        self.lasers.update()

    