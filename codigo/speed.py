import pygame
from powerup import Powerup

class Speed(Powerup):

    def __init__(self, x, y):
        super().__init__(x,y,'../imagens/speed_menor.png')
        self.image = pygame.Surface((4,20))
        self.image = pygame.image.load('../imagens/speed_menor.png')
        self.__effect_value = 1.5
        self.__duration = 5000

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
    def duration(self, value):
        self.__duration = value

    def efeito(self, player):
        player.apply_pu("speed", self.effect_value, self.duration)
        return super().efeito(player)

    def update(self):
        self.rect.y += 2
        self.destruir()
        return super().update()
    
    def destruir(self):
        return super().destruir()
