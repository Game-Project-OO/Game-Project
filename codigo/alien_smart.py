import pygame
from alien import Alien
from player import Jogador

class AlienSmart(Alien):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        self.fator_perseguicao = 0.05
        self.vidas = 3

        if image == 'enemy_green':
            self.value = 500
    
    def moveset(self, posxPlayer):
        diferencax = posxPlayer - self.rect.x
        self.rect.x += diferencax * self.fator_perseguicao