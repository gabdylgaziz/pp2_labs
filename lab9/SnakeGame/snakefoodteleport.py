import pygame
import json
import time
from random import randint
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
font = pygame.font.SysFont("Verdana", 20)
background = pygame.image.load("./img/green.jpg")
eat = pygame.mixer.Sound("./sounds/eat.mp3")
pygame.mixer.music.load("./sounds/theme.mp3")

HEIGHT = 500
WIDTH = 500
WIDTHSCREEN = 700

BLOCK_SIZE = 20


class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
        
class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.location = Point(self.x, self.y)
        self.image = pygame.image.load("./img/apple.png")
        self.rect = self.image.get_rect()
        
    def draw(self):
        point = self.location
        self.rect.center = (BLOCK_SIZE * point.x + 10, BLOCK_SIZE * point.y + 10)
        SCREEN.blit(self.image, self.rect)
    
    def respawn(self, dx, dy):
        self.dx = dx
        self.dy = dy
        self.location = Point(self.dx, self.dy)

class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.location = Point(self.x, self.y)
        self.image = pygame.image.load("./img/block.png")
        self.rect = self.image.get_rect()
        
    def draw(self):
        point = self.location
        self.rect.center = (BLOCK_SIZE * point.x + 10, BLOCK_SIZE * point.y + 10)
        SCREEN.blit(self.image, self.rect)
       
class Snake:
    def __init__(self):
        self.body = [Point(10, 11)]
        self.image = pygame.image.load("./img/zhantore.png")
        self.rect = self.image.get_rect()
        self.dx = 0
        self.dy = 0

    def move(self):    
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y

        self.body[0].x += self.dx 
        self.body[0].y += self.dy 

        if self.body[0].x * BLOCK_SIZE > WIDTH:
            self.body[0].x = 0
        
        if self.body[0].y * BLOCK_SIZE > HEIGHT:
            self.body[0].y = 0

        if self.body[0].x < 0:
            self.body[0].x = WIDTH / BLOCK_SIZE
        
        if self.body[0].y < 0:
            self.body[0].y = HEIGHT / BLOCK_SIZE

    def draw(self):
        point = self.body[0]
        self.rect.center = (BLOCK_SIZE * point.x + 10, BLOCK_SIZE * point.y + 10)
        SCREEN.blit(self.image, self.rect)


        for point in self.body[1:]:
            self.rect.center = (BLOCK_SIZE * point.x + 10, BLOCK_SIZE * point.y + 10)
            SCREEN.blit(self.image, self.rect)
        
    def check_collision(self, food, block):
        if self.body[0].x == food.location.x:
            if self.body[0].y == food.location.y:
                global SCORE
                SCORE+=randint(1, 3)
                with open("savefile.json", "w") as f:
                    if SCORE > DICT['highscore']:
                        DICT['highscore'] = SCORE
                    l = json.dumps(DICT, indent=4)
                    f.write(l)
                self.body.append(Point(food.location.x, food.location.y))
                eat.play()
                if food.location.x != block.x and food.location.y != block.y:
                    food.location.x, food.location.y = randint(2, 22), randint(2, 22)
restart = True

while restart:
    pygame.mixer.music.play(-1)
    global SCREEN, FPS
    SCREEN = pygame.display.set_mode((WIDTHSCREEN, HEIGHT))
    pygame.display.set_caption("Zhantornake")
    CLOCK = pygame.time.Clock()
    FPS = 5
    DICT = {}
    block = Block(0, 0)
    food = Food(randint(2, 22), randint(2, 22))
    count = 0
    running = True
    lose = False
    while running:
        SCREEN.blit(background, (0, 0))
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                restart = not restart
                running = not running
        wallsCoor = open("level.txt", 'r').readlines()
        walls = []
        for i, line in enumerate(wallsCoor):
            for j, each in enumerate(line):
                if each == "#":
                    walls.append(Block(j, i))
        
        for block in walls:
            block.draw()
            if food.x != block.x and food.y != block.y:
                food.draw()
                
        
            
            

        pygame.display.flip()
    pygame.display.flip()
pygame.quit()