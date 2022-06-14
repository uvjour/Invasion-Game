import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    def __init__(self, ig_game):
        super().__init__()
        self.screen = ig_game.screen

        self.image = pygame.image.load('images/enemy.bmp')
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.height
        self.rect.y = self.rect.width

        self.x = float(self.rect.x)