import pygame

class Meteor(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()

        self.image = pygame.image.load('meteor.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect(topleft = (x,y))
        

    def move(self, direction):
        self.rect.y += direction

    def update(self, direction):
        print(f"Update {direction}")
        pass