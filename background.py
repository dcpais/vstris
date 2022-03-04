import effects
from game import Game
from blocks import Blocks

from typing import List
import pygame
import random
import os

class Background:
    """
    Background animation. All assets for background animation
    are contained within this class as to not pollute main 
    file's namespace with counter variables.

    Additionally, a state class is added to be indicative
    of the frames current state, as there are multiple
    moving parts to this animation
    """

    def __init__(self):
        """
        Initialize backdrop
        """
        # MOVING BACKGROUND ------------------------ #
        _ = pygame.image.load(os.path.join("assets", "Backdrop", "Backdrop.png")).convert()
        self.background = effects.blur_surface(_, 3)
        self.background_pos = (0, -1 * self.background.get_size()[1] // 31)

        # MOVING BLOCKS ---------------------------- #
        self.block_list = []
        for block in Blocks.get_blocks().values():
            x = (block.get_size()[0] // 30) * Game.SCALE
            y = (block.get_size()[1] // 30) * Game.SCALE
            self.block_list.append(pygame.transform.scale(block, (30 * x, 30 * y)))
        self.block_states = []
        self.ticks = 0

    def update_blocks(self):
        """
        Update all moving block positions and possibly
        do some of the following:
           -> Add a new block to the falling block list
           -> Possibly randomly rotate a block
           -> Move a block left/right randomly
           -> Move all blocks down one cell
        """
        new_states = []
        cell_size = 30
        for block, pos, cd in self.block_states:
            dy = pos[1] + 2
            dx = pos[0]
            new_cd = cd

            if dy > Game.HEIGHT:
                continue
            if cd == 0:
                if self.ticks % (Game.FPS // 10) == 0 and random.random() < 0.3:
                    block = pygame.transform.rotate(block, random.choice([90, -90]))
                    new_cd = Game.FPS * 2
            
            if new_cd > 0:
                new_cd -= 1
                
            new_pos = (dx, dy)
            new_states.append((block, new_pos, new_cd))
        self.block_states = new_states

    def update_background(self):    
        """
        Update the background image's position by moving
        it down 1 pixel. Once it reaches the bottom of a
        row, it can reset and continue.
        """
        dy = self.background_pos[1] + (36 / (Game.FPS * 1))
        if dy > 0: 
            dy = -1 * self.background.get_size()[1] // 31 # Reset position if it reaches bottom
        self.background_pos = (self.background_pos[0], dy)

    def draw(self):
        """
        Draw background and moving blocks
        """
        if self.ticks % (Game.FPS // 5) == 0 and random.random() < 0.3:
            new_block = random.choice(self.block_list)
            x = random.randrange(0, Game.WIDTH - new_block.get_size()[0], 30)
            y = -1 * new_block.get_size()[1]
            self.block_states.append((new_block, (x, y), 0))

        Game.WIN.blit(self.background, self.background_pos)
        for block, pos, _ in self.block_states:
            Game.WIN.blit(block, pos)

        self.update_background()
        self.update_blocks()
        self.ticks += 1