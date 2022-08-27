class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        perimetro = self.a + self.b + self.c
        return perimetro

    def tipo_lado(self):
        if self.a == self.b and self.a == self.c and self.c == self.b :
            return 'equilátero'
        elif self.a != self.b and self.a != self.c and self.c != self.b :
            return 'escaleno'
        else:
            return 'isósceles'

    def retangulo(self):
        lados = [self.a, self.b, self.c]
        hip = max(lados)
        cateto1 = min(lados)
        cateto2 = int((hip**2 - cateto1**2)**(1/2))

        if cateto2 in lados:
            return True
        else:
            return False

    def semelhantes(self, triangulo):
        tri_1 = [self.a, self.b, self.c] # Puxa os valores referentes ao primeiro triangulo
        tri_2 = [triangulo.a, triangulo.b, triangulo.c] # Puxa os valores referentes ao segundo triangulo

        maior = sorted(max(tri_1,tri_2))    # Ordena a lista pelo maior conjunto e em ordem crescente
        menor = sorted(min(tri_1,tri_2))    # Ordena a lista pelo menor conjunto e em ordem crescente
        count = 0

        for i in range(3):
            if maior[i] % menor[i] == 0:
                count += 1
                if count == 3:  # Como o desafio pedia apenas um retornor de True, achei essa a melhor forma
                    return True
            else:
                return False




