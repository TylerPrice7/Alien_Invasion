import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class for Alien group. Controls pathing, speed, and strength"""
    def __init__(self, ai_game):
        """Initializes alien sprite"""
        super().__init__()
        self.screen = ai_game.screen
        self.alien_speed = 4

        # Load in Alien image and image size
        self.image = pygame.image.load('Alien_Invasion/images/sideways_alien.bmp')
        self.rect = self.image.get_rect()

        # Set Alien to load near top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Finer control of vertical movement
        self.y = float(self.rect.y)
        
        