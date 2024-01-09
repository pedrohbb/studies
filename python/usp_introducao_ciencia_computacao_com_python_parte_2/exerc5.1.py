"""
Exercício 1: Busca binária
Implemente a função busca(lista, elemento), que busca um determinado elemento em uma lista e devolve o índice correspondente 
à posição do elemento encontrado. Utilize o algoritmo de busca binária. Nos casos em que o elemento buscado não existir na lista, 
a função deve devolver o booleano False.

Além de devolver o índice correspondente à posição do elemento encontrado, sua função deve imprimir cada um dos índices testados pelo algoritmo.

Exemplo:

busca(['a', 'e', 'i'], 'e')
1
deve devolver => 1

busca([1, 2, 3, 4, 5], 6)
2
3
4
deve devolver => False

busca([1, 2, 3, 4, 5, 6], 4)
2
4
3
deve devolver => 3
"""
def busca(lista, elemento):
    begin = 0
    end = len(lista)-1

    if len(lista) == 0:
        return False   
    
    while begin <= end:
        aux = (begin + end)//2

        if elemento == lista[aux]:
            print(aux)
            return aux
        elif elemento < lista[aux]:
            print(aux)
            end = aux - 1
        else:
            print(aux)
            begin = aux + 1    
    return False