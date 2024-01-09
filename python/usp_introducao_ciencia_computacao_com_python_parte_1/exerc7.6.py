# https://panda.ime.usp.br/aulasPython/static/aulasPython/aula08.html
# Exercício 8.2
# Nota: Exercício 9 da lista sobre inteiros.
# Dados números inteiros n, i e j, todos maiores do que zero, imprimir em ordem crescente os n primeiros naturais que são múltiplos de i ou de j e ou de ambos.
# Por exemplo, para n = 6, i = 2 e j = 3 a saída deverá ser:
# 0   2   3   4   6   8

def main():
    count = 1
    numb = min(i,j)
    Numbs = [0]
    while count < n:
        while True:
            if (numb % i == 0) or (numb % j == 0):
                Numbs.append(numb)
                numb += 1
                count += 1
                break
            else:
                numb += 1
    Result = ''
    for nbr in Numbs:
        Result += str(nbr) + '\t'
    
    print(Result)

i = int(input("Insira um número inteiro positivo: "))
j = int(input("Insira outro número inteiro positivo: "))
n = int(input("Quantos inteiros múltiplos deseja? "))

main()

