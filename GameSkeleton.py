''' Main Game Code '''
import pygame
from pygame.locals import *
import os, sys

'''-----------------------Initialisation-----------------------'''
### Game Startup ###
# Initialising imported Pygame modules (basically getting things started) #
pygame.init()
screenDimensions = (1024, 600) # Setting the displays dimensions as a tuple / list
pygame.display.set_mode((screenDimensions))
pygame.display.set_caption('My Game') # Setting bar title of game window #
clock = pygame.time.Clock() # Creating a 'clock' variable that tracks time #
#pygame.font.init()

# Getting the drawing surface & background #
screen = pygame.display.get_surface() # Where graphics/visual output displayed #
#screen.blit(image) will output any image file to screen

# Keeping tack of which keys pressed #
pressed = None
Exit = False
canshoot = True

# Common Pygame Objects
#spaceship = Spaceship(screen, 500, 300) #this is a descendant of the Sprite class
#bulletgroup = pygame.sprite.Group() #a sprite group can add any descendant of the Sprite class. Its used for group logic (e.g. collisions) and rendering
#background = pygame.image.load("background2.jpg") #an image object
#myfont = pygame.font.SysFont() #font system

'''--------------------------GameLoop--------------------------'''
### Loop which runs until exit=True, forms basis of what happens in game ###

while not Exit:

    # Control the rate at which game run --> framerate set to 60fps #
    clock.tick(60)

    '''--------------------------Logic--------------------------'''
    ### Process Main Events and Logic ###
    for event in pygame.event.get():
        if event.type == QUIT:
            Exit = True
        elif event.type == USEREVENT + 1: #demonstrates the use of a user event
            pygame.time.set_timer(USEREVENT + 1, 0)

    # Player input - this can be received from any file that imports pygame
    pressed = pygame.key.get_pressed() # gets a list of pressed keys
    mouse_x, mouse_y = pygame.mouse.get_pos() #gets the mouse coordinates
    
    if pygame.mouse.get_pressed() == (1, 0, 0): #mouse left click
        pass

    #bulletgroup.update()
    #spaceship.update()

    '''--------------------------Drawing--------------------------'''
    # Refreshing screen every time loop run #
    screen.fill((0, 0, 0))
    #screen.blit(background, (0,0)) #blit command can be used to show any image. The top left coordinate of the image is used for placement
    #spaceship.draw(screen) #Sprite draw function called
    #bulletgroup.draw(screen) #All Sprites in Group draw function called

    pygame.display.flip() #flips off screen rendering with on screen rendering
    
'''----------------Exits the game-------------'''
print("Exiting")
pygame.quit()
sys.exit(0)


