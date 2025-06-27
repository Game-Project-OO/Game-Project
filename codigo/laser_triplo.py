import pygame
from laser_alien import LaserAlien

class LaserTriplo(LaserAlien):
    def __init__(self, pos, speed, altura_tela, speed_x):
        super().__init__(pos, speed, altura_tela)
        self.__image = pygame.Surface((4,20))
        self.__image = pygame.image.load('../imagens/ProjetilEnemy.png')
        self.__speed_x = speed_x
        self.__float_x = float(self.rect.x)

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

    @property
    def speed_x(self):
        return self.__speed_x

    @speed_x.setter
    def speed_x(self, value):
        self.__speed_x = value

    @property
    def float_x(self):
        return self.__float_x

    @float_x.setter
    def float_x(self, value):
        self.__float_x = value


    def destroy(self) -> None:
        return super().destroy()
    
    def update(self) -> None:
        self.float_x += self.speed_x
        self.rect.x = int(self.float_x)
        return super().update()