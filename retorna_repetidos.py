#Crie e teste uma função que recebe uma sequência de números inteiros e retorna uma nova lista com todos aqueles
# que foram repetidos pelo menos uma vez logo em sequência. Por exemplo,
#Input: [2,4,3,3,6,1,1,2,4,3]
#Output: [3,1]

def repetidos(lista):
    repetidos = []
    count = 0
    for i in lista:
        count += 1
        if len(lista) != count:
            # print(i, lista[count])
            if i == lista[count]:
                repetidos.append(i)
    return repetidos


lista_rept = [2, 4, 3, 3, 6, 1, 1, 2, 4, 3]

rp = repetidos(lista_rept)
rp
