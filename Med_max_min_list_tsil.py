'''a) Faça um programa que permita ao usuário inserir quantos números quiser em uma lista, até que ele passe "S" ou "s".

b) Depois disso, crie um programa em que o usuário possa solicitar, por quantas vezes quiser qualquer uma das seguintes opções, até que pressione "S" ou "s" para encerrar:

"med" para ver a média dos números da lista
"max" para ver o maior número da lista
"min" para ver o menor número da lista
"list" para ver a lista
"tsil" para ver a lista invertida '''


def med(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma / len(lista)


def max(lista):
    max = 0

    for i in range(len(lista)):
        for j in lista:
            if i == 0:
                max = j
            if j > max:
                max = j
    return max


def min(lista):
    min = 0

    for i in range(len(lista)):
        for j in lista:
            if i == 0:
                min = j
            if j < min:
                min = j
    return min


def reverse(lista):
    lista_rev = []
    for i in range(len(lista), 0, -1):
        lista_rev.append(lista[i - 1])
    return lista_rev


lista = []
loop = True

while loop:
    num = input('Digite um valor: ')

    if num in 'Ss':
        print(
            "Escolha uma das opções a baixo:\n'med' para ver a média dos números da lista\n'max' para ver o maior número da lista\n'min' para ver o menor número da lista\n'list' para ver a lista\n'tsil' para ver a lista invertida:\n ")
        while True:
            opcao = input()

            if opcao in 'Ss':
                loop = False
                break
            elif opcao == 'med':
                print(med(lista))
            elif opcao == 'max':
                print(max(lista))
            elif opcao == 'min':
                print(min(lista))
            elif opcao == 'list':
                print(lista)
            else:
                print(reverse(lista))
    else:
        lista.append(int(num))