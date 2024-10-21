
"""This file holds all constants for the Flappy Bird game."""

SCREEN_WIDTH = 600              # Width and height measured in pixels.
SCREEN_HEIGHT = 900             # Changing these two might break things. Approach with caution!

PIPE_GAP = 500                  # Bigger number -> Bigger gap (default = 500, no gap = 400)
PIPE_VELOCITY = 5               # Bigger number -> Faster moving pipes (default = 5)
DISTANCE_BETWEEN_PIPES = 300    # Bigger number -> More pipes (default = 300)
TIME_BEFORE_FIRST_PIPE = 400    # Bigger number -> More time to wait (default = 750)
GRAVITY = 0.8
BIRD_JUMP = 15

difficulty_settings = {
    'easy': {'pipe_speed': 5, 'gap_size': 550},
    'medium': {'pipe_speed': 7, 'gap_size': 525},
    'hard': {'pipe_speed': 9, 'gap_size': 500}
}

# Mängija valik raskustaseme määramiseks (näiteks keskmine)
difficulty = 'easy'

# Määrame toru kiiruse ja vahe sõltuvalt raskustasemest
PIPE_VELOCITY = difficulty_settings[difficulty]['pipe_speed']
PIPE_GAP = difficulty_settings[difficulty]['gap_size']
