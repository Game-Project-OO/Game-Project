class Ranking:
    def __init__(self,max_entradas=10):
        self.__caminho = "../dados/ranking.txt"
        self.__max_entradas = max_entradas
        self.__ranking = self.carregar()

    @property
    def caminho(self):
        return self.__caminho

    @caminho.setter
    def caminho(self, value):
        self.__caminho = value

    @property
    def max_entradas(self):
        return self.__max_entradas

    @max_entradas.setter
    def max_entradas(self, value):
        self.__max_entradas = value

    @property
    def ranking(self):
        return self.__ranking

    @ranking.setter
    def ranking(self, value):
        self.__ranking = value

    def carregar(self) -> list:
        lista = []
        try:
            with open(self.caminho, "r") as arquivo:
                for linha in arquivo:
                    nome, pontuacao = linha.strip().split(",")
                    lista.append([nome, int(pontuacao)])
        except FileNotFoundError:
            pass
        return lista
    
    def salvar(self,nome,pontuacao) -> None:
        self.ranking.append([nome,pontuacao])
        self.ranking.sort(key=lambda x: x[1], reverse=True)
        self.ranking = self.ranking[:self.max_entradas]
        with open(self.caminho, "w") as arquivo:
            for nome, pontos in self.ranking:
                arquivo.write(f"{nome},{pontos}\n")

    def exibir(self) -> None:
        for i, (nome,pontos) in enumerate(self.ranking, start=1):
            print(f"{i}. {nome} - {pontos}")