import pygame
import os
import effects

from game import Game

class LoadAnimation:
    """
    Transition animation for when the player boots up 
    the game. Contains two parts.
    """

    def __init__(self):
        """
        Initialize Loading animation
        """
        _ = pygame.image.load(os.path.join("assets", "Loading", "Logo.png")).convert()
        _.set_alpha(0)
        self.logo = pygame.transform.scale(_, (200, 200))
        self.bg_colour = (0, 0, 0)
        self.ticks = 0

    def draw(self):
        """
        Update loading frame
        """
        if self.ticks <= Game.FPS * 3.5:
            self.bg_colour = tuple([x + 255 / (Game.FPS * 3.5) for x in self.bg_colour])
        elif self.ticks <= Game.FPS * 7:
            effects.adjust_alpha(self.logo, 1.5)
        else:
            Game.set_game_mode("main_menu")
        
        Game.WIN.fill(self.bg_colour)
        Game.center_blit(self.logo, Game.get_centre_screen())
        self.ticks += 1