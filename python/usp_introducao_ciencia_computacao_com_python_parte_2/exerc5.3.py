# Exercício 1: Ordenação com insertion sort
# Implemente a função insertion_sort(lista), que recebe uma lista com números inteiros como parâmetro e devolve esta lista ordenada. 
# Utilize o algoritmo insertion sort.

def insertion_sort(lista):
    for i in range(1, len(lista)):
        k = i
        while k > 0 and lista[k] < lista[k-1]:
            lista[k-1], lista[k] = lista[k], lista[k-1]
            k -= 1
    return lista
