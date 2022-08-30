def incomodam(n):
    if n <= 0:
        return ""
    if n >= 1:
        return "incomodam " * n

def elefantes(n, num = 0):
    if n <= 0:
        return ""
    if n == 1:
        return ("Um elefante incomoda muita gente\n")
    if num == 0:  # condicao para não repetir a ultima linha
        return elefantes(n - 1, num + 1) + str(n) + " elefantes " + incomodam(n) + "muito mais\n"
    if n > 1:
        return elefantes(n) + str(n) + " elefantes incomodam muita gente\n"


# print(elefantes(4))




