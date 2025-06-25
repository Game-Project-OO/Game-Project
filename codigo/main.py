import pygame, sys
from player import Jogador
from obstacle import Meteoro
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
from heal import Heal
from shield import Shield
#from alien_spawn import SpawnAlien

class Jogo:
    def __init__(self):
        #setup do jogador
        player_sprite = Jogador((screen_width / 2,screen_height),screen_width,5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        #vida e pontuação
        self.__vidas = 5
        self.__vida_imagem = pygame.image.load('../imagens/heart.png').convert_alpha()
        self.__vida_extra_imagem = pygame.image.load('../imagens/heart_plus.png').convert_alpha()
        self.__vida_x_posicao = screen_width - (self.vida_imagem.get_size()[0] * 3 + 20)
        self.__score = 0
        self.__font = pygame.font.Font('../fonte/Pixeled.ttf',20)

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

        self.__trilhaSonora_alienSmart = pygame.mixer.Sound('../sons/musicaGameplay.mp3')
        self.__kill_sound = pygame.mixer.Sound('../sons/kill_sound.mp3')
        self.__contagem = 0 #contagem para verificar quando o alien smart é atingido
        self.__background = pygame.transform.scale(pygame.image.load('../imagens/background.png').convert(), (screen_width, screen_height))

        self.__powerups = pygame.sprite.Group()
        #criacao dos padroes de aliens
        self.enemy_spawn_cooldown = 5000

        #setup de animações
        self.animacao = Animacoes()

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
    def trilhaSonora_alienSmart(self):
        return self.__trilhaSonora_alienSmart

    @trilhaSonora_alienSmart.setter
    def trilhaSonora_alienSmart(self, value):
        self.__trilhaSonora_alienSmart = value

    @property
    def kill_sound(self):
        return self.__kill_sound

    @kill_sound.setter
    def kill_sound(self, value):
        self.__kill_sound = value
    
    @property
    def contagem(self):
        return self.__contagem

    @contagem.setter
    def contagem(self, value):
        self.__contagem = value
    
    @property
    def background(self):
        return self.__background

    @background.setter
    def background(self, value):
        self.__background = value
    
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
    def criar_obstaculo(self):
        posicao = random.randint(5,763)
        valor_rotacao = random.uniform(-2.5,2.5)
        tipo_meteoro = Meteoro(posicao,valor_rotacao)
        self.meteoro.add(tipo_meteoro)

    def alien_position_checker(self):
        all_aliens = self.aliens.sprites()
        for alien in all_aliens:
            if alien.rect.right >= screen_width:
                self.alien_direction = -1
            elif alien.rect.left <= 0:
                self.alien_direction = 1
    
    def alien_ricochete_position_checker(self):
        all_aliens = self.alien_ricochete.sprites()
        for alien in all_aliens:
            if alien.rect.right >= screen_width:
                self.alien_direction = -1
            elif alien.rect.left <= 0:
                self.alien_direction = 1
    
    def alien_triplo_position_checker(self):
        all_aliens = self.aliens_triplo.sprites()
        for alien in all_aliens:
            if alien.rect.right >= screen_width:
                self.alien_direction = -1
            elif alien.rect.left <= 0:
                self.alien_direction = 1

    def alien_shoot(self):
        if self.aliens.sprites():
            random_alien = choice(self.aliens.sprites())
            laser_sprite = LaserAlien(random_alien.rect.center,6,screen_height)
            self.alien_lasers.add(laser_sprite)
    
    def alien_shoot_ricochete(self):
        if self.alien_ricochete.sprites():
            random_alien = choice(self.alien_ricochete.sprites())
            laser_speed = 6
            laser_sprite = LaserRicochete(random_alien.rect.center,laser_speed,screen_height)
            self.alien_ricochete_lasers.add(laser_sprite)
    
    def alien_shoot_triplo(self):
        if self.aliens_triplo.sprites():
            random_alien = choice(self.aliens_triplo.sprites())
            laser_speed = 6
            laser_speed_direito = -0.75
            laser_speed_esquerdo = 0.75
            
            laser_sprite = LaserAlien(random_alien.rect.center, laser_speed, screen_height)
            self.aliens_triplo_lasers.add(laser_sprite)

            offset_x_direita = 25
            pos_direita_x = random_alien.rect.centerx + offset_x_direita
            laser_direito_sprite = LaserTriplo((pos_direita_x, random_alien.rect.centery), laser_speed, screen_height, laser_speed_direito)
            self.aliens_triplo_lasers.add(laser_direito_sprite)
            
            offset_x_esquerda = offset_x_direita * -1
            pos_esquerda_x = random_alien.rect.centerx + offset_x_esquerda
            laser_esquerdo_sprite = LaserTriplo((pos_esquerda_x, random_alien.rect.centery), laser_speed, screen_height, laser_speed_esquerdo)
            self.aliens_triplo_lasers.add(laser_esquerdo_sprite)
    
    def alien_smart_shoot(self):
        if self.aliens_smart.sprites():
            random_smart_alien = choice(self.aliens_smart.sprites())
            laser_sprite = LaserAlien(random_smart_alien.rect.center, 20, screen_height)
            self.aliens_smart_lasers.add(laser_sprite)

    def obter_inimigo(self):
        tipo = random.choices(['comum','incomum','raro','epico'], weights=[65,15,7.5,2.5], k=1)[0]

        if tipo == 'comum':
            return 'enemy'
        if tipo == 'incomum':
            return 'enemy_blue'
        if tipo == 'raro':
            return 'enemy_red'
        if tipo == 'epico':
            return 'enemy_purple'

    def obter_inimigo_inteligente(self):
        return 'enemy_green'

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
        #selecionador_de_padrao_2000 = random.choices([1,2,3,4,5,6,'lendaria'], weights=[0.01,0.01,0.01,0.01,0.01,0.01,99.94], k=1)[0] #para testes

        definir_padrao = padroes_disponiveis.get(selecionador_de_padrao_2000,padroes_disponiveis[1])

        for row_index in range(rows):
            padrao_atual = definir_padrao['par'] if row_index % 2 == 0 else definir_padrao['impar']

            for col_index in range(7):
                if col_index in padrao_atual:
                    continue


                x = posicao_x_alien[col_index]
                y = row_index * y_distance + y_offset

                if selecionador_de_padrao_2000 == 'lendaria' and row_index == 1:
                    alien_sprite = self.obter_inimigo_inteligente()
                    alien_type = AlienSmart(alien_sprite,x,y)
                    alien_type.define_alvo_y(y + 290)
                    self.aliens_smart.add(alien_type)
                else:
                    alien_sprite = self.obter_inimigo()
                    if alien_sprite == 'enemy':
                        alien_type = Alien(alien_sprite,x,y)
                        self.aliens.add(alien_type)
                    elif alien_sprite == 'enemy_blue':
                        alien_type = AlienRicochete(alien_sprite,x,y)
                        self.alien_ricochete.add(alien_type)
                    elif alien_sprite == 'enemy_red':
                        alien_type = AlienTriplo(alien_sprite,x,y)
                        self.aliens_triplo.add(alien_type)
                    elif alien_sprite == 'enemy_purple':
                        alien_type = AlienKamikaze(alien_sprite,x,y)
                        self.aliens_kamikaze.add(alien_type)
                    alien_type.define_alvo_y(y+290)

    def checar_colisao(self):
        #player laser
        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:
                #colisão com obstáculo
                if pygame.sprite.spritecollide(laser,self.meteoro,False):
                    laser.kill()

                #colisão com alien
                aliens_hit = pygame.sprite.spritecollide(laser,self.aliens,True)
                aliens_ricochete_hit = pygame.sprite.spritecollide(laser,self.alien_ricochete, True)
                aliens_triplo_hit = pygame.sprite.spritecollide(laser,self.aliens_triplo, True)
                smart_aliens_hit = pygame.sprite.spritecollide(laser, self.aliens_smart, False)
                kamikaze_hit = pygame.sprite.spritecollide(laser, self.aliens_kamikaze, True)

                if aliens_hit:
                    for alien in aliens_hit:
                        self.score += alien.value
                        self.kill_sound.set_volume(0.2)
                        self.kill_sound.play()

                    drop_chance = random.randint(1,100)
                    tipo = ""
                    if drop_chance <= 10:
                        tipo = random.choice(["heal", "shield"])
                        #criando o power up no jogo
                        if tipo == "heal":
                            powerup = Heal(alien.rect.centerx, alien.rect.centery)
                        elif tipo == "shield":
                            powerup = Shield(alien.rect.centerx, alien.rect.centery)                
                        self.powerups.add(powerup)

                            #aliens
                        if self.aliens:        
                            if pygame.sprite.spritecollide(alien,self.player,False):
                                pygame.quit()
                                sys.exit()
                    laser.kill()
                
                if aliens_ricochete_hit:
                    for alien in aliens_ricochete_hit:
                        self.score += alien.value
                        self.kill_sound.set_volume(0.2)
                        self.kill_sound.play()
                    
                    drop_chance = random.randint(1,100)
                    tipo = ""
                    if drop_chance <= 10:
                        tipo = random.choice(["heal", "shield"])
                        #criando o power up no jogo
                        if tipo == "heal":
                            powerup = Heal(alien.rect.centerx, alien.rect.centery)
                        elif tipo == "shield":
                            powerup = Shield(alien.rect.centerx, alien.rect.centery)                
                        self.powerups.add(powerup)

                            #aliens
                        if self.alien_ricochete:        
                            if pygame.sprite.spritecollide(alien,self.player,False):
                                pygame.quit()
                                sys.exit()
                    laser.kill()
                
                if aliens_triplo_hit:
                    for alien in aliens_triplo_hit:
                        self.score += alien.value
                        self.kill_sound.set_volume(0.2)
                        self.kill_sound.play()

                    drop_chance = random.randint(1,100)
                    tipo = ""
                    if drop_chance <= 10:
                        tipo = random.choice(["heal", "shield"])
                        #criando o power up no jogo
                        if tipo == "heal":
                            powerup = Heal(alien.rect.centerx, alien.rect.centery)
                        elif tipo == "shield":
                            powerup = Shield(alien.rect.centerx, alien.rect.centery)                
                        self.powerups.add(powerup)

                            #aliens
                        if self.aliens_triplo:        
                            if pygame.sprite.spritecollide(alien,self.player,False):
                                pygame.quit()
                                sys.exit()
                    laser.kill()
                
                if smart_aliens_hit:
                    for alien in smart_aliens_hit:
                        self.contagem += 1
                        print(self.contagem)
                        if self.contagem == 3:
                            self.score += alien.value
                            self.trilhaSonora_alienSmart.stop()
                            self.kill_sound.set_volume(0.2)
                            self.kill_sound.play()
                            laser.kill()
                            smart_aliens_hit = pygame.sprite.spritecollide(laser, self.aliens_smart, True)
                    laser.kill()
                
                if kamikaze_hit:
                    for kami in kamikaze_hit:
                        self.score += kami.value
                        self.kill_sound.set_volume(0.2)
                        self.kill_sound.play()
                    laser.kill()

        #alien laser
        if self.alien_lasers:
            for laser in self.alien_lasers:
                #colisão com obstáculo
                if pygame.sprite.spritecollide(laser,self.meteoro,False):
                    laser.kill()

                if pygame.sprite.spritecollide(laser,self.player,False):
                    laser.kill()
                    if self.player.sprite.shield == 0:
                        self.player.sprite.vidas -= 1
                    if self.player.sprite.vidas <= 0:
                        pygame.quit()
                        sys.exit()
        
        if self.alien_ricochete_lasers:
            for laser in self.alien_ricochete_lasers:
                #colisão com obstáculo
                if pygame.sprite.spritecollide(laser,self.meteoro,False):
                    laser.kill()

                if pygame.sprite.spritecollide(laser,self.player,False):
                    laser.kill()
                    if self.player.sprite.shield == 0:
                        self.player.sprite.vidas -= 1
                    if self.player.sprite.vidas <= 0:
                        pygame.quit()
                        sys.exit()

        if self.aliens_triplo_lasers:
            for laser in self.aliens_triplo_lasers:
                #colisão com obstáculo
                if pygame.sprite.spritecollide(laser,self.meteoro,False):
                    laser.kill()

                if pygame.sprite.spritecollide(laser,self.player,False):
                    laser.kill()
                    if self.player.sprite.shield == 0:
                        self.player.sprite.vidas -= 1
                    if self.player.sprite.vidas <= 0:
                        pygame.quit()
                        sys.exit()

        if self.aliens_smart_lasers:
            for laser in self.aliens_smart_lasers:
                if pygame.sprite.spritecollide(laser,self.meteoro,False):
                    laser.kill()

                if pygame.sprite.spritecollide(laser,self.player,False):
                    self.kill_sound.play()
                    laser.kill()
                    if self.player.sprite.shield == 0:
                        self.player.sprite.vidas -= 2
                    if self.player.sprite.vidas <= 0:
                        pygame.quit()
                        sys.exit()
                    if self.player.sprite.vidas <= 0:
                        pygame.quit()
                        sys.exit()
            
        #aliens
        if self.aliens:
            for alien in self.aliens:
                if pygame.sprite.spritecollide(alien,self.player,False):
                    pygame.quit()
                    sys.exit()
        
        power_up_coletado = pygame.sprite.spritecollide(self.player.sprite, self.powerups, True)
        for pups in power_up_coletado:
            pups.efeito(self.player.sprite)

        if self.alien_ricochete:
            for alien_rico in self.alien_ricochete:
                if pygame.sprite.spritecollide(alien_rico,self.player,False):
                    pygame.quit()
                    sys.exit()
        
        if self.aliens_triplo:
            for alien_triplo in self.aliens_triplo:
                if pygame.sprite.spritecollide(alien_triplo,self.player,False):
                    pygame.quit()
                    sys.exit()
        
        if self.aliens_smart:
            for smart_alien in self.aliens_smart:
                if pygame.sprite.spritecollide(smart_alien, self.player, False):
                    pygame.quit()
                    sys.exit()
        
        if self.aliens_kamikaze:
            for kami in self.aliens_kamikaze:
                if pygame.sprite.spritecollide(kami,self.player,True):
                    self.vidas -= int(self.vidas)
                    if self.vidas <= 0:
                        pygame.quit()
                        sys.exit()

        if self.meteoro:
            for meteoro in self.meteoro:
                if pygame.sprite.spritecollide(meteoro,self.player,False):
                    print("Usuário colidiu com o asteroide")
                    pygame.quit()
                    sys.exit()

    def mostrar_vidas(self):
        for vida in range(self.player.sprite.vidas):
            #sai do loop pois já tem o maximo de vidas
            if vida >= self.vidas:
                break

            x = self.vida_x_posicao + (vida * self.vida_imagem.get_size()[0] - 20)
            screen.blit(self.vida_imagem,(x,5))

    def mostrar_score(self):
        score_imagem = self.font.render(f'score: {self.score}',False,'white')
        score_rect = score_imagem.get_rect(topleft = (10,-10))
        screen.blit(score_imagem,score_rect)

    #desenha e atualiza todos os sprites
    def rodar(self):
        screen.blit(self.background, (0,0))
        self.player.update()
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
        self.checar_colisao()

        if self.player.sprite:
            player_x = self.player.sprite.rect.centerx
            for smart_alien in self.aliens_smart.sprites():
                smart_alien.update(player_x)
        
        if self.player.sprite:
            player_x = self.player.sprite.rect.centerx
            player_y = self.player.sprite.rect.centery
            for kamikaze in self.aliens_kamikaze.sprites():
                kamikaze.update(player_x, player_y)

        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)
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
        self.mostrar_score()

        self.meteoro.update()

        self.animacao.update(screen)
        #atualizando os power ups
        self.powerups.update()
        self.powerups.draw(screen)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((screen_width,screen_height))
    clock = pygame.time.Clock()
    game = Jogo()

    ALIENLASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIENLASER,800)
    
    ALIEN_BLUE_LASER = pygame.USEREVENT + 2
    pygame.time.set_timer(ALIEN_BLUE_LASER,1000)

    ALIEN_RED_LASER = pygame.USEREVENT + 3
    pygame.time.set_timer(ALIEN_RED_LASER,1200)

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
            if event.type == ALIEN_BLUE_LASER:
                game.alien_shoot_ricochete()
            if event.type == ALIEN_RED_LASER:
                game.alien_shoot_triplo()
            if event.type == ALIEN_SMART_LASER:
                game.alien_smart_shoot()
            if event.type == SPAWN_ALIEN_ALERT_ANIMATION:
                game.animacao.iniciar_animacao()
                if game.enemy_spawn_cooldown == 5000:
                    pygame.time.set_timer(SPAWN_ALIEN_ALERT_ANIMATION, 0)
                else:
                    pygame.time.set_timer(SPAWN_ALIEN_ALERT_ANIMATION,30000)
            if event.type == SPAWN_ALIEN:
                game.padroes()

                if game.enemy_spawn_cooldown == 5000:
                    game.enemy_spawn_cooldown += 25000
                    pygame.time.set_timer(SPAWN_ALIEN,game.enemy_spawn_cooldown)
                    pygame.time.set_timer(SPAWN_ALIEN_ALERT_ANIMATION,game.enemy_spawn_cooldown - 3000)
            if event.type == SPAWN_METEORO:
                game.criar_obstaculo()

        screen.fill((30,30,30))
        game.rodar()

        pygame.display.flip()
        clock.tick(60)