def draw(self):
    """
    Draw the bird on the game screen.
    
    Can you figure out the correct PyGame function to use in order to render the bird?
    Hint: use a sub-function of screen!
    You will need to use the image, x-coordinate and y-coordinate of the bird.
    """
    screen.blit(bird_img, (self.x, self.y))