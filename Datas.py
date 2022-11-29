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