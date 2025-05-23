import pygame

janela = pygame.display.set_mode([1280, 720])

pygame.display.set_caption('Primeiros testes')
imagemFundo = pygame.image.load('IMAGENS/TELA_NOME2.png')
navePlayer = pygame.image.load('IMAGENS/player.png')
naveInimigo = pygame.image.load('IMAGENS/enemy.png')
lula = pygame.image.load('IMAGENS/aa.png')

posxPlayer = 590
posyPlayer = 500
velPlayer = 10

loop = True

while loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False
    
    teclas = pygame.key.get_pressed()
    
    #se a tecla pressionada for SETA CIMA, vai pra riba.
    if teclas[pygame.K_UP]:
        posyPlayer -= velPlayer
    if teclas[pygame.K_DOWN]:
        posyPlayer += velPlayer
    if teclas[pygame.K_LEFT]:
        posxPlayer -= velPlayer
    if teclas[pygame.K_RIGHT]:
        posxPlayer += velPlayer
    
    if teclas[pygame.K_BACKSPACE]:
        janela.blit(lula, (0,0))
        pygame.display.update()
    
    janela.blit(imagemFundo, (0,0))
    janela.blit(navePlayer, (posxPlayer, posyPlayer))
    janela.blit(naveInimigo, (594, 50))
    
    pygame.display.update()