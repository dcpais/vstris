import effects

import pygame
import os
from PIL import Image

from pygame.locals import *
from typing import List, Tuple


class Vstris:
    """
    Container class for Vstris game logic and
    gui rendering, hosting the main surface window 
    pygame creates
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
        self.fullscreen = True
        self.mode = "load"
        self.scale = 1
        self.blurred = False
        self.toggle_fullscreen()
        Vstris.WIDTH = dimensions[0]
        Vstris.HEIGHT = dimensions[1]

        # LOAD ASSETS -------------------------- #
        self.load_assets(self.scale)

        # GAME --------------------------------- #



    def load_assets(self, scale: float):
        # LOAD TEXTS ------------------- #
        self.title = Vstris.FONT.render("Vstris", True, Vstris.WHITE,)
        

        # LOAD IMAGES ------------------ #
        self.board_img = pygame.image.load(os.path.join("assets", "Board", "board.png")).convert()

        self.block_1 = pygame.image.load(os.path.join("assets", "Tetriminos", "Purple.png")).convert()
        self.block_2 = pygame.image.load(os.path.join("assets", "Tetriminos", "yellow.png")).convert()
        self.block_3 = pygame.image.load(os.path.join("assets", "Tetriminos", "red.png")).convert()
        self.block_4 = pygame.image.load(os.path.join("assets", "Tetriminos", "green.png")).convert()
        self.block_5 = pygame.image.load(os.path.join("assets", "Tetriminos", "orange.png")).convert()
        self.block_6 = pygame.image.load(os.path.join("assets", "Tetriminos", "dark_blue.png")).convert()
        self.block_7 = pygame.image.load(os.path.join("assets", "Tetriminos", "blue.png")).convert()
        
        self.backdrop = pygame.image.load(os.path.join("assets", "Backdrop", "Backdrop.png")).convert()
        self.backdrop = effects.blur_surface(self.backdrop, 2)


        # SCALE IMAGE ------------------- #
        self.board = pygame.transform.scale(self.board_img, (self.board_img.get_size()))
        

    def run(self):
        """
        Main game loop
        
        All game logic is processed here, and all drawing is done
        at the end of each frame
        """
        CLOCK = pygame.time.Clock()

        while self.running:
            CLOCK.tick(Vstris.FPS)
            
            # EVENT HANDLING -------------------- #
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.KEYDOWN:
                    if event.key == K_F11:
                        self.toggle_fullscreen()
                    elif event.key == K_ESCAPE:
                        self.mode == "pause"

            # CLEAR FRAME ----------------------- #
            self.win.blit(self.backdrop, (0,0))

            # PICK STATE AND DRAW --------------- #
            if self.mode == "load":
                self.mode = "main_menu"
                
                self.draw_title()
                self.draw_menu()
                self.draw_version()

            elif self.mode == "main_menu":
                self.draw_title()
                self.draw_menu()
                self.draw_version()

            elif self.mode == "settings":
                pass

            elif self.mode == "singeplayer":
                pass

            elif self.mode == "pause":
                self.win.fill(Vstris.WHITE)

            # UPDATE SCREEN --------------------- #
            self.win.blit(self.board, (350, 100))
            pygame.display.update()


    def draw_title(self):
        self.win.blit(self.title, (100, 100))

    def draw_menu(self):
        pass

    def draw_version(self):
        pass




    def toggle_fullscreen(self):

        self.fullscreen = not self.fullscreen
        if self.fullscreen: 
            self.win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else: 
            self.win = pygame.display.set_mode((1920, 1000))

        Vstris.WIDTH, Vstris.HEIGHT = self.win.get_size()
        self.load_assets(self.scale)


    

if __name__ == "__main__":
    """
    Entry of program
    """
    # Initialize pygame modules -----------------
    pygame.display.init()
    pygame.display.set_caption("Vstris!")
    win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    # Start game --------------------------------
    Vstris(win, win.get_size()).run()