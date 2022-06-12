import pygame

class Settings():
    #  This class stores all the settings to run the game

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.fighter_speed = 1.5
        
        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 1.5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3


