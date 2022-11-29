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