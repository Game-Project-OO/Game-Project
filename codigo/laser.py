import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self,pos,speed,screen_height):
        super().__init__()
        self.image = pygame.Surface((4,20))
        self.image = pygame.image.load('../imagens/projetilPlayer.png')
        self.rect = self.image.get_rect(center = pos)
        self.speed = speed
        self.height_y_restricao = screen_height

    #destroi o projetil ao sair do limite da tela, evita lag!
    def destroy(self):
        if self.rect.y <= -50 or self.rect.y >= self.height_y_restricao + 50:
            self.kill()
    
    def update(self):
        self.rect.y += self.speed
        self.destroy()