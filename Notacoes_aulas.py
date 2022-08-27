### Notações para futuros usos ###

def peso_altura():
    return 63, 1.76


peso, altura = peso_altura()  # Peso e altura irão receber os valores declarados na função

print(peso)
print(altura)

'''---------------------------------------------------'''

a = 10
b = 5

a, b = b, a  # Essa atribuição permite inverter o valor das variaveis em uma unica linha

'''---------------------------------------------------'''


def pagamento_semanal(valor_hora, num_hora=40):  # atribuindo um valor padrão para o caso de não atribuição
    return valor_hora * num_hora


pagamento_semanal(100, 36)
pagamento_semanal(80)  # Sem parametro

'''---------------------------------------------------'''


