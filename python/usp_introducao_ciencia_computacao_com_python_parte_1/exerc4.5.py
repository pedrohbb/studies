# Exercício 2 - Desafio do vídeo "Repetição com while"
# Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui ao menos um dígito com um dígito adjacente igual a ele. Caso exista, imprima "sim"; se não existir, imprima "não".
# Exemplos:
# Digite um número inteiro: 12345
# não
# Digite um número inteiro: 1011
# sim

n = input("Insira um número: ")

i=0
while i < len(n) - 1:
    if n[i] == n[i+1]:
        print("sim")
        break
    else:
        i += 1

if i == len(n)-1:
    print("não")
