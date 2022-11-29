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