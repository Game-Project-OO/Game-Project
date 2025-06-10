import pygame, sys
from player import Jogador
import obstacle

class Jogo:
    def __init__(self):
        #setup do jogador
        player_sprite = Jogador((screen_width / 2,screen_height),screen_width,5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        #setup do obstaculo
        self.shape = obstacle.shape
        self.block_size = 6
        self.blocks = pygame.sprite.Group()
        self.quantidade_de_obstaculos = 4
        self.posicao_x_obstaculos = [num * (screen_width / self.quantidade_de_obstaculos) for num in range(self.quantidade_de_obstaculos)]
        self.criar_multiplos_obstaculos(*self.posicao_x_obstaculos, x_start = screen_width / 15, y_start = 600)

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


    #desenha e atualiza todos os sprites
    def rodar(self):
        self.player.update()

        self.player.draw(screen)
        self.player.sprite.lasers.draw(screen)

        self.blocks.draw(screen)
        #atualiza todos os sprites dos grupos
        #desenha os sprites dos grupos

if __name__ == '__main__':
    pygame.init()
    screen_width = 768
    screen_height = 768
    screen = pygame.display.set_mode((screen_width,screen_height))
    clock = pygame.time.Clock()
    game = Jogo()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((30,30,30))
        game.rodar()

        pygame.display.flip()
        clock.tick(60)