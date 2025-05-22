''' Main Game Code '''
print('\33c')
import pygame
import pygame.locals as CONSTANTS
import os, sys, random, time, math
import game_globals as GAME
from spaceship import Spaceship #when you from - you skip using the namespace
from enemy import Enemy

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

GAME.ENEMY_GROUP = pygame.sprite.Group() # Create a group for enemies
GAME.LASER_GROUP = pygame.sprite.Group() # Create a group for lasers
GAME.SCREEN = pygame.display.get_surface() # Where graphics/visual output displayed #
GAME.EXIT = False
GAME.STATE = "Start Game" 
GAME.MUSIC = pygame.mixer.Sound("sounds/sunsetreverie.mp3")
GAME.LASERSOUND = pygame.mixer.Sound("sounds/laser.mp3")

create_enemy_event = pygame.USEREVENT + 1 # Create a custom event for creating enemies
restart_event = pygame.USEREVENT + 2 # Create a custom event for

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
        if event.type == create_enemy_event:
            enemy = Enemy(0, 0)
        if event.type == restart_event:
            GAME.STATE = "Start Game"
            GAME.ENEMY_GROUP.empty()
            pygame.time.set_timer(restart_event, 0)

    # Collect user input
    pressed = pygame.key.get_pressed() #returns []
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos()) # returns (x,y)
    mouse_buttons = pygame.mouse.get_pressed() # return (0, 0, 0) if left button click

    GAME.SCREEN.blit(BACKGROUND_IMAGE, (0,0)) #top left image
    #GAME.SCREEN.fill((0, 0, 255)) RGB 

    if GAME.STATE == "Start Game":
        start_text = FONT2.render("Press Enter to Start Game", True, (255, 0, 0))
        GAME.SCREEN.blit(start_text, (200,300))

        if pressed[pygame.K_RETURN]:
            GAME.STATE = "Running"
            GAME.STARTTIME = time.time()
            GAME.PLAYER = Spaceship(512, 530) #CREATES OUR SPACESHIP OBJECT
            pygame.time.set_timer(create_enemy_event, 1000) #create a looping time
            GAME.MUSIC.play(-1) #play music in a loop

    elif GAME.STATE == "Running":
        
        GAME.PLAYER.update(pressed) #update player position
        GAME.LASER_GROUP.update() #update all lasers
        GAME.ENEMY_GROUP.update()

        #check for collision between lasers and enemies
        collided = pygame.sprite.groupcollide(GAME.LASER_GROUP, GAME.ENEMY_GROUP, True, True)
        #for each enemy collided add to score
        for laser, enemies in collided.items():
            for enemy in enemies:
                GAME.SCORE += 1

        GAME.PLAYER.draw()
        GAME.LASER_GROUP.draw(GAME.SCREEN) #draw all lasers
        GAME.ENEMY_GROUP.draw(GAME.SCREEN)

        #mouse_text = FONT.render("X: " + str(mouse_pos[0]) + " Y: " + str(mouse_pos[1]),True,(255,0,0))
        #GAME.SCREEN.blit(mouse_text,(10,10))

        time_text = FONT.render("Time: " + str(int(time.time() - GAME.STARTTIME)),True,(255,0,0))
        GAME.SCREEN.blit(time_text,(10,10))

        score_text = FONT.render("Score: " + str(GAME.SCORE),True,(255,255,0))
        GAME.SCREEN.blit(score_text,(10,50))
    
    elif GAME.STATE == "Game Over":
        #print text saying game over
        end_text = FONT2.render("Game Over", True, (255, 0, 0))
        GAME.SCREEN.blit(end_text, (200,300))
        pygame.time.set_timer(restart_event, 3000)

        GAME.MUSIC.stop()


    pygame.display.flip() #all drawing that was done off screen is now flipped onto the screen
    
'''------------------------ Exit --------------------------------'''
print("Exiting")
pygame.quit()
sys.exit(0)


