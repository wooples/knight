#!/usr/bin/python3

import pygame
import os
#will use find_tour from solve.py
import solve

WIDTH, HEIGHT = 400, 400
BLACK, WHITE, RED, GREEN = (0,0,0),(255,255,255),(255,0,0),(0,255,0)

##################################
print('makes a knights tour of chessboard')
print('put in coords of square to start at')
print('then when board pops up, use space bar')
print('to make knight do next move :)')
while True:
    try:
        i = int(input('enter row (0..7) >> '))
        j = int(input('enter rank (0..7 >> '))
        assert 0<=i<=7 and 0<=j<=7
        break
    except:
        print('integers 0 to 7 only!')
        continue
begin = (i,j)
#call find_tour from solve.py
l = solve.find_tour(begin)
##################################

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def draw_board():
    for i in range(4):
        for j in range(4):
            pygame.draw.rect(screen, WHITE, pygame.Rect(100*j,100*i,50,50))
            pygame.draw.rect(screen, WHITE, pygame.Rect(100*j+50, 100*i+50,50,50))
            pygame.draw.rect(screen, BLACK, pygame.Rect(100*j+50,100*i,50,50))
            pygame.draw.rect(screen, BLACK, pygame.Rect(100*j,100*i+50,50,50))

draw_board()

knight = pygame.sprite.Sprite()
pygame.sprite.Sprite.__init__(knight)
try: 
    knight.image = pygame.image.load('img/knight.png')
except:
     knight.image = pygame.image.load('knight.png')

knight.rect = knight.image.get_rect()
knight.rect.center = (50*begin[0]+25, 50*begin[1]+25)
knight_sprites = pygame.sprite.Group()
knight_sprites.add(knight)
knight_sprites.draw(screen)

def move(start, finish):
    for count in range(20):
        pos = start[0] + (count/20)*(finish[0]-start[0]),\
              start[1] + (count/20)*(finish[1]-start[1])
        knight.rect.center = pos
        knight_sprites.draw(screen)
        pygame.time.wait(int(1000/20))
        pygame.display.flip()
    draw_board()
    knight_sprites.draw(screen)


i=0
go = True
while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = False 
        if i>=63:
            continue
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            start = (50*l[i][0]+25, 50*l[i][1]+25)
            finish = (50*l[i+1][0]+25, 50*l[i+1][1]+25)
            move(start, finish)   ############
            for j in range(i+1):
                pygame.draw.line(screen, RED, (50*l[j][0]+25, 50*l[j][1]+25), (50*l[j+1][0]+25, 50*l[j+1][1]+25))
                pygame.draw.circle(screen, RED, (50*l[j+1][0]+25, 50*l[j+1][1]+25), 10)
                pygame.draw.circle(screen, RED, (50*begin[0]+25, 50*begin[1]+25), 10)
            i+=1
            knight_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)
