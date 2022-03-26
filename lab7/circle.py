import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)

FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CIRCLE")

finished = False

x, y = WIDTH // 2, HEIGHT // 2
radius = 25
clock = pygame.time.Clock()

while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    keydowns = pygame.key.get_pressed()
    if keydowns[pygame.K_UP] and y - radius > 0:
        y += -20
    elif keydowns[pygame.K_DOWN] and y + radius < HEIGHT:
        y += 20
    elif keydowns[pygame.K_LEFT] and x - radius > 0:
        x += -20
    elif keydowns[pygame.K_RIGHT] and x + radius < WIDTH:
        x += 20
        
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), radius)
    
    pygame.display.flip()
pygame.quit()