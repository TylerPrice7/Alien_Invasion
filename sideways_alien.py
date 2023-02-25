import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class for Alien group. Controls pathing, speed, and strength"""
    def __init__(self, ai_game):
        """Initializes alien sprite"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load in Alien image and image size
        self.image = pygame.image.load('images/sideways_alien.bmp')
        self.rect = self.image.get_rect()

        # Set Alien to load near top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Finer control of vertical movement
        self.y = float(self.rect.y)

    def check_edges(self):
        """Checks if alien is at an edge of the screen and return True if so"""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
            return True

    def update(self):
        """Moves alien up or down the screen, depending on change_direction"""
        self.y += self.settings.alien_speed * self.settings.change_direction
        self.rect.y = self.y