import pygame
from alien import Alien
from var_globais import *

class SpawnAlien(Alien):
    def __init__(self):
        pass

    ''' x_offset = posicao do alien em relação a borda da tela
        y_ofsset =  ^^^^^^^^^^^
        x_distance = not defined
        y_distance = distancia entre 1 alien e outro no eixo y
    '''

    def padrao_1(self,group,rows=3,cols=6,y_distance=100,x_offset=60,y_offset=-250):
        posicao_x_alien = [num * ((screen_width - 2 * x_offset) / cols) for num in range(cols)]
        for row_index in range(rows):
            for col_index in range(cols):
                x = posicao_x_alien[col_index]
                y = row_index * y_distance + y_offset

                if row_index == 0: 
                    alien_sprite = Alien('enemy_red',x,y)
                elif row_index == 1:
                    alien_sprite = Alien('enemy_blue',x,y)
                else:
                    alien_sprite = Alien('enemy',x,y)

                alien_sprite.define_alvo_y(y + 290)
                group.add(alien_sprite)