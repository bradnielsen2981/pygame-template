#Create a spaceship object that will be used to shoot the aliens
import pygame
import game_globals as GAME

# This class inherits from the pygame sprite class
class Boss(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.speed = 2
        self.image = pygame.image.load("images/alien.png")
        self.image.convert_alpha() # transparent background
        self.image = pygame.transform.scale(self.image, (80, 80))

        self.original_image = self.image.copy() # Store the original image for rotation

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.angle = 0
        self.direction = pygame.Vector2(0, 0) #change in x and change in y
        GAME.ENEMY_GROUP.add(self)

    def update(self):

        playerposition = pygame.Vector2(GAME.PLAYER.rect.center)
        self.direction = playerposition - pygame.Vector2(self.rect.center)
        self.direction = self.direction.normalize()
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

        #ROTATE - YOU MUST CREATE COPY OF THE IMAGE IN __INIT__() orginal_image = image.copy()
        self.angle = self.direction.angle_to(pygame.Vector2(0, 1))
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def draw(self):
        GAME.SCREEN.blit(self.image, self.rect)
        return
    
