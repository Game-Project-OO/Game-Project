class Ranking:
    def __init__(self,max_entradas=10):
        self.caminho = "../dados/ranking.txt"
        self.max_entradas = max_entradas
        self.ranking = self.carregar()

    def carregar(self):
        lista = []
        try:
            with open(self.caminho, "r") as arquivo:
                for linha in arquivo:
                    nome, pontuacao = linha.strip().split(",")
                    lista.append([nome, int(pontuacao)])
        except FileNotFoundError:
            pass
        return lista
    
    def salvar(self,nome,pontuacao):
        self.ranking.append([nome,pontuacao])
        self.ranking.sort(key=lambda x: x[1], reverse=True)
        self.ranking = self.ranking[:self.max_entradas]
        with open(self.caminho, "w") as arquivo:
            for nome, pontos in self.ranking:
                arquivo.write(f"{nome},{pontos}\n")

    def exibir(self):
        for i, (nome,pontos) in enumerate(self.ranking, start=1):
            print(f"{i}. {nome} - {pontos}")