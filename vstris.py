import pygame
import os
from typing import List, Tuple

class Animated:
    """
    Wrapper class to hold animated elements of 
    tetris game.
    """
    def __init__(self, frames: List[pygame.Surface], speed: float):
        self.frames = frames
        self.current_frame = 0
        self.is_running = False
        self.speed
        
    

class Tetris:
    """
    Container class for tetris game logic and
    gui rendering, hosting the main surface window 
    pygame creates
    """
    
    # General use variables
    WIDTH, HEIGHT = 0, 0
    FPS = 60

    #Colors
    WHITE = (255, 255, 255) 
    LIGHT_GRAY = (85, 81, 81)
    BACKGROUND = (30, 25, 25)

    def __init__(self, window: pygame.Surface, dimensions: Tuple[int, int]):
        self.win = window
        self.running = True
        self.mode = "main_menu"
        Tetris.WIDTH = dimensions[0]
        Tetris.HEIGHT = dimensions[1]
        
        # title and main menu
        #self.backdrop_img = pygame.image.load(os.path.join("assets", "Backdrop", "Backdrop.jpg")).convert()
        #self.backdrop = pygame.transform.scale(self.backdrop_img, (732, 600))

        self.title_img = pygame.image.load(os.path.join("assets", "Title", "Title.png")).convert()
        self.title = pygame.transform.scale(self.title_img, (60, 20))
        self.title_fc = 0
        self.title_is_animating = True
        self.title_pos = (366, 50)

        # tetris blocks
        

        # sounds
        self.sound_track = None


        # board and additional game cards
        #self.board_img = pygame.image.load(os.path.join("assets", "Board", "Board.png")).convert()
        #self.board = pygame.transform.scale(self.board_img, (432, 792))


    def change_soundtrack(self, song_number: int):
        """
        Change the song that is played by pygame's 
        music mixer in the background.
        """
        pygame.mixer.music.stop()
        self.sound_track = pygame.mixer.music.load(os.path.join("assets", "Music", f"0{song_number}.mp3"))
        pygame.mixer.music.play(10)


    def animate_title(self):
        """
        Animates title by progressively making it larger.
        This works by slowly increasing its scale.
        """
        if self.title_fc >= 120:
            # Once title has gone 1000 frames, it will stop its animation
            self.title_is_animating = False
            self.title_fc = 0
            return
        
        scale = 1 + (self.title_fc / 24) # current scale at which title should be displayed
        self.title = pygame.transform.scale(self.title_img, (59 * scale, 20 * scale))
        x, y = self.title.get_size()
        self.title_pos = (366 - (x / 2), 50)
        self.title_fc += 1


    def draw_backdrop(self):
        self.win.blit(self.backdrop, (0, 0))


    def draw_title(self):
        self.win.blit(self.title, self.title_pos)
        


    def run(self):
        """
        Main game loop. 
        
        All game logic is processed here, and all drawing is done
        at the end of each frame
        """
        #self.change_soundtrack(4)
        clock = pygame.time.Clock()

        while self.running:
            clock.tick(Tetris.FPS)
            
            # Handle every frame event
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            # Empty frame so it can be redrawn
            self.win.fill(Tetris.BACKGROUND)
            
            if self.mode == "main_menu":
                if self.title_is_animating:
                    self.animate_title()
                
                
                #self.draw_backdrop()
                self.draw_title()


            # Update Screen ---------------------
            pygame.display.update()


if __name__ == "__main__":
    """
    Entry of program
    """
    # Initialize pygame modules -----------------
    pygame.display.init()
    pygame.mixer.init()
    pygame.display.set_caption("Tetris!")
    win = pygame.display.set_mode((1000, 800))

    # Start game --------------------------------
    Tetris(win, win.get_size()).run() 

    # Exit everything ---------------------------
    pygame.quit()
    exit()