''' Spaceship Sprite Code '''
import pygame
from laser import Laser
import game_globals as GAME
import math, time

#Sprite Object for the Space Ship
class Player(pygame.sprite.Sprite): ##Q what does sprite class mean?

    # Constructing the player
    def __init__(self, x, y):
        super().__init__() 
        
        # Sprite Image
        self.image = pygame.image.load("images/robotsprite.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.originalimage = self.image.copy() #need original image to rotate

        # Sprite Movement
        self.vspeed = 0
        self.hspeed = 0
        self.speedlimit = 5
        self.friction = 0.1
        self.gravity = 0.1

        self.invincible = False

        # health
        self.health = 100
        self.on_platform = False

        # Sprite Positioning
        self.rect = self.image.get_rect() # gets rectangle of the image #
        self.rect.center = (x,y)
        
        self.last_shoot_time = 0 #used to stop machine gun effect
        return
    
    # draw the sprite
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        return
    
        # Updates the sprite every frame
    def update(self, pressed, mouse_pos, mouse_buttons):
        # Apply movement
        self.rect.centerx += self.hspeed
        self.rect.centery += self.vspeed

        self.on_platform = False  # Start assuming we're not on a platform

        for platform in GAME.PLATFORM_GROUP:
            if self.rect.colliderect(platform.rect):
                cliprect = self.rect.clip(platform.rect)

                if cliprect.width < cliprect.height:
                    # Horizontal collision
                    if self.rect.centerx < platform.rect.centerx:
                        self.rect.right = platform.rect.left
                    else:
                        self.rect.left = platform.rect.right
                    self.hspeed = 0
                else:
                    # Vertical collision
                    if self.rect.centery < platform.rect.centery:
                        self.rect.bottom = platform.rect.top
                        self.vspeed = 0
                        self.on_platform = True
                    else:
                        self.rect.top = platform.rect.bottom
                        self.vspeed = 0

        # Check if the sprite is just above a platform (used for jump checks)
        if not self.on_platform:
            test_rect = self.rect.copy()
            test_rect.y += 1  # Just below feet
            for platform in GAME.PLATFORM_GROUP:
                if test_rect.colliderect(platform.rect):
                    self.on_platform = True
                    break

        # Jumping and gravity
        if pressed[pygame.K_w] and self.on_platform:
            self.vspeed = -5
        elif not self.on_platform:
            self.vspeed += self.gravity

        # Horizontal movement
        if pressed[pygame.K_a]:
            self.hspeed = -5
        elif pressed[pygame.K_d]:
            self.hspeed = 5
        else:
            # Apply friction
            if abs(self.hspeed) > 0:
                self.hspeed -= self.friction * (self.hspeed / abs(self.hspeed))
                if abs(self.hspeed) < 0.1:
                    self.hspeed = 0

        # Keep sprite within screen bounds (wrap around)
        screen_rect = pygame.Rect((0, 0), GAME.SCREEN.get_size())
        GAME.is_sprite_outside_rectangle(self, screen_rect, wrap=True)

        # Cap falling speed
        if self.vspeed > 10:
            self.vspeed = 10