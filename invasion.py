import sys
import pygame
from settings import Settings


class Invasion():
    # init function
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Invasion')

    def rungame(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Redrawing the color at every pass of the loop
            self.screen.fill(self.settings.bg_color)
            
            pygame.display.flip()

if __name__ == '__main__':
    ig = Invasion()
    ig.rungame()