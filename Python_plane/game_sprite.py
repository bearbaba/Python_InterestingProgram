import pygame
class GameSprite(pygame.sprite.Sprite):
    def __init__(self,img,speed=1):
        super().__init__()
        self.image=self.image.load(img)
        self.speed=speed
        self.rect=self.image.get_rect()
    def update(self, *args):
        self.rect.y+=self.speed

