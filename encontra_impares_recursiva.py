def encontra_impares(lista):
    if len(lista) == 0:
        return []
    impares = lista.pop(0)  # salva o valor removido na primeira posicao
    if impares % 2 != 0:
        return [impares] + encontra_impares(lista)  # Se o valor removido for impar, ele votar a adicionar na lista
    return encontra_impares(lista)  # retorna a lista apenas com os valores impares


print(encontra_impares([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))
