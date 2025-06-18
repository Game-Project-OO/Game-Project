import pygame, sys
from player import Jogador
import obstacle
from alien import Alien
from random import choice
import random
from laser import Laser
from var_globais import *
#from alien_spawn import SpawnAlien

class Jogo:
    def __init__(self):
        #setup do jogador
        player_sprite = Jogador((screen_width / 2,screen_height),screen_width,5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        #vida e pontuação
        self.__vidas = 3
        self.__vida_imagem = pygame.image.load('../imagens/heart.png').convert_alpha()
        self.__vida_x_posicao = screen_width - (self.vida_imagem.get_size()[0] * 3 + 20)
        self.__score = 0
        self.__font = pygame.font.Font('../fonte/Pixeled.ttf',20)

        #setup do obstaculo
        self.__shape = obstacle.shape
        self.__block_size = 6
        self.__blocks = pygame.sprite.Group()
        self.__quantidade_de_obstaculos = 4
        self.posicao_x_obstaculos = [num * (screen_width / self.quantidade_de_obstaculos) for num in range(self.quantidade_de_obstaculos)]
        self.criar_multiplos_obstaculos(*self.posicao_x_obstaculos, x_start = screen_width / 15, y_start = 600)
    
        #setup do alien
        self.__aliens = pygame.sprite.Group()
        self.__alien_direction = 1
        self.__alien_lasers = pygame.sprite.Group()

        #criacao dos padroes de aliens
        self.padroes()

    @property
    def vidas(self):
        return self.__vidas
    
    @vidas.setter
    def vidas(self, value):
        self.__vidas = value

    @property
    def vida_imagem(self):
        return self.__vida_imagem
    
    @vida_imagem.setter
    def vida_imagem(self, value):
        self.__vida_imagem = value

    @property
    def vida_x_posicao(self):
        return self.__vida_x_posicao
    
    @vida_x_posicao.setter
    def vida_x_posicao(self, value):
        self.__vida_x_posicao = value

    @property
    def score(self):
        return self.__score
    
    @score.setter
    def score(self, value):
        self.__score = value

    @property
    def font(self):
        return self.__font
    
    @font.setter
    def font(self, value):
        self.__font = value

    @property
    def shape(self):
        return self.__shape
    
    @shape.setter
    def shape(self, value):
        self.__shape = value

    @property
    def block_size(self):
        return self.__block_size
    
    @block_size.setter
    def block_size(self, value):
        self.__block_size = value

    @property
    def blocks(self):
        return self.__blocks
    
    @blocks.setter
    def blocks(self, value):
        self.__blocks = value

    @property
    def quantidade_de_obstaculos(self):
        return self.__quantidade_de_obstaculos
    
    @quantidade_de_obstaculos.setter
    def quantidade_de_obstaculos(self, value):
        self.__quantidade_de_obstaculos = value

    @property
    def aliens(self):
        return self.__aliens
    
    @aliens.setter
    def aliens(self, value):
        self.__aliens = value

    @property
    def alien_direction(self):
        return self.__alien_direction
    
    @alien_direction.setter
    def alien_direction(self, value):
        self.__alien_direction = value

    @property
    def alien_lasers(self):
        return self.__alien_lasers
    
    @alien_lasers.setter
    def alien_lasers(self, value):
        self.__alien_lasers = value

    #cria um obstaculo
    def criar_obstaculo(self, x_start, y_start,offset_x):
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col =='x':
                    x = x_start + col_index * self.block_size + offset_x
                    y = y_start + row_index * self.block_size
                    block = obstacle.Bloco(self.block_size,(241,79,80),x,y)
                    self.blocks.add(block)

    #cria multiplos obstaculos com um espaçamento entre eles, necessita da função anterior ^^^
    def criar_multiplos_obstaculos(self,*offset,x_start,y_start):
        for offset_x in offset:
            self.criar_obstaculo(x_start,y_start,offset_x)

    def alien_position_checker(self):
        all_aliens = self.aliens.sprites()
        for alien in all_aliens:
            if alien.rect.right >= screen_width:
                self.alien_direction = -1
            elif alien.rect.left <= 0:
                self.alien_direction = 1

    def alien_shoot(self):
        if self.aliens.sprites():
            random_alien = choice(self.aliens.sprites())
            laser_sprite = Laser(random_alien.rect.center,6,screen_height)
            self.alien_lasers.add(laser_sprite)

    def obter_inimigo(self):
        tipo = random.choices(['comum','incomum','raro','lendario'], weights=[75,15,9.5,0.5], k=1)[0]

        if tipo == 'comum':
            return 'enemy'
        elif tipo == 'incomum':
            return 'enemy_blue'
        elif tipo == 'raro':
            return 'enemy_red'

    def padroes(self,rows=3,y_distance=100,x_offset=60,y_offset=-250):
        posicao_x_alien = [num * ((screen_width - 2 * x_offset) / 7) for num in range(7)]
        
        #par é impar e impar é par, enfim, a hipocrisia
        padroes_disponiveis = {
            1: {'par': [1,3,5], 'impar': [0,2,4,6]},
            2: {'par': [0,3,6], 'impar': [1,2,4,5]},
            3: {'par': [1,2,4,5], 'impar': [0,3,6]},
            4: {'par': [1,3,5], 'impar': [1,3,5]},
            5: {'par': [], 'impar': [0,2,3,4,6]},
            6: {'par': [], 'impar': [1,3,5]},
            'lendaria': {'par': [], 'impar': [0,1,2,4,5,6]}
        }

        selecionador_de_padrao_2000 = random.choices([1,2,3,4,5,6,'lendaria'], weights=[15.83,15.83,15.83,15.83,15.83,15.83,5.02], k=1)[0]

        definir_padrao = padroes_disponiveis.get(selecionador_de_padrao_2000,padroes_disponiveis[1])

        for row_index in range(rows):
            padrao_atual = definir_padrao['par'] if row_index % 2 == 0 else definir_padrao['impar']

            for col_index in range(7):
                if col_index in padrao_atual:
                    continue

                x = posicao_x_alien[col_index]
                y = row_index * y_distance + y_offset

                alien_sprite = self.obter_inimigo()
                alien_type = Alien(alien_sprite,x,y)

                alien_type.define_alvo_y(y + 290)
                self.aliens.add(alien_type)

    def checar_colisao(self):
        #player laser
        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:
                #colisão com obstáculo
                if pygame.sprite.spritecollide(laser,self.blocks,False):
                    laser.kill()

                #colisão com alien
                aliens_hit = pygame.sprite.spritecollide(laser,self.aliens,True)
                if aliens_hit:
                    for alien in aliens_hit:
                        self.score += alien.value
                    laser.kill()
        
        #alien laser
        if self.alien_lasers:
            for laser in self.alien_lasers:
                #colisão com obstáculo
                if pygame.sprite.spritecollide(laser,self.blocks,False):
                    laser.kill()

                if pygame.sprite.spritecollide(laser,self.player,False):
                    laser.kill()
                    self.vidas -= 1
                    if self.vidas <= 0:
                        pygame.quit()
                        sys.exit()

            
        #aliens
        if self.aliens:
            for alien in self.aliens:
                if pygame.sprite.spritecollide(alien,self.player,False):
                    pygame.quit()
                    sys.exit()

    def mostrar_vidas(self):
        for vida in range(self.vidas):
            x = self.vida_x_posicao + (vida * self.vida_imagem.get_size()[0] + 10)
            screen.blit(self.vida_imagem,(x,8))

    def mostrar_score(self):
        score_imagem = self.font.render(f'score: {self.score}',False,'white')
        score_rect = score_imagem.get_rect(topleft = (10,-10))
        screen.blit(score_imagem,score_rect)

    #desenha e atualiza todos os sprites
    def rodar(self):
        self.player.update()
        self.alien_lasers.update()

        self.aliens.update(self.alien_direction)
        self.alien_position_checker()
        self.checar_colisao()

        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)
        self.blocks.draw(screen)
        self.aliens.draw(screen)
        self.alien_lasers.draw(screen)

        self.mostrar_vidas()
        self.mostrar_score()

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((screen_width,screen_height))
    clock = pygame.time.Clock()
    game = Jogo()

    ALIENLASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIENLASER,800)

    SPAWN_ALIEN = pygame.USEREVENT + 2
    pygame.time.set_timer(SPAWN_ALIEN,30000)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == ALIENLASER:
                game.alien_shoot()
            if event.type == SPAWN_ALIEN:
                print("Mais aliens chegando...")

        screen.fill((30,30,30))
        game.rodar()

        pygame.display.flip()
        clock.tick(60)