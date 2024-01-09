# Exercício 2: Ordenação com selection sort
# Implemente a função ordena(lista), que recebe uma lista com números inteiros 
# como parâmetro e devolve esta lista ordenada em ordem crescente. Utilize o algoritmo selection sort.

def ordena(lista: list) -> list:
    for i in range(len(lista)):
        idx = i
        for j in range(i+1, len(lista)):
            if lista[idx] > lista[j]:
                idx = j
        lista[i], lista[idx] = lista[idx], lista[i]
    return lista