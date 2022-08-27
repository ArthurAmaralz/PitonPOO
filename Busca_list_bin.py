def busca(lista, valor):
    inicio = 0
    fim = len(lista)-1
    lista = sorted(lista)

    while inicio <= fim:
        metade = (inicio + fim) // 2
        if lista[metade] == valor:
            print(metade)
            return metade
        else:
            if lista[metade] < valor:
                inicio = metade + 1
                print(metade)
            else:
                fim = metade - 1
                print(metade)
    return False

