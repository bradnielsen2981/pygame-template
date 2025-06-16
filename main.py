''' Main Game Code '''
import pygame
from pygame.locals import *
import os, sys, random, time, math
import game_globals as GAME
from player import Player
from enemy import Enemy
from platforms import Platform

'''----------------------- Initialisation --------------------------'''
# Initialising imported Pygame modules (basically getting things started) #
pygame.init()
pygame.mixer.init()
pygame.font.init()
pygame.display.set_mode((1024, 768))
pygame.display.set_caption('Space Game') # Setting bar title of game window #

# Global game objects and variables
CLOCK= pygame.time.Clock() # Creating a 'clock' variable that tracks time #
FONT = pygame.font.SysFont('Comic Sans MS', 30)
BACKGROUND_IMAGE = pygame.image.load("images/background.jpg")

GAME.SCREEN = pygame.display.get_surface() # Where graphics/visual output displayed #
GAME.EXIT = False
GAME.STATE = "Start Game"
GAME.PLATFORM_GROUP = pygame.sprite.Group()

grid = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,0,1,1,1,0,0,0,0,0,0,1,1,1,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
        [0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0],
        [0,0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

def create_platforms_from_grid(grid):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 1:  # If the cell is a platform
                p = Platform((x * 64, y * 64), 64, 64)

create_platforms_from_grid(grid)  # Create platforms from the grid


'''-------------------------- Game Loop --------------------------'''
while not GAME.EXIT:

    # Control the rate at which game run --> framerate set to 60fps #
    CLOCK.tick(60)

    # GAME LOGIC ------------------------------------
    # Process events
    for event in pygame.event.get():
        if event.type == QUIT:
            GAME.EXIT = True

    # Collect user input
    pressed = pygame.key.get_pressed() #returns []
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos()) # returns (x,y)
    mouse_buttons = pygame.mouse.get_pressed() # return (1, 0, 0) if left button click

    GAME.SCREEN.blit(BACKGROUND_IMAGE, (0,0))
    #GAME.SCREEN.fill((0, 0, 0))

    if GAME.STATE == "Start Game":
        coord = FONT.render("x: " + str(mouse_pos.x) + " y: " + str(mouse_pos.y),True,(200,200,200))
        GAME.SCREEN.blit(coord, (10,10))
        button_rect = pygame.rect.Rect(460,330,200,100)
        pygame.draw.rect(GAME.SCREEN,(200,0,0),button_rect) 
        button_text = FONT.render("Play",True,(200,200,200))
        GAME.SCREEN.blit(button_text,(520,360))
        
        if pressed[pygame.K_SPACE]:
            GAME.STATE = "Running"
            GAME.STARTTIME = time.time()
            GAME.PLAYER = Player(500,500)
            #GAME.MUSIC = pygame.mixer.Sound("sounds/sunsetreverie.mp3")
            #GAME.MUSIC.play(-1)

    elif GAME.STATE == "Running":
        # Update Sprites
        if GAME.PLAYER:
            GAME.PLAYER.update(pressed, mouse_pos, mouse_buttons) #update all sprites by calling their update function
        GAME.PLATFORM_GROUP.update()

        # GAME DRAWING ---------------------------------
        GAME.PLATFORM_GROUP.draw(GAME.SCREEN)
        if GAME.PLAYER:
            GAME.PLAYER.draw(GAME.SCREEN) # draw sprite
        
        timer = int(time.time() - GAME.STARTTIME)
        timer_text = FONT.render("Time: " + str(timer),True,(200,200,200))
        GAME.SCREEN.blit(timer_text,(10,10))
        
        score_text = FONT.render("Score: " + str(GAME.SCORE),True,(200,200,200))
        GAME.SCREEN.blit(score_text,(10,80))

        #draw player health
        if GAME.PLAYER:
            health_rect = pygame.rect.Rect(200,10,400,50)
            pygame.draw.rect(GAME.SCREEN,(200,0,0),health_rect)
            playerhealth = int(400*GAME.PLAYER.health/100)
            health_remaining_rect = pygame.rect.Rect(200+(400-playerhealth),10,playerhealth,50)
            pygame.draw.rect(GAME.SCREEN,(0,200,0),health_remaining_rect)         

    elif GAME.STATE == "Game Over":
        LABEL = FONT.render("GAME OVER",True,(200,200,200))
        GAME.SCREEN.blit(LABEL, (400,360))
        GAME.PLAYER = None #Now kill the player
        GAME.PLATFORM_GROUP.empty()

        if time.time() - GAME.ENDTIME > 3:
            GAME.STATE = "Start Game"

    pygame.display.flip() #all drawing that was done off screen is now flipped onto the screen
    
'''------------------------ Exit --------------------------------'''
print("Exiting")
pygame.quit()
sys.exit(0)


