import pygame

class Ship():
    """Controls the ship in the sideways_shooter"""
    def __init__(self, ai_game):
        """Initialize image size and location"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        # Load image file into game
        self.image = pygame.image.load('images/ship.bmp')
        self.img_rect = self.image.get_rect()
        self.img_rect.midbottom = self.screen_rect.midbottom
        # Decimal placeholder for ship's position
        self.x = float(self.img_rect.x)
        self.y = float(self.img_rect.y)
        # Movement Flags
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False

    def update_movement(self):
        """Checks _keyup_events() and _key_down_events() for verification"""
        if self.move_left and self.img_rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.move_right and self.img_rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.move_up and self.img_rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed
        if self.move_down and self.img_rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        # Adds non-integer value of x/y coordinate to ship's speed
        self.img_rect.x = self.x
        self.img_rect.y = self.y

    def blitme(self):
        """Loads in the ship with the designated coordinates"""
        self.screen.blit(self.image, self.img_rect)