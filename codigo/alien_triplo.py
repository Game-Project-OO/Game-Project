import pygame
from alien import Alien

class AlienTriplo(Alien):
    
    def __init__(self, image, x, y):
        super().__init__(image, x, y)

        if image == 'enemy_red':
            self.value = 300
    
    def define_alvo_y(self, novo_y):
        return super().define_alvo_y(novo_y)
    
    def update(self, direction):
        return super().update(direction)