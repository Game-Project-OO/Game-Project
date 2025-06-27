import pygame
from laser import Laser

class Jogador(pygame.sprite.Sprite):
    def __init__(self,pos,restricao,speed):
        super().__init__()
        self.__image = pygame.image.load('../imagens/player.png').convert_alpha()
        self.__image_frente = pygame.image.load('../imagens/player.png').convert_alpha()
        self.__image_dir = pygame.image.load('../imagens/player_dir.png').convert_alpha()
        self.__image_esq = pygame.image.load('../imagens/player_esq.png').convert_alpha()
        self.__image_escudo_frente = pygame.image.load('../imagens/player_escudo.png').convert_alpha()
        self.__image_escudo_dir = pygame.image.load('../imagens/playerdir_escudo.png').convert_alpha()
        self.__image_escudo_esq = pygame.image.load('../imagens/playeresq_escudo.png').convert_alpha()

        #Checagem para os power ups 
        self.__vidas = 3
        self.__escudo = 0 
        self.__powerup_ativo = None
        self.__powerup_inicio = 0
        self.__powerup_fim = 0 
        self.__true_speed = speed
        self.__vel = speed

        self.__rect = self.image.get_rect(midbottom = pos)
        self.__speed = speed
        self.__max_x_restricao = restricao
        self.__ready = True
        self.__shoot_sound = pygame.mixer.Sound('../sons/shoot_sound.mp3')
        self.__laser_tempo = 0
        self.__laser_recarga = 600

        self.__lasers = pygame.sprite.Group()

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, value):
        self.__image = value

    @property
    def image_frente(self):
        return self.__image_frente

    @image_frente.setter
    def image_frente(self, value):
        self.__image_frente = value

    @property
    def image_dir(self):
        return self.__image_dir

    @image_dir.setter
    def image_dir(self, value):
        self.__image_dir = value

    @property
    def image_esq(self):
        return self.__image_esq

    @image_esq.setter
    def image_esq(self, value):
        self.__image_esq = value

    @property
    def image_escudo_frente(self):
        return self.__image_escudo_frente

    @image_escudo_frente.setter
    def image_escudo_frente(self, value):
        self.__image_escudo_frente = value

    @property
    def image_escudo_dir(self):
        return self.__image_escudo_dir

    @image_escudo_dir.setter
    def image_escudo_dir(self, value):
        self.__image_escudo_dir = value

    @property
    def image_escudo_esq(self):
        return self.__image_escudo_esq

    @image_escudo_esq.setter
    def image_escudo_esq(self, value):
        self.__image_escudo_esq = value

    @property
    def vidas(self):
        return self.__vidas

    @vidas.setter
    def vidas(self, value):
        self.__vidas = value

    @property
    def escudo(self):
        return self.__escudo

    @escudo.setter
    def escudo(self, value):
        self.__escudo = value

    @property
    def powerup_ativo(self):
        return self.__powerup_ativo

    @powerup_ativo.setter
    def powerup_ativo(self, value):
        self.__powerup_ativo = value

    @property
    def powerup_inicio(self):
        return self.__powerup_inicio

    @powerup_inicio.setter
    def powerup_inicio(self, value):
        self.__powerup_inicio = value

    @property
    def powerup_fim(self):
        return self.__powerup_fim

    @powerup_fim.setter
    def powerup_fim(self, value):
        self.__powerup_fim = value

    @property
    def true_speed(self):
        return self.__true_speed

    @true_speed.setter
    def true_speed(self, value):
        self.__true_speed = value
    
    @property
    def vel(self):
        return self.__vel

    @vel.setter
    def vel(self, value):
        self.__vel = value

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, value):
        self.__rect = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.__speed = value

    @property
    def max_x_restricao(self):
        return self.__max_x_restricao

    @max_x_restricao.setter
    def max_x_restricao(self, value):
        self.__max_x_restricao = value

    @property
    def ready(self):
        return self.__ready

    @ready.setter
    def ready(self, value):
        self.__ready = value

    @property
    def shoot_sound(self):
        return self.__shoot_sound

    @shoot_sound.setter
    def shoot_sound(self, value):
        self.__shoot_sound = value

    @property
    def laser_tempo(self):
        return self.__laser_tempo

    @laser_tempo.setter
    def laser_tempo(self, value):
        self.__laser_tempo = value

    @property
    def laser_recarga(self):
        return self.__laser_recarga

    @laser_recarga.setter
    def laser_recarga(self, value):
        self.__laser_recarga = value

    @property
    def lasers(self):
        return self.__lasers

    @lasers.setter
    def lasers(self, value):
        self.__lasers = value

    #aplicar o efeito
    def aplicar_powerup(self, tipo, valor_efeito, duracao) -> None:
        
        if self.powerup_ativo is not None:
            self.remove()

        if tipo == "cura":
            self.vidas += valor_efeito
            if self.vidas > 5:
                self.vidas = 5
        elif tipo == "escudo":
            self.escudo = 1
            self.image = self.image_escudo_frente
        elif tipo == "velocidade":
            self.true_speed *= valor_efeito
            self.speed = self.true_speed

        self.powerup_ativo = {"tipo": tipo, "valor_efeito": valor_efeito, "duracao": duracao, "inicio": pygame.time.get_ticks()}


    #remover efeito
    def remove_powerup(self) -> None:
        if self.powerup_ativo:
            if self.powerup_ativo["tipo"] == "escudo":
                self.escudo = 0
                self.image = self.image_frente
            elif self.powerup_ativo["tipo"] == "velocidade":
                self.true_speed = self.vel  
                self.speed = self.true_speed
        self.powerup_ativo = None


    #inpowerupts
    def get_input(self) -> None:
        keys = pygame.key.get_pressed()

        if self.escudo == 1:
            if keys[pygame.K_RIGHT]:
                self.rect.x += self.speed
                self.image = self.image_escudo_dir
            if keys[pygame.K_LEFT]:
                self.rect.x -= self.speed
                self.image = self.image_escudo_esq
            if not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
                self.image = self.image_escudo_frente

        else:
            if keys[pygame.K_RIGHT]:
                self.rect.x += self.speed
                self.image = self.image_dir
            if keys[pygame.K_LEFT]:
                self.rect.x -= self.speed
                self.image = self.image_esq
            if not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
                self.image = self.image_frente

        if keys[pygame.K_SPACE] and self.ready:
            self.shoot_laser()
            self.shoot_sound.play()
            self.ready = False
            self.laser_tempo = pygame.time.get_ticks()

    #delay entre tiros do projetil do jogador
    def recarregar(self) -> None:
        if not self.ready:
            current_tempo = pygame.time.get_ticks()
            if current_tempo - self.laser_tempo >= self.laser_recarga:
                self.ready = True
    
    #função para o jogador não sair da tela
    def restricao(self) -> None:
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.max_x_restricao:
            self.rect.right = self.max_x_restricao

    #função que atira o projetil
    def shoot_laser(self) -> None:
        self.lasers.add(Laser(self.rect.center,-8,self.rect.bottom))
    
    def update(self) -> None:
        self.get_input()
        self.restricao()
        self.recarregar()
        self.lasers.update()
        #checar se o power up ainda está ativo...
        if self.powerup_ativo:
            tempo_atual = pygame.time.get_ticks()
            if tempo_atual - self.powerup_ativo["inicio"] >= self.powerup_ativo["duracao"]:
                self.remove_powerup()