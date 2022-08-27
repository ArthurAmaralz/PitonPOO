
def soma_lista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        # Estudar mais a respeito
        return lista[0] + soma_lista(lista[1:])

print(soma_lista([2,3,6,9,13]))



