"""This file holds all images and sounds for the Flappy Bird game."""
from constants import *
import pygame

# Load images
# Here's some examples how images can be loaded using PyGame.
background_img = pygame.image.load("images/Istoprocent.png")
pipe_img = pygame.image.load("images/pipe_real.png")
score_img = pygame.image.load("images/score.png")
logo_img = pygame.image.load("images/logo.png")
instructions_img = pygame.image.load("images/instructions.png")
bird_img = pygame.image.load("images/isto_real.png")

# Now's your turn! Load the image for the bird (bird_img).



# Load sound effects
# Here's an example how sounds can be loaded using PyGame.
flap_sound = pygame.mixer.Sound("sounds/flap.wav")
point_sound = pygame.mixer.Sound("sounds/point.wav")
hurt_sound = pygame.mixer.Sound("sounds/metalpipe.wav")

# But our game needs more sounds! Add sound effects for:
# the bird colliding with the pipe (hurt_sound), and
# a score increase (point_sound).

# Scale images
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
try:
    bird_img = pygame.transform.scale(bird_img, (80, 80))
except NameError:
    pass
pipe_img = pygame.transform.scale(pipe_img, (80, 800))
score_img = pygame.transform.scale(score_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
