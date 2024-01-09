# Exercício 2 - Invertendo sequência
# Como pedido na primeira video-aula desta semana, escreva um programa que recebe uma sequência de números inteiros e imprima todos os valores em ordem inversa. A sequência sempre termina pelo número 0. Note que 0 (ZERO) não deve fazer parte da sequência.
# Exemplo:
# Digite um número: 1
# Digite um número: 7
# Digite um número: 4
# Digite um número: 0
# 4
# 7
# 1

def seq_inverter(lst):
    inv_lst = []
    for i in range(len(lst)-1,-1,-1):
        inv_lst.append(lst[i])
    
    return inv_lst


def main():
    lst = []
    while True:
        numb = int(input("Digite um número: "))
        if numb == 0:
            break
        else:
            lst.append(numb)

    for elem in seq_inverter(lst):
        print(elem)
    

main()

    