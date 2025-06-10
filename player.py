import pygame
from laser import Laser

class Jogador(pygame.sprite.Sprite):
    def __init__(self,pos,restricao,speed):
        super().__init__()
        self.image = pygame.image.load('IMAGENS/player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)
        self.speed = speed
        self.max_x_restricao = restricao
        self.ready = True
        self.laser_time = 0
        self.laser_cooldown = 600

        self.lasers = pygame.sprite.Group()

    #inputs
    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pygame.K_SPACE] and self.ready:
            self.shoot_laser()
            self.ready = False
            self.laser_time = pygame.time.get_ticks()

    #delay entre tiros do projetil do jogador
    def recarregar(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_cooldown:
                self.ready = True
    
    #função para o jogador não sair da tela
    def restricao(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.max_x_restricao:
            self.rect.right = self.max_x_restricao

    #função que atira o projetil
    def shoot_laser(self):
        self.lasers.add(Laser(self.rect.center,-8,self.rect.bottom))
    
    def update(self):
        self.get_input()
        self.restricao()
        self.recarregar()
        self.lasers.update()