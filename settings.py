import pygame

class Settings():
    """Settings class for alien game"""
    def __init__(self):
        """Initializes static settings for the  alien game"""
        # Screen config
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.screen_width = 1200
        self.screen_height = 700 
        self.bg_color = (230, 230, 230)
        # Bullet config
        self.bullet_color = (60, 60, 60)
        self.bullet_height = 30
        self.bullet_width = 10
        # Alien config
        self.alien_drop_speed = 10

        self.difficulty_level = 'medium'

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        self.alien_speed = 1.0
        self.bullet_speed = 2.0
        self.ship_speed = 1.2
        self.set_difficulty()

        # Direction of 1 means down, -1 means up
        self.change_direction = 1

    def set_difficulty(self):
        """
        Difficulty changes how fast the game becomes overtime, 
        score multiplier, and the number of hits allowed
        """
        if self.difficulty_level == 'easy':
            self.difficulty_scale = 0.10
            self.ships_limit = 3
            self.bullet_limit = 4
        elif self.difficulty_level == 'medium':
            self.difficulty_scale = 0.15
            self.ships_limit = 2
            self.bullet_limit = 3
        elif self.difficulty_level == 'hard':
            self.difficulty_scale = .30
            self.ships_limit = 1
            self.bullet_limit = 2

    def increase_difficulty(self):
        """Increase speed settings"""
        self.alien_speed += self.difficulty_scale
        self.bullet_speed += self.difficulty_scale
        self.ship_speed += self.difficulty_scale
