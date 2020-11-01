import pygame


pygame.init()

screen_width, screen_height = 800, 600
pygame.display.set_caption("Click Square")
screen = pygame.display.set_mode((screen_width, screen_height))

yellow = (255, 255, 0)
red = (255, 0, 0)


clock = pygame.time.Clock()
finished = False

while not finished:
    # Check mouse events here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    pygame.draw.rect(screen, yellow, (10, 10, 200, 100), 3)
    pygame.draw.rect(screen, red, (400, 300, 50, 50))

    # Updates the drawing on the screen
    pygame.display.update()
    # Screen color
    screen.fill((51, 51, 51))
    # Sets 50 screen update per second
    clock.tick(50)

# End the game window
pygame.display.quit()
# End the pygame
pygame.quit()
