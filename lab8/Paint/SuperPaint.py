import pygame
from random import randint
pygame.init()

WIDTH = 800
HEIGHT = 600
FPS = 60
RAD = 15

rectangle = pygame.image.load("./img/rect.png")
circle = pygame.image.load("./img/circ.png")
eras = pygame.image.load("./img/eraser.png")
brush = pygame.image.load("./img/brush.png")
clrs = pygame.image.load("./img/clrscr.png")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SuperPaint")

clock = pygame.time.Clock()

finished = False

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


drawing = False
color = BLACK

screen.fill(WHITE)

start_pos = 0
end_pos = 0

mode = 0

COLORS = []

for _ in range(17):
    COLORS.append((randint(0,255), randint(0,255), randint(0,255)))



while not finished:
    clock.tick(FPS)
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = pos
            if pos[0] > 765 and pos[0] < 800 and pos[1] > 0 and pos[1] < HEIGHT:
                color = screen.get_at(pos)
            if pos[0] > 0 and pos[0] < 35 and pos[1] > 0 and pos[1] < 35:
                mode = 1
            if pos[0] > 0 and pos[0] < 35 and pos[1] > 35 and pos[1] < 70:
                mode = 2
            if pos[0] > 0 and pos[0] < 35 and pos[1] > 70 and pos[1] < 105:
                mode = 3
            if pos[0] > 0 and pos[0] < 35 and pos[1] > 105 and pos[1] < 140:
                mode = 0
            if pos[0] > 0 and pos[0] < 35 and pos[1] > 140 and pos[1] < 175:
                screen.fill(WHITE)
                
        if event.type == pygame.MOUSEBUTTONUP:
            global x, y
            drawing = False
            end_pos = pos
            x = abs(start_pos[0] - end_pos[0])
            y = abs(start_pos[1] - end_pos[1])
            
            if mode == 1:
                pygame.draw.rect(screen, color, (pos[0], pos[1], x, y), 4)
            elif mode == 2:
                pygame.draw.circle(screen, color, pos, x, 4)
            
        if event.type == pygame.MOUSEMOTION and drawing:
            if mode == 3:
                pygame.draw.circle(screen, WHITE, pos, RAD)
            if mode == 0:
                pygame.draw.circle(screen, color, pos, 20)
    

    
    
    each = 35
    for i, col in enumerate(COLORS):
        pygame.draw.rect(screen, col, (765, i * each, each, 35))
        
    rectangle_size = rectangle.get_rect()
    screen.blit(rectangle, rectangle_size)
    
    circle_size = rectangle.get_rect()
    screen.blit(circle, (circle_size[0], circle_size[1] + 35))
    
    eras_size = eras.get_rect()
    screen.blit(eras, (eras_size[0], eras_size[1] + 70))
    
    brush_size = brush.get_rect()
    screen.blit(brush, (brush_size[0], brush_size[1] + 105))
    
    clrs_size = clrs.get_rect()
    screen.blit(clrs, (clrs_size[0], clrs_size[1] + 140))

        
    pygame.display.flip()
pygame.quit()