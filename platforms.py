import pygame
import game_globals as GAME

class Platform(pygame.sprite.Sprite):
    def __init__(self, position, width, height):

        super().__init__()  #need to call the super constructor to work with Groups

        self.image = pygame.Surface((width, height))
        self.image.fill((200, 10, 10))  # Green color
        self.rect = self.image.get_rect(center=position)
        self.position = position
        GAME.PLATFORM_GROUP.add(self)  # Add the platform to the global platform group
        return

    #moving platform?
    def update(self):
        #self.rect.y += 1 #make the platforms move

        if self.rect.y > 768:
            self.kill()
        return
    

