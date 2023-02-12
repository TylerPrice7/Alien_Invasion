import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Holds attributes for bullets fired from the ship in game"""
    def __init__(self, ai_game):
        """Create bullet at ship's location"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        # Create bullet on screen, then move to correct location
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.img_rect.midtop
        # Store bullet's y value at float
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""
        self.y -= self.settings.bullet_speed
        # Set bullet location to the float value
        self.rect.y = self.y

    def draw_bullet(self):
        """Draws bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
