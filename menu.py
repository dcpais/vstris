from game import Game

import pygame

class MainMenu:

    def __init__(self):
        """
        Initialize main menu
        """
        self.title = Game.FONT.render("VStris", True, Game.COLORS.WHITE)
        self.title_pos = (Game.WIDTH // 2, Game.HEIGHT // 6)       
        self.buttons = []

    def check_buttons(self, mx: int, my: int, click: bool):
        """
        Check if a button has been pressed
        """
        pass

    def draw(self):
        """
        Draw main menu
        """
        Game.center_blit(self.title, self.title_pos)


class Button(pygame.Rect):
    """
    Constructs a button for the main menu, 
    that when pressed will change the state of
    the window. Child of a pygame Rect
    """

    def __init__(self, x: int, y: int, width: int, height: int):
        """
        Initialize button
        """
        super().__init__(x, y, width, height)
        self.hovered = False
        self.pressed = False



    def draw(self):
        """
        Draw the button
        """
        if self.pressed:
            pygame.draw.rect(Game.WIN, Game.COLORS.BLACK, self)
        elif self.hovered:
            pygame.draw.rect(Game.WIN, Game.COLORS.FOREGROUND, self)
        else:
            pygame.draw.rect(Game.WIN, Game.COLORS.BLACK, self)

    def on_click(self):
        pass