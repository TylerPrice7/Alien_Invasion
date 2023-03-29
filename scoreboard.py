import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard():
    """Keeps track of scoring information in a single game"""
    def __init__(self, ai_game):
        """Initalizes attributes"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        
        # Info for score image 
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_image()

    def prep_image(self):
        self.prep_score()
        self.prep_high_score()
        self.prep_ship_lives()

    def prep_score(self):
        """Turn score into a rendered image in the top right corner"""
        # Score needs to be a string to render
        self.score_str = "Score: {:,}".format(self.stats.score)
        self.score_img = self.font.render(self.score_str, True, self.text_color, self.settings.bg_color)
        self.score_rect = self.score_img.get_rect()

        # 20 left and down of right corner so it's cleaner
        self.score_rect.right = self.screen_rect.right - 15
        self.score_rect.top = 70

    def prep_high_score(self):
        """Turn score into a rendered image in the top right corner"""
        # Score needs to be a string to render
        self.high_score_str = str(self.stats.high_score)
        self.high_score_img = self.font.render(self.high_score_str, True, self.text_color, self.settings.bg_color)
        self.high_score_rect = self.high_score_img.get_rect()

        # 20 right and down of left corner so it's cleaner
        if self.stats.high_score >= 1000:
            self.high_score_rect.right = self.screen_rect.right - 15
        else:
            self.high_score_rect.right = self.screen_rect.right - 15
        self.high_score_rect.top = 20

    def prep_ship_lives(self):
        """Amount of ship lives is illustrated by images in top left"""
        self.lives = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.y = 10
            #ship.rect.y = ship.rect.height
            ship.rect.x = 10 + ship.rect.width * ship_number
            #ship.rect.x = (ship.rect.width +
                #ship.rect.width * ship_number)
            self.lives.add(ship)

    def check_new_high_score(self):
        """Writes new high score to file if game score is higher"""
        if self.stats.score > self.stats.high_score:
            self.stats.write_new_high_score()
            self.prep_high_score()
    
    def show_scores(self):
        """Draw the scores to the screen"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.lives.draw(self.screen)