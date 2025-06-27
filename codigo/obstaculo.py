import pygame
import random

class Meteoro(pygame.sprite.Sprite):
    def __init__(self,x,valor_rotacao):
        super().__init__()
        self.__imagem_original = pygame.image.load("../imagens/asteroid.png").convert_alpha()
        self.__largura_base = self.imagem_original.get_width()
        self.__altura_base = self.imagem_original.get_height()
        self.__escala = random.uniform(1.0, 1.75)

        nova_largura = int(self.largura_base * self.escala)
        nova_altura = int(self.altura_base * self.escala)

        self.__imagem_redimensionada = pygame.transform.scale(self.imagem_original, (nova_largura, nova_altura))
        self.__image = self.imagem_redimensionada
        self.__rect = self.image.get_rect(topleft = (x,-50))
        self.__speed = 0.75
        self.__valor_rotacao = valor_rotacao
        self.__angulo = 0

    @property
    def imagem_original(self):
        return self.__imagem_original

    @imagem_original.setter
    def imagem_original(self, value):
        self.__imagem_original = value

    @property
    def largura_base(self):
        return self.__largura_base

    @largura_base.setter
    def largura_base(self, value):
        self.__largura_base = value

    @property
    def altura_base(self):
        return self.__altura_base

    @altura_base.setter
    def altura_base(self, value):
        self.__altura_base = value

    @property
    def escala(self):
        return self.__escala

    @escala.setter
    def escala(self, value):
        self.__escala = value
    
    @property
    def imagem_redimensionada(self):
        return self.__imagem_redimensionada

    @imagem_redimensionada.setter
    def imagem_redimensionada(self, value):
        self.__imagem_redimensionada = value

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
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.__speed = value

    @property
    def valor_rotacao(self):
        return self.__valor_rotacao

    @valor_rotacao.setter
    def valor_rotacao(self, value):
        self.__valor_rotacao = value

    @property
    def angulo(self):
        return self.__angulo

    @angulo.setter
    def angulo(self, value):
        self.__angulo = value

    def update(self) -> None:
        self.rect.y += self.speed

        self.angulo = (self.angulo + self.valor_rotacao) % 360

        self.image = pygame.transform.rotate(self.imagem_redimensionada,self.angulo)
        self.rect = self.image.get_rect(center=self.rect.center)