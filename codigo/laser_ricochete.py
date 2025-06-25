import pygame
from laser_alien import LaserAlien

class LaserRicochete(LaserAlien):
    
    def __init__(self, pos, speed, screen_height):
        super().__init__(pos, speed, screen_height)
        self.image = pygame.Surface((4,20))
        self.image = pygame.image.load('../imagens/ProjetilEnemy_ricochete.png')
    
    def destroy(self):
        if self.speed > 0 and self.rect.y >= self.height_y_restricao + 70:
            self.speed *= -1
        elif self.speed < 0 and self.rect.y <= -50:
            self.kill()
    
    def update(self):
        self.rect.y += self.speed
        return super().update()