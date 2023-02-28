import pygame

class Settings():
    """Settings class for Alien Invasion game"""
    def __init__(self):
        """Initializes settings for the screen, background color, ship,"""
        """ and bullets"""
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.screen_width = 1200
        self.screen_height = 700 
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.2
        self.bullet_color = (60, 60, 60)
        self.bullet_height = 30
        self.bullet_width = 10
        self.bullet_speed = 1.0
        self.bullet_max = 5
        self.alien_speed = 1.0
        self.alien_drop_speed = 10
        # Direction of 1 means down, -1 means up
        self.change_direction = 1
        self.ships_limit = 3
        self.aliens_until_win = 50

