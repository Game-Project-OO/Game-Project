import pygame
from powerup import Powerup

class Velocidade(Powerup):

    def __init__(self, x, y):
        super().__init__(x,y,'../imagens/velocidade_menor.png')
        self.__image = pygame.Surface((4,20))
        self.__image = pygame.image.load('../imagens/velocidade_menor.png')
        self.__valor_efeito = 1.5
        self.__duracao = 5000

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, value):
        self.__image = value

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
    def duracao(self, value):
        self.__duracao = value

    def efeito(self, player) -> None:
        player.aplicar_powerup("velocidade", self.valor_efeito, self.duracao)
        return super().efeito(player)

    def update(self) -> any:
        self.rect.y += 2
        self.destruir()
        return super().update()
    
    def destruir(self) -> None:
        return super().destruir()
