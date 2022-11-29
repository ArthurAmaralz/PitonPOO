def func(*args, **kwargs):
    print(args)
    #print(kwargs['nome'], kwargs['sobrenome'],kwargs['ultimo'])
    for i in kwargs:
        print(kwargs[i])

lista = [1,2,3,4,5]
func(*lista, nome='Arthur', sobrenome='Amaral', ultimo='lima', test='qwerty')

dic = { 'chave1' : 'valor', 'chave2' : 'outro valor', 'chave3' : 'ultimo valor'}
for k,v in dic.items():
    print (v, k)

def inverter(a, b):
    print(a[b:])
    print(a[:b])
    return a[b:] + a[:b]

a = [1,2,3,4,5,6,7,8,9]
print(inverter(a,3))

def func(*args, **kwargs):
    print(args)
    print(kwargs['nome'], kwargs['sobrenome'])

dic = { 'chave1' : 'valor', 'chave2' : 'outro valor', 'chave3' : 'ultimo valor'}
for k,v in dic.items():
    print (k, v)

lista = [1,2,3,4,5]
func(*lista, nome='Arthur', sobrenome='Amaral')

lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='Luiz', sobrenome='Miranda')

print(*lista) # desempacota lista

linguagem_desejada = input('Digite a linguagem que você gostaria de aprender: ')

linguagens = ['Python', 'JavaScript', 'C#', 'Java']

if linguagem_desejada in linguagens:
  print(f'Faça o curso de {linguagem_desejada} conosco! :)')
else:
  print('Não temos esse curso disponível no momento :(')

pares = [0, 2, 4, 8, 10]
pares.insert(3, 6)
print(pares) #resultado: [0, 2, 4, 6, 8, 10]

string_original = "let's Code"
lista = list(string_original)
lista[0] = 'L'
lista.append('!')
string_final = ''.join(lista) # antes do . temos uma string vazia
print(string_final)
# resultado: "Let's Code!"
