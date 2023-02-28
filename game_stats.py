from sideways_settings import Settings

class GameStats():
    """Game Stats for Alien Invasion class"""
    def __init__(self, ai_game):
        """Initialize statistics"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.reset_stats()
        # Sets the Alien Invasion game as an active state
        self.game_active = True

    def reset_stats(self):
        """Reset game stats"""
        self.ships_left = self.settings.ships_limit
        self.aliens_left = self.settings.aliens_until_win