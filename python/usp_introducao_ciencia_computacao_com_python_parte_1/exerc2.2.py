# Exercício 2
# Faça um programa em Python que receba quatro notas, calcule e imprima a média aritmética. Observe o exemplo abaixo:
# Exemplo:
# Entrada de Dados:
# Digite a primeira nota: 4
# Digite a segunda nota: 5
# Digite a terceira nota: 6
# Digite a quarta nota: 7
# Saída de Dados:
# A média aritmética é 5.5

notap1 = float(input("Digite a primeira nota: "))
notap2 = float(input("Digite a segunda nota: "))
notap3 = float(input("Digite a terceira nota: "))
notap4 = float(input("Digite a quarta nota: "))
media = (notap1+notap2+notap3+notap4)/4

print(f"A média aritmética é {media}")
