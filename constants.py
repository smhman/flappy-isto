"""This file holds all constants for the Flappy Bird game."""

SCREEN_WIDTH = 600              # Width and height measured in pixels.
SCREEN_HEIGHT = 900             # Changing these two might break things. Approach with caution!

# TODO: A gravity modifier needs to be defined.
# Bigger number -> Higher gravity. 
# A value of 1.2 should work well!

# TODO: You should define how high your bird will be able to jump, measured in pixels.
# Bigger number -> Higher jumps.
# According to our testing, a jump height of 15 works great!

PIPE_GAP = 500                  # Bigger number -> Bigger gap (default = 500, no gap = 400)
PIPE_VELOCITY = 5               # Bigger number -> Faster moving pipes (default = 5)
DISTANCE_BETWEEN_PIPES = 300    # Bigger number -> More pipes (default = 300)
TIME_BEFORE_FIRST_PIPE = 750    # Bigger number -> More time to wait (default = 750)
GRAVITY = 1.2
BIRD_JUMP = 15

