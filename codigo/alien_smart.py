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

    def moveset(self,pos_x_player):
        diferenca_x = pos_x_player - self.rect.centerx
        self.rect.x += diferenca_x * self.fator_perseguicao

    def update(self,pos_x_player):
        if self.rect.y != self.alvo_y:
            if self.rect.y == self.alvo_y - 290:
                self.rect.x += 70
            if self.rect.y < self.alvo_y:
                self.rect.y += self.speed
            elif self.rect.y == self.alvo_y:
                self.rect.y = self.rect.y
        
        self.moveset(pos_x_player)