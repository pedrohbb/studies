# Exercício 1
# Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros correspondentes à largura e à altura de um retângulo, respectivamente. O programa deve imprimir, usando repetições encaixadas (laços aninhados), uma cadeia de caracteres que represente o retângulo informado com caracteres '#' na saída.
# Por exemplo:
# digite a largura: 10
# digite a altura: 3
# ##########
# ##########
# ##########
# digite a largura: 2
# digite a altura: 2
# ##
# ##

m = int(input("digite a largura: "))
n = int(input("digite a altura: "))

for j in range(n):
    print('#'*m)

