import pygame, os
from powerup import Powerup

class Heal(Powerup):
    def __init__(self, x, y):
        super().__init__(x, y,'../imagens/heart_plus.png')
        self.__effect_value = 1
        self.__duration = 0

    @property
    def effect_value(self):
        return self.__effect_value
    @effect_value.setter
    def effect_value(self, value):
        self.__effect_value = value
    @property
    def duration(self):
        return self.__duration
    @duration.setter
    def set_duration(self, value):
        self.__duration = value

    def efeito(self, player):
        if player.vidas != 5:
            player.vidas += self.effect_value
        return super().efeito(player) 
    
    def update(self):
        self.rect.y += 2
        self.destruir()
        return super().update()
    
    def destruir(self):
        return super().destruir()
