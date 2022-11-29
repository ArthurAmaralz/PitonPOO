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