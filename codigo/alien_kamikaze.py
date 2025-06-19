import pygame
from alien import Alien

class AlienKamikaze(Alien):

    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        self.fator_perseguicao = 0.0092
        
        if image == 'enemy_purple':
            self.value = 700
    
    def moveset(self, pos_x_player, pos_y_player):
        diferenca_x = pos_x_player - self.rect.x
        self.rect.x += diferenca_x * self.fator_perseguicao

        diferenca_y = pos_y_player - self.rect.y
        self.rect.y += diferenca_y * self.fator_perseguicao
    
    def update(self, pos_x_player, pos_y_player):
        '''if self.rect.y != self.alvo_y:
            if self.rect.y == self.alvo_y - 290:
                self.rect.x += 70
            if self.rect.y < self.alvo_y:
                self.rect.y += self.speed
            elif self.rect.y == self.alvo_y:
                self.rect.y = self.rect.y'''
        self.moveset(pos_x_player, pos_y_player)