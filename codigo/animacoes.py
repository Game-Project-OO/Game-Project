import pygame, sys
import time
from var_globais import *

class Animacoes(pygame.sprite.Sprite):
    def __init__(self,duracao=3):
        self.fonte = pygame.font.Font('../fonte/Pixeled.ttf',30)
        self.duracao = duracao
        self.ativa = False
        self.inicio = 0
        self.mensagem = ""
    
    def iniciar_animacao(self):
        self.ativa = True
        self.inicio = time.time()
        self.mensagem = "Proxima onda em"
    
    def update(self,screen):
        if not self.ativa:
            return False
        
        tempo_passado = time.time() - self.inicio
        tempo_restante = int(self.duracao - tempo_passado) + 1

        if tempo_passado >= self.duracao:
            self.ativa = False
            return False
        
        texto = f"{self.mensagem} {tempo_restante}..."
        imagem_texto = self.fonte.render(texto,False,"white")
        posicao_texto = imagem_texto.get_rect(center=(screen_width // 2, screen_height // 2))

        screen.blit(imagem_texto,posicao_texto)
        return True