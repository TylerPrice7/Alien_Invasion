import pygame
from pathlib import Path

class Logo():
    def __init__(self, ai_game):
        """Initializes screen attributes and calls to load logo"""
        self.screen  = ai_game.screen
        self.screen_rect = ai_game.screen_rect
        self.load_logo()

    def load_logo(self):
        """Recieves logo image and sets it to the center top of the screen"""
        self.logo = Path(__file__).parent / "images/logo.jpeg"
        self.logo = pygame.image.load(self.logo)
        self.rect = self.logo.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.y += 15

    def blitme(self):
        """Loads in the logo at the set coords"""
        self.screen.blit(self.logo, self.rect)
