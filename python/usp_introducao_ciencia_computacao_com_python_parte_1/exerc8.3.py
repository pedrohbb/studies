# Exercício 1 - Maior elemento de uma lista
# Escreva a função maior_elemento que recebe como parâmetro uma lista com números inteiros e devolve um número inteiro correspondente ao maior valor presente na lista recebida.

def maior_elemento(lst):
    maxim = lst[0]
    for elem in lst:
        if maxim <= elem :
            maxim = elem
    
    return maxim


