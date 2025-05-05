#Create a spaceship object that will be used to shoot the aliens
import pygame
import game_globals as GAME

# This class inherits from the pygame sprite class
class Spaceship(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.speed = 5
        self.image = pygame.image.load("images/spaceship.png")
        self.image.convert_alpha() # transparent background
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, pressed):
        if pressed[pygame.K_LEFT]:
            self.rect.x -= self.speed
        return
    
    def draw(self):
        GAME.SCREEN.blit(self.image, self.rect)
        return
    
