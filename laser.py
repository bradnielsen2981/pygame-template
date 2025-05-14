#Create a laser object that will be used to shoot
import pygame
import game_globals as GAME

class Laser(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((2, 10), pygame.SRCALPHA)
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 10
        self.angle = 0
        GAME.LASER_GROUP.add(self) #add the whole object to the Sprite group

    def update(self):
        self.rect.y = self.rect.y - self.speed

    def draw(self):
        GAME.SCREEN.blit(self.image, self.rect)



        
