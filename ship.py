import pygame
from pygame.sprite import Sprite
from pathlib import Path

class Ship(Sprite):
    """Controls the ship in the sideways_shooter"""
    def __init__(self, ai_game):
        """Initialize image size and location"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load image file into game
        self.image = Path(__file__).parent / "images/ship.bmp"
        self.image = pygame.image.load(self.image)
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        # Decimal placeholder for ship's position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        # Movement Flags
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False

    def update_movement(self):
        """Moves the ship by rect x or rect y"""
        if self.move_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.move_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        # Adds non-integer value of x/y coordinate to ship's speed
        self.rect.x = self.x
        self.rect.y = self.y

    def center_ship(self):
        """Center the ship to its original position"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """Loads in the ship with the designated coordinates"""
        self.screen.blit(self.image, self.rect)