import os
import pygame

pygame.init()

WIDTH = 800
HEIGHT = 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
player = True
done = False
path = ''
pygame.mixer.music.load('./music/hello.mp3')
font = pygame.font.Font("./fonts/coco.ttf", 100)
while player:
    pygame.mixer.music.play(1)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                player = not player
                done = not done
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                path = input()
                ya = pygame.mixer.Sound(f'./music/{path}.mp3')
                ya.play(1)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_o:
                pygame.mixer.pause()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                pygame.mixer.unpause()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                pygame.mixer.pause()
                path = int(path) + 1
                ya = pygame.mixer.Sound(f'./music/{path}.mp3')
                ya.play(1)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.mixer.pause()
                path = int(path) - 1
                ya = pygame.mixer.Sound(f'./music/{path}.mp3')
                ya.play(1)
                
        pygame.display.flip() 
    pygame.display.flip()            
pygame.quit()