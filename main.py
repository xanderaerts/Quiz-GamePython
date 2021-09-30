import pygame

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My First Game")

carrOn = True
clock = pygame.time.Clock()

while carrOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carrOn = False

    screen.fill(WHITE)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()