"""Exercício 2: Tipos de triângulos
Na classe triângulo, definida na Questão 1, escreva o metodo tipo_lado() que devolve uma string dizendo se o triângulo é:

isósceles (dois lados iguais)

equilátero (todos os lados iguais)

escaleno (todos os lados diferentes)

Note que se o triângulo for equilátero, a função não deve devolver isóceles.

Exemplos:

t = Triangulo(4, 4, 4)
t.tipo_lado()
# deve devolver 'equilátero'

u = Triangulo(3, 4, 5)
.tipo_lado()
# deve devolver 'escaleno'"""

class Triangulo:
    def __init__(self, a, b, c):
        self.lado1 = a
        self.lado2 = b
        self.lado3 = c
    
    def perimetro(self):
        P = self.lado1 + self.lado2 + self.lado3
        return P

    def tipo_lado(self):
        count=0
        if self.lado1 == self.lado2:
            count += 1
        
        if self.lado1 == self.lado3:
            count += 1

        if self.lado2 == self.lado3:
            count += 1
        
        if count == 3:
            return 'equilátero'       
        elif count == 1:
            return 'isósceles'
        else:
            return 'escaleno'
        
if __name__ == '__main__':

    t = Triangulo(3,4,4)
    print(t.perimetro())
    print(t.tipo_lado())