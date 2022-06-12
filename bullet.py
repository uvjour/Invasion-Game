import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ig_game):
        super().__init__()
        self.screen = ig_game.screen
        self.settings = ig_game.settings
        self.color = ig_game.settings.bullet_color
        
        self.rect = pygame.Rect(0,0, ig_game.settings.bullet_width, ig_game.settings.bullet_height)
        self.rect.midtop = ig_game.fighter.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
