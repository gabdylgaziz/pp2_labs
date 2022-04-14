import pygame
pygame.init()

WIDTH = 800
HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()
start_pos = 0
end_pos = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Triangle")

running = True

while running:
    clock.tick(FPS)
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = pos
        if event.type == pygame.MOUSEBUTTONUP:
            global x, y
            drawing = False
            end_pos = pos
            x = abs(start_pos[0] - end_pos[0])
            y = abs(start_pos[1] - end_pos[1])
            
            pygame.draw.rect(screen, BLACK, (pos[0], pos[1], x, y), 4)
            
    screen.fill(WHITE)
    
    #pygame.draw.circle(screen, BLACK, [250, 250], 40, 0, draw_top_right=True)
    #pygame.draw.circle(screen, BLACK, [250, 250], 40, 30, draw_top_left=True)
    #pygame.draw.circle(screen, BLACK, [250, 250], 40, 20, draw_bottom_left=True)
    #pygame.draw.circle(screen, BLACK, [250, 250], 40, 10, draw_bottom_right=True)
    #pygame.draw.polygon(screen, BLACK, [[50, 50], [0, 100], [100, 100]], 5)
    pygame.draw.rect(screen, BLACK, (250, 250, 50, 50), 4)
            
    pygame.display.flip()
pygame.quit()