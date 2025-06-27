import pygame
from var_globais import *
from laser import Laser
from random import choice

class Alien(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        super().__init__()
        file_path = '../imagens/' + image + '.png'
        self.__image = pygame.image.load(file_path).convert_alpha()
        self.__rect = self.image.get_rect(topleft=(x,y))
        self.__alvo_y = y
        self.__velocidade = 1.75

        if image == 'inimigo':
            self.valor = 100
        else:
            self.valor = 0
    
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

    @property
    def alvo_y(self):
        return self.__alvo_y

    @alvo_y.setter
    def alvo_y(self, value):
        self.__alvo_y = value

    @property
    def velocidade(self):
        return self.__velocidade

    @velocidade.setter
    def velocidade(self, value):
        self.__velocidade = value

    def define_alvo_y(self, novo_y) -> None:
        self.alvo_y = novo_y

    def update(self,direction) -> None:
        if self.rect.y != self.alvo_y:
            if self.rect.y == self.alvo_y - 290:
                self.rect.x += 70
            if self.rect.y < self.alvo_y:
                self.rect.y += self.velocidade
        else:
            self.rect.x += direction