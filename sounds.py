from game import Game

import pygame
import os

class Sounds:
    """
    Static class to hold all sound assets for game
    """

    MUSIC = None
    MUSIC_CHANNEL = None
    SFX_CHANNEL = None

    @staticmethod
    def init():
        Sounds.MUSIC = pygame.mixer.Sound(os.path.join("assets", "Sounds", "probability machine.mp3"))