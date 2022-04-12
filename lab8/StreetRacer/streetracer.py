import pygame
import random
import json

pygame.init()

#Initial conditions
WIDTH = 600
HEIGHT = 600
FPS = 10
HIGHSCORE = 0
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Resources
#Images
player = pygame.image.load("./img/Player.png")
enemy = pygame.image.load("./img/Enemy.png")
Background = pygame.image.load("./img/AnimatedStreet.png")
Background2 = pygame.image.load("./img/StreetGame.png")
coin = pygame.image.load("./img/coin1.png")
#Fonts
font = pygame.font.SysFont("Verdana", 20)
#Sounds
pygame.mixer.music.load("./sounds/music.ogg")
get = pygame.mixer.Sound("./sounds/coin.wav")
accident = pygame.mixer.Sound("./sounds/accident.wav")

#Разрешение экрана и set_caption(название) и фпс
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("StreetRacer")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = player
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        self.dx = 3
        self.dy = 3
 
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 38 and pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.dx, 0)
        if self.rect.right < 400 - 38 and pressed_keys[pygame.K_RIGHT]:        
            self.rect.move_ip(self.dx, 0)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect) 
        
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = enemy
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(62, 400-62),0) 
        self.dx = 3
        self.dy = 3
 
      def move(self):
        global SCORE, DICT
        self.rect.move_ip(0,self.dy)        
        if (self.rect.bottom > HEIGHT):
            #для прибавления очков и сохранения
            SCORE+=1
            with open("savefile.json", "w") as f:
                if SCORE > DICT['highscore']:
                    DICT['highscore'] = SCORE
                l = json.dumps(DICT, indent=4)
                f.write(l)
            self.rect.top = 0
            self.rect.center = (random.randint(62, 400-62), 0)
 
      def draw(self, surface):
        surface.blit(self.image, self.rect) 
        
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = coin
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(62, 400-62),0) 
        self.dx = 3
        self.dy = 3
 
    def move(self):
        self.rect.move_ip(0, self.dy)  
        if (self.rect.bottom > HEIGHT):
            self.rect.top = 0
            self.rect.center = (random.randint(62, 400-62), 0)
            
    def draw(self, surface):
        surface.blit(self.image, self.rect) 

restart = True
while restart:
    #initial conditions for restart
    pygame.mixer.music.play(-1)
    SCORE = 0
    HIGHSCORE = 0
    COINS = 0
    DICT = {}
    running = True
    lose = False
    P1 = Player()
    E1 = Enemy()
    C1 = Coin()
    enemies = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    enemies.add(E1)
    coins.add(C1)
    while running:
        #for save
        with open("savefile.json", "r") as f:
            DICT = json.loads(f.read())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                restart = not restart
                running = not running
            
        P1.update()
        E1.move()
        C1.move()

        #Collisions
        if pygame.sprite.spritecollideany(P1, enemies):
            accident.play()
            lose = True
        coincoll = pygame.sprite.spritecollide(P1, coins, False)
        for _ in coincoll:
            get.play()
            SCORE+=2
            COINS+=1
            #for save
            with open("savefile.json", "w") as f:
                if SCORE > DICT['highscore']:
                    DICT['highscore'] = SCORE
                if COINS > DICT['coins']:
                    DICT['coins'] = COINS
                l = json.dumps(DICT, indent=4)
                f.write(l)
            C1.rect.top = 0
            C1.center = (random.randint(62, 400-62), 0)
        
        while lose:
            #event_lose
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    restart = False
                    running = not running
                    lose = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    running = not running
                    lose = False
            game_over = font.render("Game Over", True, BLACK)
            rrr = font.render("Press R to restart", True, BLACK)
            your_score = font.render(f"Your score: {SCORE}", True, BLACK)
            highscore_text = font.render(f"Highscore: {DICT['highscore']}", True, BLACK)
            coins_text = font.render(f"Coins: {COINS}", True, BLACK)
            pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 200, HEIGHT // 2 - 200, 400, 400))
            screen.blit(game_over, game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100)))
            screen.blit(rrr, rrr.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
            screen.blit(your_score, your_score.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 75)))
            screen.blit(highscore_text, score_img.get_rect(center=(WIDTH // 2 - 60, HEIGHT // 2 - 50)))
            screen.blit(coins_text, coins_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 25)))
            pygame.display.flip()
            
            
        #DRAW    
        screen.blit(Background2, (0, 0))
        screen.blit(Background, (0, 0))
        coins_text = font.render(f"COINS", True, BLACK)
        score_img = font.render(f"{SCORE}", True, BLACK)
        highscore = font.render(f"{DICT['highscore']}", False, False)
        coins_cnt = font.render(f"{COINS}", False, False)
        #ProgressBar  
        screen.blit(font.render(f"SCORE", True, BLACK), (470, 10))
        screen.blit(font.render(f"HIGHSCORE", True, BLACK), (445, 70))
        screen.blit(coins_text, (470, 130))
        screen.blit(score_img, score_img.get_rect(center=(505, 50)))
        screen.blit(highscore, highscore.get_rect(center=(505, 110)))
        screen.blit(coins_cnt, coins_cnt.get_rect(center=(505, 170)))
        
        P1.draw(screen)
        E1.draw(screen)
        C1.draw(screen)
         
        pygame.display.update()
    pygame.display.update()
pygame.quit()   
