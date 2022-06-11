import pygame

class Fighter():
    def __init__(self, ig_game):
        self.screen = ig_game.screen
        self.screen_rect = ig_game.screen.get_rect()

        self.image = pygame.image.load('images/fighter.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        # movement flag
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

