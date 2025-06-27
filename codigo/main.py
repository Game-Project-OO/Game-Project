import pygame, sys
from jogador import Jogador
from obstaculo import Meteoro
from alien import Alien
from alien_smart import AlienSmart
from alien_kamikaze import AlienKamikaze
from alien_ricochete import AlienRicochete
from alien_triplo import AlienTriplo
from random import choice
import random
from laser import Laser
from laser_alien import LaserAlien
from laser_ricochete import LaserRicochete
from laser_triplo import LaserTriplo
from var_globais import *
from animacoes import Animacoes
from ranking import Ranking
from cura import Cura
from escudo import Escudo
from velocidade import Velocidade
from menu import *
#from alien_spawn import SpawnAlien

screen = pygame.display.set_mode((largura_tela, altura_tela))


class Jogo:
    def __init__(self):
        #setup do jogador
        jogador_sprite = Jogador((largura_tela / 2,altura_tela),largura_tela,5)
        self.__jogador = pygame.sprite.GroupSingle(jogador_sprite)
        self.__jogador_nome = ""

        #vida e pontuação
        self.__vidas = 3
        self.__vida_imagem = pygame.image.load('../imagens/coracao.png').convert_alpha()
        self.__vida_extra_imagem = pygame.image.load('../imagens/coracao_boost.png').convert_alpha()
        self.__vida_x_posicao = largura_tela - (self.__vida_imagem.get_size()[0] * 3 + 20)
        self.__pontuacao = 0
        self.__font = pygame.font.Font(fonte,20)

        #setup do obstaculo
        self.__meteoro = pygame.sprite.Group()
    
        #setup do alien
        self.__aliens = pygame.sprite.Group()
        self.__alien_direction = 1
        self.__alien_lasers = pygame.sprite.Group()
        
        self.__alien_ricochete = pygame.sprite.Group()
        self.__alien_ricochete_lasers = pygame.sprite.Group()

        self.__aliens_triplo = pygame.sprite.Group()
        self.__aliens_triplo_lasers = pygame.sprite.Group()

        self.__aliens_smart = pygame.sprite.Group()
        self.__aliens_smart_lasers = pygame.sprite.Group()
        self.__aliens_smart_spawned = False

        self.__aliens_kamikaze = pygame.sprite.Group()
        self.__aliens_kamikaze_spawned = False

        self.__trilha_sonora = pygame.mixer.Sound('../sons/gameplay_sound.mp3')
        self.__som_morte = pygame.mixer.Sound('../sons/som_morte.mp3')
        self.__contagem = 0 #contagem para verificar quando o alien smart é atingido
        self.__fundo = pygame.transform.scale(pygame.image.load('../imagens/fundo.png').convert(), (largura_tela, altura_tela))

        self.__powerups = pygame.sprite.Group()
        #criacao dos padroes de aliens
        self.recarga_spawn_inimigo = 5000

        #setup de animações
        self.animacao = Animacoes()

    @property
    def jogador(self):
        return self.__jogador

    @jogador.setter
    def jogador(self, value):
        self.__jogador = value

    @property
    def jogador_nome(self):
        return self.__jogador_nome

    @jogador_nome.setter
    def jogador_nome(self, value):
        self.__jogador_nome = value

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
    def vida_extra_imagem(self):
        return self.__vida_extra_imagem
    
    @vida_extra_imagem.setter
    def vida_extra_imagem(self, value):
        self.vida_extra_imagem = value

    @property
    def vida_x_posicao(self):
        return self.__vida_x_posicao
    
    @vida_x_posicao.setter
    def vida_x_posicao(self, value):
        self.__vida_x_posicao = value

    @property
    def pontuacao(self):
        return self.__pontuacao
    
    @pontuacao.setter
    def pontuacao(self, value):
        self.__pontuacao = value

    @property
    def font(self):
        return self.__font
    
    @font.setter
    def font(self, value):
        self.__font = value

    @property
    def meteoro(self):
        return self.__meteoro
    
    @meteoro.setter
    def meteoro(self, value):
        self.meteoro = value

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
    
    @property
    def alien_ricochete(self):
        return self.__alien_ricochete

    @alien_ricochete.setter
    def alien_ricochete(self, value):
        self.__alien_ricochete = value

    @property
    def alien_ricochete_lasers(self):
        return self.__alien_ricochete_lasers

    @alien_ricochete_lasers.setter
    def alien_ricochete_lasers(self, value):
        self.__alien_ricochete_lasers = value
    
    @property
    def aliens_smart(self):
        return self.__aliens_smart

    @aliens_smart.setter
    def aliens_smart(self, value):
        self.__aliens_smart = value
    
    @property
    def aliens_smart_lasers(self):
        return self.__aliens_smart_lasers

    @aliens_smart_lasers.setter
    def aliens_smart_lasers(self, value):
        self.__aliens_smart_lasers = value
    
    @property
    def aliens_smart_spawned(self):
        return self.__aliens_smart_spawned

    @aliens_smart_spawned.setter
    def aliens_smart_spawned(self, value):
        self.__aliens_smart_spawned = value
    
    @property
    def aliens_kamikaze(self):
        return self.__aliens_kamikaze

    @aliens_kamikaze.setter
    def aliens_kamikaze(self, value):
        self.__aliens_kamikaze = value

    @property
    def aliens_kamikaze_spawned(self):
        return self.__aliens_kamikaze_spawned

    @aliens_kamikaze_spawned.setter
    def aliens_kamikaze_spawned(self, value):
        self.__aliens_kamikaze_spawned = value

    @property
    def trilha_sonora(self):
        return self.__trilha_sonora

    @trilha_sonora.setter
    def trilha_sonora(self, value):
        self.__trilha_sonora = value

    @property
    def som_morte(self):
        return self.__som_morte

    @som_morte.setter
    def som_morte(self, value):
        self.__som_morte = value
    
    @property
    def contagem(self):
        return self.__contagem

    @contagem.setter
    def contagem(self, value):
        self.__contagem = value
    
    @property
    def fundo(self):
        return self.__fundo

    @fundo.setter
    def fundo(self, value):
        self.__fundo = value
    
    @property
    def aliens_triplo(self):
        return self.__aliens_triplo

    @aliens_triplo.setter
    def aliens_triplo(self, value):
        self.__aliens_triplo = value

    @property
    def aliens_triplo_lasers(self):
        return self.__aliens_triplo_lasers

    @aliens_triplo_lasers.setter
    def aliens_triplo_lasers(self, value):
        self.__aliens_triplo_lasers = value

    @property
    def powerups(self):
        return self.__powerups

    @powerups.setter
    def powerups(self, value):
        self.__powerups = value

    #cria um obstaculo
    def criar_obstaculo(self) -> None:
        posicao = random.randint(5,763)
        valor_rotacao = random.uniform(-2.5,2.5)
        tipo_meteoro = Meteoro(posicao,valor_rotacao)
        self.meteoro.add(tipo_meteoro)

    def alien_position_checker(self) -> None:
        todos_aliens = self.aliens.sprites()
        for alien in todos_aliens:
            if alien.rect.right >= largura_tela:
                self.alien_direction = -1
            elif alien.rect.left <= 0:
                self.alien_direction = 1
    
    def alien_ricochete_position_checker(self) -> None:
        todos_aliens = self.alien_ricochete.sprites()
        for alien in todos_aliens:
            if alien.rect.right >= largura_tela:
                self.alien_direction = -1
            elif alien.rect.left <= 0:
                self.alien_direction = 1
    
    def alien_triplo_position_checker(self) -> None:
        todos_aliens = self.aliens_triplo.sprites()
        for alien in todos_aliens:
            if alien.rect.right >= largura_tela:
                self.alien_direction = -1
            elif alien.rect.left <= 0:
                self.alien_direction = 1

    def alien_shoot(self) -> None:
        if self.aliens.sprites():
            alien_aleatorio = choice(self.aliens.sprites())
            laser_sprite = LaserAlien(alien_aleatorio.rect.center,6,altura_tela)
            self.alien_lasers.add(laser_sprite)
    
    def alien_shoot_ricochete(self) -> None:
        if self.alien_ricochete.sprites():
            alien_aleatorio = choice(self.alien_ricochete.sprites())
            laser_velocidade = 6
            laser_sprite = LaserRicochete(alien_aleatorio.rect.center,laser_velocidade,altura_tela)
            self.alien_ricochete_lasers.add(laser_sprite)
    
    def alien_shoot_triplo(self) -> None:
        if self.aliens_triplo.sprites():
            alien_aleatorio = choice(self.aliens_triplo.sprites())
            laser_velocidade = 6
            laser_velocidade_direito = -0.75
            laser_velocidade_esquerdo = 0.75
            
            laser_sprite = LaserAlien(alien_aleatorio.rect.center, laser_velocidade, altura_tela)
            self.aliens_triplo_lasers.add(laser_sprite)

            offset_x_direita = 25
            pos_direita_x = alien_aleatorio.rect.centerx + offset_x_direita
            laser_direito_sprite = LaserTriplo((pos_direita_x, alien_aleatorio.rect.centery), laser_velocidade, altura_tela, laser_velocidade_direito)
            self.aliens_triplo_lasers.add(laser_direito_sprite)
            
            offset_x_esquerda = offset_x_direita * -1
            pos_esquerda_x = alien_aleatorio.rect.centerx + offset_x_esquerda
            laser_esquerdo_sprite = LaserTriplo((pos_esquerda_x, alien_aleatorio.rect.centery), laser_velocidade, altura_tela, laser_velocidade_esquerdo)
            self.aliens_triplo_lasers.add(laser_esquerdo_sprite)
    
    def alien_smart_shoot(self) -> None:
        if self.aliens_smart.sprites():
            alien_smart_aleatorio = choice(self.aliens_smart.sprites())
            laser_sprite = LaserAlien(alien_smart_aleatorio.rect.center, 20, altura_tela)
            self.aliens_smart_lasers.add(laser_sprite)

    def obter_inimigo(self) -> str:
        tipo = random.choices(['comum','incomum','raro','epico'], weights=[inimigo_peso_1, inimigo_peso_2, inimigo_peso_3, inimigo_peso_4], k=1)[0]

        if tipo == 'comum':
            return 'inimigo'
        if tipo == 'incomum':
            return 'inimigo_azul'
        if tipo == 'raro':
            return 'inimigo_vermelho'
        if tipo == 'epico':
            return 'inimigo_roxo'

    def obter_inimigo_inteligente(self) -> str:
        return 'inimigo_verde'

    def padroes(self,linhas=3,distancia_y=100,offset_x=60,offset_y=-250) -> None:
        posicao_x_alien = [num * ((largura_tela - 2 * offset_x) / 7) for num in range(7)]
        
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

        #não vou mexer nos pesos dos padrões, ta maluco, muita dor de cabeça, seloco, num compensa
        selecionador_de_padrao_2000 = random.choices([1,2,3,4,5,6,'lendaria'], weights=[15.83,15.83,15.83,15.83,15.83,15.83,5.02], k=1)[0]
        #selecionador_de_padrao_2000 = random.choices([1,2,3,4,5,6,'lendaria'], weights=[0.01,0.01,0.01,0.01,0.01,0.01,99.94], k=1)[0] #para testes

        definir_padrao = padroes_disponiveis.get(selecionador_de_padrao_2000,padroes_disponiveis[1])

        for indice_linha in range(linhas):
            padrao_atual = definir_padrao['par'] if indice_linha % 2 == 0 else definir_padrao['impar']

            for indice_coluna in range(7):
                if indice_coluna in padrao_atual:
                    continue


                x = posicao_x_alien[indice_coluna]
                y = indice_linha * distancia_y + offset_y

                if selecionador_de_padrao_2000 == 'lendaria' and indice_linha == 1:
                    alien_sprite = self.obter_inimigo_inteligente()
                    alien_selecionado = AlienSmart(alien_sprite,x,y)
                    alien_selecionado.define_alvo_y(y + 290)
                    self.aliens_smart.add(alien_selecionado)
                else:
                    alien_sprite = self.obter_inimigo()
                    if alien_sprite == 'inimigo':
                        alien_selecionado = Alien(alien_sprite,x,y)
                        self.aliens.add(alien_selecionado)
                    elif alien_sprite == 'inimigo_azul':
                        alien_selecionado = AlienRicochete(alien_sprite,x,y)
                        self.alien_ricochete.add(alien_selecionado)
                    elif alien_sprite == 'inimigo_vermelho':
                        alien_selecionado = AlienTriplo(alien_sprite,x,y)
                        self.aliens_triplo.add(alien_selecionado)
                    elif alien_sprite == 'inimigo_roxo':
                        alien_selecionado = AlienKamikaze(alien_sprite,x,y)
                        self.aliens_kamikaze.add(alien_selecionado)
                    alien_selecionado.define_alvo_y(y+290)

    def tela_de_morte(self) -> str:
        self.trilha_sonora.stop()

        nome = ""
        nome_inserido = False
        while not nome_inserido:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN and nome.strip():
                        self.definir_ranking(nome.strip())
                        nome_inserido = True
                    elif evento.key == pygame.K_BACKSPACE:
                        nome = nome[:-1]
                    else:
                        if len(nome) < 3 and evento.unicode.isalnum():
                            nome += evento.unicode.upper()

            screen.fill(cor_menu_fundo)
            titulo = self.font.render("VOCÊ MORREU", True, cor_menu_branco)
            screen.blit(titulo, (largura_tela / 2 - titulo.get_width() / 2, 80))

            instrucao = self.font.render("DIGITE 3 LETRAS:", True, cor_menu_branco)
            screen.blit(instrucao, (largura_tela / 2 - instrucao.get_width() / 2, altura_tela / 2 - 50))
            texto_nome = self.font.render(nome, True, cor_menu_branco)

            screen.blit(texto_nome, (largura_tela / 2 - texto_nome.get_width() / 2, altura_tela / 2))
            
            pygame.display.flip()
            pygame.time.Clock().tick(30)

        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        return 'menu'

            screen.fill(cor_menu_fundo)
            titulo_fim = self.font.render("FIM DE JOGO", True, cor_menu_branco)
            screen.blit(titulo_fim, (largura_tela / 2 - titulo_fim.get_width() / 2, 150))
            
            texto_voltar = self.font.render("VOLTAR AO MENU", True, cor_menu_texto_selecionado)
            rect_voltar = texto_voltar.get_rect(center=(largura_tela / 2, 300))
            screen.blit(texto_voltar, rect_voltar)

            pygame.display.flip()
            pygame.time.Clock().tick(30)

    def checar_colisao(self) -> str:
        #jogador laser
        if self.jogador.sprite.lasers:
            for laser in self.jogador.sprite.lasers:
                #colisão com obstáculo
                if pygame.sprite.spritecollide(laser,self.meteoro,False):
                    laser.kill()

                #colisão com alien
                aliens_atingiu = pygame.sprite.spritecollide(laser,self.aliens,True)
                aliens_ricochete_atingiu = pygame.sprite.spritecollide(laser,self.alien_ricochete, True)
                aliens_triplo_atingiu = pygame.sprite.spritecollide(laser,self.aliens_triplo, True)
                smart_aliens_atingiu = pygame.sprite.spritecollide(laser, self.aliens_smart, False)
                kamikaze_atingiu = pygame.sprite.spritecollide(laser, self.aliens_kamikaze, True)

                if aliens_atingiu:
                    for alien in aliens_atingiu:
                        self.pontuacao += alien.valor
                        self.som_morte.play()

                    drop_chance = random.randint(1,100)
                    tipo = ""
                    if drop_chance <= 10 + chance_drop_aditivo * 1:
                        tipo = random.choices(["escudo", "velocidade", "cura"],weights=[peso_1, peso_2, peso_3], k=1)[0]
                        #criando o power up no jogo
                        if tipo == "cura":
                            powerup = Cura(alien.rect.centerx, alien.rect.centery)
                        elif tipo == "escudo":
                            powerup = Escudo(alien.rect.centerx, alien.rect.centery)
                        elif tipo == "velocidade":
                            powerup = Velocidade(alien.rect.centerx, alien.rect.centery)          
                        self.powerups.add(powerup)

                            #aliens
                        if self.aliens:        
                            if pygame.sprite.spritecollide(alien,self.jogador,False):
                                pygame.quit()
                                sys.exit()
                    laser.kill()
                
                if aliens_ricochete_atingiu:
                    for alien in aliens_ricochete_atingiu:
                        self.pontuacao += alien.valor
                        self.som_morte.play()
                    
                    drop_chance = random.randint(1,100)
                    tipo = ""
                    if drop_chance <= 10 + chance_drop_aditivo * 3:
                        tipo = random.choices(["escudo", "velocidade", "cura"],weights=[peso_1, peso_2, peso_3], k=1)[0]
                        #criando o power up no jogo
                        if tipo == "cura":
                            powerup = Cura(alien.rect.centerx, alien.rect.centery)
                        elif tipo == "escudo":
                            powerup = Escudo(alien.rect.centerx, alien.rect.centery)
                        elif tipo == "velocidade":
                            powerup = Velocidade(alien.rect.centerx, alien.rect.centery)               
                        self.powerups.add(powerup)

                            #aliens
                        if self.alien_ricochete:        
                            if pygame.sprite.spritecollide(alien,self.jogador,False):
                                pygame.quit()
                                sys.exit()
                    laser.kill()
                
                if aliens_triplo_atingiu:
                    for alien in aliens_triplo_atingiu:
                        self.pontuacao += alien.valor
                        self.som_morte.play()

                    drop_chance = random.randint(1,100)
                    tipo = ""
                    if drop_chance <= 10 + chance_drop_aditivo * 5:
                        tipo = random.choices(["escudo", "velocidade", "cura"],weights=[peso_1, peso_2, peso_3], k=1)[0]
                        #criando o power up no jogo
                        if tipo == "cura":
                            powerup = Cura(alien.rect.centerx, alien.rect.centery)
                        elif tipo == "escudo":
                            powerup = Escudo(alien.rect.centerx, alien.rect.centery)
                        elif tipo == "velocidade":
                            powerup = Velocidade(alien.rect.centerx, alien.rect.centery)               
                        self.powerups.add(powerup)

                            #aliens
                        if self.aliens_triplo:        
                            if pygame.sprite.spritecollide(alien,self.jogador,False):
                                pygame.quit()
                                sys.exit()
                    laser.kill()
                
                if smart_aliens_atingiu:
                    for alien in smart_aliens_atingiu:
                        self.contagem += 1
                        print(self.contagem)
                        if self.contagem == 3:
                            self.pontuacao += alien.valor
                            self.som_morte.play()
                            laser.kill()
                            smart_aliens_atingiu = pygame.sprite.spritecollide(laser, self.aliens_smart, True)
                    laser.kill()
                
                if kamikaze_atingiu:
                    for kami in kamikaze_atingiu:
                        self.pontuacao += kami.valor
                        self.som_morte.play()
                    laser.kill()

        #alien laser
        if self.alien_lasers:
            for laser in self.alien_lasers:
                #colisão com obstáculo
                if pygame.sprite.spritecollide(laser,self.meteoro,False):
                    laser.kill()

                if pygame.sprite.spritecollide(laser,self.jogador,False):
                    laser.kill()
                    if self.jogador.sprite.escudo == 0:
                        self.vidas -= 1
                        self.jogador.sprite.vidas -= 1
                    if self.vidas <= 0:
                        return self.tela_de_morte()

        if self.alien_ricochete_lasers:
            for laser in self.alien_ricochete_lasers:
                #colisão com obstáculo
                if pygame.sprite.spritecollide(laser,self.meteoro,False):
                    laser.kill()

                if pygame.sprite.spritecollide(laser,self.jogador,False):
                    laser.kill()
                    if self.jogador.sprite.escudo == 0:
                        self.vidas -= 1
                        self.jogador.sprite.vidas -= 1
                    if self.vidas <= 0:
                        return self.tela_de_morte()

        if self.aliens_triplo_lasers:
            for laser in self.aliens_triplo_lasers:
                #colisão com obstáculo
                if pygame.sprite.spritecollide(laser,self.meteoro,False):
                    laser.kill()

                if pygame.sprite.spritecollide(laser,self.jogador,False):
                    laser.kill()
                    if self.jogador.sprite.escudo == 0:
                        self.vidas -= 1
                        self.jogador.sprite.vidas -= 1
                    if self.vidas <= 0:
                        return self.tela_de_morte()

        if self.aliens_smart_lasers:
            for laser in self.aliens_smart_lasers:
                if pygame.sprite.spritecollide(laser,self.meteoro,False):
                    laser.kill()

                if pygame.sprite.spritecollide(laser,self.jogador,False):
                    self.som_morte.play()
                    laser.kill()
                    if self.jogador.sprite.escudo == 0:
                        self.jogador.sprite.vidas -= 2
                    if self.jogador.sprite.vidas <= 0:
                        return self.tela_de_morte()

        #aliens
        if self.aliens:
            for alien in self.aliens:
                if pygame.sprite.spritecollide(alien,self.jogador,False):
                    pygame.quit()
                    sys.exit()
        
        power_up_coletado = pygame.sprite.spritecollide(self.jogador.sprite, self.powerups, True)
        for powerups in power_up_coletado:
            powerups.efeito(self.jogador.sprite)

        if self.alien_ricochete:
            for alien_rico in self.alien_ricochete:
                if pygame.sprite.spritecollide(alien_rico,self.jogador,False):
                    pygame.quit()
                    sys.exit()
        
        if self.aliens_triplo:
            for alien_triplo in self.aliens_triplo:
                if pygame.sprite.spritecollide(alien_triplo,self.jogador,False):
                    pygame.quit()
                    sys.exit()
        
        if self.aliens_smart:
            for smart_alien in self.aliens_smart:
                if pygame.sprite.spritecollide(smart_alien, self.jogador, False):
                    pygame.quit()
                    sys.exit()
        
        if self.aliens_kamikaze:
            for kami in self.aliens_kamikaze:
                if pygame.sprite.spritecollide(kami,self.jogador,False):
                    self.vidas -= int(self.vidas)
                    if self.vidas <= 0:
                        return self.tela_de_morte()

        if self.meteoro:
            for meteoro in self.meteoro:
                if pygame.sprite.spritecollide(meteoro,self.jogador,False):
                    print("Usuário colidiu com o asteroide")
                    return self.tela_de_morte()

    def mostrar_vidas(self) -> None:
        for vida in range(self.jogador.sprite.vidas):
            #sai do loop pq já tem o maximo de vidas
            if vida >= 5:
                break

            x = self.vida_x_posicao + (vida * self.vida_imagem.get_size()[0] - 20)
            screen.blit(self.vida_imagem,(x,5))

    def mostrar_pontuacao(self) -> None:
        pontuacao_imagem = self.font.render(f'PONTUACAO: {self.pontuacao}',False,'white')
        pontuacao_rect = pontuacao_imagem.get_rect(topleft = (10,-10))
        screen.blit(pontuacao_imagem,pontuacao_rect)

    def controlar_fase(self, spawn_alien_event, spawn_alien_alert_event, spawn_meteoro_event, alien_laser, alien_azul_laser, alien_vermelho_laser) -> int:
        global padroes_spawnados, cooldown_spawn_padroes, cooldown_spawn_meteoro, modificador_do_peso, chance_drop_aditivo, modificador_peso_inimigo
        global  alien_laser_cooldown, alien_azul_cooldown, alien_vermelho_cooldown

        padroes_spawnados+=1

        if cooldown_spawn_padroes == 5000 and padroes_spawnados <= 1:
            return
        
        if padroes_spawnados % 2 == 0:
            efeitos = [
                "reduzir_cooldown_padroes",
                "reduzir_cooldown_meteoro",
                "aumentar_chance_drops",
                "aumentar_chance_buffs",
                "aumentar_chance_inimigos_raros",
                "diminuir_cooldown_tiro_inimigos"
            ]

            tentativas = 0
            max_tentativas = 25
            efeito_aplicado = False

            while tentativas < max_tentativas and not efeito_aplicado:
                efeito = random.choice(efeitos)
                tentativas += 1

                if efeito == "reduzir_cooldown_padroes" and cooldown_spawn_padroes > 10000:
                    cooldown_spawn_padroes = max(10000, cooldown_spawn_padroes - 1000)
                    print(">> Cooldown de spawn dos inimigos reduzido para", cooldown_spawn_padroes / 1000, "segundos")
                    efeito_aplicado = True
                elif efeito == "reduzir_cooldown_meteoro" and cooldown_spawn_meteoro > 7500:
                    cooldown_spawn_meteoro = max(7500, cooldown_spawn_meteoro - 500)
                    print(">> Cooldown do spawn do meteoro reduzido para", cooldown_spawn_meteoro / 1000, "segundos")
                    efeito_aplicado = True
                elif efeito == "aumentar_chance_drops" and chance_drop_aditivo < 3:
                    chance_drop_aditivo = min(3, chance_drop_aditivo + 0.25)
                    print(">> Chance de drops aumentado em 0.25%")
                    efeito_aplicado = True
                elif efeito == "aumentar_chance_buffs" and modificador_do_peso < 10:
                    modificador_do_peso = min(10, modificador_do_peso + 0.5)
                    print(">> Chance de buffs melhores aumentada em 0.5%")
                    efeito_aplicado = True
                elif efeito == "aumentar_chance_inimigos_raros" and modificador_peso_inimigo < 2.5:
                    modificador_peso_inimigo = min(2.5, modificador_peso_inimigo + 0.25)
                    if modificador_peso_inimigo == 0.25:
                        print(">> Chance de inimigos mais raros aumentada em 0.25% + NOVO INIMIGO!!!")
                    else:
                        print(">> Chance de inimigos mais raros aumentada em 0.25%")
                    efeito_aplicado = True
                elif efeito == "diminuir_cooldown_tiro_inimigos" and alien_laser_cooldown > 800:
                    alien_laser_cooldown = max(800, alien_laser_cooldown - 100)
                    alien_azul_cooldown = max(1000, alien_azul_cooldown - 100)
                    alien_vermelho_cooldown = max(1200, alien_vermelho_cooldown - 100)
                    print(">> Tiro dos inimigos reduzido em 0.1 segundos")
                    efeito_aplicado = True

        pygame.time.set_timer(spawn_alien_event, cooldown_spawn_padroes)
        pygame.time.set_timer(spawn_alien_alert_event, max(7000, cooldown_spawn_padroes - 3000))
        pygame.time.set_timer(spawn_meteoro_event, cooldown_spawn_meteoro)
        pygame.time.set_timer(alien_laser, alien_laser_cooldown)
        pygame.time.set_timer(alien_azul_laser, alien_azul_cooldown)
        pygame.time.set_timer(alien_vermelho_laser, alien_vermelho_cooldown)

    def definir_ranking(self, nome):
        pontuacao = self.pontuacao
            
        ranking = Ranking()
        ranking.salvar(nome,pontuacao)

    #desenha e atualiza todos os sprites
    def rodar(self) -> str:
        screen.blit(self.fundo, (0,0))
        self.jogador.update()
        self.alien_lasers.update()
        self.alien_ricochete_lasers.update()
        self.aliens_triplo_lasers.update()
        self.aliens_smart_lasers.update()

        self.aliens.update(self.alien_direction)
        self.alien_ricochete.update(self.alien_direction)
        self.aliens_triplo.update(self.alien_direction)
        self.alien_position_checker()
        self.alien_ricochete_position_checker()
        self.alien_triplo_position_checker()
        acao_pos_colisao = self.checar_colisao()

        if self.jogador.sprite:
            jogador_x = self.jogador.sprite.rect.centerx
            for smart_alien in self.aliens_smart.sprites():
                smart_alien.update(jogador_x)
        
        if self.jogador.sprite:
            jogador_x = self.jogador.sprite.rect.centerx
            jogador_y = self.jogador.sprite.rect.centery
            for kamikaze in self.aliens_kamikaze.sprites():
                kamikaze.update(jogador_x, jogador_y)

        self.jogador.sprite.lasers.draw(screen)
        self.jogador.draw(screen)
        self.aliens.draw(screen)
        self.alien_ricochete.draw(screen)
        self.aliens_triplo.draw(screen)
        self.aliens_smart.draw(screen)
        self.aliens_kamikaze.draw(screen)
        self.alien_lasers.draw(screen)
        self.alien_ricochete_lasers.draw(screen)
        self.aliens_triplo_lasers.draw(screen)
        self.aliens_smart_lasers.draw(screen)
        self.meteoro.draw(screen)

        self.mostrar_vidas()
        self.mostrar_pontuacao()

        self.meteoro.update()

        self.animacao.update(screen)
        #atualizando os power ups
        self.powerups.update()
        self.powerups.draw(screen)

        return acao_pos_colisao

def start_game(volume_musica=0.5, volume_game=0.5) -> str:
    pygame.display.set_caption("Jogo")
    global cooldown_spawn_padroes, cooldown_spawn_meteoro, modificador_do_peso, chance_drop_aditivo, modificador_peso_inimigo, alien_laser_cooldown, alien_azul_cooldown, alien_vermelho_cooldown, padroes_spawnados
    global inimigo_peso_1, inimigo_peso_2, inimigo_peso_3, inimigo_peso_4, peso_1, peso_2, peso_3


    #reseta tudo ao iniciar o jogo novamente
    padroes_spawnados = 0
    cooldown_spawn_padroes = 5000
    cooldown_spawn_meteoro = 20000
    modificador_do_peso = 0
    peso_1 = 80
    peso_2 = 15
    peso_3 = 5
    chance_drop_aditivo = 0
    modificador_peso_inimigo = 0
    inimigo_peso_1 = 75
    inimigo_peso_2 = 7.5
    inimigo_peso_3 = 2.5
    inimigo_peso_4 = 0
    alien_laser_cooldown = 1600
    alien_azul_cooldown = 1800
    alien_vermelho_cooldown = 2000

    pygame.init()
    screen = pygame.display.set_mode((largura_tela,altura_tela))
    clock = pygame.time.Clock()
    game = Jogo()
    game.som_morte.set_volume(volume_game)

    jogador = game.jogador.sprite
    jogador.shoot_sound.set_volume(volume_game)
    animacao = game.animacao
    animacao.sound.set_volume(volume_musica)

    game.trilha_sonora.set_volume(volume_musica)
    game.trilha_sonora.play(-1)

    ALIENLASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIENLASER,1600)
    
    ALIEN_AZUL_LASER = pygame.USEREVENT + 2
    pygame.time.set_timer(ALIEN_AZUL_LASER,1800)

    ALIEN_VERMELHO_LASER = pygame.USEREVENT + 3
    pygame.time.set_timer(ALIEN_VERMELHO_LASER,2000)

    SPAWN_ALIEN = pygame.USEREVENT + 4
    pygame.time.set_timer(SPAWN_ALIEN,5000)
    
    ALIEN_SMART_LASER = pygame.USEREVENT + 5
    pygame.time.set_timer(ALIEN_SMART_LASER,1500)

    SPAWN_ALIEN_ALERT_ANIMATION = pygame.USEREVENT + 6
    pygame.time.set_timer(SPAWN_ALIEN_ALERT_ANIMATION,2000)

    SPAWN_METEORO = pygame.USEREVENT + 7
    pygame.time.set_timer(SPAWN_METEORO, 12500)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == ALIENLASER:
                game.alien_shoot()
            if event.type == ALIEN_AZUL_LASER:
                game.alien_shoot_ricochete()
            if event.type == ALIEN_VERMELHO_LASER:
                game.alien_shoot_triplo()
            if event.type == ALIEN_SMART_LASER:
                game.alien_smart_shoot()
            if event.type == SPAWN_ALIEN_ALERT_ANIMATION:
                game.animacao.iniciar_animacao()
                if game.recarga_spawn_inimigo == 5000:
                    pygame.time.set_timer(SPAWN_ALIEN_ALERT_ANIMATION, 0)
                else:
                    continue
            if event.type == SPAWN_ALIEN:
                game.padroes()
                if cooldown_spawn_padroes == 5000:
                    cooldown_spawn_padroes += 25000
                    pygame.time.set_timer(SPAWN_ALIEN,cooldown_spawn_padroes)
                    pygame.time.set_timer(SPAWN_ALIEN_ALERT_ANIMATION,cooldown_spawn_padroes - 3000)
                else:
                    game.controlar_fase(SPAWN_ALIEN, SPAWN_ALIEN_ALERT_ANIMATION, SPAWN_METEORO, ALIENLASER, ALIEN_AZUL_LASER, ALIEN_VERMELHO_LASER)
            if event.type == SPAWN_METEORO:
                game.criar_obstaculo()

        screen.fill((30,30,30))
        acao = game.rodar()

        if acao == 'menu':
            return

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    menu = Menu()
    menu.mostrar_menu_principal()
    start_game()