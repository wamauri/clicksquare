import pygame
import random


class Squares:

    def __init__(self, screen):
        self.screen = screen
        self.width = 20
        self.height = 20
        self.x = random.randint(0, screen_width - self.width)
        self.y = random.randint(0, screen_height - self.height)
        self.area = pygame.Rect(self.x, self.y, self.width, self.height)
        # self.color = (random.randint(20, 255), random.randint(20, 255), random.randint(20, 255))
        self.color = (random.randint(255, 255), random.randint(0, 0), random.randint(0, 0))

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.area)


# screen_width = 800
# screen_height = 600
screen_width = 1200
screen_height = 700
initial_squares = 500
black = (0, 0, 0)
white = (255, 255, 255)
initial_time = 10

pygame.init()
pygame.display.set_caption("Click Square")
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()


finished = False
while not finished:
    # Check mouse events here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    lists = []
    for i in range(0, initial_squares):
        s = Squares(screen)
        s.draw(screen)
        lists.append(s)

    # Updates the drawing on the screen
    pygame.display.update()
    # Screen color
    screen.fill((51, 51, 51))
    # Sets 50 screen update per second
    clock.tick(10)

# End the game window
pygame.display.quit()
# End the pygame
pygame.quit()
