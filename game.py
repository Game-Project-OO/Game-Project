import sys, pygame

pygame.init()

tamanho_tela = altura, largura = 1366, 768
velocidade = [2, 2]
cor_fundo = pygame.image.load('IMAGENS/TELA_NOME2.png')

tela = pygame.display.set_mode(tamanho_tela)
nave = pygame.image.load('IMAGENS/nave.png')
nave_redimensionada = pygame.transform.scale(nave, (50,70))
nave_rect = nave_redimensionada.get_rect()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()

    nave_rect = nave_rect.move(velocidade)
    if nave_rect.left > 0 or nave_rect.right < largura:
        velocidade[0] = -velocidade[0]
    if nave_rect.top > 0 or nave_rect.bottom < altura:
        velocidade[1] = -velocidade[1]

    tela.blit(cor_fundo, (-100,-70))
    tela.blit(nave_redimensionada, nave_rect)

    pygame.display.flip()