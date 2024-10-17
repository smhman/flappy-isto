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
