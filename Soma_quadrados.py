# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
# Faça este mesmo programa em duas versões: sem list comprehension e com list comprehension.

# sem list compreheension
vetor = [1,2,3,4,5,6,7,8,9,10]
vetor_quadrado = []

for i in vetor:
  i *= i
  vetor_quadrado.append(i)
print(vetor_quadrado)

