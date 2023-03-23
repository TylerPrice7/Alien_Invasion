import pygame

class Button():
    """Class for making a button for players to press"""
    def __init__(self, ai_game, msg, base_color=(210, 210, 210), highlight_color=()):
        """Initialize button attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Get dimensions and properties for button
        self.width, self.height = 250, 50
        self.base_color = base_color
        self.highlight_color = highlight_color
        self.button_color = base_color
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)
        self.msg = msg

        # Build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Prep message on button
        self._prep_msg()

    def _prep_msg(self):
        """Turns msg into a rendered image and center text on button"""
        self.msg_image = self.font.render(self.msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def set_base_color(self):
        """Sets the button to its base color (not currently selected)"""
        self.button_color = self.base_color
        self._prep_msg()

    def set_highlight_color(self):
        """Highlights the color of the (selected) button"""
        self.button_color = self.highlight_color
        self._prep_msg()

    def update_msg_rect(self):
        """Moves text rect to where the button is when it moves"""
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draws button to the screen and the message on top"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

