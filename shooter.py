import pygame, sys
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats

class AlienInvasion():
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = self.settings.screen
        self.screen_rect = self.screen.get_rect()
        #self.screen = pygame.display.set_mode((self.settings.screen_width,
            #self.settings.screen_height))
        self.stats = GameStats(self)
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
        """Sets movement booleans if key is not currently pressed"""
        if event.key == pygame.K_LEFT:
            self.ship.move_left = False
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        if event.key == pygame.K_UP:
            self.ship.move_up = False
        if event.key == pygame.K_DOWN:
            self.ship.move_down = False
    
    def _fire_bullet(self):
        """Create a new bullet and add to bullets group"""
        if len(self.bullets) < self.settings.bullet_max:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_bullet_collision(self):
        """Checks if any bullet has hit an alien. Both are deleted on impact"""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        for alien in collisions:
            self.stats.aliens_left -= 1

    def _update_bullets(self):
        """Removes bullets that have exited the screen perimeter"""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            self._check_bullet_collisions()

    def _check_bullet_collisions(self):
        """If all aliens are defeated, add new fleet and replenish bullets"""
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _create_fleet(self):
        """Creates the alien fleet"""
        alien = Alien(self)
        width, height = alien.rect.size
        # Checks how many aliens can fit down the screen and how many rows
        # can be comfortably placed so the ship has room to move
        available_y = self.screen_rect.height - self.ship.rect.height - (3 * height)
        available_x = self.screen_rect.width - 2 * width
        numalien_y = available_y // (2 * height)
        numalien_x = available_x // (2 * width)
        # Creates aliens in specific columns and row
        for alien_column in range(numalien_y):
            for alien_number in range(numalien_x):
                alien = Alien(self)
                width, height = alien.rect.size
                alien.x = width + (2 * width * alien_number)
                alien.rect.x = alien.x
                alien.rect.y = height + 2 * height * alien_column
                self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Checks all aliens to see if they have hit an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Changes the direction of the aliens and moves the fleet closer"""
        self.settings.change_direction *= -1
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.alien_drop_speed

    def _check_alien_screenend(self):
        """Checks if any alien has hit the end of the screen"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.screen_rect.bottom:
                self._ship_hit()
                break

    def _update_aliens(self):
        """Updates rect coordinates of aliens"""
        self._check_fleet_edges()
        self.aliens.update()

        # Check for ship and any alien collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        # Check for any aliens hitting bottom of screen
        self._check_alien_screenend()
        # Game is won once required aliens are hit
        if self.stats.aliens_left <= 0:
            self._invasion_win()

    def _ship_hit(self):
        if self.stats.ships_left > 1:
            self.stats.ships_left -= 1
            self.stats.aliens_left = self.settings.aliens_until_win

            # Get rid of any bullets or aliens on screen
            self.bullets.empty()
            self.aliens.empty()

            # Create a new alien fleet and put ship back to original position
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)
        else:
            self.stats.game_active = False

    def _invasion_win(self):
        # Get rid of any bullets or aliens on screen
        self.bullets.empty()
        self.aliens.empty()

        # Put the ship back to original position
        self.ship.center_ship()
        # End game
        self.stats.game_active = False

    def _update_screen(self):
        """Updates screen with background, ship, and bullets"""
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
            if self.stats.game_active:
                self.ship.update_movement()
                self.bullets.update()
                self._update_bullets()
                self._check_bullet_collision()
                self._update_aliens()
            self._update_screen()

if __name__ == '__main__':
    newgame = AlienInvasion()
    newgame.run_game()