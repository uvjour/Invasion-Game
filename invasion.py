import sys
import pygame
from settings import Settings
from fighter import Fighter

class Invasion():
    # init function
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Invasion')
        self.fighter = Fighter(self)
        self.fighter.update()

    def rungame(self):
        while True:
            self._check_events()
            self._update_screen()



    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        # Move plane to the right
                        self.fighter.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        # Move plane to the right
                        self.fighter.moving_left = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.fighter.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.fighter.moving_left = False

        

    def _update_screen(self):
        # Redrawing the color at every pass of the loop
        self.screen.fill(self.settings.bg_color)
        self.fighter.blitme()
        
        pygame.display.flip()



if __name__ == '__main__':
    ig = Invasion()
    ig.rungame()