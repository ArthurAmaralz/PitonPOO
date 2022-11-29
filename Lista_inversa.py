#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa. NÃO VALE USAR REVERSE

lista = [1,2,3,4,5,6,7,8,9,10]
lista_reversa = []
#lista [::-1]

for i in range(len(lista),0,-1):
  lista_reversa.append(i)
print(lista_reversa)