import pygame
import pygame.font
from pathlib import Path

from settings import Settings

class InfoScreen():
    def __init__(self, ai_game):
        """Initializes screen attributes and calls to load logo"""
        self.screen  = ai_game.screen
        self.screen_rect = ai_game.screen_rect
        self.settings = Settings()

        self.load_info_img()
        # Attributes for info string image 
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.instructions_active = False
        

    def load_info_img(self):
        """Recieves help image and sets it to the center top of the screen"""
        self.image = Path(__file__).parent / "images/help_image.jpeg"
        self.image = pygame.image.load(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = self.screen_rect.bottom - self.rect.height - 20

    def load_instructions(self):
        """Instructions are sent to the screen over the background"""
        self.instructions_img = (Path(__file__).parent / 
            "images/instructions.jpeg")
        self.instructions_img = pygame.image.load(self.instructions_img)
        self.instructions_rect = self.instructions_img.get_rect()
        self.instructions_rect.center = self.screen_rect.center
        self.show_instructions()

    def show_instructions(self):
        """Loads in the logo at the set coords"""
        self.instructions_active = True
        self.screen.blit(self.instructions_img, self.instructions_rect)
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)
