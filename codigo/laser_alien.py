import pygame
from laser import Laser

class LaserAlien(Laser):
    def __init__(self, pos, speed, altura_tela):
        super().__init__(pos, speed, altura_tela)
        self.__image = pygame.Surface((4,20))
        self.__image = pygame.image.load('../imagens/ProjetilEnemy.png')

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, value):
        self.__image = value

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, value):
        self.__image = value

    def destroy(self) -> None:
        return super().destroy()
    
    def update(self) -> None:
        return super().update()