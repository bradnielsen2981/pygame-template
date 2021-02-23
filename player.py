import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__() #call the init function of the Sprite
        self.image = pygame.image.load("ninja.png")
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        return
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return

    def update(self, pressed):
        if pressed[pygame.K_UP] == 1:
            self.rect.y = self.rect.y - 3
        if pressed[pygame.K_DOWN] == 1:
            self.rect.y = self.rect.y + 3
        if pressed[pygame.K_LEFT] == 1:
            self.rect.x = self.rect.x - 3
        if pressed[pygame.K_RIGHT] == 1:
            self.rect.x = self.rect.x + 3
        return           

