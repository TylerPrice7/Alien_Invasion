import pygame.mixer
from pathlib import Path
class Sounds():
    def __init__(self):
        """Gets sounds for playing in Alien Invasion"""
        pygame.mixer.init()
        # Sound taken from qubodup on opengameart
        self.bullet_sound = Path(__file__).parent / (
            "Sounds/arrowHit/arrowHit02.wav")
        # Sound taken from Iwan Gabovitch on opengameart
        self.alien_hit_sound = Path(__file__).parent / (
            "Sounds/swoshes/swosh-01.flac")
        # Sound taken from Zane Little Music on opengameart
        self.bg_sound = Path(__file__).parent / "Sounds/lick_the_chorus.wav"

    def sfx_bullet_sound(self):
        """Plays the sound of a bullet being shot (not really lol)"""
        pygame.mixer.Sound(self.bullet_sound).play()

    def sfx_alien_hit(self):
        """Play sound of target being hit"""
        pygame.mixer.Sound(self.alien_hit_sound).play()

    def play_bg_music(self):
        bg_music = pygame.mixer.Sound(self.bg_sound)
        pygame.mixer.Channel(2).play(bg_music, -1)

    def lower_bg_volume(self):
        pygame.mixer.Channel(2).set_volume(0.5)

    def reset_bg_volume(self):
        pygame.mixer.Channel(2).set_volume(1.0)

