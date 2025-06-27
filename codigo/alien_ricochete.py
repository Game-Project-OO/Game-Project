import pygame
from alien import Alien

class AlienRicochete(Alien):
    
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        
        if image == 'inimigo_azul':
            self.valor = 200
    
    def define_alvo_y(self, novo_y) -> None:
        return super().define_alvo_y(novo_y)

    def update(self, direcao) -> None:
        return super().update(direcao)