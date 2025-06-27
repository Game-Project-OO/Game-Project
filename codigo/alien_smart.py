import pygame
from alien import Alien
from jogador import Jogador

class AlienSmart(Alien):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        self.__fator_perseguicao = 0.05
        self.__vidas = 3

        if image == 'inimigo_verde':
            self.valor = 500
    
    @property
    def fator_perseguicao(self):
        return self.__fator_perseguicao

    @fator_perseguicao.setter
    def fator_perseguicao(self, value):
        self.__fator_perseguicao = value

    @property
    def vidas(self):
        return self.__vidas

    @vidas.setter
    def vidas(self, value):
        self.__vidas = value

    def moveset(self,pos_x_player) -> None:
        diferenca_x = pos_x_player - self.rect.centerx
        self.rect.x += diferenca_x * self.fator_perseguicao

    def update(self,pos_x_player) -> None:
        if self.rect.y != self.alvo_y:
            if self.rect.y == self.alvo_y - 290:
                self.rect.x += 70
            if self.rect.y < self.alvo_y:
                self.rect.y += self.velocidade
            elif self.rect.y == self.alvo_y:
                self.rect.y = self.rect.y
        
        self.moveset(pos_x_player)