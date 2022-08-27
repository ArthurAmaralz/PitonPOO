
def menor_nome(nomes):
    nome = ''
    for i in range(len(nomes)):
        sem_esp = nomes[i].replace(" ","")
        if i == 0:
            nome += sem_esp
        elif len(sem_esp) < len(nome):
            nome = sem_esp
    nome = nome.capitalize()
    print(nome)
    return nome

