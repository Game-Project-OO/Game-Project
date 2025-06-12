import pygame, sys
from player import Jogador
import obstacle
from alien import Alien
from random import choice
from laser import Laser

class Jogo:
    def __init__(self):
        #setup do jogador
        player_sprite = Jogador((screen_width / 2,screen_height),screen_width,5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        #vida e pontuação
        self.vidas = 3
        self.vida_imagem = pygame.image.load('../IMAGENS/heart.png').convert_alpha()
        self.vida_x_posicao = screen_width - (self.vida_imagem.get_size()[0] * 2 + 20)
        self.score = 0
        self.font = pygame.font.Font('../FONTE/Pixeled.ttf',20)

        #setup do obstaculo
        self.shape = obstacle.shape
        self.block_size = 6
        self.blocks = pygame.sprite.Group()
        self.quantidade_de_obstaculos = 4
        self.posicao_x_obstaculos = [num * (screen_width / self.quantidade_de_obstaculos) for num in range(self.quantidade_de_obstaculos)]
        self.criar_multiplos_obstaculos(*self.posicao_x_obstaculos, x_start = screen_width / 15, y_start = 600)

        #setup do alien
        self.aliens = pygame.sprite.Group()
        self.alien_setup(rows = 3, cols = 6)
        self.alien_direction = 1
        self.alien_lasers = pygame.sprite.Group()

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

    def alien_setup(self,rows,cols,y_distance=100,x_offset = 70,y_offset = 100):
        posicao_x_alien = [num * ((screen_width - 2 * x_offset) / cols) for num in range(cols)]
        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):
                x = posicao_x_alien[col_index]
                y = row_index * y_distance + y_offset

                if row_index == 0: 
                    alien_sprite = Alien('enemy_red',x,y)
                elif row_index == 1:
                    alien_sprite = Alien('enemy_blue',x,y)
                else:
                    alien_sprite = Alien('enemy',x,y)

                self.aliens.add(alien_sprite)

    def alien_position_checker(self):
        all_aliens = self.aliens.sprites()
        for alien in all_aliens:
            if alien.rect.right >= screen_width:
                self.alien_direction = -1
                self.alien_move_down(2)
            elif alien.rect.left <= 0:
                self.alien_direction = 1
                self.alien_move_down(2)

    def alien_move_down(self,distance):
        if self.aliens:
            for alien in self.aliens.sprites():
                alien.rect.y += distance

    def alien_shoot(self):
        if self.aliens.sprites():
            random_alien = choice(self.aliens.sprites())
            laser_sprite = Laser(random_alien.rect.center,6,screen_height)
            self.alien_lasers.add(laser_sprite)

    def collision_checks(self):

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
        for vida in range(self.vidas - 1):
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
        self.collision_checks()

        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)
        self.blocks.draw(screen)
        self.aliens.draw(screen)
        self.alien_lasers.draw(screen)

        self.mostrar_vidas()
        self.mostrar_score()

if __name__ == '__main__':
    pygame.init()
    screen_width = 768
    screen_height = 768
    screen = pygame.display.set_mode((screen_width,screen_height))
    clock = pygame.time.Clock()
    game = Jogo()

    ALIENLASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIENLASER,800)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == ALIENLASER:
                game.alien_shoot()

        screen.fill((30,30,30))
        game.rodar()

        pygame.display.flip()
        clock.tick(60)