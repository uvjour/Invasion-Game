import sys
import pygame

class Invasion():
    # init function
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Invasion')

        # Background Color
        self.bg_color = (230, 230, 230)

    def rungame(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Redrawing the color at every pass of the loop
            self.screen.fill(self.bg_color)
            
            pygame.display.flip()

if __name__ == '__main__':
    ig = Invasion()
    ig.rungame()