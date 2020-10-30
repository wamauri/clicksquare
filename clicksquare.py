import pygame


pygame.init()
screen_width, screen_height = 800, 600
pygame.display.set_caption("Click Square")
screen = pygame.display.set_mode((screen_width, screen_height))


finished = False
while not finished:
    # Updates the drawing on the screen
    pygame.display.update()

    # Check mouse events here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    # Screen color
    screen.fill((51, 51, 51))

# End the game window
pygame.display.quit()
# End the pygame
pygame.quit()
