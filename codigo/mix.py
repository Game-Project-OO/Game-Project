import pygame

pygame.mixer.init()

tela_menu = pygame.image.load('../imagens/TELA_NOME2.png')
musica_menu = pygame.mixer.Sound('../sons/musicaMenu.mp3')

musica_gameplay = pygame.mixer.Sound('../sons/musicaGameplay.mp3')