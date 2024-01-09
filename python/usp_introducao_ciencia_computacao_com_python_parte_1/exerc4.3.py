# Exercício 3
# Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída
# Exemplo:
# Digite um número inteiro: 123
# 6

n_str = input("Digite um número inteiro: ")

i = 0
soma = 0
while i < len(n_str):
    soma = soma + int(n_str[i])
    i = i+1

print(soma)

