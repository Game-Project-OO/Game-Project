import pygame, sys
import time
from var_globais import *

class Animacoes(pygame.sprite.Sprite):
    def __init__(self,duracao=3):
        self.__fonte = pygame.font.Font('../fonte/Pixeled.ttf',30)
        self.__duracao = duracao
        self.__ativa = False
        self.__inicio = 0
        self.__mensagem = ""
        self.__sound = pygame.mixer.Sound('../sons/risada.mp3')

    @property
    def fonte(self):
        return self.__fonte

    @fonte.setter
    def fonte(self, value):
        self.__fonte = value

    @property
    def duracao(self):
        return self.__duracao

    @duracao.setter
    def duracao(self, value):
        self.__duracao = value

    @property
    def ativa(self):
        return self.__ativa

    @ativa.setter
    def ativa(self, value):
        self.__ativa = value

    @property
    def inicio(self):
        return self.__inicio

    @inicio.setter
    def inicio(self, value):
        self.__inicio = value

    @property
    def mensagem(self):
        return self.__mensagem

    @mensagem.setter
    def mensagem(self, value):
        self.__mensagem = value

    @property
    def sound(self):
        return self.__sound

    @sound.setter
    def sound(self, value):
        self.__sound = value
    
    def iniciar_animacao(self) -> None:
        self.ativa = True
        self.inicio = time.time()
        self.sound.play()
        self.mensagem = "PROXIMA ONDA EM"
    
    def update(self,screen) -> bool:
        if not self.ativa:
            return False
        
        tempo_passado = time.time() - self.inicio
        tempo_restante = int(self.duracao - tempo_passado) + 1

        if tempo_passado >= self.duracao:
            self.ativa = False
            return False
        
        texto = f"{self.mensagem} {tempo_restante}..."
        imagem_texto = self.fonte.render(texto,False,"white")
        posicao_texto = imagem_texto.get_rect(center=(largura_tela // 2, altura_tela // 2))

        screen.blit(imagem_texto,posicao_texto)
        return True