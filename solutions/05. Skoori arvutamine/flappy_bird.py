# TODO: Detect if bird is currently between pipes.
# If yes, add +1 to the score.
# Don't forget to update the pipe's has_been_passed value to True!
# You can try to play a point sound here as well.
if pipe.has_been_passed == False and bird.x > pipe.x + 25:
    pipe.has_been_passed = True
    score += 1


# BETTER STYLE FOR THE SAME CODE:
if not pipe.has_been_passed and bird.x > pipe.x + 25:
    pipe.has_been_passed = True
    score += 1