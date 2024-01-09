# https://panda.ime.usp.br/aulasPython/static/aulasPython/aula08.html
# Exercício 8.3
# Nota: Exercício 12 da lista sobre inteiros.
# Dados dois inteiros positivos calcular o máximo divisor comum entre eles usando o algoritmo de Euclides.
# 1
# 2
# 3
# 4
# 5
# 6
# 7

def main():
    a = i
    b = j
    aux = 0

    while b != 0:
        aux = b
        b = (a % b)
        a = aux
        
    print(a)

i = int(input("Insira um número inteiro positivo: "))
j = int(input("Insira outro número inteiro positivo: "))

main()