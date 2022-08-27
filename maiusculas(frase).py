
def maiusculas(frase):
    up = ''
    for i in range(len(frase)):
        valor_ord = ord(frase[i])
        if 65 <= valor_ord <= 90:
            up += frase[i]
    return up

