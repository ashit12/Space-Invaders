import time
import pygame
import random
import sys
from pygame.locals import *
from time import time
from random import randint
import math
from alien import *
from Spaceship import *
from missile import *


pygame.init()
pygame.font.init()

score = 0
width = 850
height = 800
ini_pos = 500
FPS = 30
x = 5
y = 0
score = 0
flag = 0
missilelist = []
alienlist = []


prev_time = time()
play_time = time()
fpsClock = pygame.time.Clock()
Space = ship()


alien_image_1 = pygame.image.load('alien_image_1.png')
alien_image_2 = pygame.image.load('alien_image_2.png')
spaceship = pygame.image.load('Spaceship.jpg')
missile_image_1 = pygame.image.load('finalmissile1.png')
missile_image_2 = pygame.image.load('finalmissile2.png')
DISPLAYSURF = pygame.display.set_mode((width, height), 0, 32)
DISPLAYSURF.fill((0, 0, 0))
DISPLAYSURF.blit(spaceship, (ini_pos, 700))
scorefont = pygame.font.SysFont("monospace", 25)
scoretext = scorefont.render("Score = "+str(score), 1, (0, 0, 255))
DISPLAYSURF.blit(scoretext, (675, 750))

# initial alien
#var = time()
# initial_alien=alien(posx[5],posy[0],var,0,0)
# alienlist.append(initial_alien)
# DISPLAYSURF.blit(alien_image_1,(posx[5],posy[0]))

game_start = time() - 10
while True:

        # Detects which event is going on in the game
    for event in pygame.event.get():
        if(event.type == KEYDOWN):
            if(event.key == K_a):
                ini_pos = Space.Moveleft(ini_pos)
            if(event.key == K_d):
                ini_pos = Space.Moveright(ini_pos)
            if(event.key == K_SPACE):
                start_time = time()
                new_missile_1 = missile1(start_time, 0, ini_pos, 600)
                missilelist.append(new_missile_1)
            if(event.key == K_s):
                start_time = time()
                new_missile_2 = missile2(start_time, 0, ini_pos, 600)
                missilelist.append(new_missile_2)
            if(event.key == K_q):
                pygame.quit()
                sys.exit()

    # Detects if a collision takes place
    cur_time = time()
    for i in alienlist:
        for j in missilelist:
            if(j.position_y <= i.alien_posy+99 and (abs(i.alien_posx-j.position_x) <= 5) and i.freeze == 0):
                score += 1
                print score
                if(j.typeo == 1):
                    alienlist.pop(alienlist.index(i))
                    missilelist.pop(missilelist.index(j))
                if(j.typeo == 2):
                    i.freeze = 1
                    missilelist.pop(missilelist.index(j))
                    i.freeze_time = time()

    # Puts an alien on a random location on the screen
    cur_time = time()
    if(game_start+10 <= cur_time):
        x = randint(0, 7) * 100
        y = randint(0, 1) * 100
        new_alien = alien(x, y, cur_time, 0, 0)
        alienlist.append(new_alien)
        game_start = cur_time

    # Gets the background and spaceship on the screen
    DISPLAYSURF.fill((0, 0, 0))
    DISPLAYSURF.blit(spaceship, (ini_pos, 700))
    scoretext = scorefont.render("Score = "+str(score), 1, (0, 0, 255))
    DISPLAYSURF.blit(scoretext, (675, 750))

    # Displays the alien on the screen depending on its freeze status
    cur_time = time()
    for i in alienlist:
        if(i.freeze == 0):
            if(i.alien_time+8 <= cur_time):
                alienlist.pop(alienlist.index(i))
            else:
                DISPLAYSURF.blit(alien_image_1, (i.alien_posx, i.alien_posy))
        elif(i.freeze == 1):
            if(i.freeze_time+5 <= cur_time):
                alienlist.pop(alienlist.index(i))
            else:
                DISPLAYSURF.blit(alien_image_2, (i.alien_posx, i.alien_posy))

    # Displays all the missiles on the screen and
    # changes their position depending on their type
    cur_time = time()
    for i in missilelist:
        if(i.position_y <= -100):
            missilelist.pop(missilelist.index(i))
        else:
            if(i.typeo == 1):
                DISPLAYSURF.blit(missile_image_1, (i.position_x, i.position_y))
                if(i.missile_start_time+1 <= cur_time):
                    i.update(cur_time)
                    i.position_y -= 100
            if(i.typeo == 2):
                DISPLAYSURF.blit(missile_image_2, (i.position_x, i.position_y))
                if(i.missile_start_time+1 <= cur_time):
                    i.update(cur_time)
                    i.position_y -= 200

    # pygame.display.flip()
    pygame.display.update()
    fpsClock.tick(FPS)
