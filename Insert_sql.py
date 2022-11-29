saldo = 0
transacoes = []

while True:
  print('1) Depósito')
  print('2) Saque')

  opcao = int(input('Informe a opção desejada: '))
  if (opcao == 0): break

  valor = float(input('Informe o valor da transação: '))

  if opcao == 1:
    saldo = saldo + valor
    transacoes.append({ 'deposito': valor })
  elif opcao == 2:
    saldo = saldo - valor
    transacoes.append({ 'saque': valor })