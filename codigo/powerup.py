import pygame, os
from abc import ABC, abstractmethod

class Powerup(ABC,pygame.sprite.Sprite):

    def __init__(self, x, y, imagePath):
        super().__init__()
        self.__image = pygame.image.load(imagePath).convert_alpha()
        self.__rect = self.image.get_rect(topleft=(x,y))
        

    @property
    def image(self):
        return self.__image
    @image.setter
    def image(self, value):
        self.__image = value
    @property
    def rect(self):
        return self.__rect
    @rect.setter
    def rect(self, value):
        self.__rect = value

    def efeito(self, player):
        pass

    def destruir(self):
        if self.rect.y <= 50:
            self.kill()

    def pup_update(self):
        self.rect.y -= 2