from transitions import LoadAnimation
from background import Background
from blocks import Blocks
from game import Game
from menu import MainMenu
from sounds import Sounds

import pygame
from pygame.locals import *
  
def run():
    """
    Main game loop
    """
    load_screen = LoadAnimation()
    background = Background()
    main_menu = MainMenu()
    Sounds.MUSIC.play()
    Game.set_game_mode("loading")

    while True:

        Game.CLOCK.tick(Game.FPS)
        mx, my = pygame.mouse.get_pos()
        click = False

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
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # CLEAR FRAME ----------------------- #
        Game.WIN.fill(Game.COLORS.BACKGROUND)

        # PICK STATE AND DRAW --------------- #
        if Game.MODE == "loading":
            load_screen.draw()

        elif Game.MODE == "main_menu":
            background.draw()
            main_menu.check_buttons(mx, my, click)
            main_menu.draw()

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
    pygame.font.init()
    pygame.mixer.init()
    Blocks.init()
    Sounds.init()

    # START GAME -------------------------------- #
    Game.start(WIN)
    run()
    
    