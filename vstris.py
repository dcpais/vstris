import effects
import animated

import pygame
import os
from PIL import Image

from pygame.locals import *
from typing import List, Tuple


class Vstris:
    """
    Container class for Vstris game logic and gui rendering, hosting 
    the main surface window pygame creates

    #-----------------------DRAWING----------------------------#
    Throughout this class there are "draw" functions, which 
    are responsible for blitting (i.e. drawing onto the screen)
    all componenets of the game / GUI. 

    Each draw function independently updates its segment's 
    frame state. They are also responsible for playing any
    audio associated with frame updates if any.
    """
    # CONSTANTS -------------------------------- #
    WIDTH, HEIGHT = 0, 0
    FPS = 60
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
        self.mode = "main_menu"
        self.scale = 1
        self.blurred = False
        Vstris.WIDTH = dimensions[0]
        Vstris.HEIGHT = dimensions[1]

        # LOAD ASSETS -------------------------- #
        self.load_assets(self.scale) 

        # ANIMATION STATES --------------------- #
        """ Loading screen"""
        self.load_ticks = 0
        self.is_loading = True
        self.load_cf = Vstris.BLACK


    def load_assets(self, scale: float):
        # LOAD TEXTS ------------------- #
        self.title = Vstris.FONT.render("Vstris", True, Vstris.WHITE,)

        # LOAD IMAGES ------------------ #
        logo_img = pygame.image.load(os.path.join("assets", "Loading", "Logo.jpg")).convert()
        logo_img.set_alpha(0)
        logo_img = pygame.transform.scale(logo_img, (200, 200))
        
        self.logo = animated.Animated(logo_img, Vstris.FPS / 20, effects.adjust_alpha, 1)
        self.board = pygame.image.load(os.path.join("assets", "Board", "board.png")).convert()

        self.block_1 = pygame.image.load(os.path.join("assets", "Tetriminos", "Purple.png")).convert_alpha()
        self.block_2 = pygame.image.load(os.path.join("assets", "Tetriminos", "yellow.png")).convert_alpha()
        self.block_3 = pygame.image.load(os.path.join("assets", "Tetriminos", "red.png")).convert_alpha()
        self.block_4 = pygame.image.load(os.path.join("assets", "Tetriminos", "green.png")).convert_alpha()
        self.block_5 = pygame.image.load(os.path.join("assets", "Tetriminos", "orange.png")).convert_alpha()
        self.block_6 = pygame.image.load(os.path.join("assets", "Tetriminos", "dark_blue.png")).convert_alpha()
        self.block_7 = pygame.image.load(os.path.join("assets", "Tetriminos", "blue.png")).convert_alpha()
        
        self.b_block_1 = effects.blur_surface(3, self.block_1)
        self.b_block_2 = effects.blur_surface(3, self.block_2)
        self.b_block_3 = effects.blur_surface(3, self.block_3)
        self.b_block_4 = effects.blur_surface(3, self.block_4)
        self.b_block_5 = effects.blur_surface(3, self.block_5)
        self.b_block_6 = effects.blur_surface(3, self.block_6)
        self.b_block_7 = effects.blur_surface(3, self.block_7)

        self.backdrop = pygame.image.load(os.path.join("assets", "Backdrop", "Backdrop.png")).convert()
        self.backdrop = effects.blur_surface(3, self.backdrop)

        # SCALE IMAGE ------------------- #
        self.board = pygame.transform.scale(self.board, (self.board.get_size()))
    

    def draw_loading(self):
        if self.load_ticks <= Vstris.FPS * 3.5:
            self.win.fill(self.load_cf)
            self.load_cf = (self.load_cf[0] + 1, self.load_cf[1] + 1, self.load_cf[2] + 1)
        
        elif self.load_ticks <= Vstris.FPS * 7:
            self.logo.tick()
            self.win.fill(self.load_cf)
            self.center_blit(self.logo.get_state(), (Vstris.WIDTH // 2, Vstris.HEIGHT // 2))

        else:
            self.mode = "main_menu"
            self.is_loading = False

        self.load_ticks += 1
        
        

    def draw_title(self):
        self.win.blit(self.title, (100, 100))
        self.win.blit(self.board, (100, 100))


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


    def center_blit(self, surface: pygame.Surface, coordinate: Tuple[int, int]):
        size = surface.get_size()
        self.win.blit(surface, (coordinate[0] - size[0] // 2, coordinate[1] - size[1] // 2))


    def run(self):
        """
        Main game loop
        
        All game logic is processed here, and all drawing is done
        at the end of each frame
        """
        self.clock = pygame.time.Clock()

        while self.running:
            self.clock.tick(Vstris.FPS)
            
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
                        pygame.quit()
                        return


            # CLEAR FRAME ----------------------- #
            self.win.fill(Vstris.BACKGROUND)

            # PICK STATE AND DRAW --------------- #
            if self.mode == "intro":
                self.draw_loading()

            elif self.mode == "main_menu":
                self.draw_title()
                self.draw_menu()
                self.draw_version() 
                self.win.blit(self.block_1, (100, 100))

            elif self.mode == "settings":
                pass

            elif self.mode == "singeplayer":
                pass

            elif self.mode == "pause":
                self.win.fill(Vstris.WHITE)

            # UPDATE SCREEN --------------------- #
            #self.win.blit(self.board, (350, 100))
            pygame.display.update()

    

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