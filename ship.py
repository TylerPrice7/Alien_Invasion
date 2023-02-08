import pygame
from settings import Settings

class Ship():
    """Controls the ship in the sideways_shooter"""
    def __init__(self):
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('Alien_Invasion/images/ship.bmp')
        self.img_rect = self.image.get_rect()
        self.img_rect.midbottom = self.screen.midbottom

    def update(self):
        pass
    def blitme(self):
        self.screen.blit(self.image, self.img_rect) # Load in the image

