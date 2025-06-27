import pygame, os
from powerup import Powerup

class Cura(Powerup):
    def __init__(self, x, y):
        super().__init__(x, y,'../imagens/coracao_boost.png')
        self.__valor_efeito = 1
        self.__duracao = 0

    @property
    def valor_efeito(self):
        return self.__valor_efeito
    
    @valor_efeito.setter
    def valor_efeito(self, value):
        self.__valor_efeito = value

    @property
    def duracao(self):
        return self.__duracao
    
    @duracao.setter
    def set_duracao(self, value):
        self.__duracao = value

    def efeito(self, player) -> None:
        if player.vidas != 5:
            player.vidas += self.valor_efeito
        return super().efeito(player) 
    
    def update(self) -> any:
        self.rect.y += 2
        self.destruir()
        return super().update()
    
    def destruir(self) -> None:
        return super().destruir()
