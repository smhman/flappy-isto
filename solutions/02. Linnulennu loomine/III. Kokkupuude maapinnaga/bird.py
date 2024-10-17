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
