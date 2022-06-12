import pygame

class Fighter():
    def __init__(self, ig_game):
        self.screen = ig_game.screen
        self.settings = ig_game.settings
        self.screen_rect = ig_game.screen.get_rect()

        self.image = pygame.image.load('images/fighter.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        # movement flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        if self.moving_right:
            self.rect.x += self.settings.fighter_speed

        if self.moving_left:
            self.rect.x -= self.settings.fighter_speed


    def blitme(self):
        self.screen.blit(self.image, self.rect)

