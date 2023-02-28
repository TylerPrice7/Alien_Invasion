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
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Set Alien to load near top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Finer control of horizontal movement
        self.x = float(self.rect.x)

    def check_edges(self):
        """Checks if alien is at an edge of the screen and return True if so"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Moves alien left or right, depending on change_direction"""
        self.x += self.settings.alien_speed * self.settings.change_direction
        self.rect.x = self.x