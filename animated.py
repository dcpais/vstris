from typing import Optional, List
from functools import partial

class Animated:
    """
    A Container class for any surface/image that needs
    to be animated. Will hold the current animation tick
    aswell as current animated state the surface/image
    should be in
    """

    def __init__(self, 
                 start_state: any,
                 tick_delta: int,
                 update_func: Optional[callable] = None,
                 *func_args: List[any]):
        """
        Initialize an animated object
        
        Inputs:
        :param: start_state -> state OR actual sprite / surface
        :param: tick_delta -> time elapsed between each automatic
                            state change
        :param: update_func -> callable function that updates the state
        :param: func_args -> the callable func's optional args
        """
        self.state = start_state
        self.ticks = 0
        self.tick_delta = int(tick_delta)
        if func_args:
            self.updater = partial(update_func, *func_args)
        else:
            self.updater = partial(update_func)


    def tick(self, next_state: Optional[any] = None):
        """
        Ticks the animation along. If a next state is supplied, will
        also update the current state of the animation

        :param: next_state -> next state of the animation
        """
        if next_state is not None:
            self.state = next_state
        elif self.ticks % self.tick_delta == 0:
            self.state = self.updater()
        self.ticks += 1
    

    def get_state(self) -> any:
        """
        Returns state
        """
        return self.state


    