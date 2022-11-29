class Arvore:

    def __init__(self, dados):
        self.esquerda = None
        self.direita = None
        self.dados = dados

    def nos(self, dados, index):
        if self.dados[index]:
            #o noddeve ser inserido na subárvore esquerda
            if dados[index] < self.dados[index]:
                if self.esquerda == None:
                    self.esquerda = Arvore(dados)
                else:
                    self.esquerda.nos(dados, index)
            #o nodo deve ser inserido na subárvore direita
            elif dados[index] > self.dados[index]:
                if self.direita == None:
                    self.direita = Arvore(dados)
                else:
                    self.direita.nos(dados, index)
        else:
            #o nodo deve ser inserido na raiz
            self.dadofim = dados

tree = Arvore()
