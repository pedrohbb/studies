# Exercício 2 - Desafio da videoaula
# Como pedido na videoaula desta semana, escreva um programa que calcula as raízes de uma equação do segundo grau.
# O programa deve receber os parâmetros  a, b e c da equação  ax^2 + bx + c respectivamente, e imprimir o resultado 
# na saída da seguinte maneira:
# Quando não houver raízes reais imprima:
# esta equação não possui raízes reais
# Quando houver apenas uma raiz (ou seja, uma raiz com multiplicidade 2) imprima:
# a raiz desta equação é X
# ou
# a raiz dupla desta equação é X
# onde X é o valor da raiz dupla
# Quando houver duas raízes reais imprima:
# as raízes da equação são X e Y
# onde X e Y são os valor das raízes.
# Além disso, no caso de existirem 2 raízes reais distintas, elas devem ser impressas em ordem crescente. Exemplos:
# as raízes da equação são 1.0 e 2.0
# as raízes da equação são -2.0 e 0.0

a = float(input("Digite o coeficiente 'a': "))
b = float(input("Digite o coeficiente 'b': "))
c = float(input("Digite o coeficiente 'c': "))

delta = b**2 - 4*a*c

if delta >= 0:
    x1 = (-b + delta**(1/2))/(2*a)
    x2 = (-b - delta**(1/2))/(2*a)
    if x1 == x2:
        print(f"a raiz desta equação é {x1}")
    else:
        if x1 < x2:
            print(f"as raízes da equação são {x1} e {x2}")
        else:
            print(f"as raízes da equação são {x2} e {x1}")

if delta < 0:
    print("esta equação não possui raízes reais")