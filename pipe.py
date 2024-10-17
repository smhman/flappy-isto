"""This file holds everything responsible for representing a pipe."""
import random
from game import screen
from constants import *
from resources import *

class Pipe:
    """
    Class representing the pipes in the FlappyAgo game.

    :param x (int): The x-coordinate of the pipe's position.
    :param y (int): The y-coordinate of the top of the bottom pipe.
    """
    def __init__(self):
        """Initialize the Pipe object with default position."""
        self.x = SCREEN_WIDTH
        self.y = random.randint(-250, 250)
        self.has_been_passed = False

    def update(self):
        """Update the pipe's position."""
        self.x -= PIPE_VELOCITY

    def off_screen(self):
        """
        Check if the pipe is off the screen.

        :return bool: True if the pipe is off the left side of the screen, False otherwise.
        """
        return self.x < -100

    def draw(self):
        """Draw the pipe on the game screen."""
        screen.blit(pipe_img, (self.x, self.y - PIPE_GAP))
        screen.blit(pygame.transform.flip(pipe_img, False, True), (self.x, self.y + PIPE_GAP))
