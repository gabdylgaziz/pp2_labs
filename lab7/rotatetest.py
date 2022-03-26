import pygame
import math
import datetime

pygame.init()

WIDTH = 1400
HEIGHT = 1050
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

FPS = 60

t = datetime.datetime.now()
angle = int(t.strftime("%S")) * 6
angle1 = (int(t.strftime("%S")) * 6) - 60

x, y = (WIDTH // 2 + math.sin(math.radians(angle)) * 345), (HEIGHT // 2 + 3 - math.cos(math.radians(angle)) * 345)


#Background
#background = pygame.image.load('./img/mickeyclock12.png')
second = pygame.image.load('./img/seconddd1.png')

#rotate
def rotate(image, rect, angle):
    new_image = pygame.transform.rotate(image, angle)
    rect = new_image.get_rect(center=rect.center)
    return new_image, rect

#second
image = pygame.Surface((63, HEIGHT), pygame.SRCALPHA)
image.blit(second, (0, 0))
orig_image = image
rect = image.get_rect(center=(WIDTH//2, HEIGHT//2))

#Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RotateTest")

finished = False
clock = pygame.time.Clock()

while not finished:
    clock.tick(FPS)  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            
    image, rect = rotate(orig_image, rect, angle)
    screen.fill(WHITE)
    #screen.blit(background, (0, 0))
    screen.blit(image, rect)
    
    pygame.draw.circle(screen, RED, (x, y), 10)
    pygame.draw.line(screen, RED, (WIDTH // 2, HEIGHT // 2), (x, y), 5)

    x = WIDTH // 2 + math.sin(math.radians(angle1)) * 345
    y = HEIGHT // 2 + 3 - math.cos(math.radians(angle1)) * 345

    angle -= 0.099
    angle1 += 0.099
    
    pygame.display.flip()

pygame.quit()
    

