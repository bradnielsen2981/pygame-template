#Create a spaceship object that will be used to shoot the aliens
import pygame
import game_globals as GAME

# This class inherits from the pygame sprite class
class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.speed = 5
        self.image = pygame.image.load("images/alien.png")
        self.image.convert_alpha() # transparent background
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.angle = 0
        GAME.ENEMY_GROUP.add(self)

    def update(self):
        self.rect.x += self.speed
        if GAME.is_sprite_outside_rectangle(self, GAME.SCREEN.get_rect(), align=True):
            self.speed *= 1.2
            self.speed = -self.speed
            self.rect.y += 80
            if self.rect.y > GAME.SCREEN.get_height():
                self.kill()
    
    def draw(self):
        GAME.SCREEN.blit(self.image, self.rect)
        return
    
