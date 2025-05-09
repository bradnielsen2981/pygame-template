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
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.angle = 0

    def update(self, pressed):
        if pressed[pygame.K_a]:
            self.rect.x -= self.speed
        if pressed[pygame.K_d]:
            self.rect.x += self.speed
        boundary = GAME.SCREEN.get_rect()
        is_outside = GAME.is_sprite_outside_rectangle(self, boundary, wrap=False, align=True)
        return
    
    def draw(self):
        GAME.SCREEN.blit(self.image, self.rect)
        return
    
