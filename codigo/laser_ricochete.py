import pygame
from laser_alien import LaserAlien

class LaserRicochete(LaserAlien):
    
    def __init__(self, pos, speed, altura_tela):
        super().__init__(pos, speed, altura_tela)
        self.__image = pygame.Surface((4,20))
        self.__image = pygame.image.load('../imagens/ProjetilEnemy_ricochete.png')

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
        if self.speed > 0 and self.rect.y >= self.restricao_altura + 70:
            self.speed *= -1
        elif self.speed < 0 and self.rect.y <= -50:
            self.kill()
    
    def update(self) -> None:
        self.rect.y += self.speed
        return super().update()