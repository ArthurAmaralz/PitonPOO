# Arthur Amaral de Lima

# Faça um Programa que leia uma lista de 10 caracteres e passe apenas as consoantes para uma nova lista.
# Depois disso, imprima na tela quais são estas consoantes, e quantas elas são.

lista = ['a','b','c','d','e','f','g','h','i','j']
count = 0
lista_consoante = []

for i in lista:
  if i not in 'AaEeIiOoUu':
    lista_consoante.append(i)
    count += 1
print(f'Total de {count} consoantes, sendo elas : {lista_consoante}')


#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

lista = ['a','b','c','d','e','f','g','h','i','j']
aluno = 0

for i in lista:
  if i not in 'AaEeIiOoUu':
    aluno += 1
print(aluno)

# lista = ['a','b','c','d','e','f','g','h','i','j']
# consoantes = ['b','c','d','f','g','h','j','l','m','n','p','q','r','s','t','v','x','z','y']
# count = 0
#
# for i in lista:
#   if i in consoantes:
#     count +=1
# print(count)

#Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

vetor, par, impar = [], [], []

for i in range(5):
  valor = int(input(f'Digite o {i+1}º valor: '))
  vetor.append(valor)
  if valor % 2 == 0:
    par.append(valor)
  else:
    impar.append(valor)

vetor = [vetor, par, impar]

#vetor.append(par, impar)
#vetor.append(impar)
print(vetor[0])
print(vetor[1])
print(vetor[2])


#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.

lista_media = []
count, aluno, soma = 0, 0, 0

while True:

    for i in range(4):
        nota = float(input(f'{aluno + 1}º Aluno - Digite a {i + 1}º nota: '))
        soma += nota

    media = soma / 4
    soma = 0
    aluno += 1
    lista_media.append(media)
    print(media)

    if media >= 7:
        count += 1
    if aluno == 10:
        break
print(f'Alunos com media maior/igual a 7: {count}')
print(lista_media)

#Data com mês por extenso. Construa uma função que receba uma data no formato "DD/MM/AAAA" e devolva uma string no formato D
# de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

def trans_data(data:str) -> str:
  # data = data.split("/")
  # dia = data[0]
  # mes = data[1]
  # ano = data[2]

  dia = data[0:2]
  mes = data[3:5]
  ano = data[6:]

  meses = ["janeiro", "fevereiro", "marco", "abril","maio", "junho","julho","agosto", "setembro", "outubro", "novembro","dezembro"]

  numero_mes = int(mes)
  nome_do_mes = meses[numero_mes - 1]

  # print(f"{dia} de {nome_do_mes} de {ano}")
  return f"{dia} de {nome_do_mes} de {ano}"

#Faça o oposto do exercício anterior: Uma função que receba os valores por extenso como argumento
# (DD, mes_por_extenso, AAAA) e retorne a data na forma DD/MM/AAAA

def trans_data2(data: str) -> str:
    data = data.split(",")
    dia = data[0]
    mes = data[1]
    ano = data[2]

    count = 0

    meses = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro",
             "novembro", "dezembro"]

    for i in meses:
        count += 1
        if mes == i:
            mes = count

    # numero_mes = int(mes)
    # nome_do_mes = meses[numero_mes - 1]

    return f"{dia}/{mes}/{ano}"

datas = trans_data2('28,agosto,1993')

datas

#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa. NÃO VALE USAR REVERSE

lista = [1,2,3,4,5,6,7,8,9,10]
lista_reversa = []
#lista [::-1]

for i in range(len(lista),0,-1):
  lista_reversa.append(i)
print(lista_reversa)

# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
# Faça este mesmo programa em duas versões: sem list comprehension e com list comprehension.

# sem list compreheension
vetor = [1,2,3,4,5,6,7,8,9,10]
vetor_quadrado = []

for i in vetor:
  i *= i
  vetor_quadrado.append(i)
print(vetor_quadrado)

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

# ------------------------------------------------------------------------------------------

def mediana(lista):
  lista_ord = sorted(lista)
  if len(lista_ord) % 2 == 0:
    centro = int(len(lista_ord)/2)
    calc_mediana = sum(lista_ord[centro-1:centro+1])/2
    return calc_mediana
  else:
    centro = int(len(lista_ord)/2)
    calc_mediana = lista_ord[centro]
    return calc_mediana

def moda(lista):
  unico = []
  contar = []
  modas = []
  for i in lista:
    if i not in unico:
      unico.append(i)

  for x in unico:
    conta = 0
    for y in lista:
      if x == y:
        conta += 1
    contar.append(conta)

  for z in range(len(contar)):
    if max(contar) == contar[z]:
      modas.append(unico[z])
  return modas

def dp(lista):
  aux_desvio_padrao = []
  MA = sum(lista)/len(lista)
  for i in range(len(lista)):
    aux_desvio_padrao.append(((lista[i])-MA)**2)
  return ((sum(aux_desvio_padrao)/len(lista))**(1/2))


def estatistica(lista):
  v_minimo = min(lista)
  v_media = sum(lista)/len(lista)
  v_mediana = mediana(lista)
  v_moda = moda(lista)
  v_desviopadrao = dp(lista)
  v_maximo = max(lista)
  return v_minimo, v_media, v_mediana, v_moda, v_desviopadrao, v_maximo

numeros = [1,4,7,2,8,5,9,7,3,5,1,7]
minimo, media, mediana, moda, dp, maximo = estatistica(numeros)

