from turtle import back
import animated
import effects

import pygame
import random
import os
from typing import Dict, Tuple, List

class Background(animated.Animated):
    """
    Background animation. All assets for background animation
    are contained within this class as to not pollute main 
    file's namespace with counter variables.

    Additionally, a state class is added to be indicative
    of the frames current state, as there are multiple
    moving parts to this animation
    """

    # STATE CLASS --------------------------------- #
    class State:
        """
        State container class for animation state
        The current state of the animation is described by
        the bg and block state variables

        :param: bg_state -> Tuple pair with image and current
                            image position
        :var: block_states -> A list of pairs containing
                            the block images and their current 
                            position.
        """

        def __init__(self, background: pygame.Surface, res: Tuple[int, int]):
            """
            Initialize background animation state
            """
            self.res = res
            self.bg_state = [background, (0, 0)]
            self.block_states = []
            self.angles = [90, -90, 180, -180]

        def update_block_states(self):
            """
            Update each blocks position by modifiying its
            current state. This will move each block down
            by 1 pixel.
            """
            new_states = []
            for block, pos in self.block_states:
                dy = pos[1] + (self.res[1] // 31)
                if dy > self.res[1]:
                    continue
                if random.random() < 0.3:
                    block = pygame.transform.rotate(block, random.choice(self.angles))
                new_pos = (pos[0], dy)
                new_states.append((block, new_pos)) # COULD BE FASTER?
            self.block_states = new_states

        def update_background_state(self):
            """
            Update the background image's position by moving
            it down 1 pixel. Once it reaches the bottom of a
            row, it can reset and continue.
            """
            dy = self.bg_state[1][1] + 0.2
            if dy > 0: dy =  -1 * self.bg_state[0].get_size()[1] // 31 # Reset position if it reaches bottom
            self.bg_state[1] = (self.bg_state[1][0], dy)

        def add_block(self, block: pygame.Surface):
            """
            Add a random falling block to bg animation. Random
            blocks are added as such: 
            - Random colour block is chosen
            - it will have a randomly chosen column to fall from
            - Random falling blocks should fall every 'x' seconds
                (this is decided by background.new_block_tick
            """
            new_block = [block, (random.randint(0, self.res[0] - block.get_size()[0]), 
                         -1 * block.get_size()[1])]
            self.block_states.append(new_block)

        def get_block_states(self):
            return self.block_states

        def get_bg_state(self):
            return self.bg_state


    # BACKGROUND CLASS ---------------------------- #
    def __init__(self, window: pygame.Surface, fps: int, blurred_blocks: Dict):
        """
        Initialize Background animation class.
        """
        Background.WIN = window
        Background.FPS = fps
        Background.NEW_BLOCK_TICK = fps * 3

        _ = pygame.image.load(os.path.join("assets", "Backdrop", "Backdrop.png")).convert()
        backdrop = effects.blur_surface(3, _)
        self.blocks = list(blurred_blocks.values())
        self.new_block_counter = 0
        super().__init__(Background.State(backdrop, window.get_size()), 1, self.update_state)

    def update_state(self):
        """
        Update the current background animation state by:
        - moving the background down,
        - moving all blocks down,
        - spawning new blocks every 'x' seconds
        """
        self.state.update_background_state()
        self.state.update_block_states()
        if self.new_block_counter > Background.NEW_BLOCK_TICK:
            self.state.add_block(random.choice(self.blocks))
            Background.NEW_BLOCK_TICK = random.randint(Background.FPS, Background.FPS * 2)
            self.new_block_counter = 0
        else:
            self.new_block_counter += 1
        return self.state

    
    def draw(self):
        """
        Draw all moving parts of background
        """
        bg_state = self.state.get_bg_state()
        Background.WIN.blit(bg_state[0], bg_state[1])
        for block, pos in self.state.get_block_states():
            Background.WIN.blit(self.state.bg_state[0].blit(block, pos)
        self.tick()
