# Arthur Amaral de Lima

from random import randrange

class Gerador:
    def __init__(self, limite=1, escopo=50):
        self.lista = []
        for i in range(limite):
            self.lista.append(randrange(escopo))

    def lista_resultado(self):
        return self.lista

lista = Gerador(1, 50) # Aqui como parametro recebemos o numero de termos a ser gerados e o escopo do valor apresentado

lista.lista_resultado()
#print(valor_gerador.list_aleatorio())

## verificar se os dados estão sendo ultilizados ou consumidos
