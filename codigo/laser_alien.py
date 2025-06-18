import pygame
from laser import Laser

class LaserAlien(Laser):
    def __init__(self, pos, speed, screen_height):
        super().__init__(pos, speed, screen_height)
        self.image = pygame.Surface((4,20))
        self.image = pygame.image.load('../imagens/ProjetilEnemy.png')

    def destroy(self):
        return super().destroy()
    
    def update(self):
        return super().update()