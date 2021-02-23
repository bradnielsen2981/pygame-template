import pygame
import random
#create a blueprint for an object
# An object is a very advanced variable 
class myrectangle(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        #self.x = x; self.y = y
        self.colour = (0,100,255)
        self.width = 50; self.height = 50
        self.hspeed = random.randint(-3,3); self.vspeed = random.randint(-3,3)

        self.image = pygame.Surface((50, 50))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x; self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return

    def update(self, dimensions):
        if (self.rect.centerx > dimensions[0]):
            self.rect.centerx = dimensions[0]
            self.hspeed = -self.hspeed
        elif (self.rect.centerx < 0):
            self.rect.centerx = 0
            self.hspeed = -self.hspeed

        if (self.rect.centery > dimensions[1]):
            self.rect.centery = dimensions[1]
            self.vspeed = -self.vspeed 
        elif (self.rect.centery < 0):
            self.rect.centery = 0
            self.vspeed = -self.vspeed 

        self.rect.x = self.rect.x + self.hspeed
        self.rect.y = self.rect.y + self.vspeed
        return