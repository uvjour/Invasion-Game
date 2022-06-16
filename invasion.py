import sys
import pygame
from settings import Settings
from fighter import Fighter
from bullet import Bullet
from enemy import Enemy

class Invasion():
    # init function
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Invasion')
        self.fighter = Fighter(self)
        self.bullets = pygame.sprite.Group()
        self.enemy = pygame.sprite.Group()
        self._create_fleet()



    def rungame(self):
        while True:
            self._check_events()
            self.fighter.update()
            self._update_bullets()
            self._update_screen()


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        # Move plane to the right
        if event.key == pygame.K_RIGHT:
            self.fighter.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move plane to the right
            self.fighter.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.fighter.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.fighter.moving_left = False


    def _update_screen(self):
        # Redrawing the color at every pass of the loop
        self.screen.fill(self.settings.bg_color)
        self.fighter.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            self.enemy.draw(self.screen)
        pygame.display.flip()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    
    def _create_fleet(self):
        enemy = Enemy(self)
        enemy_width = enemy.rect.width
        available_space_x = self.settings.screen_width - (2 * enemy_width)
        number_enemy_x = available_space_x // (2 * enemy_width)

        for enemy_number in range(number_enemy_x):
            enemy = Enemy(self)
            enemy.x = enemy_width + 2 * enemy_width * enemy_number
            enemy.rect.x = enemy.x
            self.enemies.add(enemy)
        


if __name__ == '__main__':
    ig = Invasion()
    ig.rungame()