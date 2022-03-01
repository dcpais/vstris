import pygame
import os
import effects
from typing import Dict, Tuple

class Blocks:
    """ 
    Static container class for block surfaces
    Acts as a static class, which
    """

    # BLOCK IMAGES ------------------------------- #
    BLOCK_1 = pygame.image.load(os.path.join("assets", "Tetriminos", "Purple.png")).convert_alpha()
    BLOCK_2 = pygame.image.load(os.path.join("assets", "Tetriminos", "yellow.png")).convert_alpha()
    BLOCK_3 = pygame.image.load(os.path.join("assets", "Tetriminos", "red.png")).convert_alpha()
    BLOCK_4 = pygame.image.load(os.path.join("assets", "Tetriminos", "green.png")).convert_alpha()
    BLOCK_5 = pygame.image.load(os.path.join("assets", "Tetriminos", "orange.png")).convert_alpha()
    BLOCK_6 = pygame.image.load(os.path.join("assets", "Tetriminos", "dark_blue.png")).convert_alpha()
    BLOCK_7 = pygame.image.load(os.path.join("assets", "Tetriminos", "blue.png")).convert_alpha()
    
    # BLOCK LIST --------------------------------- #
    BLOCKS = {
        "purple" : BLOCK_1,
        "yellow" : BLOCK_2,
        "red" : BLOCK_3,
        "green" : BLOCK_4,
        "orange" : BLOCK_5,
        "dark_blue" : BLOCK_6,
        "blue" : BLOCK_7
        }
        
    # BLOCK SIZES -------------------------------- #
    BLOCK_OUTLINES = {
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
        return Blocks.BLOCKS.get(block_id)

    @staticmethod
    def get_block_list() -> Dict[str: pygame.Surface]:
        return Blocks.BLOCKS

    @staticmethod
    def get_block_outlines(block_id: str) -> pygame.Surface:
        return Blocks.BLOCK_OUTLINES.get(block_id)

    @staticmethod
    def get_all_outlines() -> Dict[str: pygame.Surface]:
        return Blocks.BLOCK_OUTLINES

    @staticmethod
    def get_blurred_blocks() -> Dict[str: pygame.Surface]:
        ret = dict()
        for key, val in Blocks.BLOCKS:
            ret[key] = effects.blur_surface(3, val)
        return ret