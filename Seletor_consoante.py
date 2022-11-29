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