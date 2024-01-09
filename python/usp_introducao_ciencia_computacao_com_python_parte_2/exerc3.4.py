"""Exercício 2: Triângulos semelhantes
Ainda na classe Triangulo, escreva um método semelhantes(triangulo) que recebe um objeto do tipo Triangulo como parâmetro e verifica se o triângulo atual é semelhante ao triângulo passado como parâmetro. Caso positivo, o método deve devolver True. Caso negativo, deve devolver False

Um triângulo é semelhante a outro triângulo se a razão (divisão) entre os comprimentos dos seus lados forem iguais.

Dica: você pode colocar os lados de cada um dos triângulos em uma lista diferente e ordená-las.

Exemplo:
t1 = Triangulo(2, 3, 5)
t2 = Triangulo(4, 6, 10)
t1.semelhantes(t2)
# deve devolver True
"""
class Triangulo:
    def __init__(self, x, y, z) :
        self.a = x
        self.b = y
        self.c = z
    
    def semelhantes(self, t):      
        aux1 = max(self.a, self.b, self.c)
        aux2 = min(self.a, self.b, self.c)
        lst = [self.a, self.b, self.c]
        lst.remove(aux1)
        lst.remove(aux2)
        aux3 = lst[0]

        t_max = max(t.a, t.b, t.c)
        t_min = min(t.a, t.b, t.c)
        lst = [t.a, t.b, t.c]
        lst.remove(t_max)
        lst.remove(t_min)
        t_med = lst[0]
        
        ratio = t_max/aux1
        
        if t_med/aux3 != ratio:
            return False
        elif t_min/aux2 != ratio:
            return False
        else:
            return True