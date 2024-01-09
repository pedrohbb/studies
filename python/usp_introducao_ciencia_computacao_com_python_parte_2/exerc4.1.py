# Exercício 1: Lista ordenada
# Escreva a função ordenada(lista), que recebe uma lista com números inteiros como parâmetro e devolve o booleano True 
# se a lista estiver ordenada e False se a lista não estiver ordenada.

def ordenada(lista: list) -> bool:
    if len(lista) <= 1:
        return True
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            return False
    return True