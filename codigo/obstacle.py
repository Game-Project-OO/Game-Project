import pygame
import random

class Meteoro(pygame.sprite.Sprite):
    def __init__(self,x,valor_rotacao):
        super().__init__()
        self.imagem_original = pygame.image.load("../imagens/asteroid.png").convert_alpha()
        self.largura_base = self.imagem_original.get_width()
        self.altura_base = self.imagem_original.get_height()

        self.escala = random.uniform(1.0, 1.75)

        nova_largura = int(self.largura_base * self.escala)
        nova_altura = int(self.altura_base * self.escala)

        self.imagem_redimensionada = pygame.transform.scale(self.imagem_original, (nova_largura, nova_altura))

        self.image = self.imagem_redimensionada
        self.rect = self.image.get_rect(topleft = (x,-50))
        self.speed = 0.75
        self.valor_rotacao = valor_rotacao
        self.angulo = 0

    def update(self):
        self.rect.y += self.speed

        self.angulo = (self.angulo + self.valor_rotacao) % 360

        self.image = pygame.transform.rotate(self.imagem_redimensionada,self.angulo)
        self.rect = self.image.get_rect(center=self.rect.center)