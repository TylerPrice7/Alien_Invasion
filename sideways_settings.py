import pygame

class Settings():
    """Settings class for Alien Invasion game (sideways edition)"""
    def __init__(self):
        """Initializes settings for the screen, background color, ship,"""
        """ and bullets"""
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.screen_width = 1200
        self.screen_height = 700 
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.2
        self.bullet_color = (60, 60, 60)
        self.bullet_height = 10
        self.bullet_width = 30
        self.bullet_speed = 1.0
        self.bullet_max = 5
        self.alien_speed = 1
        # Direction of 1 means down, -1 means up
        self.change_direction = 1       



