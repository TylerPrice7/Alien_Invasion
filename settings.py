import pygame

class Settings():
    def __init__(self):
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.screen_width = 1200
        self.screen_height = 700 
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.2


