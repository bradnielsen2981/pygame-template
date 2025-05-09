''' Main Game Code '''
import pygame
import pygame.locals as CONSTANTS
import os, sys, random, time, math
import game_globals as GAME
from spaceship import Spaceship #when you from - you skip using the namespace

'''----------------------- Initialisation --------------------------'''
# Initialising imported Pygame modules (basically getting things started) #
pygame.init()
pygame.mixer.init()
pygame.font.init()
pygame.display.set_mode((1024, 680))
pygame.display.set_caption('Space Game') # Setting bar title of game window #

# Global game objects and variables
CLOCK = pygame.time.Clock() # Creating a 'clock' variable that tracks time #
FONT = pygame.font.SysFont('Comic Sans MS', 30)
FONT2 = pygame.font.SysFont('Impact', 60)
BACKGROUND_IMAGE = pygame.image.load("images/background.jpg")

GAME.SCREEN = pygame.display.get_surface() # Where graphics/visual output displayed #
GAME.EXIT = False
GAME.STATE = "Start Game" 

'''-------------------------- Game Loop --------------------------'''
while not GAME.EXIT:

    # Control the rate at which game run --> framerate set to 60fps #
    CLOCK.tick(60)

    # GAME LOGIC ------------------------------------

    # Process events
    for event in pygame.event.get():
        #set game exit true if player pressed escape
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                GAME.EXIT = True
        if event.type == pygame.QUIT:
            GAME.EXIT = True

    # Collect user input
    pressed = pygame.key.get_pressed() #returns []
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos()) # returns (x,y)
    mouse_buttons = pygame.mouse.get_pressed() # return (0, 0, 0) if left button click

    GAME.SCREEN.blit(BACKGROUND_IMAGE, (0,0)) #top left image
    #GAME.SCREEN.fill((0, 0, 255)) RGB 

    if GAME.STATE == "Start Game":
        start_text = FONT2.render("Press Enter to Start Game", True, (255, 0, 0))
        GAME.SCREEN.blit(start_text, (300,300))
        if pressed[pygame.K_RETURN]:
            GAME.STATE = "Running"
            GAME.STARTTIME = time.time()
            GAME.PLAYER = Spaceship(512, 530) #CREATES OUR SPACESHIP OBJECT
    elif GAME.STATE == "Running":
        
        GAME.PLAYER.update(pressed) #update player position
        GAME.PLAYER.draw()

        mouse_text = FONT.render("X: " + str(mouse_pos[0]) + " Y: " + str(mouse_pos[1]),True,(255,0,0))
        GAME.SCREEN.blit(mouse_text,(10,10))

    pygame.display.flip() #all drawing that was done off screen is now flipped onto the screen
    
'''------------------------ Exit --------------------------------'''
print("Exiting")
pygame.quit()
sys.exit(0)


