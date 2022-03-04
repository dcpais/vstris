import pygame
import os
import effects
from typing import Dict, Tuple

class Blocks:
    """ 
    Static class used as a holder for all block surfaces and 
    """

    # BLOCK IMAGES ------------------------------- #
    BLOCK_1 = None
    BLOCK_2 = None
    BLOCK_3 = None
    BLOCK_4 = None
    BLOCK_5 = None
    BLOCK_6 = None
    BLOCK_7 = None
    
    # BLOCK LISTS --------------------------------- #
    BLOCKS = None
    BLOCK_OUTLINES = None

    @staticmethod
    def init():
        """
        Load all block images
        """
        Blocks.BLOCK_1 = pygame.image.load(os.path.join("assets", "Tetriminos", "Purple.png")).convert_alpha()
        Blocks.BLOCK_2 = pygame.image.load(os.path.join("assets", "Tetriminos", "yellow.png")).convert_alpha()
        Blocks.BLOCK_3 = pygame.image.load(os.path.join("assets", "Tetriminos", "red.png")).convert_alpha()
        Blocks.BLOCK_4 = pygame.image.load(os.path.join("assets", "Tetriminos", "green.png")).convert_alpha()
        Blocks.BLOCK_5 = pygame.image.load(os.path.join("assets", "Tetriminos", "orange.png")).convert_alpha()
        Blocks.BLOCK_6 = pygame.image.load(os.path.join("assets", "Tetriminos", "dark_blue.png")).convert_alpha()
        Blocks.BLOCK_7 = pygame.image.load(os.path.join("assets", "Tetriminos", "blue.png")).convert_alpha()

        Blocks.BLOCKS = {
        "purple" : Blocks.BLOCK_1,
        "yellow" : Blocks.BLOCK_2,
        "red" : Blocks.BLOCK_3,
        "green" : Blocks.BLOCK_4,
        "orange" : Blocks.BLOCK_5,
        "dark_blue" : Blocks.BLOCK_6,
        "blue" : Blocks.BLOCK_7
        }

        Blocks.BLOCK_OUTLINES = {
        "purple" : [[0, 1, 0], [1, 1, 1]],
        "yellow" : [[1, 1], [1, 1]],
        "red" : [[1, 1, 0], [0, 1, 1]],
        "green" : [[0, 1, 1], [1, 1, 0]],
        "orange" : [[0, 0, 1], [1, 1, 1]],
        "dark_blue" : [[1, 0, 0], [1, 1, 1]],
        "blue" : [[1, 1, 1, 1]]
        }

        

    @staticmethod
    def get_block(block_id: str) -> pygame.Surface:
        """
        Get a block surface by its ID
        """
        return Blocks.BLOCKS.get(block_id)

    @staticmethod
    def get_blocks() -> Dict:
        """
        Get the dict of all block surfaces
        """
        return Blocks.BLOCKS

    @staticmethod
    def get_block_outline(block_id: str) -> pygame.Surface:
        """
        Get the 2D array outline mapping of a block given
        its ID
        """
        return Blocks.BLOCK_OUTLINES.get(block_id)

    @staticmethod
    def get_all_outlines() -> Dict:
        """
        Get the dict of all block outline mappings
        """
        return Blocks.BLOCK_OUTLINES

    @staticmethod
    def get_blurred_blocks() -> Dict:
        """
        Get the dict of all blurred block images 
        (specifically for background.py)
        """
        ret = dict()
        for key, val in Blocks.BLOCKS.items():
            ret[key] = effects.blur_surface(val, 1)
        return ret