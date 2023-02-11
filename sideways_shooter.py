import pygame
import sys
from settings import Settings
from ship import Ship

class AlienInvasion():
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = self.settings.screen
        #self.screen = pygame.display.set_mode((self.settings.screen_width,
#self.settings.screen_height))
        self.ship = Ship(self)
        pygame.display.set_caption("Alien Rocket")

    def _check_events(self):
        """Checks for keyboard presses"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._keyup_events(event)

    def _keydown_events(self, event):
        """Sets movement boolean if key is being pressed"""
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_LEFT:
            self.ship.move_left = True
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        if event.key == pygame.K_UP:
            self.ship.move_up = True
        if event.key == pygame.K_DOWN:
            self.ship.move_down = True

    def _keyup_events(self, event):
        """Sets movement booleans if key is not currently pressed"""
        if event.key == pygame.K_LEFT:
            self.ship.move_left = False
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        if event.key == pygame.K_UP:
            self.ship.move_up = False
        if event.key == pygame.K_DOWN:
            self.ship.move_down = False
    
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color) # Fill screen with bg color
        self.ship.blitme() # Load ship image
        pygame.display.flip() # Show the screen

    def run_game(self):
        """Runs main loop of the game"""
        while True:
            self._check_events()
            self.ship.update_movement()
            self._update_screen()

if __name__ == '__main__':
    newgame = AlienInvasion()
    newgame.run_game()