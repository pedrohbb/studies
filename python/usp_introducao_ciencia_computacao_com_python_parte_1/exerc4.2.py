# Exercício 2
# Receba um número inteiro positivo na entrada e imprima os n primeiros números ímpares naturais. Para a saída, siga o formato do exemplo abaixo.
# Exemplo:
# 6 9

n = int(input("Digite um número natural: "))

i = 1
j = 1

while i <= n:
    if j % 2 != 0:
        print(j)
        j = j+1
        i = i+1
    else: 
        j = j+1