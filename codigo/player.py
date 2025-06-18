import pygame
from laser import Laser

class Jogador(pygame.sprite.Sprite):
    def __init__(self,pos,restricao,speed):
        super().__init__()
        self.image = pygame.image.load('../imagens/player.png').convert_alpha()
        self.imageFrente = pygame.image.load('../imagens/player.png').convert_alpha()
        self.imageDir = pygame.image.load('../imagens/player_dir.png').convert_alpha()
        self.imageEsq = pygame.image.load('../imagens/player_esq.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)
        self.speed = speed
        self.max_x_restricao = restricao
        self.ready = True
        self.shoot_sound = pygame.mixer.Sound('../sons/shoot_sound.mp3')
        self.laser_time = 0
        self.laser_cooldown = 600

        self.lasers = pygame.sprite.Group()

    #inputs
    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.image = pygame.transform.rotate(self.imageDir,355)
            self.rect = self.image.get_rect(center=self.rect.center)
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.image = pygame.transform.rotate(self.imageEsq,5)
            self.rect = self.image.get_rect(center=self.rect.center)
        if not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
            self.image = self.imageFrente
        
        if keys[pygame.K_SPACE] and self.ready:
            self.shoot_laser()
            self.shoot_sound.set_volume(0.1)
            self.shoot_sound.play()
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