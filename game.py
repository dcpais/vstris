import pygame
from typing import Tuple

class Game:
    """
    Static class to be used as a way for other packages 
    to access window and game clock. Allows other
    files to access metrics such as fps and resolution 
    from one access point.

    ### SHOULD NOT BE INSTANTIATED, ACTS SOMEWHAT LIKE
    ### A SINGLETON OBJECT. TO INITALIZE, USE 
    ### Metrics.start()
    """

    WINDOW = None
    RESOLUTION = None
    WIDTH = None
    HEIGHT = None
    CLOCK = None
    FPS = None
    SCALE = None
    IS_FULLSCREEN = None
    MODE = None

    class COLORS:
        """
        Container class for Colors (american spelling used to save chars)
        """
        WHITE = (255, 255, 255) 
        BLACK = (0, 0, 0)
        FOREGROUND = (85, 81, 81)
        BACKGROUND = (30, 25, 25) 

    @staticmethod
    def start(window: pygame.Surface):
        """
        Initialize all parts of the game module
        """
        Game.WIN = window
        Game.RESOLUTION = window.get_size()
        Game.WIDTH, Game.HEIGHT = Game.RESOLUTION
        Game.CLOCK = pygame.time.Clock()
        Game.FPS = 144
        Game.SCALE = 1
        Game.IS_FULLSCREEN = True
        Game.MODE = "loading"       

    @staticmethod
    def set_fps(fps: int):
        """
        Set the FPS of the game
        """
        Game.FPS = fps

    @staticmethod
    def toggle_fullscreen():
        """
        Toggles fullscreen mode
        """
        Game.IS_FULLSCREEN = not Game.IS_FULLSCREEN
        if Game.IS_FULLSCREEN: 
            Game.WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else: 
            Game.WIN = pygame.display.set_mode((1920, 1000))
        Game.RESOLUTION = Game.WIN.get_size()
        Game.WIDTH, Game.HEIGHT = Game.RESOLUTION

    @staticmethod
    def center_blit(surface: pygame.Surface, coordinate: Tuple[int, int]):
        """
        Blit a surface centered on the supplied coordinate
        """
        size = surface.get_size()
        Game.WIN.blit(surface, (coordinate[0] - size[0] // 2, coordinate[1] - size[1] // 2))

    @staticmethod
    def set_game_mode(mode: str):
        """
        Sets the current mode of the game. 
        #! This universally accessible setter 
        #! method could be problematic for
        #! the security of the game later on. 
        """
        Game.MODE = mode

    @staticmethod
    def get_centre_screen():
        return (Game.WIDTH // 2, Game.HEIGHT // 2)