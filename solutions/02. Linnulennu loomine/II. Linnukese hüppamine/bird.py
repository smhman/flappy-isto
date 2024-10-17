def flap(self):
    """
    Make the bird flap, adjusting its vertical velocity upward.
    
    When this function is activated, the bird's velocity should be set to
    the value of the BIRD_JUMP constant.

    However, you should know that PyGame counts coordinates increasing from top to bottom.
    Therefore, to make the bird fly upwards, the resulting velocity should be negative.
    """
    self.velocity = -BIRD_JUMP
