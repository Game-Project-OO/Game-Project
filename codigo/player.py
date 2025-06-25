import pygame
from laser import Laser

class Jogador(pygame.sprite.Sprite):
    def __init__(self,pos,restricao,speed):
        super().__init__()
        self.image = pygame.image.load('../imagens/player.png').convert_alpha()
        self.imageFrente = pygame.image.load('../imagens/player.png').convert_alpha()
        self.imageDir = pygame.image.load('../imagens/player_dir.png').convert_alpha()
        self.imageEsq = pygame.image.load('../imagens/player_esq.png').convert_alpha()
        self.imageEscudoFrente = pygame.image.load('../imagens/player_shield.png').convert_alpha()
        self.imageEscudoDir = pygame.image.load('../imagens/playerdir_shield.png').convert_alpha()
        self.imageEscudoEsq = pygame.image.load('../imagens/playeresq_shield.png').convert_alpha()

        #Checagem para os power ups 
        self.vidas = 3
        self.shield = 0 
        self.pu_active = None
        self.pu_start = 0
        self.pu_end = 0 
        self.true_speed = speed

        self.rect = self.image.get_rect(midbottom = pos)
        self.speed = speed
        self.max_x_restricao = restricao
        self.ready = True
        self.shoot_sound = pygame.mixer.Sound('../sons/shoot_sound.mp3')
        self.laser_time = 0
        self.laser_cooldown = 600
        self.coconut = self.true_speed

        self.lasers = pygame.sprite.Group()

    #aplicar o efeito
    def apply_pu(self, tipo, valor_efeito, duracao):
        
        if self.pu_active is not None:
            self.remove()

        if tipo == "heal":
            self.vidas += valor_efeito
            if self.vidas > 5:
                self.vidas = 5
        elif tipo == "shield":
            self.shield = 1
            self.image = self.imageEscudoFrente
        elif tipo == "speed":
            self.true_speed *= valor_efeito
            self.speed = self.true_speed

        self.pu_active = {"tipo": tipo, "valor_efeito": valor_efeito, "duracao": duracao, "inicio": pygame.time.get_ticks()}


    #remover efeito
    def remove_pu(self):
        if self.pu_active:
            if self.pu_active["tipo"] == "shield":
                self.shield = 0
                self.image = self.imageFrente
            elif self.pu_active["tipo"] == "speed":
                self.speed = self.coconut
        self.pu_active = None


    #inputs
    def get_input(self):
        keys = pygame.key.get_pressed()

        if self.shield == 1:
            if keys[pygame.K_RIGHT]:
                self.rect.x += self.speed
                self.image = self.imageEscudoDir
            if keys[pygame.K_LEFT]:
                self.rect.x -= self.speed
                self.image = self.imageEscudoEsq
            if not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
                self.image = self.imageEscudoFrente

        else:
            if keys[pygame.K_RIGHT]:
                self.rect.x += self.speed
                self.image = self.imageDir
            if keys[pygame.K_LEFT]:
                self.rect.x -= self.speed
                self.image = self.imageEsq
            if not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
                self.image = self.imageFrente

        if keys[pygame.K_SPACE] and self.ready:
            self.shoot_laser()
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
        #checar se o power up ainda está ativo...
        if self.pu_active:
            tempo_atual = pygame.time.get_ticks()
            if tempo_atual - self.pu_active["inicio"] >= self.pu_active["duracao"]:
                self.remove_pu()