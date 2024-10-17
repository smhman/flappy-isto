import math
import pygame

# Initialize Pygame
pygame.init()
pygame.mixer.init()

from bird import *
from pipe import *
from game import screen

from resources import *

# You can set constants in the constants.py file!

# Change the window text
pygame.display.set_caption("FlappyTux 2024")
try:
    pygame.display.set_icon(bird_img)
except NameError:
    pass

# Clock
clock = pygame.time.Clock()

bird = Bird()
pipes = []


def main():
    """
    Main function to run the FlappyTux game.

    This function handles the main game loop, including event handling,
    updating the game state, rendering the game objects, detecting collisions,
    and managing the game's main logic such as generating new pipes and keeping track of score.
    """

    # Initialize variables for scores and timers
    score = 0
    best_score = 0
    first_pipe_timer = 0
    dead_timer = 0
    running = True

    # Start the game at the main menu
    game_state = "main_menu"

    # Initialize fonts
    font_large = pygame.font.Font('gamecamper.ttf', 69)
    font = pygame.font.Font('gamecamper.ttf', 20)
    while running:

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Start the game if a mouse button is clicked.
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_state == "dead":
                    # A little delay to avoid accidentally starting a new game.
                    if dead_timer > 50:
                        # Reset variables to the beginning state.
                        score = 0
                        first_pipe_timer = 0
                        dead_timer = 0
                        pipes.clear()
                        bird.y = SCREEN_HEIGHT // 2
                        game_state = "main_menu"
                else:
                    game_state = "in_game"
                    bird.flap()
                    flap_sound.play()

            #  if spacebar is clicked.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if game_state == "dead":
                        # A little delay to avoid accidentally starting a new game.
                        if dead_timer > 50:
                            # Reset variables to the beginning state.
                            score = 0
                            first_pipe_timer = 0
                            dead_timer = 0
                            pipes.clear()
                            bird.y = SCREEN_HEIGHT // 2
                            game_state = "main_menu"
                    else:
                        game_state = "in_game"
                        bird.flap()
                        flap_sound.play()

                # Quit the game if Esc is clicked.
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        if game_state == "main_menu":
            # Draw the initial start image and the bird.
            screen.blit(background_img, (0, 0))
            screen.blit(logo_img, ((SCREEN_WIDTH - logo_img.get_width()) / 2, SCREEN_HEIGHT // 6))
            screen.blit(instructions_img, ((SCREEN_WIDTH - instructions_img.get_width()) / 2, SCREEN_HEIGHT - 400))
            bird.draw()
            try:
                screen.blit(bird_img, ((SCREEN_WIDTH - bird_img.get_width()) // 2, SCREEN_HEIGHT // 2 - 50))
            except NameError:
                # If the bird image has not been defined yet, don't render it.
                pass

            # Update the display to show the newly drawn changes.
            pygame.display.update()
            clock.tick(60)

        if game_state == "in_game":
            # Draw the background image
            screen.blit(background_img, (0, 0))

            # Bird update and draw
            bird.update()
            bird.draw()
            if bird.check_collision_with_floor():
                game_state = "dead"
                # TODO: Play a sound!
                # Play the hurt sound here.

            # Pipe update and draw
            for pipe in pipes.copy():
                pipe.update()
                pipe.draw()

                # TODO: Detect if bird is currently between pipes.
                # If yes, add +1 to the score.
                # Don't forget to update the pipe's has_been_passed value to True!
                # You can try to play a point sound here as well.
                if not pipe.has_been_passed and bird.x > pipe.x + 25:
                    pipe.has_been_passed = True
                    score += 1
                # TODO: Play a sound!
                # Play the point sound here.
                    point_sound.play()
                # Removes the pipe when it's off screen
                if pipe.off_screen():
                    pipes.remove(pipe)

            # Give the player time to adjust to the controls.
            first_pipe_timer += clock.get_rawtime()
            if first_pipe_timer > TIME_BEFORE_FIRST_PIPE:
                if len(pipes) == 0:
                    pipes.append(Pipe())

                # TODO: Generate new pipes
                if pipes[-1].x < DISTANCE_BETWEEN_PIPES:
                    pipes.append(Pipe())

            # Collision detection
            for pipe in pipes:

                # If bird is horizontally between the gap
                if bird.x + 50 > pipe.x and bird.x < pipe.x + 50:

                    # Please don't touch this...
                    if bird.y < pipe.y + 290 or bird.y + 70 > pipe.y + PIPE_GAP:
                        game_state = "dead"
                        # TODO: Play a sound!
                        # Play the hurt sound here.
                        hurt_sound.play()

            # Display the live score counter
            score_text = font_large.render(str(math.floor(score)), True, (255, 255, 255))
            screen.blit(score_text,
                        ((SCREEN_WIDTH - score_text.get_width()) / 2,
                         ((SCREEN_HEIGHT / 4) - score_text.get_height())))

            # Update the display to show the newly drawn changes.
            pygame.display.update()
            clock.tick(60)

        if game_state == "dead":
            dead_timer += 1

            # Save best score
            if score >= best_score:
                best_score = score

            # Display the endscreen, including score and best score
            screen.blit(score_img, (0, 0))

            score_text = font.render(f"Score: {score}", True, (0, 0, 0))
            best_score_text = font.render(f"Best: {best_score}", True, (0, 0, 0))
            play_again_text = font.render("Press SPACE to restart", True, (0, 0, 0))

            # Hard-coded coordinates below.
            # Feel free to experiment with them!
            screen.blit(score_text,
                        ((SCREEN_WIDTH - score_text.get_width()) / 2,
                         ((SCREEN_HEIGHT / 2) - score_text.get_height() - 60)))
            screen.blit(best_score_text,
                        ((SCREEN_WIDTH - best_score_text.get_width()) / 2,
                         ((SCREEN_HEIGHT / 2) - best_score_text.get_height() - 10)))
            screen.blit(play_again_text,
                        ((SCREEN_WIDTH - play_again_text.get_width()) / 2,
                         ((SCREEN_HEIGHT / 2) - play_again_text.get_height() + 95)))

            # Update the display to show the newly drawn changes.
            pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
