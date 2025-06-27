import pygame
from alien import Alien

class AlienKamikaze(Alien):

    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        self.__fator_perseguicao = 0.0092
        
        if image == 'inimigo_roxo':
            self.valor = 700
    
    @property
    def fator_perseguicao(self):
        return self.__fator_perseguicao

    @fator_perseguicao.setter
    def fator_perseguicao(self, value):
        self.__fator_perseguicao = value
    
    def moveset(self, pos_x_player, pos_y_player) -> None:
        diferenca_x = pos_x_player - self.rect.x
        self.rect.x += diferenca_x * self.fator_perseguicao

        diferenca_y = pos_y_player - self.rect.y
        self.rect.y += diferenca_y * self.fator_perseguicao
    
    def update(self, pos_x_player, pos_y_player) -> None:
        self.moveset(pos_x_player, pos_y_player)