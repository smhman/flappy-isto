
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
pygame.display.set_caption("Flappy Isto")
try:
    pygame.display.set_icon(bird_img)
except NameError:
    pass

# Clock
clock = pygame.time.Clock()

bird = Bird()
pipes = []

def load_highscore():
    try:
        with open('highscore.txt', 'r') as f:
            return int(f.read())
    except FileNotFoundError:
        return 0

def save_highscore(score):
    global best_score
    with open('highscore.txt', 'w') as f:
        f.write(str(score))

best_score = load_highscore()

def main():
    """
    Main function to run the FlappyTux game.

    This function handles the main game loop, including event handling,
    updating the game state, rendering the game objects, detecting collisions,
    and managing the game's main logic such as generating new pipes and keeping track of score.
    """
    global best_score  # Lisame selle, et kasutada globaalset muutujat
    # Initialize variables for scores and timers
    score = 0
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
                    if dead_timer > 50:
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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if game_state == "dead":
                        if dead_timer > 50:
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

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        if game_state == "main_menu":
            screen.blit(background_img, (0, 0))
            screen.blit(logo_img, ((SCREEN_WIDTH - logo_img.get_width()) / 2, SCREEN_HEIGHT // 6))
            screen.blit(instructions_img, ((SCREEN_WIDTH - instructions_img.get_width()) / 2, SCREEN_HEIGHT - 400))
            bird.draw()
            try:
                screen.blit(bird_img, ((SCREEN_WIDTH - bird_img.get_width()) // 2, SCREEN_HEIGHT // 2 - 50))
            except NameError:
                pass

            pygame.display.update()
            clock.tick(60)

        if game_state == "in_game":
            screen.blit(background_img, (0, 0))
            bird.update()
            bird.draw()
            if bird.check_collision_with_floor():
                game_state = "dead"
                hurt_sound.play()

            for pipe in pipes.copy():
                pipe.update()
                pipe.draw()

                if not pipe.has_been_passed and bird.x > pipe.x + 25:
                    pipe.has_been_passed = True
                    score += 1
                    point_sound.play()

                if pipe.off_screen():
                    pipes.remove(pipe)

            first_pipe_timer += clock.get_rawtime()
            if first_pipe_timer > TIME_BEFORE_FIRST_PIPE:
                if len(pipes) == 0:
                    pipes.append(Pipe())

                if pipes[-1].x < DISTANCE_BETWEEN_PIPES:
                    pipes.append(Pipe())

            # Kontrollime kokkupõrkeid torudega
            for pipe in pipes:
                # Kontroll, kas lind on horisontaalselt toru piirkonnas
                if bird.x + bird_width > pipe.x and bird.x < pipe.x + pipe_width:
                # Ajutised kastid kokkupõrkeala kontrollimiseks
                    # Kontrollime, kas lind on väljaspool toruava (ülal või all)
                    if bird.y < pipe.y or bird.y + bird_height > pipe.y + PIPE_GAP:
                        # Kui lind on väljaspool avaust, loetakse kokkupõrge
                        game_state = "dead"
                        hurt_sound.play()  # Mängi surmaheli
            score_text = font_large.render(str(math.floor(score)), True, (255, 255, 255))
            screen.blit(score_text,
                        ((SCREEN_WIDTH - score_text.get_width()) / 2,
                         ((SCREEN_HEIGHT / 4) - score_text.get_height())))

            pygame.display.update()
            clock.tick(60)

        if game_state == "dead":
            dead_timer += 1
            save_highscore(best_score)

            if score >= best_score:
                best_score = score

            screen.blit(score_img, (0, 0))

            score_text = font.render(f"Score: {score}", True, (0, 0, 0))
            best_score_text = font.render(f"Best: {best_score}", True, (0, 0, 0))
            play_again_text = font.render("Press SPACE to restart", True, (0, 0, 0))

            screen.blit(score_text,
                        ((SCREEN_WIDTH - score_text.get_width()) / 2,
                         ((SCREEN_HEIGHT / 2) - score_text.get_height() - 60)))
            screen.blit(best_score_text,
                        ((SCREEN_WIDTH - best_score_text.get_width()) / 2,
                         ((SCREEN_HEIGHT / 2) - best_score_text.get_height() - 10)))
            screen.blit(play_again_text,
                        ((SCREEN_WIDTH - play_again_text.get_width()) / 2,
                         ((SCREEN_HEIGHT / 2) - play_again_text.get_height() + 95)))

            pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
