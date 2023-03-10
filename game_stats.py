from sideways_settings import Settings

class GameStats():
    """Game Stats for Alien Invasion class"""
    def __init__(self, ai_game):
        """Initialize statistics"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.reset_stats()
        # Start the Alien Invasion game in an inactive state
        self.game_active = False

    def reset_stats(self):
        """Reset game stats"""
        self.ships_left = self.settings.ships_limit
        self.aliens_left = self.settings.aliens_until_win