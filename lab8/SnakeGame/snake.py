import pygame
import json
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
    def __init__(self):
        #появление еды на рандомных местах
        self.x = randint(2, 22)
        self.y = randint(2, 22)
        self.location = Point(self.x, self.y)
        #загрузка текстуры вместо прямоугольника
        self.image = pygame.image.load("./img/apple.png")
        self.rect = self.image.get_rect()
        
    def draw(self):
        point = self.location
        self.rect.center = (BLOCK_SIZE * point.x + 10, BLOCK_SIZE * point.y + 10)
        SCREEN.blit(self.image, self.rect)
        
class Speed:
    def __init__(self):
        #появление уменьшителя скорости на рандомных местах
        self.x = randint(2, 22)
        self.y = randint(2, 22)
        self.location = Point(self.x, self.y)
        #загрузка текстуры вместо прямоугольника
        self.image = pygame.image.load("./img/yellow.png")
        self.rect = self.image.get_rect()
    
    def draw(self):
        point = self.location
        self.rect.center = (BLOCK_SIZE * point.x + 10, BLOCK_SIZE * point.y + 10)
        SCREEN.blit(self.image, self.rect)

class Block:
    def __init__(self, x, y):
        #задать определенные координаты для блока
        self.x = x
        self.y = y
        self.location = Point(self.x, self.y)
        #загрузка текстуры вместо прямоугольника
        self.image = pygame.image.load("./img/block.png")
        self.rect = self.image.get_rect()
        
    def draw(self):
        point = self.location
        self.rect.center = (BLOCK_SIZE * point.x + 10, BLOCK_SIZE * point.y + 10)
        SCREEN.blit(self.image, self.rect)
        
class PortalIn:
    def __init__(self):
        #появление синего портала на рандомных местах
        self.x = randint(2, 22)
        self.y = randint(2, 22)
        self.location = Point(self.x, self.y)
        #загрузка текстуры вместо прямоугольника
        self.image = pygame.image.load("./img/portalin.png")
        self.rect = self.image.get_rect()
    
    def draw(self):
        point = self.location
        self.rect.center = (BLOCK_SIZE * point.x + 10, BLOCK_SIZE * point.y + 10)
        SCREEN.blit(self.image, self.rect)
        
class PortalOut:
    def __init__(self):
        #появление оранжевого портала на рандомных местах
        self.x = randint(2, 22)
        self.y = randint(2, 22)
        self.location = Point(self.x, self.y)
        #загрузка текстуры вместо прямоугольника
        self.image = pygame.image.load("./img/portalout.png")
        self.rect = self.image.get_rect()
    
    def draw(self):
        point = self.location
        self.rect.center = (BLOCK_SIZE * point.x + 10, BLOCK_SIZE * point.y + 10)
        SCREEN.blit(self.image, self.rect)
        
class Snake:
    def __init__(self):
        self.body = [Point(10, 11)]
        #загрузка текстуры вместо прямоугольника
        self.image = pygame.image.load("./img/zhantore.png")
        self.rect = self.image.get_rect()
        self.dx = 0
        self.dy = 0

    def move(self):    
        for i in range(len(self.body) - 1, 0, -1):
            #увеличение размера змейки
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y
        #для движения
        self.body[0].x += self.dx 
        self.body[0].y += self.dy 
        #чтобы он не улетел за границы карты
        if self.body[0].x * BLOCK_SIZE > WIDTH:
            self.body[0].x = 0
        
        if self.body[0].y * BLOCK_SIZE > HEIGHT:
            self.body[0].y = 0

        if self.body[0].x < 0:
            self.body[0].x = WIDTH / BLOCK_SIZE
        
        if self.body[0].y < 0:
            self.body[0].y = HEIGHT / BLOCK_SIZE

    def draw(self):
        #отрисовка головы
        point = self.body[0]
        self.rect.center = (BLOCK_SIZE * point.x + 10, BLOCK_SIZE * point.y + 10)
        SCREEN.blit(self.image, self.rect)

        #отрисовка тела
        for point in self.body[1:]:
            self.rect.center = (BLOCK_SIZE * point.x + 10, BLOCK_SIZE * point.y + 10)
            SCREEN.blit(self.image, self.rect)
    
    #проверка коллизии
    def check_collision(self, food, block, speeds, cin, cout):
        if self.body[0].x == food.location.x:
            if self.body[0].y == food.location.y:
                global SCORE
                SCORE+=1
                with open("savefile.json", "w") as f:
                    if SCORE > DICT['highscore']:
                        DICT['highscore'] = SCORE
                    l = json.dumps(DICT, indent=4)
                    f.write(l)
                self.body.append(Point(food.location.x, food.location.y))
                eat.play()
                if food.location.x != block.x and food.location.y != block.y:
                    food.location.x, food.location.y = randint(2, 22), randint(2, 22)
        if self.body[0].x == speeds.location.x:
            if self.body[0].y == speeds.location.y:
                global LEVEL, FPS
                LEVEL-=1
                FPS-=5
                if speeds.location.x != block.x and speeds.location.y != block.y:
                    speeds.location.x, speeds.location.y = randint(2, 22), randint(2, 22)
        if self.body[0].x == cin.location.x:
            if self.body[0].y == cin.location.y:
                snake.body[0].x = cout.location.x
                snake.body[0].y = cout.location.y
                
                if cin.location.x != block.x and cin.location.y != block.y:
                    cin.location.x, cin.location.y = randint(2, 22), randint(2, 22)
                if cout.location.x != block.x and cout.location.y != block.y:
                    cout.location.x, cout.location.y = randint(2, 22), randint(2, 22)
restart = True

while restart:
    #Initial conditions for restart
    pygame.mixer.music.play(-1)
    global SCREEN, FPS
    SCREEN = pygame.display.set_mode((WIDTHSCREEN, HEIGHT))
    pygame.display.set_caption("Zhantornake")
    CLOCK = pygame.time.Clock()
    SCORE = 0
    LEVEL = 0
    FPS = 5
    DICT = {}

    block = Block(0, 0)
    snake = Snake()
    food = Food()
    speeds = Speed()
    cin = PortalIn()
    cout = PortalOut()
    running = True
    lose = False
    while running: 
        #для показа highscore
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

        #чтобы прочитать уровень
        wallsCoor = open("level.txt", 'r').readlines()
        walls = []
        for i, line in enumerate(wallsCoor):
            for j, each in enumerate(line):
                if each == "#":
                    walls.append(Block(j, i))
        
        
        #для отрисовки уровня
        for block in walls:
            block.draw()
            if snake.body[0].x == block.x and snake.body[0].y == block.y:
                lose = True
            if food.x != block.x and food.y != block.y:
                food.draw()
            if SCORE >= 5:
                if speeds.x != block.x and speeds.y != block.y:
                    speeds.draw()
                if cin.x != block.x and cin.y != block.y:
                    cin.draw()
                if cout.x != block.x and cout.y != block.y:
                    cout.draw()
        
        
        
            
        
        #event lose
        while lose:
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

        snake.check_collision(food, block, speeds, cin, cout)
        snake.draw()
        
        if SCORE > 0 and SCORE % 5 == 0:
            SCORE+=1
            LEVEL+=1
            FPS+=5
        
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
