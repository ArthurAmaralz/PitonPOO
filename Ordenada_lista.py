
def ordenada(lista):
    list_ori = lista[:]                 # Clonando a lista principal
    for i in range(len(lista)):         # Um primeiro for, para puxar a primeira possicao da variavel
        val = i
        for j in range(i+1,len(lista)): # No segundo for, é puxado o segundo valor e comparado se é menos que o anterior
            if lista[j] < lista[val]:   # Sendo menor ele sera substituido
                val = j                 # E tera sua prosiçao trocada com o valor anterior na linha abaixo
        lista[i], lista[val] = lista[val], lista[i]
    if lista != list_ori:
        #print(False)
        return False
    #print(True)
    return True


# orde = [1,2,3,4,5,6,7,8,9,10,11,1,2,3,4,12,13,14,15,16,17,18,]
# ordenada(orde)

