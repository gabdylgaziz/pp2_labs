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
        #загрузка сюрфэйса
        self.image = pygame.image.load("./img/apple.png")
        self.rect = self.image.get_rect()
        
    def draw(self):
        point = self.location
        self.rect.center = (BLOCK_SIZE * point.x + 10, BLOCK_SIZE * point.y + 10)
        SCREEN.blit(self.image, self.rect)
        
    def respawn(self, dx, dy):
        #телепорт еды
        self.dx = dx
        self.dy = dy
        self.location = Point(self.dx, self.dy)

class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.location = Point(self.x, self.y)
        #загрузка сюрфэйса
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
        #когда змейка хавает, размер увеличивается
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y

        self.body[0].x += self.dx 
        self.body[0].y += self.dy 
        
        #когда змейка выходит за карту, чтобы он возвращался
        if self.body[0].x * BLOCK_SIZE > WIDTH:
            self.body[0].x = 0
        
        if self.body[0].y * BLOCK_SIZE > HEIGHT:
            self.body[0].y = 0

        if self.body[0].x < 0:
            self.body[0].x = WIDTH / BLOCK_SIZE
        
        if self.body[0].y < 0:
            self.body[0].y = HEIGHT / BLOCK_SIZE
    #отрисовка головы и тела
    def draw(self):
        point = self.body[0]
        self.rect.center = (BLOCK_SIZE * point.x + 10, BLOCK_SIZE * point.y + 10)
        SCREEN.blit(self.image, self.rect)


        for point in self.body[1:]:
            self.rect.center = (BLOCK_SIZE * point.x + 10, BLOCK_SIZE * point.y + 10)
            SCREEN.blit(self.image, self.rect)
        
        
    #коллизия
    def check_collision(self, food, block):
        if self.body[0].x == food.location.x:
            if self.body[0].y == food.location.y:
                global SCORE, count
                count = 0
                #сохранение в файл
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
    #начальные условия после рестарта
    pygame.mixer.music.play(-1)
    global SCREEN, FPS
    SCREEN = pygame.display.set_mode((WIDTHSCREEN, HEIGHT))
    pygame.display.set_caption("Zhantornake")
    CLOCK = pygame.time.Clock()
    SCORE = 0
    LEVEL = 0
    FPS = 5
    DICT = {}
    count = 0

    block = Block(0, 0)
    snake = Snake()
    food = Food(randint(1, 25), randint(1, 25))
    running = True
    lose = False
    while running: 
        #чтобы отображать лучший счет
        with open("savefile.json", "r") as f:
            DICT = json.loads(f.read())
        SCREEN.blit(background, (0, 0))
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                restart = not restart
                running = not running
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1

        #для отрисовки уровня
        wallsCoor = open("level.txt", 'r').readlines()
        walls = []
        for i, line in enumerate(wallsCoor):
            for j, each in enumerate(line):
                if each == "#":
                    walls.append(Block(j, i))
        
        

        for block in walls:
            block.draw()
            if snake.body[0].x == block.x and snake.body[0].y == block.y:
                lose = True
            if food.x != block.x and food.y != block.y:
                food.draw()
        #-----------------------------------------
        while lose:
            #цикл для луза, чтобы можно было начать сначала
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    restart = not restart
                    running = not running
                    lose = not lose
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    running = not running
                    lose = not lose
            game_over = font.render("Game Over", True, BLACK)
            rrr = font.render("Press R to restart", True, BLACK)
            your_score = font.render(f"Your score: {SCORE}", True, BLACK)
            highscore_text = font.render(f"Highscore: {DICT['highscore']}", True, BLACK)
            level_text = font.render(f"Level: {LEVEL}", True, BLACK)
            pygame.draw.rect(SCREEN, WHITE, (WIDTH // 2 - 200, HEIGHT // 2 - 200, 400, 400))
            SCREEN.blit(game_over, game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100)))
            SCREEN.blit(rrr, rrr.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
            SCREEN.blit(your_score, your_score.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 75)))
            SCREEN.blit(highscore_text, score_img.get_rect(center=(WIDTH // 2 - 60, HEIGHT // 2 - 50)))
            SCREEN.blit(level_text, level_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 25)))
            pygame.display.flip()
            
        snake.move()
        snake.check_collision(food, block)
        snake.draw()
        
        if SCORE > 0 and SCORE % 5 == 0:
            SCORE+=1
            LEVEL+=1
            FPS+=2
        #зависимость телепорта еды от фпс
        #можно делать по другому с юзеривент, но я не хочу простоты и сделал по другому
        count += (FPS % 3)
        if count % 100 == 0 and count > 0:
            food.respawn(randint(2, 22), randint(2, 22))
        
        #Text------------------------------
        score_img = font.render(f"{SCORE}", True, BLACK)
        highscore = font.render(f"{DICT['highscore']}", False, False)
        coins_cnt = font.render(f"{LEVEL}", False, False)
        SCREEN.blit(font.render(f"SCORE", True, BLACK), (565, 25))
        SCREEN.blit(font.render(f"HIGHSC", True, BLACK), (560, 80))
        SCREEN.blit(font.render("LEVEL", True, BLACK), (570, 135))
        SCREEN.blit(score_img, score_img.get_rect(center=(600, 65)))
        SCREEN.blit(highscore, highscore.get_rect(center=(600, 120)))
        SCREEN.blit(coins_cnt, coins_cnt.get_rect(center=(600, 170)))
        

        pygame.display.flip()
    pygame.display.flip()
pygame.quit()
