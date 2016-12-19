import pygame
class Spöke(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("rsz_spoke.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.left = True
    def upp(self):
        self.rect.y -= self.rect.height * 1.2
        if self.rect.y < 0:
           self.rect.y = 0
    def ner(self):
        self.rect.y += self.rect.height * 1.2
        if self.rect.y > 540:
            self.rect.y = 600 - self.rect.height 
    def höger(self):
        if self.rect.x + self.rect.width < 750:
            self.rect.x += self.rect.width 
    
    def vänster(self):
        if self.rect.x > 0:
            self.rect.x -= self.rect.width 
