import effects
from menu import Button
from game import Game

import pygame
from typing import Tuple


class Testing:
    """
    Test suite
    """
    # CONSTANTS -------------------------------- #
    WIDTH, HEIGHT = 0, 0
    FPS = 144
    if not pygame.font.get_init(): pygame.font.init()
    FONT = pygame.font.SysFont("Fira Code", 60)

    # COLOURS ---------------------------------- #
    WHITE = (255, 255, 255) 
    BLACK = (0, 0, 0)
    FOREGROUND = (85, 81, 81)
    BACKGROUND = (30, 25, 25)

    def __init__(self, window: pygame.Surface, dimensions: Tuple[int, int]):
        """
        Initialize Vstris game
        """
        # SET DEFAULTS ------------------------- #
        self.win = window
        self.running = True
        Testing.WIDTH = dimensions[0]
        Testing.HEIGHT = dimensions[1]
        Game.start(self.win)

        # LOAD ASSETS -------------------------- #
        self.button = Button(100, 100, 300, 80)

    def run(self):
        """
        Main logic loop for testing
        """
        CLOCK = pygame.time.Clock()

        while self.running:
            CLOCK.tick(Testing.FPS)
            
            # EVENT HANDLING -------------------- #
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return    

            # CLEAR FRAME ----------------------- #
            self.win.fill(Testing.WHITE)

            # DRAW ------------------------------ #
            self.button.draw()

            # UPDATE SCREEN --------------------- #
            pygame.display.update()



if __name__ == "__main__":
    """
    Testing grounds
    """
    # Init -------------------------------------- #
    pygame.display.init()
    pygame.display.set_caption("Testing")
    win = pygame.display.set_mode((600, 800))

    # Start screen ------------------------------ #
    Testing(win, win.get_size()).run()