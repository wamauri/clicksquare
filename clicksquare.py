import pygame


pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

finished = False
while not finished:
    # Updates the drawing on the screen
    pygame.display.update()

    # Check mouse events here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

# End the game window
pygame.display.quit()
# End the pygame
pygame.quit()
