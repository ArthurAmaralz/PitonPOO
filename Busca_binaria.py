
def busca_bin(lista, valor):
    inicio = 0
    fim = len(lista)-1
    lista = sorted(lista)

    while inicio <= fim:
        metade = (inicio + fim) // 2
        if lista[metade] == valor:
            return metade
        else:
            if lista[metade] < valor:
                inicio += 1
            else:
                fim -= 1
    return -1

# l = [1,2,3,4,5,6,7,8,9,10,11]

# print(busca_bin(l,10))

