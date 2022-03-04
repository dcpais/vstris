from transitions import *
from background import *
from blocks import *
from game import *

import pygame
from pygame.locals import *

# ASSETS ------------------------------------------ #
#if not pygame.font.get_init(): pygame.font.init()
#FONT = pygame.font.SysFont("Fira Code", 60)
  
def run():
    """
    Main game loop
    """
    load_screen = LoadAnimation()
    background = Background(Blocks.get_blocks().values())
    Game.set_game_mode("main_menu")

    while True:
        Game.CLOCK.tick(Game.FPS)

        # EVENT HANDLING -------------------- #
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == K_F11:
                    Game.toggle_fullscreen()
                elif event.key == K_ESCAPE:
                    pygame.quit()
                    exit()

        # CLEAR FRAME ----------------------- #
        Game.WIN.fill(Game.COLORS.BACKGROUND)

        # PICK STATE AND DRAW --------------- #
        if Game.MODE == "loading":
            load_screen.draw()

        elif Game.MODE == "main_menu":
            background.draw()

        elif Game.MODE == "settings":
            pass

        elif Game.MODE == "singeplayer":
            pass

        elif Game.MODE == "pause":
            Game.WIN.fill(Game.COLORS.WHITE)

        # UPDATE SCREEN --------------------- #
        pygame.display.update()


if __name__ == "__main__":
    """
    Entry of program
    """
    # SETUP ------------------------------------- #
    pygame.display.init()
    pygame.display.set_caption("VStris!")
    WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    Blocks.init()

    # START GAME -------------------------------- #
    Game.start(WIN)
    run()
    
    