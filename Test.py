def x(n):
    if n == 0:
        print(n)
    else:
        print(n)  # Dessa forma a fila puxa a ordem seguindo a sequencia padrão
        x(n-1)
        print(n)  # Aqui vemos a chamada das fila invertendo a ordem da sequencia, imprimindo o ultimo termo da fila
                  # primeiro e seguindo sucessivamente

x(10)
