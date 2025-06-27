import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self,pos,speed,altura_tela):
        super().__init__()
        self.__image = pygame.Surface((4,20))
        self.__image = pygame.image.load('../imagens/projetilPlayer.png')
        self.__rect = self.__image.get_rect(center = pos)
        self.__speed = speed
        self.__restricao_altura = altura_tela

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, value):
        self.__image = value

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, value):
        self.__rect = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.__speed = value

    @property
    def restricao_altura(self):
        return self.__restricao_altura

    @restricao_altura.setter
    def restricao_altura(self, value):
        self.__restricao_altura = value


    #destroi o projetil ao sair do limite da tela, evita lag!
    def destroy(self) -> None:
        if self.rect.y <= -50 or self.rect.y >= self.restricao_altura + 50:
            self.kill()
    
    def update(self) -> None:
        self.rect.y += self.speed
        self.destroy()