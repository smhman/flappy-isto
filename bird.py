"""This file holds everything responsible for representing the bird."""
from constants import *
from resources import *
from game import screen


class Bird:
    """
    Class representing the bird in the Flappy Tux game.

    :param x (int): The x-coordinate of the bird's position.
    :param y (int): The y-coordinate of the bird's position.
    :param velocity (float): The vertical velocity of the bird.
    """

    def __init__(self):
        """
        Initialize the Bird object with default position and velocity.

        The bird's x-coordinate should be set to 150.
        The bird's y-coordinate should be set to the center of the screen vertically.
        The bird's initial velocity should be set to zero. 
        """
        self.x = 150
        self.y = SCREEN_HEIGHT / 2
        self.velocity = 0

    def flap(self):
        """
        Make the bird flap, adjusting its vertical velocity upward.
        
        When this function is activated, the bird's velocity should be set to
        the value of the BIRD_JUMP constant.

        However, you should know that PyGame counts coordinates increasing from top to bottom.
        Therefore, to make the bird fly upwards, the resulting velocity should be negative.
        """
        self.velocity = -BIRD_JUMP

    def update(self):
        """
        Update the bird's position based on gravity and velocity.

        This function will be activated once every frame.

        The bird's velocity should be increased by the value of the GRAVITY constant.
        The bird's y-coordinate should be increased by the amount of the bird's current velocity.

        Remember that PyGame counts coordinates increasing from top to bottom.
        Thus, an increase in coordinates will result in the bird moving down on the screen.
        """
        self.velocity += GRAVITY
        self.y += self.velocity

    def draw(self):
        """
        Draw the bird on the game screen.
        
        Can you figure out the correct PyGame function to use in order to render the bird?
        Hint: use a sub-function of screen!
        You will need to use the image, x-coordinate and y-coordinate of the bird.
        """
        screen.blit(bird_img, (self.x, self.y))

    def check_collision_with_floor(self):
        """
        Check if the bird has fallen off the level.

        This function can be completed using a simple if-check.

        Remember that PyGame counts coordinates increasing from top to bottom.
        Thus, an increase in coordinates will result in the bird moving down on the screen.

        Our testing shows that the bird has fallen out of the level if its y-coordinate is
        greater than the screen's height, minus the height of the bird image.

        :returns bool: Whether the bird is colliding with the floor
        """
        if self.y > SCREEN_HEIGHT - 50:
            return True
        else:
            return False

