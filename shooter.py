import pygame, sys
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard
from bgmusic import Sounds
from game_logo import Logo
from help_screen import InfoScreen

class AlienInvasion():
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        # Initialize screen attributes
        self.screen = self.settings.screen
        self.screen_rect = self.screen.get_rect()
        #self.screen = pygame.display.set_mode((self.settings.screen_width,
            #self.settings.screen_height))

        # Create instances for each module
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.aliens = pygame.sprite.Group()  
        self.bullets = pygame.sprite.Group()
        self.scoreboard = Scoreboard(self)
        self.music = Sounds()
        self.logo = Logo(self)
        self.help_button = InfoScreen(self)

        pygame.display.set_caption("Alien Rocket")
        self._create_fleet()

        # Create the Play/Pause and Difficulty buttons
        self._create_play_pause_buttons()
        self._create_difficulty_buttons()
        self.music.play_bg_music()
        
    def _create_play_pause_buttons(self):
        self.play_button = Button(self, "Play")
        self.paused = False
        self.paused_button = Button(self, "Paused")

    def _create_difficulty_buttons(self):
        self.easy_difficulty = Button(self, "Easy", (0, 100, 0), (0, 240, 0))
        self.medium_difficulty = Button(self, "Normal", 
            (190, 190, 0), (255, 255, 0))
        self.hard_difficulty = Button(self, "Hard", 
            (190, 0, 50), (255, 0, 0))

        # Sets all buttons horizontal to each other, and above play button 
        self.easy_difficulty.rect.bottomright = self.play_button.rect.topleft
        self.easy_difficulty.rect.top /= 1.2
        self.easy_difficulty.update_msg_rect()

        self.medium_difficulty.rect.top = self.easy_difficulty.rect.top
        self.medium_difficulty.update_msg_rect()
         
        self.hard_difficulty.rect.topleft = (
            self.medium_difficulty.rect.topright)
        self.hard_difficulty.update_msg_rect()

        self.medium_difficulty.set_highlight_color()

    def _check_events(self):
        """Checks for keyboard and mouse presses"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.scoreboard.check_new_high_score()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_mouse_coords()
            elif event.type == pygame.KEYDOWN:
                self._keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._keyup_events(event)
    
    def _check_mouse_coords(self):
        """Checks if the mouse is clicked over any event buttons"""
        if not self.stats.game_active and not self.paused:
            mouse_pos = pygame.mouse.get_pos()
            self._check_play_button(mouse_pos)
            self._check_difficulty_buttons(mouse_pos)
            self._check_help_button(mouse_pos)
        
    def _check_play_button(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos):
            self.reset_game()
            self.stats.game_active = True
            pygame.mouse.set_visible(False)

    def _check_difficulty_buttons(self, mouse_pos):
        """Changes difficulty when a button is pressed and highlights color"""
        if self.easy_difficulty.rect.collidepoint(mouse_pos):
            self.settings.difficulty_level = "easy"
            self.settings.set_difficulty()
            self.stats.get_difficulty_high_score()
            self.easy_difficulty.set_highlight_color()
            self.medium_difficulty.set_base_color()
            self.hard_difficulty.set_base_color()

        elif self.medium_difficulty.rect.collidepoint(mouse_pos):
            self.settings.difficulty_level = "medium"
            self.settings.set_difficulty()
            self.stats.get_difficulty_high_score()
            self.medium_difficulty.set_highlight_color()
            self.easy_difficulty.set_base_color()
            self.hard_difficulty.set_base_color()

        elif self.hard_difficulty.rect.collidepoint(mouse_pos):
            self.settings.difficulty_level = "hard"
            self.settings.set_difficulty()
            self.stats.get_difficulty_high_score()
            self.hard_difficulty.set_highlight_color()
            self.easy_difficulty.set_base_color()
            self.medium_difficulty.set_base_color()

        self.reset_game()
        self.scoreboard.prep_high_score()
    
    def _check_help_button(self, mouse_pos):
        if self.help_button.rect.collidepoint(mouse_pos):
            self.help_button.load_instructions()

    def _keydown_events(self, event):
        """Sets movement boolean if key is being pressed"""
        if event.key == pygame.K_q:
            self.scoreboard.check_new_high_score()
            sys.exit()
        if event.key == pygame.K_p:
            if not self.stats.game_active and self.paused:
                self.paused = False
                self.stats.game_active = True
            elif self.stats.game_active and not self.paused:
                self.paused = True
        if event.key == pygame.K_b:
            if self.help_button.instructions_active:
                self.help_button.instructions_active = False
        if event.key == pygame.K_RETURN:
            if (not self.stats.game_active and not self.paused):
                self.reset_game()
                self.stats.game_active = True
                pygame.mouse.set_visible(False)
        if event.key == pygame.K_SPACE:
            if self.stats.game_active:
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
        if len(self.bullets) < self.settings.bullet_limit:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.music.sfx_bullet_sound()

    def _update_bullets(self):
        """Updates and removes bullets that have exited the screen"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_collisions()

    def _check_bullet_collisions(self):
        """
        Collisions with aliens increases the score. 
        Full fleet wipe increases difficulty
        """
        if pygame.sprite.groupcollide(self.bullets, self.aliens, True, True):
            self.music.sfx_alien_hit()
            self.stats.score += 1
            self.scoreboard.prep_score()

        if not self.aliens:
            # No aliens left to shoot, replenish and increase the speed
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_difficulty()

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

    def _check_alien_screen_end(self):
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
        self._check_alien_screen_end()

    def _ship_hit(self):
        """When your ship loses a life"""
        self.stats.ships_left -= 1
        sleep(0.5)
        if self.stats.ships_left > 0:
            self._reset_screen()
        else:
            self.stats.game_active = False
            self.reset_game()
            pygame.mouse.set_visible(True)

    def _reset_screen(self):
        """Clear screen, reset alien fleet, and center ship for next game"""
        # Get rid of any bullets or aliens on screen
        self.bullets.empty()
        self.aliens.empty()

        # Create new alien fleet and center the ship
        self._create_fleet()
        self.ship.center_ship()

    def _update_screen(self):
        """Updates screen with background, ship, and bullets"""
        self.screen.fill(self.settings.bg_color)
        if self.help_button.instructions_active:
            self.help_button.load_instructions()
            pygame.display.flip()
            return
        self.ship.blitme()
        for bullet in self.bullets:
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.scoreboard.prep_ship_lives()
        self.scoreboard.show_scores()

        if (not self.stats.game_active and not self.paused and
            (self.stats.ships_left == self.settings.ships_limit
            or self.stats.ships_left < 1)):
            # When the game has not started, 
            # has been beaten, or the player has lost all lives
            self.logo.blitme()
            self.help_button.blitme()
            self.play_button.draw_button()
            self.easy_difficulty.draw_button()
            self.medium_difficulty.draw_button()
            self.hard_difficulty.draw_button()
            self.music.reset_bg_volume()
        elif (not self.stats.game_active and not self.paused):
            # When the game is no longer paused
            self.stats.game_active = True
        elif self.paused:
            # When the game is paused
            self.stats.game_active = False
            self.paused_button.draw_button()

        pygame.display.flip()

    def run_game(self):
        """Runs main loop of the game"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.music.lower_bg_volume()
                self.ship.update_movement()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

    def reset_game(self):
        """Reset the game for next session"""
        self.scoreboard.check_new_high_score()
        self.stats.reset_stats()
        self.scoreboard.prep_score()
        self.scoreboard.prep_ship_lives()
        self._reset_screen()

if __name__ == '__main__':
    newgame = AlienInvasion()
    newgame.run_game()