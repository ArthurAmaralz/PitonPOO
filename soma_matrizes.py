def dimensoes(matriz):
    tam_matriz = (len(matriz), len(matriz[0]))
    return tam_matriz

def soma_matrizes(m1, m2):
    matriz_soma = []
    dim = (len(m1), len(m1[0]))
    if dimensoes(m1) == dimensoes(m2):
        for i in range(dim[0]):
            linha = []
            for j in range(dim[1]):
                linha.append(m1[i][j]+m2[i][j])
            matriz_soma.append(linha)
    else:
        return False
    print(matriz_soma)
    return matriz_soma

'''
### Exemplos que podem ser ultilizados ###
m1 = [[1], [2], [3]]
m2 = [[2, 3, 4], [5, 6, 7]]

ou

m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]

soma_matrizes(m1, m2)
'''