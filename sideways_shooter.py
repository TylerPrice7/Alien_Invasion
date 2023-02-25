import pygame
import sys
from sideways_settings import Settings
from sideways_ship import Ship
from sideways_bullet import Bullet
from sideways_alien import Alien

class AlienInvasion():
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = self.settings.screen
        self.screen_rect = self.screen.get_rect()
        #self.screen = pygame.display.set_mode((self.settings.screen_width,
            #self.settings.screen_height))
        self.ship = Ship(self)
        self.aliens = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        pygame.display.set_caption("Alien Rocket")
        self._create_fleet()

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
        if event.key == pygame.K_SPACE:
            self._fire_bullet()
        if event.key == pygame.K_LEFT:
            self.ship.move_left = True
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        if event.key == pygame.K_UP:
            self.ship.move_up = True
        if event.key == pygame.K_DOWN:
            self.ship.move_down = True

    def _keyup_events(self, event):
        """Sets movement booleans for ship if key is not currently pressed"""
        if event.key == pygame.K_LEFT:
            self.ship.move_left = False
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        if event.key == pygame.K_UP:
            self.ship.move_up = False
        if event.key == pygame.K_DOWN:
            self.ship.move_down = False
    
    def _fire_bullet(self):
        """Create a new bullet and adds to bullets group"""
        if len(self.bullets) < self.settings.bullet_max:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Removes bullets that have exited the screen perimeter"""
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.ship.screen_rect.right:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """Creates the alien fleet"""
        alien = Alien(self)
        width, height = alien.rect.size
        # Checks how many aliens can fit down the screen and how many rows
        # can be comfortably placed so the ship has room to move
        available_y = self.screen_rect.height - (2 * height) 
        available_x = self.screen_rect.width - self.ship.img_rect.width - 4 * width
        numalien_y = available_y // (2 * height)
        numalien_x = available_x // (2 * width)
        # Creates aliens in specific columns and row
        for alien_column in range(numalien_x):
            for alien_number in range(numalien_y):
                alien = Alien(self)
                width, height = alien.rect.size
                alien.rect.x = self.screen_rect.right - 2 * width * alien_column
                alien.y = height + 2 * height * alien_number
                alien.rect.y = alien.y
                self.aliens.add(alien)


    def _update_alien(self):
        """Moves alien down until hits screen, then left and up, vise-versa"""
        

    def _update_screen(self):
        """Updates screen with background, ship, aliens, and bullets"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets:
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def run_game(self):
        """Runs main loop of the game"""
        while True:
            self._check_events()
            self.ship.update_movement()
            self.bullets.update()
            self._update_bullets()
            self._update_screen()

if __name__ == '__main__':
    newgame = AlienInvasion()
    newgame.run_game()