import pygame
from powerup import Powerup

class Shield(Powerup):

    def __init__(self, x, y):
        super().__init__(x, y,'../imagens/shield_menor.png')
        self.image = pygame.Surface((4,20))
        self.image = pygame.image.load('../imagens/shield_menor.png')
        self.__effect_value = 0
        self.__duration = 5000

    def efeito(self, player):
        player.apply_pu("shield", self.effect_value, self.duration)
        return super().efeito(player)
    
    @property
    def duration(self):
        return self.__duration
    @duration.setter
    def duration(self, value):
        self.__duration = value
    @property
    def effect_value(self):
        return self.__effect_value
    @effect_value.setter
    def effect_value(self, value):
        self.__effect_value = value

    def update(self):
        self.rect.y += 2
        self.destruir()
        return super().update()
    
    def destruir(self):
        return super().destruir()