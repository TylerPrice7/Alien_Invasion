from pathlib import Path

class GameStats():
    """Game Stats for Alien Invasion class"""
    def __init__(self, ai_game):
        """Initialize statistics"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.file_name = Path(__file__).parent / "high_score.txt"
        self.reset_stats()

        # Score gets made after reset_stats()
        self.get_high_score()

        # Start the Alien Invasion game in an inactive state
        self.game_active = False

    def reset_stats(self):
        """Reset game stats"""
        self.score = 0
        self.ships_left = self.settings.ships_limit

    def create_high_score_file(self):
        """Creates a new text file if none exists or a score is missing"""
        self.scores = ['0\n', '0\n', '0\n']
        with open(self.file_name, 'w') as file_object:
            file_object.writelines(self.scores)
        self.high_score = 0

    def write_new_high_score(self):
        """Write new highscore to text file"""
        with open(self.file_name, 'w') as file_object:
            if self.settings.difficulty_level == 'easy':
                self.scores[0] = str(self.score) + '\n'
            elif self.settings.difficulty_level == 'medium':
                self.scores[1] = str(self.score) + '\n'
            elif self.settings.difficulty_level == 'hard':
                self.scores[2] = str(self.score) + '\n'
            else: pass
            file_object.writelines(self.scores)
        self.high_score = self.score

    def get_high_score(self):
        """Tries to read folder and get high score"""
        try:
            with open(self.file_name, 'r') as file_object:
                self.scores = file_object.readlines()
        except FileNotFoundError:
            self.create_high_score_file()
        # In case there is a text file already made without any contents
        if not self.scores:
            self.create_high_score_file()
        else: 
            self.get_difficulty_high_score()

    def get_difficulty_high_score(self):
        """Sets the high score as the one set by the difficulty level"""
        self.difficulty_level = self.settings.difficulty_level
        if self.difficulty_level == 'easy':
            self.high_score = int(self.scores[0].strip())
        elif self.difficulty_level == 'medium':
            self.high_score =  int(self.scores[1].strip())
        elif self.difficulty_level == 'hard':
            self.high_score = int(self.scores[2].strip())