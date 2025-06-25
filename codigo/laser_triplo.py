import pygame
from laser_alien import LaserAlien

class LaserTriplo(LaserAlien):
    def __init__(self, pos, speed, screen_height, speed_x):
        super().__init__(pos, speed, screen_height)
        self.image = pygame.Surface((4,20))
        self.image = pygame.image.load('../imagens/ProjetilEnemy.png')
        self.speed_x = speed_x
        self.float_x = float(self.rect.x)

    def destroy(self):
        return super().destroy()
    
    def update(self):
        self.float_x += self.speed_x
        self.rect.x = int(self.float_x)
        return super().update()