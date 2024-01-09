# Exercício 1
# Escreva um programa que receba um número natural n na entrada e imprima n! (fatorial) na saída.
# Exemplo:
# Digite o valor de n: 5
# 120

n = int(input("Digite um número natural: "))

j = 0
i = 1
numb = 1
while True:
    numb = numb * i
    j = i
    i = i+1
    if j >= n:
        break

print(numb)