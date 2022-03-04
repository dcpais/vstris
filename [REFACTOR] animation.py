from game import Game
from typing import Optional, List, Tuple

class Animation:
    """
    An abstract class for any surface/image that needs
    to be animated. Will hold the current animation tick
    aswell as current animated state the surface/image
    should be in.
    """

    def __init__(self, fps: int):
        """
        Initialize an animated object
        
        :param: fps -> fps of the animation
        :value: tick_delta -> number of ticks before
                        the update function is called
        :value: current_tick -> current_tick of animation
        ## 1 tick = 1 frame
        """
        self.fps = fps
        self.tick_delta = Game.FPS // fps
        # If requested animation fps is greater than game's,
        # Set tick delta to be same rate as game's
        if self.tick_delta == 0: 
            self.tick_delta = 1
        self.ticks = 0

    def tick(self):
        """
        Ticks the animation along. Will update the 
        current frame of animation if needed. Should
        generally be called after every draw.
        
        #THIS METHOD CAN BE OVERWRITTEN BY INHERITOR
        #TO CREATE SPECIALIZED INTERACTIONS
        """
        self.ticks += 1
        if self.ticks % self.tick_delta == 0:
            self.update()
        

    def update(self):
        """
        Abstract method that must be implemented by the
        animation itself. Is used after every tick to 
        update the state of the animation
        """
        raise NotImplementedError
    