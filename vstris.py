import pygame
import os
from typing import List, Tuple

class Animated:
    """
    Wrapper class to hold animated elements of 
    Vstris game.
    """
    def __init__(self, frames: List[pygame.Surface], speed: float):
        self.frames = frames
        self.current_frame = 0
        self.is_running = False
        self.speed
        
    

class Vstris:
    """
    Container class for Vstris game logic and
    gui rendering, hosting the main surface window 
    pygame creates
    """
    
    # General use variables
    WIDTH, HEIGHT = 0, 0
    FPS = 144

    #Colors
    WHITE = (255, 255, 255) 
    BLACK = (0, 0, 0)
    FOREGROUND = (85, 81, 81)
    BACKGROUND = (30, 25, 25)

    def __init__(self, window: pygame.Surface, dimensions: Tuple[int, int]):
        self.win = window
        self.running = True
        self.mode = "main_menu"
        Vstris.WIDTH = dimensions[0]
        Vstris.HEIGHT = dimensions[1]


    def run(self):
        """
        Main game loop. 
        
        All game logic is processed here, and all drawing is done
        at the end of each frame
        """
        CLOCK = pygame.time.Clock()

        while self.running:
            CLOCK.tick(Vstris.FPS)
            
            # EVENT HANDLING --------------------
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            # CLEAR FRAME -----------------------
            self.win.fill(Vstris.BACKGROUND)


            # UPDATE SCREEN ---------------------
            pygame.display.update()


if __name__ == "__main__":
    """
    Entry of program
    """
    # Initialize pygame modules -----------------
    pygame.display.init()
    pygame.display.set_caption("Vstris!")
    win = pygame.display.set_mode((1000, 800))

    # Start game --------------------------------
    Vstris(win, win.get_size()).run()