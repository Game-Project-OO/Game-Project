import pygame

pygame.mixer.init()

tela_menu = pygame.image.load('IMAGENS/TELA_NOME2.png')
musica_menu = pygame.mixer.Sound('SONS/musicaMenu.mp3')

musica_gameplay = pygame.mixer.Sound('SONS/musicaGameplay.mp3')