# Exercício 2 - Soma dos elementos de uma lista
# Escreva a função soma_elementos que recebe como parâmetro uma lista com números inteiros e devolve um número inteiro correspondente à soma dos elementos da lista recebida.

def soma_elementos(lst):
    
    soma = 0
    for elem in lst:
        soma += elem
    
    return soma
