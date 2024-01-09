"""Estes exercícios são baseados na classe Triangulo que você deve ter criado na lista de exercícios obrigatórios desta semana.

Exercício 1: Triângulos retângulos
Escreva, na classe Triangulo, o método retangulo() que devolve True se o triângulo for retângulo, e False caso contrário.

Exemplos:
t = Triangulo(1, 3, 5)
t.retangulo()
# deve devolver False

u = Triangulo(3, 4, 5)
u.retangulo()
# deve devolver True
"""

class Triangulo:
    def __init__(self, x, y, z) :
        self.a = x
        self.b = y
        self.c = z
    
    def retangulo(self):      
        hip = max(self.a, self.b, self.c)

        if hip**2 == (self.a)**2 + (self.b)**2:
            return True
        else:
            return False

t = Triangulo(3,4,5)

print(t)