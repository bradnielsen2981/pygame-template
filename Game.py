import pygame
from pygame.locals import *
import os, sys
import random
from myrectangle import myrectangle
from player import Player

pygame.init()
pygame.mixer.init()
pygame.font.init()

#create display
dimensions = (1024, 600)
pygame.display.set_mode(dimensions)
pygame.display.set_caption('My Space Game')
screen = pygame.display.get_surface() # Surface object
screen.fill((124, 255, 0)) #(255,255,255)  R,G,B

#create an image object
background = pygame.image.load("background.jpg") 
screen.blit(background, (0,0)) #blit command can be used to show any image.

#create a font
myfont = pygame.font.SysFont('ArialBold', 30)

#create a shape or line on the screen
#challenge: Draw three shapes or lines - look up pygame.draw

#play music
pygame.mixer.music.load('backgroundmusic.mp3')
pygame.mixer.music.play()

clock = pygame.time.Clock()
Exit = False
x = 0
y = 200

rectanglesprites = pygame.sprite.Group()
hero = Player(200,200)
 
pygame.time.set_timer(USEREVENT + 1, 3000)

while not Exit: #game loop

    clock.tick(60) #framerate
    # Process Main Events and Logic
    for event in pygame.event.get():
        if event.type == QUIT:
            Exit = True
        elif event.type == USEREVENT + 1:
            newrectangle = myrectangle(random.randint(0,1024),random.randint(0,600))
            rectanglesprites.add(newrectangle) #adding the sprite to the sprite group
            pygame.time.set_timer(USEREVENT + 1, 3000)

    #Process Input
    pressed = pygame.key.get_pressed()
    mouse_x, mouse_y = pygame.mouse.get_pos()

    #Logic
    timer = int(pygame.time.get_ticks()/1000)
    timer = str(timer)
    label = myfont.render("Time: " + timer,True,(255,255,255))

    rectanglesprites.update(dimensions)
    hero.update(pressed)

    #detect a collision
    collidedsprites = pygame.sprite.spritecollide(hero, rectanglesprites, True)
    '''for collidedsprite in collidedsprites:
        r1 = myrectangle(100,100)
        r2 = myrectangle(200,200)
        rectanglesprites.add(r1)
        rectanglesprites.add(r2)'''
    
    #Drawing
    screen.blit(background, (0,0))
    screen.blit(label,(50,50))
    rectanglesprites.draw(screen)
    hero.draw(screen)

    #flip
    pygame.display.flip()


pygame.quit()
sys.exit()






