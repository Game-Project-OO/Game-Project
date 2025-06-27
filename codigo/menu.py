import pygame, sys
from main import start_game
from var_globais import *
from ranking import Ranking

class Menu:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Menu do Jogo")
        self.__screen = pygame.display.set_mode((largura_tela, altura_tela))
        self.__clock = pygame.time.Clock()
        self.__font = pygame.font.Font(fonte, 30)
        self.__controles_imagem = pygame.image.load('../imagens/controls_image.png')
        self.__volume_musica = 0.5
        self.__volume_game = 0.5
        self.__menu_click_start = pygame.mixer.Sound('../sons/menu_sound.mp3')
        self.__menu_click_start.set_volume(self.volume_game)

        pygame.mixer.music.load('../sons/menu_music.mp3')
        pygame.mixer.music.set_volume(self.volume_musica)
        pygame.mixer.music.play(-1)

    @property
    def screen(self):
        return self.__screen

    @screen.setter
    def screen(self, value):
        self.__screen = value

    @property
    def clock(self):
        return self.__clock

    @clock.setter
    def clock(self, value):
        self.__clock = value

    @property
    def font(self):
        return self.__font

    @font.setter
    def font(self, value):
        self.__font = value

    @property
    def controles_imagem(self):
        return self.__controles_imagem

    @controles_imagem.setter
    def controles_imagem(self, value):
        self.__controles_imagem = value

    @property
    def volume_musica(self):
        return self.__volume_musica

    @volume_musica.setter
    def volume_musica(self, value):
        self.__volume_musica = value

    @property
    def volume_game(self):
        return self.__volume_game

    @volume_game.setter
    def volume_game(self, value):
        self.__volume_game = value

    @property
    def menu_click_start(self):
        return self.__menu_click_start

    @menu_click_start.setter
    def menu_click_start(self, value):
        self.__menu_click_start = value

    @property
    def menu_click_start(self):
        return self.__menu_click_start

    @menu_click_start.setter
    def menu_click_start(self, value):
        self.__menu_click_start = value

    def desenhar_menu(self, opcoes, selecionado, titulo="", info="") -> None:
        self.screen.fill(cor_menu_fundo)

        if titulo:
            titulo_txt = self.font.render(titulo, True, cor_menu_branco)
            titulo_rect = titulo_txt.get_rect(center=(largura_tela / 2, 100))
            self.screen.blit(titulo_txt, titulo_rect)

        for i, opcao in enumerate(opcoes):
            cor = cor_menu_texto_selecionado if i == selecionado else cor_menu_branco
            texto = self.font.render(opcao, True, cor)
            rect = texto.get_rect(center=(largura_tela / 2, 300 + i * 60))
            self.screen.blit(texto, rect)

        if info:
            info_txt = self.font.render(info, True, cor_menu_branco)
            info_rect = info_txt.get_rect(center=(largura_tela / 2, altura_tela - 60))
            self.screen.blit(info_txt, info_rect)

        pygame.display.flip()
    
    def mostrar_ranking(self) -> None:
        ranking_obj = Ranking()
        ranking_obj.carregar()
        top_5 = ranking_obj.ranking[:5]

        selecionado = 0
        executando = True

        while executando:
            self.screen.fill(cor_menu_fundo)

            titulo_txt = self.font.render("TOP 5 RANKING", True, cor_menu_branco)
            titulo_rect = titulo_txt.get_rect(center=(largura_tela / 2, 100))
            self.screen.blit(titulo_txt, titulo_rect)

            for i, (nome, pontos) in enumerate(top_5):
                rank_txt = self.font.render(f"{i+1}. {nome} - {pontos}", True, cor_menu_branco)
                rank_rect = rank_txt.get_rect(center=(largura_tela / 2, 200 + i * 60))
                self.screen.blit(rank_txt, rank_rect)

            cor_voltar = cor_menu_texto_selecionado if selecionado == 0 else cor_menu_branco
            texto_voltar = self.font.render("VOLTAR", True, cor_voltar)
            rect_voltar = texto_voltar.get_rect(center=(largura_tela / 2, altura_tela - 100))
            self.screen.blit(texto_voltar, rect_voltar)

            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        self.menu_click_start.play()
                        self.menu_click_start.set_volume(self.volume_game)
                        executando = False
            self.clock.tick(30)
    
    def mostrar_controles(self) -> None:
        selecionado = 0
        executando = True

        while executando:
            self.screen.fill(cor_menu_fundo)

            titulo_txt = self.font.render("CONTROLES", True, cor_menu_branco)
            titulo_rect = titulo_txt.get_rect(center=(largura_tela / 2, 100))
            self.screen.blit(titulo_txt, titulo_rect)

            controls_rect = self.controles_imagem.get_rect(center=(largura_tela / 2, altura_tela / 2))
            self.screen.blit(self.controles_imagem, controls_rect)

            cor_voltar = cor_menu_texto_selecionado if selecionado == 0 else cor_menu_branco
            texto_voltar = self.font.render("VOLTAR", True, cor_voltar)
            rect_voltar = texto_voltar.get_rect(center=(largura_tela / 2, altura_tela - 100))
            self.screen.blit(texto_voltar, rect_voltar)

            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        self.menu_click_start.play()
                        self.menu_click_start.set_volume(self.volume_game)
                        executando = False
            self.clock.tick(30)

    def mostrar_opcoes(self) -> None:
        opcoes = ["- VOLUME MUSICA +", "- VOLUME EFEITOS +", "CONTROLES", "VOLTAR"]
        selecionado = 0
        executando = True

        while executando:
            info = f"MUSICA: {int(self.volume_musica * 100)}  EFEITOS: {int(self.volume_game * 100)}"
            self.desenhar_menu(opcoes, selecionado, "OPCOES", info)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_UP:
                        self.menu_click_start.play()
                        self.menu_click_start.set_volume(self.volume_game)
                        selecionado = (selecionado - 1) % len(opcoes)
                    elif evento.key == pygame.K_DOWN:
                        self.menu_click_start.play()
                        self.menu_click_start.set_volume(self.volume_game)
                        selecionado = (selecionado + 1) % len(opcoes)
                    elif evento.key == pygame.K_RIGHT:
                        self.menu_click_start.play()
                        self.menu_click_start.set_volume(self.volume_game)
                        opcao = opcoes[selecionado]
                        if opcao == "- VOLUME MUSICA +":
                            self.menu_click_start.play()
                            self.volume_musica = min(self.volume_musica + 0.1, 1.0)
                            pygame.mixer.music.set_volume(self.volume_musica)
                        elif opcao == "- VOLUME EFEITOS +":
                            self.menu_click_start.play()
                            self.volume_game = min(self.volume_game + 0.1, 1.0)
                            self.menu_click_start.set_volume(self.volume_game)
                    elif evento.key == pygame.K_LEFT:
                        self.menu_click_start.play()
                        self.menu_click_start.set_volume(self.volume_game)
                        opcao = opcoes[selecionado]
                        if opcao == "- VOLUME MUSICA +":
                            self.menu_click_start.play()
                            self.volume_musica = max(self.volume_musica - 0.1, 0.0)
                            self.menu_click_start.set_volume(self.volume_game)
                            pygame.mixer.music.set_volume(self.volume_musica)
                        if opcao == "- VOLUME EFEITOS +":
                            self.menu_click_start.play()
                            self.volume_game = max(self.volume_game - 0.1, 0.0)
                            self.menu_click_start.set_volume(self.volume_game)
                    elif evento.key == pygame.K_RETURN:
                        self.menu_click_start.play()
                        self.menu_click_start.set_volume(self.volume_game)
                        opcao = opcoes[selecionado]
                        if opcao == "CONTROLES":
                            self.menu_click_start.play()
                            self.menu_click_start.set_volume(self.volume_game)
                            self.mostrar_controles()
                        elif opcao == "VOLTAR":
                            self.menu_click_start.play()
                            self.menu_click_start.set_volume(self.volume_game)
                            executando = False
            self.clock.tick(30)

    def mostrar_menu_principal(self) -> None:
        opcoes = ["START", "OPCOES", "RANKING","SAIR"]
        selecionado = 0
        executando = True

        while executando:
            self.desenhar_menu(opcoes, selecionado, "Crazy Nave")

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    executando = False
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_UP:
                        self.menu_click_start.play()
                        self.menu_click_start.set_volume(self.volume_game)
                        selecionado = (selecionado - 1) % len(opcoes)
                    elif evento.key == pygame.K_DOWN:
                        self.menu_click_start.play()
                        self.menu_click_start.set_volume(self.volume_game)
                        selecionado = (selecionado + 1) % len(opcoes)
                    elif evento.key == pygame.K_RETURN:
                        self.menu_click_start.play()
                        self.menu_click_start.set_volume(self.volume_game)
                        opcao = opcoes[selecionado]
                        if opcao == "START":
                            self.menu_click_start.play()
                            pygame.mixer.music.stop()
                            start_game(self.volume_musica, self.volume_game)
                            pygame.mixer.music.play(-1) 
                        elif opcao == "RANKING":
                            self.menu_click_start.play()
                            self.menu_click_start.set_volume(self.volume_game)
                            self.mostrar_ranking()
                        elif opcao == "OPCOES":
                            self.menu_click_start.play()
                            self.menu_click_start.set_volume(self.volume_game)
                            self.mostrar_opcoes()
                        elif opcao == "SAIR":
                            self.menu_click_start.play()
                            self.menu_click_start.set_volume(self.volume_game)
                            executando = False

            self.clock.tick(30)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    menu = Menu()
    menu.mostrar_menu_principal()